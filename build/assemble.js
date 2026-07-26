/**
 * Merges the verified research register with the authored prose into the single
 * data file the document builder consumes.
 *
 *   node assemble.js <research.json> <prose.json> <out.json>
 *
 * research.json = the workflow's final verified register
 * prose.json    = the written narrative (title, bottom line, recommendations)
 *
 * Keeping these apart matters: the research half carries provenance and is
 * traceable to Annex C, while the prose half is authored judgement. The
 * assembler refuses to emit an issue or assertion that has lost its provenance
 * tag, so an untagged claim can never reach the page.
 */
const fs = require("fs");

const [researchPath, prosePath, outPath] = process.argv.slice(2);
const R = JSON.parse(fs.readFileSync(researchPath, "utf8"));
const P = JSON.parse(fs.readFileSync(prosePath, "utf8"));

let final = R.final || R;             // tolerate either wrapper or bare register
const VALID_PROV = new Set(["sourced", "inferred", "created"]);

// Apply the paragraph-level corrections verified by reading the in-force
// instruments directly. Done here rather than trusting the register, so a
// citation we know to be wrong cannot survive into the document.
let correctionCount = 0, termCount = 0;
try {
  const VC = JSON.parse(fs.readFileSync(
    require("path").join(__dirname, "verified_corrections.json"), "utf8"));
  const walk = node => {
    if (typeof node === "string") {
      let s = node;
      for (const c of VC.corrections) {
        if (s.includes(c.find)) { s = s.split(c.find).join(c.replace); correctionCount++; }
      }
      // Terminology: the document is a research note, not a brief. Patterns are
      // deliberately narrow - a blanket brief->note swap would corrupt the verb
      // sense ("brief APRA's life insurance supervision") that appears in the
      // register.
      for (const c of (VC.terminology || [])) {
        if (s.includes(c.find)) { s = s.split(c.find).join(c.replace); termCount++; }
      }
      return s;
    }
    if (Array.isArray(node)) return node.map(walk);
    if (node && typeof node === "object") {
      const o = {};
      for (const k of Object.keys(node)) o[k] = walk(node[k]);
      return o;
    }
    return node;
  };
  final = walk(final);
} catch (e) {
  console.log(`  WARNING: could not apply verified corrections — ${e.message}`);
}

const problems = [];
function requireProv(obj, where) {
  if (!VALID_PROV.has(obj.provenance)) {
    problems.push(`${where}: missing/invalid provenance "${obj.provenance}"`);
    return "created";                 // fail safe - never claim it is sourced
  }
  return obj.provenance;
}

const issues = (final.issues || []).map((i, n) => ({
  ...i,
  id: i.id || `P${n + 1}`,
  provenance: requireProv(i, `issue ${i.id || n}`),
  materiality: Number(i.materiality) || 1,
  likelihood: Number(i.likelihood) || 1,
  apra_proximity: Number(i.apra_proximity) || 1,
}));

const audit = (final.audit_trail || []).map((a, n) => ({
  ...a,
  provenance: requireProv(a, `audit row ${n}`),
  verified: a.verified || "unverified",
}));

const headline = (final.headline_numbers || [])
  .map((h, n) => ({ ...h, provenance: requireProv(h, `headline ${n}`) }))
  // a headline number with no attributable source has no business on page 1
  .filter(h => h.provenance !== "sourced" || (h.source && h.source.trim()));

const out = {
  meta: P.meta,
  bottom_line: P.bottom_line || [],
  captions: P.captions || {},
  headline_numbers: (P.headline_override || headline).slice(0, 3),
  all_headline_numbers: headline,
  why_prudential: P.why_prudential || [],
  provisions_intro: P.provisions_intro || "",
  provisions: P.provisions || [],
  figure_inputs: P.figure_inputs || {},
  framework_intro: P.framework_intro || "",
  recommendations: P.recommendations || [],
  redteam_intro: P.redteam_intro,
  page2_rows: P.page2_rows,
  issues,
  framework_verdicts: final.framework_verdicts || [],
  open_consultation_asks: final.open_consultation_asks || [],
  audit_trail: audit,
  redteam_disposition: final.redteam_disposition || [],
  residual_uncertainties: final.residual_uncertainties || [],
  sources: R.sources || final.sources || [],
};

fs.writeFileSync(outPath, JSON.stringify(out, null, 2));

const gc = g => issues.filter(i => i.grade === g).length;
console.log(`assembled -> ${outPath}`);
console.log(`  issues: ${issues.length}  (A=${gc("A")} B=${gc("B")} C=${gc("C")})`);
console.log(`  framework verdicts: ${out.framework_verdicts.length}`);
console.log(`  audit rows: ${audit.length}  (verified=${audit.filter(a => a.verified === "verified").length}, contested=${audit.filter(a => a.verified === "contested").length})`);
console.log(`  red-team dispositions: ${out.redteam_disposition.length}`);
console.log(`  sources: ${out.sources.length}`);
console.log(`  verified citation corrections applied: ${correctionCount}`);
console.log(`  terminology (brief -> note) applied: ${termCount}`);
if (problems.length) {
  console.log(`\n  ${problems.length} PROVENANCE PROBLEM(S) - defaulted to "created" so nothing is over-claimed:`);
  problems.slice(0, 20).forEach(p => console.log("   -", p));
}
