/**
 * Builds the Division 296 prudential brief (.docx).
 *
 *   node build_docx.js <data.json> <out.docx>
 *
 * Structure: a 3-page plain-English brief, then annexes carrying the detail,
 * the provenance audit trail and the red-team record.
 *
 * APRA house style: Arial, navy #012169 headings, cobalt/teal/orange accents.
 */
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, AlignmentType, HeadingLevel, PageBreak,
  Header, Footer, PageNumber, VerticalAlign, LevelFormat, convertInchesToTwip,
} = require("docx");

// ------------------------------------------------------------------ brand ---
const NAVY = "012169", COBALT = "0072CE", TEAL = "00B398", ORANGE = "E87722";
const MAGENTA = "890C58", INK = "1A1A1A", SECOND = "52514E", MUTED = "898781";
const RULE = "D9D8D2", TINT = "F4F9FC", TINT2 = "EFEEE9";

const FONT = "Arial";
const A4_W = 11906, A4_H = 16838;
const MARGIN_X = 1000, MARGIN_Y = 1080;
const CONTENT_W = A4_W - MARGIN_X * 2;   // 9906 DXA

const GRADE_COLOR = { A: MAGENTA, B: ORANGE, C: "A8891F" };
const PROV_COLOR = { sourced: "00806D", inferred: COBALT, created: ORANGE };
const PROV_TAG = { sourced: "S", inferred: "I", created: "C" };

const args = process.argv.slice(2);
const DATA = JSON.parse(fs.readFileSync(args[0], "utf8"));
const OUT = args[1];
const ASSETS = path.resolve(__dirname, "..", "assets");

// ----------------------------------------------------------- png helpers ----
function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}
/** Scale an image to a target width in points (1pt = 1/72"), preserving ratio. */
function img(file, widthPx) {
  const f = path.join(ASSETS, file);
  const { w, h } = pngSize(f);
  return new ImageRun({
    type: "png",
    data: fs.readFileSync(f),
    transformation: { width: widthPx, height: Math.round(widthPx * h / w) },
  });
}
function figure(file, widthPx, caption) {
  const out = [new Paragraph({
    children: [img(file, widthPx)],
    alignment: AlignmentType.CENTER,
    spacing: { before: 90, after: caption ? 40 : 110 },
  })];
  if (caption) {
    out.push(new Paragraph({
      children: [new TextRun({ text: caption, font: FONT, size: 13, color: MUTED, italics: true })],
      alignment: AlignmentType.CENTER,
      spacing: { after: 120 },
    }));
  }
  return out;
}

// ------------------------------------------------------------ text atoms ----
const t = (text, o = {}) => new TextRun({
  text, font: FONT, size: o.size || 19, color: o.color || INK,
  bold: o.bold, italics: o.italics, allCaps: o.caps,
});

function para(text, o = {}) {
  return new Paragraph({
    children: Array.isArray(text) ? text : [t(text, o)],
    spacing: { before: o.before ?? 0, after: o.after ?? 110, line: o.line ?? 264 },
    alignment: o.align,
    indent: o.indent,
    border: o.border,
    shading: o.shading,
  });
}

function h1(text) {
  return new Paragraph({
    children: [t(text, { size: 30, bold: true, color: NAVY })],
    spacing: { before: 0, after: 60 },
  });
}
function h2(text, o = {}) {
  return new Paragraph({
    children: [t(text, { size: 22, bold: true, color: NAVY })],
    spacing: { before: o.before ?? 240, after: 100 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COBALT, space: 4 } },
  });
}
function h3(text, o = {}) {
  return new Paragraph({
    children: [t(text, { size: 19, bold: true, color: COBALT })],
    spacing: { before: o.before ?? 160, after: 60 },
  });
}
function bullet(runs, o = {}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [t(runs, o)],
    numbering: { reference: "brief-bullets", level: o.level ?? 0 },
    spacing: { before: 0, after: o.after ?? 60, line: 258 },
  });
}
/** Inline provenance chip, e.g. [S]. Never omit - the audit trail depends on it. */
function prov(kind) {
  return new TextRun({
    text: ` [${PROV_TAG[kind] || "?"}]`, font: FONT, size: 13,
    color: PROV_COLOR[kind] || MUTED, bold: true, superScript: true,
  });
}

// ---------------------------------------------------------------- tables ----
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const hair = { style: BorderStyle.SINGLE, size: 3, color: RULE };

function cell(children, o = {}) {
  return new TableCell({
    children: Array.isArray(children) ? children : [children],
    width: { size: o.w, type: WidthType.DXA },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    margins: { top: 70, bottom: 70, left: 100, right: 100 },
    verticalAlign: VerticalAlign.TOP,
    columnSpan: o.span,
    borders: {
      top: o.topRule ? { style: BorderStyle.SINGLE, size: 8, color: COBALT } : hair,
      bottom: hair, left: noBorder, right: noBorder,
    },
  });
}

/**
 * cols: [{key,label,w,align}]  rows: array of objects
 * render(row,col) may return a string or an array of TextRun.
 */
function table(cols, rows, render, o = {}) {
  const widths = cols.map(c => c.w);
  const head = new TableRow({
    tableHeader: true,
    children: cols.map(c => cell(
      new Paragraph({
        children: [t(c.label, { size: 15, bold: true, color: NAVY, caps: true })],
        spacing: { after: 0, line: 240 }, alignment: c.align,
      }), { w: c.w, fill: TINT, topRule: true })),
  });
  const body = rows.map((r, i) => new TableRow({
    children: cols.map(c => {
      const v = render(r, c);
      const kids = Array.isArray(v) ? [new Paragraph({
        children: v, spacing: { after: 0, line: 250 }, alignment: c.align,
      })] : [new Paragraph({
        children: [t(String(v ?? ""), { size: o.size || 16 })],
        spacing: { after: 0, line: 250 }, alignment: c.align,
      })];
      return cell(kids, { w: c.w, fill: i % 2 ? TINT2 : undefined });
    }),
  }));
  return new Table({
    rows: [head, ...body],
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    layout: "fixed",
  });
}

/** Grade pill: letter + colour + always the word, so colour never carries it alone. */
function gradeRuns(g) {
  return [new TextRun({ text: g, font: FONT, size: 18, bold: true, color: GRADE_COLOR[g] || MUTED })];
}

// ------------------------------------------------------------- stat tiles ---
function statTiles(nums) {
  const n = Math.min(nums.length, 3);
  if (!n) return [];
  const w = Math.floor(CONTENT_W / n);
  return [new Table({
    rows: [new TableRow({
      cantSplit: true,   // never let the tiles break across a page
      children: nums.slice(0, n).map(s => new TableCell({
        width: { size: w, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: TINT, color: "auto" },
        margins: { top: 85, bottom: 85, left: 140, right: 140 },
        borders: {
          top: { style: BorderStyle.SINGLE, size: 14, color: COBALT },
          bottom: noBorder,
          left: { style: BorderStyle.SINGLE, size: 8, color: "FFFFFF" },
          right: { style: BorderStyle.SINGLE, size: 8, color: "FFFFFF" },
        },
        children: [
          new Paragraph({
            children: [t(s.figure, { size: 30, bold: true, color: NAVY })],
            spacing: { after: 24, line: 270 },
          }),
          new Paragraph({
            children: [t(s.meaning, { size: 13, color: SECOND }), prov(s.provenance)],
            spacing: { after: 0, line: 230 },
          }),
        ],
      })),
    })],
    width: { size: w * n, type: WidthType.DXA },
    columnWidths: Array(n).fill(w),
    layout: "fixed",
  })];
  // No trailing spacer paragraph: the tiles close page 1, and an empty
  // paragraph after them is enough to spill onto a blank page 2.
}

/** Callout band used for the bottom line / recommended position. */
function callout(title, lines, color = NAVY) {
  return new Table({
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: TINT, color: "auto" },
        margins: { top: 150, bottom: 150, left: 180, right: 180 },
        borders: {
          top: noBorder, bottom: noBorder, right: noBorder,
          left: { style: BorderStyle.SINGLE, size: 24, color },
        },
        children: [
          new Paragraph({
            children: [t(title, { size: 19, bold: true, color, caps: true })],
            spacing: { after: 80, line: 240 },
          }),
          ...lines.map(l => {
            // Bottom-line bullets are objects carrying provenance, so the most
            // quoted claims on page 1 are marked like every other claim in the
            // note. A custom `mark` covers mixed cases (e.g. sourced figures
            // combined with an original comparison).
            let kids;
            if (Array.isArray(l)) kids = l;
            else if (typeof l === "string") kids = [t(l, { size: 17 })];
            else {
              kids = [t(l.text, { size: 17 })];
              kids.push(l.mark
                ? new TextRun({ text: ` ${l.mark}`, font: FONT, size: 12,
                    color: MUTED, bold: true, superScript: true })
                : prov(l.provenance));
            }
            return new Paragraph({
              children: kids,
              numbering: { reference: "brief-bullets", level: 0 },
              spacing: { after: 60, line: 258 },
            });
          }),
        ],
      })],
    })],
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    layout: "fixed",
  });
}

const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

module.exports = {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, AlignmentType, HeadingLevel, PageBreak,
  Header, Footer, PageNumber, VerticalAlign, LevelFormat,
  NAVY, COBALT, TEAL, ORANGE, MAGENTA, INK, SECOND, MUTED, RULE, TINT, TINT2,
  FONT, A4_W, A4_H, MARGIN_X, MARGIN_Y, CONTENT_W, GRADE_COLOR, PROV_COLOR, PROV_TAG,
  DATA, OUT, ASSETS, pngSize, img, figure, t, para, h1, h2, h3, bullet, prov,
  cell, table, gradeRuns, statTiles, callout, pageBreak, noBorder, hair,
};

if (require.main === module) require("./compose.js");
