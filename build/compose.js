/** Lays out the Division 296 prudential brief. Required by build_docx.js. */
const B = require("./build_docx.js");
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  BorderStyle, ShadingType, AlignmentType, Header, Footer, PageNumber, LevelFormat,
  NAVY, COBALT, TEAL, ORANGE, MAGENTA, INK, SECOND, MUTED, TINT, TINT2, FONT,
  A4_W, A4_H, MARGIN_X, MARGIN_Y, CONTENT_W, GRADE_COLOR, PROV_COLOR,
  DATA, OUT, ASSETS, figure, t, para, h1, h2, h3, bullet, prov, table,
  gradeRuns, statTiles, callout, pageBreak, img, noBorder,
} = B;

const FIG_W = 645;
const D = DATA;
const has = f => fs.existsSync(require("path").join(ASSETS, f));
const issues = D.issues || [];
const byGrade = g => issues.filter(i => i.grade === g);
const ordered = [...issues].sort((a, b) =>
  ("ABC".indexOf(a.grade) - "ABC".indexOf(b.grade)) ||
  (b.materiality * b.likelihood - a.materiality * a.likelihood));

// ------------------------------------------------------------- page one -----
function pageOne() {
  const k = [];

  // masthead: logo left, classification right
  k.push(new Table({
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: Math.round(CONTENT_W * 0.5), type: WidthType.DXA },
          borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
          margins: { top: 0, bottom: 0, left: 0, right: 0 },
          children: [new Paragraph({
            children: has("apra-logo-navy.png") ? [img("apra-logo-navy.png", 108)] : [t("APRA", { size: 26, bold: true, color: NAVY })],
            spacing: { after: 0 },
          })],
        }),
        new TableCell({
          width: { size: Math.round(CONTENT_W * 0.5), type: WidthType.DXA },
          borders: { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder },
          margins: { top: 40, bottom: 0, left: 0, right: 0 },
          children: [
            new Paragraph({
              children: [t(D.meta.classification, { size: 15, bold: true, color: MAGENTA, caps: true })],
              alignment: AlignmentType.RIGHT, spacing: { after: 20 },
            }),
            new Paragraph({
              children: [t(D.meta.date, { size: 15, color: MUTED })],
              alignment: AlignmentType.RIGHT, spacing: { after: 0 },
            }),
          ],
        }),
      ],
    })],
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [Math.round(CONTENT_W * 0.5), Math.round(CONTENT_W * 0.5)],
    layout: "fixed",
  }));

  k.push(new Paragraph({
    children: [t(D.meta.title, { size: 34, bold: true, color: NAVY })],
    spacing: { before: 220, after: 50, line: 340 },
  }));
  k.push(new Paragraph({
    children: [t(D.meta.subtitle, { size: 20, color: SECOND })],
    spacing: { after: 40, line: 270 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: TEAL, space: 8 } },
  }));
  k.push(para("", { after: 140 }));

  k.push(callout("The bottom line", D.bottom_line || [], NAVY));
  k.push(para("", { after: 160 }));

  k.push(h3("What Division 296 now does", { before: 0 }));
  if (has("fig1_tiers.png")) k.push(...figure("fig1_tiers.png", FIG_W, D.captions?.fig1));

  if ((D.headline_numbers || []).length) {
    k.push(...statTiles(D.headline_numbers));
  }

  return k;
}

// ------------------------------------------------------------- page two -----
function pageTwo() {
  const k = [pageBreak()];

  // Opens page 2 rather than page 1: page 1 is full after the rate figure and
  // the stat tiles, and these bullets are the bridge into the graded map.
  k.push(h3("Why this is a prudential matter, not just a tax matter", { before: 0 }));
  (D.why_prudential || []).forEach(b =>
    k.push(bullet([t(b.text, { size: 17 }), prov(b.provenance)], { after: 50 })));

  k.push(h2("Where the prudential risk actually sits"));
  k.push(para([
    t("Each issue is graded on three things: how material it is prudentially, how likely the adverse consequence is to crystallise, and how directly we can act on it. ", { size: 17 }),
    t("A serious problem that belongs to Treasury is not automatically a priority for us — the map separates the two.", { size: 17, bold: true }),
  ], { after: 90 }));

  if (has("fig2_grade_map.png")) k.push(...figure("fig2_grade_map.png", FIG_W, D.captions?.fig2));

  // Deliberately terse: full titles and full recommendations belong in Annex A.
  // On the page the CEO reads, the job is to rank and route, not to explain.
  const ACTION = {
    "standard-amendment": "Amend a standard",
    "new-or-updated-guidance": "Guidance",
    "supervisory-practice": "Supervision",
    "legislative-change": "Treasury / ATO call",
    "no-change-monitor": "Monitor only",
  };
  const short = s => {
    if (!s) return "";
    const cut = s.split(/,| — | - |: /)[0];
    const base = (cut.length >= 34 && cut.length <= 82) ? cut : s;
    return base.length > 88 ? base.slice(0, 86).replace(/\s+\S*$/, "") + "…" : base;
  };

  k.push(h3("The graded issues"));
  const W = [560, 4400, 860, 1150, 2936];
  k.push(table(
    [
      { key: "id", label: "ID", w: W[0] },
      { key: "title", label: "Issue", w: W[1] },
      { key: "grade", label: "Grade", w: W[2], align: AlignmentType.CENTER },
      { key: "score", label: "M · L · P", w: W[3], align: AlignmentType.CENTER },
      { key: "action", label: "What it needs", w: W[4] },
    ],
    ordered.slice(0, D.page2_rows ?? 9),
    (r, c) => {
      if (c.key === "id") return [t(r.id, { size: 15, bold: true, color: NAVY })];
      if (c.key === "title") return [t(short(r.title), { size: 15 }), prov(r.provenance)];
      if (c.key === "grade") return gradeRuns(r.grade);
      if (c.key === "score") return [t(`${r.materiality} · ${r.likelihood} · ${r.apra_proximity}`, { size: 14, color: MUTED })];
      return [t(ACTION[r.action_type] || r.action_type, { size: 14, color: SECOND })];
    }
  ));
  k.push(para([
    t("A = raise now · B = press and monitor · C = watch.  Scores out of 5.  All 18 issues are in Annex A.", { size: 13, color: MUTED }),
  ], { before: 70, after: 0 }));
  return k;
}

// ----------------------------------------------------------- page three -----
function pageThree() {
  const k = [pageBreak()];
  k.push(h2("What the prudential framework actually needs", { before: 0 }));
  k.push(para(D.framework_intro || "", { after: 90, size: 18 }));
  if (has("fig3_framework.png")) k.push(...figure("fig3_framework.png", FIG_W, D.captions?.fig3));

  k.push(h2("The runway — and APRA's window to act"));
  if (has("fig4_timeline.png")) k.push(...figure("fig4_timeline.png", FIG_W, D.captions?.fig4));

  k.push(h2("What APRA should do"));
  (D.recommendations || []).forEach(r => {
    k.push(new Paragraph({
      children: [
        t(r.horizon ? `${r.horizon}  ` : "", { size: 15, bold: true, color: TEAL, caps: true }),
        t(r.text, { size: 18 }), prov(r.provenance),
      ],
      numbering: { reference: "brief-bullets", level: 0 },
      spacing: { after: 70, line: 258 },
    }));
  });

  // The points to carry into engagement are in Annex E: there is no open public
  // consultation to submit into, and page 3 is full with the recommendations.

  // provenance legend - every page-1..3 claim carries one of these
  k.push(para("", { after: 120 }));
  k.push(new Table({
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: TINT, color: "auto" },
        margins: { top: 90, bottom: 90, left: 150, right: 150 },
        borders: { top: noBorder, bottom: noBorder, right: noBorder, left: { style: BorderStyle.SINGLE, size: 18, color: TEAL } },
        children: [
          new Paragraph({
            children: [
              t("How to read the provenance marks.  ", { size: 14, bold: true, color: NAVY }),
              new TextRun({ text: "[S]", font: FONT, size: 14, bold: true, color: PROV_COLOR.sourced }),
              t(" Sourced — stated in a citable document.  ", { size: 14, color: SECOND }),
              new TextRun({ text: "[I]", font: FONT, size: 14, bold: true, color: PROV_COLOR.inferred }),
              t(" Inferred — our reasoning from sourced facts.  ", { size: 14, color: SECOND }),
              new TextRun({ text: "[C]", font: FONT, size: 14, bold: true, color: PROV_COLOR.created }),
              t(" Created — original judgement written for this meeting, flagged deliberately.  Citations and reasoning chains are in Annex C.", { size: 14, color: SECOND }),
            ],
            spacing: { after: 0, line: 240 },
          }),
        ],
      })],
    })],
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W], layout: "fixed",
  }));
  return k;
}

// -------------------------------------------------------------- annexes -----
function annexes() {
  const k = [pageBreak()];
  k.push(new Paragraph({
    children: [t("Annex", { size: 20, bold: true, color: TEAL, caps: true })],
    spacing: { after: 30 },
  }));
  k.push(new Paragraph({
    children: [t("Supporting detail, evidence and audit trail", { size: 30, bold: true, color: NAVY })],
    spacing: { after: 60, line: 330 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: TEAL, space: 8 } },
  }));
  k.push(para("Everything in the three-page brief traces back to this annex. Nothing in the brief is asserted without a provenance mark.", { after: 160, size: 17, color: SECOND }));

  // Where each part of the machinery actually sits. Placed first because the
  // numbering genuinely misleads - Division 296 itself obliges no fund.
  if ((D.provisions || []).length) {
    k.push(h2("Where the obligations actually sit", { before: 0 }));
    k.push(para(D.provisions_intro || "", { after: 120, size: 17, color: SECOND }));
    const WP = [2300, 4900, 1500, 1206];
    k.push(table(
      [
        { key: "cite", label: "Provision", w: WP[0] },
        { key: "what", label: "What it does", w: WP[1] },
        { key: "heading", label: "Heading", w: WP[2] },
        { key: "obliges", label: "Obliges", w: WP[3], align: AlignmentType.CENTER },
      ],
      D.provisions,
      (r, c) => {
        if (c.key === "cite") return [t(r.cite, { size: 15, bold: true, color: NAVY })];
        if (c.key === "obliges") {
          const col = r.obliges === "The fund" ? MAGENTA : r.obliges === "No one" ? MUTED : COBALT;
          return [t(r.obliges, { size: 14, bold: true, color: col })];
        }
        if (c.key === "heading") return [t(r.heading, { size: 14, italics: true, color: SECOND })];
        return [t(r.what, { size: 14, color: SECOND })];
      }
    ));
    k.push(para("", { after: 200 }));
  }

  // Two orienting figures: where the affected population sits relative to our
  // perimeter, and how much of the register is actually ours to act on.
  if (has("fig5_perimeter.png")) k.push(...figure("fig5_perimeter.png", FIG_W, D.captions?.fig5));
  if (has("fig6_split.png")) {
    k.push(h3("How much of this is ours to fix"));
    k.push(...figure("fig6_split.png", 330, D.captions?.fig6));
  }

  // --- Annex A: full issue register
  k.push(h2("Annex A — Full prudential issue register", { before: 0 }));
  ordered.forEach(i => {
    k.push(new Paragraph({
      children: [
        t(`${i.id}. `, { size: 19, bold: true, color: NAVY }),
        t(i.title, { size: 19, bold: true, color: NAVY }),
        new TextRun({ text: `   GRADE ${i.grade}`, font: FONT, size: 15, bold: true, color: GRADE_COLOR[i.grade] }),
      ],
      spacing: { before: 200, after: 60, line: 264 },
    }));
    k.push(para([t("In plain terms.  ", { size: 17, bold: true, color: TEAL }), t(i.plain_english, { size: 17 })], { after: 60 }));
    k.push(para([t("Why it matters.  ", { size: 17, bold: true, color: TEAL }), t(i.why_it_matters, { size: 17 })], { after: 60 }));
    k.push(para([t("Who bears it.  ", { size: 17, bold: true, color: TEAL }), t(i.who_bears_it, { size: 17 })], { after: 60 }));
    k.push(para([t("Recommended APRA position.  ", { size: 17, bold: true, color: TEAL }), t(i.recommended_apra_position, { size: 17 }), prov(i.provenance)], { after: 60 }));
    k.push(para([
      t("Scoring.  ", { size: 15, bold: true, color: MUTED }),
      t(`Materiality ${i.materiality}/5 · Likelihood ${i.likelihood}/5 · APRA proximity ${i.apra_proximity}/5 · Action: ${i.action_type}`, { size: 15, color: MUTED }),
    ], { after: 40 }));
    k.push(para([
      t("Instruments.  ", { size: 15, bold: true, color: MUTED }),
      t((i.instruments || []).join("; ") || "—", { size: 15, color: MUTED }),
    ], { after: 40 }));
    k.push(para([
      t("Evidence.  ", { size: 15, bold: true, color: MUTED }),
      t((i.evidence_refs || []).join("  ·  ") || "—", { size: 14, color: MUTED }),
    ], { after: 60 }));
  });

  // --- Annex B: framework mapping
  k.push(pageBreak());
  k.push(h2("Annex B — Prudential framework mapping", { before: 0 }));
  k.push(para("One row per instrument examined, including those needing no change — the absence of a required change is itself a finding.", { after: 120, size: 17, color: SECOND }));
  const WB = [2100, 2700, 3106, 1300, 700];
  k.push(table(
    [
      { key: "instrument", label: "Instrument", w: WB[0] },
      { key: "current_requirement", label: "What it requires now", w: WB[1] },
      { key: "div296_stress", label: "What Division 296 stresses", w: WB[2] },
      { key: "verdict", label: "Verdict", w: WB[3] },
      { key: "confidence", label: "Conf.", w: WB[4], align: AlignmentType.CENTER },
    ],
    D.framework_verdicts || [],
    (r, c) => {
      if (c.key === "instrument") return [t(r.instrument, { size: 15, bold: true, color: NAVY })];
      if (c.key === "verdict") {
        const col = r.verdict === "amend-standard" ? MAGENTA : r.verdict === "update-guidance" ? COBALT : r.verdict === "supervisory-practice-only" ? TEAL : MUTED;
        return [t(r.verdict.replace(/-/g, " "), { size: 14, bold: true, color: col })];
      }
      if (c.key === "confidence") return [t(r.confidence, { size: 14, color: MUTED })];
      return [t(r[c.key], { size: 14, color: SECOND })];
    }
  ));

  // --- Annex B2: the verified figures, in full
  if ((D.all_headline_numbers || []).length) {
    k.push(h2("Annex B2 — The figures, verified"));
    k.push(para("Every figure re-checked against a named source with a date. Where a figure in the draft was wrong, the correction is stated rather than quietly applied.", { after: 120, size: 17, color: SECOND }));
    const WN = [3400, 4600, 1906];
    k.push(table(
      [
        { key: "figure", label: "Figure", w: WN[0] },
        { key: "meaning", label: "What it means, and any correction", w: WN[1] },
        { key: "source", label: "Source / as at", w: WN[2] },
      ],
      D.all_headline_numbers,
      (r, c) => {
        if (c.key === "figure") return [t(r.figure, { size: 14, bold: true, color: NAVY })];
        if (c.key === "source") return [t(`${r.source}${r.as_at ? " · " + r.as_at : ""}`, { size: 13, color: MUTED })];
        return [t(r.meaning, { size: 13, color: SECOND })];
      }
    ));
  }

  // --- Annex C: audit trail
  k.push(pageBreak());
  k.push(h2("Annex C — Provenance and fact-check audit trail", { before: 0 }));
  k.push(para("Every material assertion in the brief, classified and checked. 'Created' entries are original analysis written for this meeting and are marked so they are never mistaken for sourced fact.", { after: 120, size: 17, color: SECOND }));
  const WC = [3900, 800, 4306, 900];
  k.push(table(
    [
      { key: "assertion", label: "Assertion", w: WC[0] },
      { key: "provenance", label: "Type", w: WC[1], align: AlignmentType.CENTER },
      { key: "basis", label: "Basis — citation, or reasoning chain", w: WC[2] },
      { key: "verified", label: "Check", w: WC[3], align: AlignmentType.CENTER },
    ],
    D.audit_trail || [],
    (r, c) => {
      if (c.key === "provenance") {
        return [new TextRun({ text: (B.PROV_TAG[r.provenance] || "?"), font: FONT, size: 16, bold: true, color: PROV_COLOR[r.provenance] || MUTED })];
      }
      if (c.key === "verified") {
        const col = r.verified === "verified" ? "00806D" : r.verified === "contested" ? MAGENTA : ORANGE;
        return [t(r.verified, { size: 13, bold: true, color: col })];
      }
      if (c.key === "assertion") return [t(r.assertion, { size: 14 })];
      return [t(r.basis, { size: 13, color: SECOND })];
    }
  ));

  // --- Annex D: red team
  k.push(pageBreak());
  k.push(h2("Annex D — Red-team challenge and disposition", { before: 0 }));
  k.push(para(D.redteam_intro || "The draft register was attacked by three independent adversarial reviewers: a hostile fact-checker, a grading sceptic, and a completeness critic. Every challenge was dispositioned — accepted, partially accepted, or rejected with reasons.", { after: 120, size: 17, color: SECOND }));
  const WD = [4300, 1500, 4106];
  k.push(table(
    [
      { key: "attack", label: "Challenge raised", w: WD[0] },
      { key: "outcome", label: "Outcome", w: WD[1], align: AlignmentType.CENTER },
      { key: "reasoning", label: "Reasoning", w: WD[2] },
    ],
    D.redteam_disposition || [],
    (r, c) => {
      if (c.key === "outcome") {
        const col = r.outcome === "accepted-and-fixed" ? "00806D" : r.outcome === "partially-accepted" ? ORANGE : MUTED;
        return [t(r.outcome.replace(/-/g, " "), { size: 13, bold: true, color: col })];
      }
      if (c.key === "attack") return [t(r.attack, { size: 14 })];
      return [t(r.reasoning, { size: 13, color: SECOND })];
    }
  ));

  // --- Annex E1: points to carry into engagement
  if ((D.open_consultation_asks || []).length) {
    k.push(h2("Annex E1 — Points to carry into engagement with Treasury and the ATO"));
    k.push(para("Both public consultations on this measure have closed, so these are points for bilateral engagement and the ATO co-design process rather than a submission. They are confined to prudential and member-outcomes consequences; the tax design remedies are left to the policy owner.", { after: 120, size: 17, color: SECOND }));
    (D.open_consultation_asks || []).forEach(a =>
      k.push(bullet([t(typeof a === "string" ? a : a.text, { size: 17 })])));
  }

  // --- Annex E2: uncertainties
  k.push(h2("Annex E2 — What we still do not know"));
  k.push(para("Stated plainly so the meeting does not over-read the analysis.", { after: 100, size: 17, color: SECOND }));
  (D.residual_uncertainties || []).forEach(u => k.push(bullet([t(u, { size: 17 })])));

  // --- Annex F: sources
  k.push(h2("Annex F — Sources consulted"));
  (D.sources || []).forEach(s => k.push(new Paragraph({
    children: [t(s, { size: 13, color: SECOND })],
    spacing: { after: 30, line: 230 },
  })));

  return k;
}

// ------------------------------------------------------------------ doc -----
const doc = new Document({
  creator: "APRA", title: D.meta.title, description: D.meta.subtitle,
  styles: { default: { document: { run: { font: FONT, size: 19, color: INK } } } },
  numbering: {
    config: [{
      reference: "brief-bullets",
      levels: [
        { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 250, hanging: 170 } }, run: { color: COBALT, size: 19 } } },
        { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 520, hanging: 170 } }, run: { color: TEAL, size: 18 } } },
      ],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: A4_W, height: A4_H },
        margin: { top: MARGIN_Y, bottom: MARGIN_Y, left: MARGIN_X, right: MARGIN_X, footer: 560 },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          children: [
            t(D.meta.classification + "  ·  " + D.meta.footer_note, { size: 13, color: MUTED }),
            new TextRun({ text: "\t", font: FONT }),
            new TextRun({ children: ["Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES], font: FONT, size: 13, color: MUTED }),
          ],
          tabStops: [{ type: "right", position: CONTENT_W }],
          border: { top: { style: BorderStyle.SINGLE, size: 4, color: B.RULE, space: 6 } },
          spacing: { before: 0 },
        })],
      }),
    },
    children: [...pageOne(), ...pageTwo(), ...pageThree(), ...annexes()],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT, buf);
  console.log(`wrote ${OUT}  (${(buf.length / 1024).toFixed(0)} KB)`);
});
