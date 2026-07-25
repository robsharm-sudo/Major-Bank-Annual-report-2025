"""Shared document furniture for the CPS 240 / CPG 240 prudential drafting package.

Both Word deliverables are built from the same style sheet so that the standard and
the practice guide read as one family of instruments. Everything is Arial: the
supplied CPS XXX template inherits Calibri for headings through the theme's major
font, which we deliberately do not carry over.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# House palette. Deep navy for the instrument name, a muted slate for structural
# headings, and an amber reserved exclusively for verification annotations so a
# reader can find every evidential caveat by scanning for colour.
NAVY = RGBColor(0x1B, 0x33, 0x5F)
SLATE = RGBColor(0x2F, 0x54, 0x97)
AMBER = RGBColor(0x9C, 0x63, 0x00)
GREY = RGBColor(0x59, 0x59, 0x59)
RULE = "1B335F"
BANNER_FILL = "1B335F"
BOX_FILL = "EEF2F8"
SHADE_HEADER = "1B335F"
SHADE_ALT = "F4F6FA"

ARIAL = "Arial"


# --------------------------------------------------------------------------- #
# low-level OOXML helpers
# --------------------------------------------------------------------------- #

def _set_run_fonts(rpr, name: str = ARIAL) -> None:
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), name)
    # Strip theme references; otherwise Word silently resolves back to Calibri.
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rfonts.get(qn(attr)) is not None:
            del rfonts.attrib[qn(attr)]


def shade(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:color"), "auto")
    el.set(qn("w:fill"), fill)
    tc_pr.append(el)


def cell_margins(table, top=60, bottom=60, left=110, right=110) -> None:
    tbl_pr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for tag, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        node = OxmlElement(f"w:{tag}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        mar.append(node)
    tbl_pr.append(mar)


def borders(table, colour: str = "B7C3D6", size: int = 4) -> None:
    tbl_pr = table._tbl.tblPr
    el = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:val"), "single")
        node.set(qn("w:sz"), str(size))
        node.set(qn("w:space"), "0")
        node.set(qn("w:color"), colour)
        el.append(node)
    tbl_pr.append(el)


def no_borders(table) -> None:
    tbl_pr = table._tbl.tblPr
    el = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:val"), "none")
        node.set(qn("w:sz"), "0")
        el.append(node)
    tbl_pr.append(el)


def repeat_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def keep_with_next(paragraph) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    el = OxmlElement("w:keepNext")
    p_pr.append(el)


def bottom_rule(paragraph, colour: str = RULE, size: int = 8) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), colour)
    pbdr.append(bottom)
    p_pr.append(pbdr)


def add_field(paragraph, instr: str) -> None:
    """Insert a Word field code (used for PAGE / NUMPAGES in the footer)."""
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr_el = OxmlElement("w:instrText")
    instr_el.set(qn("xml:space"), "preserve")
    instr_el.text = instr
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(begin)
    run._r.append(instr_el)
    run._r.append(end)


# --------------------------------------------------------------------------- #
# style sheet
# --------------------------------------------------------------------------- #

def _style(doc, name, *, size, bold=False, italic=False, colour=None,
           space_before=0, space_after=6, base="Normal", outline=None,
           left_indent=None, keep=False):
    from docx.enum.style import WD_STYLE_TYPE

    try:
        st = doc.styles[name]
    except KeyError:
        st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        if base:
            st.base_style = doc.styles[base]
    f = st.font
    f.name = ARIAL
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    if colour is not None:
        f.color.rgb = colour
    pf = st.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = 1.06
    if left_indent is not None:
        pf.left_indent = Cm(left_indent)
    _set_run_fonts(st.element.get_or_add_rPr())
    if outline is not None:
        p_pr = st.element.get_or_add_pPr()
        lvl = OxmlElement("w:outlineLvl")
        lvl.set(qn("w:val"), str(outline))
        p_pr.append(lvl)
    if keep:
        p_pr = st.element.get_or_add_pPr()
        for tag in ("w:keepNext", "w:keepLines"):
            p_pr.append(OxmlElement(tag))
    return st


def build_styles(doc) -> None:
    """Define the shared style sheet. Requirement is the only bold body style."""
    normal = doc.styles["Normal"]
    normal.font.name = ARIAL
    normal.font.size = Pt(10)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.06
    _set_run_fonts(normal.element.get_or_add_rPr())

    _style(doc, "DocTitle", size=26, bold=True, colour=NAVY, space_before=0, space_after=2)
    _style(doc, "DocSubtitle", size=13, colour=SLATE, space_after=2)
    _style(doc, "DocMeta", size=9, colour=GREY, space_after=2)
    _style(doc, "Heading 1", size=15, bold=True, colour=NAVY,
           space_before=16, space_after=6, outline=0, keep=True)
    _style(doc, "Heading 2", size=11.5, bold=True, colour=SLATE,
           space_before=11, space_after=4, outline=1, keep=True)
    _style(doc, "Heading 3", size=10, bold=True, colour=SLATE,
           space_before=8, space_after=3, outline=2, keep=True)

    # The operative distinction the whole package turns on.
    _style(doc, "Requirement", size=10, bold=True, space_before=3, space_after=6, keep=True)
    _style(doc, "Guidance", size=10, space_before=0, space_after=6)

    _style(doc, "CrossRef", size=9, italic=True, colour=SLATE, space_before=0, space_after=8)
    _style(doc, "SourceNote", size=9, italic=True, colour=GREY, space_before=0, space_after=4)
    _style(doc, "Verification", size=9, colour=AMBER, space_before=0, space_after=8)
    _style(doc, "Bullet", size=10, space_after=3, left_indent=0.55)
    _style(doc, "TableText", size=8.5, space_before=1, space_after=1)
    _style(doc, "TableHead", size=8.5, bold=True, colour=RGBColor(0xFF, 0xFF, 0xFF),
           space_before=1, space_after=1)
    _style(doc, "Caption", size=8.5, italic=True, colour=GREY, space_before=2, space_after=8)
    _style(doc, "GuideBody", size=10, space_after=6)


def page_setup(doc, *, landscape_annex=False) -> None:
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(1.9)
    sec.left_margin = Cm(2.2)
    sec.right_margin = Cm(2.2)
    sec.header_distance = Cm(1.1)
    sec.footer_distance = Cm(1.0)


def add_header_footer(doc, header_text: str, footer_left: str) -> None:
    sec = doc.sections[0]

    hp = sec.header.paragraphs[0]
    hp.text = ""
    hp.style = doc.styles["DocMeta"]
    run = hp.add_run(header_text)
    run.font.name = ARIAL
    run.font.size = Pt(8)
    run.font.color.rgb = GREY
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    bottom_rule(hp, colour="C7D0DF", size=4)

    fp = sec.footer.paragraphs[0]
    fp.text = ""
    fp.style = doc.styles["DocMeta"]
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    tab_stops = fp.paragraph_format.tab_stops
    usable = Cm(21.0 - 2.2 - 2.2)
    tab_stops.add_tab_stop(usable)
    run = fp.add_run(footer_left + "\t")
    run.font.name = ARIAL
    run.font.size = Pt(8)
    run.font.color.rgb = GREY
    page_run = fp.add_run("Page ")
    page_run.font.name = ARIAL
    page_run.font.size = Pt(8)
    page_run.font.color.rgb = GREY
    add_field(fp, " PAGE ")
    of_run = fp.add_run(" of ")
    of_run.font.name = ARIAL
    of_run.font.size = Pt(8)
    of_run.font.color.rgb = GREY
    add_field(fp, " NUMPAGES ")
    for r in fp.runs:
        r.font.name = ARIAL
        r.font.size = Pt(8)
        r.font.color.rgb = GREY


# --------------------------------------------------------------------------- #
# building blocks
# --------------------------------------------------------------------------- #

def para(doc, text: str, style: str = "Normal"):
    p = doc.add_paragraph(style=style)
    if text:
        p.add_run(text)
    return p


def bullets(doc, items, style: str = "Bullet"):
    out = []
    for it in items:
        p = doc.add_paragraph(style=style)
        p.add_run("• " + it)
        out.append(p)
    return out


def banner(doc, text: str, fill: str = BANNER_FILL):
    """Full-width status banner, e.g. POLICY DEVELOPMENT DRAFT — NOT IN FORCE."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    no_borders(t)
    cell_margins(t, top=70, bottom=70, left=140, right=140)
    c = t.cell(0, 0)
    shade(c, fill)
    c.width = Cm(16.6)
    p = c.paragraphs[0]
    p.style = doc.styles["Normal"]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.font.name = ARIAL
    r.font.size = Pt(9)
    r.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    doc.add_paragraph(style="DocMeta")
    return t


def callout(doc, title: str, body: str, fill: str = BOX_FILL):
    """Soft-filled note box used for interpretation notes and legal reservations."""
    t = doc.add_table(rows=1, cols=1)
    borders(t, colour="C7D0DF", size=4)
    cell_margins(t, top=90, bottom=90, left=140, right=140)
    c = t.cell(0, 0)
    shade(c, fill)
    c.width = Cm(16.6)
    p = c.paragraphs[0]
    p.style = doc.styles["Normal"]
    r = p.add_run(title)
    r.bold = True
    r.font.name = ARIAL
    r.font.size = Pt(9.5)
    r.font.color.rgb = NAVY
    p2 = c.add_paragraph(style="Normal")
    r2 = p2.add_run(body)
    r2.font.name = ARIAL
    r2.font.size = Pt(9.5)
    doc.add_paragraph(style="DocMeta")
    return t


def xref_box(doc, text: str):
    """The single-cell cross-reference strip used at the head of each guide chapter."""
    t = doc.add_table(rows=1, cols=1)
    borders(t, colour="C7D0DF", size=4)
    cell_margins(t, top=60, bottom=60, left=130, right=130)
    c = t.cell(0, 0)
    shade(c, BOX_FILL)
    c.width = Cm(16.6)
    p = c.paragraphs[0]
    p.style = doc.styles["Normal"]
    r = p.add_run(text)
    r.bold = True
    r.font.name = ARIAL
    r.font.size = Pt(9)
    r.font.color.rgb = NAVY
    doc.add_paragraph(style="DocMeta")
    return t


def table(doc, headers, rows, widths_cm, *, font_pt=8.5, zebra=True,
          landscape_width=None):
    """Standard data table: navy header row, optional zebra striping, repeating header."""
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    borders(t)
    cell_margins(t)
    t.autofit = False

    hdr = t.rows[0]
    repeat_header(hdr)
    for i, h in enumerate(headers):
        c = hdr.cells[i]
        c.width = Cm(widths_cm[i])
        shade(c, SHADE_HEADER)
        p = c.paragraphs[0]
        p.style = doc.styles["TableHead"]
        r = p.add_run(h)
        r.font.name = ARIAL
        r.font.size = Pt(font_pt)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for n, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            c = cells[i]
            c.width = Cm(widths_cm[i])
            if zebra and n % 2 == 1:
                shade(c, SHADE_ALT)
            p = c.paragraphs[0]
            p.style = doc.styles["TableText"]
            text = "" if val is None else str(val)
            # A leading marker lets a cell carry a bold lead-in without extra plumbing.
            if text.startswith("**") and "**" in text[2:]:
                lead, rest = text[2:].split("**", 1)
                rb = p.add_run(lead)
                rb.bold = True
                rb.font.name = ARIAL
                rb.font.size = Pt(font_pt)
                text = rest
            r = p.add_run(text)
            r.font.name = ARIAL
            r.font.size = Pt(font_pt)

    for i, w in enumerate(widths_cm):
        for row in t.rows:
            row.cells[i].width = Cm(w)
    return t


def landscape_section(doc):
    """Start a landscape section for the wide comparison annexes."""
    from docx.enum.section import WD_SECTION, WD_ORIENT

    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    w, h = sec.page_width, sec.page_height
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = h, w
    sec.top_margin = Cm(1.6)
    sec.bottom_margin = Cm(1.6)
    sec.left_margin = Cm(1.5)
    sec.right_margin = Cm(1.5)
    return sec


def portrait_section(doc):
    from docx.enum.section import WD_SECTION, WD_ORIENT

    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    w, h = sec.page_width, sec.page_height
    sec.orientation = WD_ORIENT.PORTRAIT
    if w > h:
        sec.page_width, sec.page_height = h, w
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(1.9)
    sec.left_margin = Cm(2.2)
    sec.right_margin = Cm(2.2)
    return sec


def page_break(doc):
    from docx.enum.text import WD_BREAK

    p = doc.add_paragraph(style="DocMeta")
    p.add_run().add_break(WD_BREAK.PAGE)
    return p


# --------------------------------------------------------------------------- #
# post-processing and verification
# --------------------------------------------------------------------------- #

def force_arial(path: str | Path) -> int:
    """Rewrite the package so nothing can resolve to a theme font.

    python-docx writes rFonts on the styles we define, but Word also consults
    docDefaults and the theme. We set Arial in all three and strip every
    *Theme attribute. Returns the number of theme references removed.
    """
    path = Path(path)
    tmp = path.with_suffix(".tmp.docx")
    removed = 0
    theme_attr = re.compile(r'\s(?:w:)?(?:ascii|hAnsi|eastAsia|cs)Theme="[^"]*"')

    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(
        tmp, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename in ("word/styles.xml", "word/document.xml",
                                 "word/header1.xml", "word/footer1.xml"):
                text = data.decode("utf-8")
                removed += len(theme_attr.findall(text))
                text = theme_attr.sub("", text)
                if item.filename == "word/styles.xml":
                    text = _patch_doc_defaults(text)
                data = text.encode("utf-8")
            elif item.filename == "word/theme/theme1.xml":
                text = data.decode("utf-8")
                text = re.sub(r'(<a:(?:major|minor)Font><a:latin typeface=")[^"]*(")',
                              r"\1Arial\2", text)
                data = text.encode("utf-8")
            zout.writestr(item, data)

    shutil.move(str(tmp), str(path))
    return removed


def _patch_doc_defaults(styles_xml: str) -> str:
    target = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial"/>'
    if "<w:rPrDefault>" not in styles_xml:
        return styles_xml
    def repl(m):
        block = m.group(0)
        if "<w:rFonts" in block:
            return re.sub(r"<w:rFonts[^>]*/>", target, block, count=1)
        return block.replace("<w:rPr>", "<w:rPr>" + target, 1)
    return re.sub(r"<w:rPrDefault>.*?</w:rPrDefault>", repl, styles_xml, flags=re.S)


def render_pages(docx_path: str | Path, out_dir: str | Path, pages=None, scale=1.6):
    """Convert to PDF via LibreOffice and rasterise so the layout can be eyeballed."""
    import pypdfium2 as pdfium

    docx_path = Path(docx_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out_dir),
         str(docx_path)],
        check=True, capture_output=True, timeout=300,
    )
    pdf_path = out_dir / (docx_path.stem + ".pdf")
    pdf = pdfium.PdfDocument(str(pdf_path))
    n = len(pdf)
    targets = range(n) if pages is None else [p for p in pages if p < n]
    written = []
    for i in targets:
        img = pdf[i].render(scale=scale).to_pil()
        out = out_dir / f"{docx_path.stem}-p{i + 1:02d}.png"
        img.save(out)
        written.append(out)
    return pdf_path, n, written


def audit_fonts(docx_path: str | Path):
    """Assert Arial everywhere and report the bold/plain split of the body styles."""
    doc = Document(str(docx_path))
    bad = []
    req = plain = 0

    def check(p, where):
        nonlocal req, plain
        st = p.style.name if p.style is not None else "?"
        for r in p.runs:
            if r.font.name not in (None, ARIAL):
                bad.append((where, st, r.font.name, r.text[:40]))
        if st == "Requirement" and p.text.strip():
            req += 1
            if not all(r.bold for r in p.runs if r.text.strip()):
                bad.append((where, st, "NOT BOLD", p.text[:60]))
        if st == "Guidance" and p.text.strip():
            plain += 1
            if any(r.bold for r in p.runs if r.text.strip()):
                bad.append((where, st, "UNEXPECTED BOLD", p.text[:60]))

    for p in doc.paragraphs:
        check(p, "body")
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    check(p, "table")
    return {"violations": bad, "requirement_paras": req, "guidance_paras": plain}
