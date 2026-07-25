# Model risk management — draft cross-industry standard, practice guide and gap assessment

**Policy development draft — not in force.** Nothing in this repository has legal effect.
Instrument numbers are placeholders. Information was verified to **25 July 2026**.

## Deliverables

| File | What it is |
|---|---|
| `CPS_XXXX_Model_Risk_Management.docx` | Draft cross-industry prudential standard. 44 bold mandatory requirements with plain-text explanatory guidance beneath each, and six annexes including a full international comparison. 28 pages, Arial throughout. |
| `CPG_XXXX_Model_Risk_Management.docx` | Draft prudential practice guide. 131 numbered "should" paragraphs across 15 chapters, with cross-reference strips, source attribution carrying legal-status codes, and amber verification annotations. 34 pages. |
| `MRM_Regulatory_Comparison_and_Improvement_Assessment.xlsx` | 15-sheet evidence base: gap scoring with a documented methodology, an eight-authority crosswalk, requirement-by-authority challenge, traceability, statement provenance ledger, red-team audit trail and source register. 249 live formulas. |

Bold means mandatory. Everything not bold is explanatory and imposes no obligation.

## The eight authorities compared

APRA · US OCC / Federal Reserve / FDIC · PRA (UK) · OSFI (Canada) · ECB and SSM (EU) ·
MAS (Singapore) · BCBS · FSB.

Legal status differs sharply between them and is recorded for every source. An overseas
instrument is not binding in Australia whatever its status at home, and several of the most
influential model risk instruments are supervisory guidance rather than law even in their
home jurisdiction.

## What the scoring measures

How well the **current** Australian prudential framework addresses each of 34 model risk
domains, against the strongest comparator practice in that domain. It does not score entity
maturity and does not rank the comparator authorities against one another.

Each domain is scored 0–5 on coverage, specificity, enforceability and international
alignment. Gap is `max(0, benchmark − domain score)`; priority is `gap × domain weight`,
banded Critical / High / Medium / Low. Weights and band thresholds are editable inputs on
the Scoring Methodology sheet, and everything downstream recalculates.

## Reproducing and re-verifying

Everything is generated from the content modules under `build/`, so the artefacts and the
audit trail can be regenerated and re-checked rather than taken on trust.

```bash
pip install python-docx openpyxl mcp
python build/build_cps_xxxx.py
python build/build_cpg_xxxx.py
python build/build_workbook.py
```

### MCP server

`mcp/mrm_policy_server.py` exposes the pipeline as tools so it can be executed and repeated
from an agent session. Register it with the `.mcp.json` at the repository root.

| Tool | Purpose |
|---|---|
| `build_package` | Regenerate any or all of the three deliverables, optionally recalculating the workbook |
| `verify_package` | Cross-reference integrity, source coverage, typography and the bold-means-mandatory invariant |
| `check_source_urls` | Fetch every registered source URL and report which still resolve |
| `list_requirements`, `get_requirement` | Query the requirement register, with guidance inlined |
| `list_sources`, `get_principles`, `get_crosswalk` | Query the evidence base and the verbatim principles register |
| `get_audit_trail` | Red-team corrections and the statement provenance ledger |
| `score_gaps`, `scoring_methodology` | Recompute the assessment under different weights; return the rubric |

`check_source_urls` is the one worth re-running before relying on the package: regulatory
URLs move and instruments get rescinded.

## Repository layout

```
build/
  content_requirements.py   the 44 mandatory requirements, with provenance and rationale
  content_guide.py          the practice guide, paragraph numbering derived at build time
  content_sources.py        source register, crosswalk, principles register, audit trail
  content_scoring.py        the gap scoring model and its rubric
  docx_common.py            shared Word furniture and the typography audit
  xlsx_common.py            shared workbook furniture
  build_*.py                the three builders
mcp/
  mrm_policy_server.py      MCP server wrapping the pipeline
```

Cross-references between the standard and the guide are computed from the guide's own
paragraph numbering at build time, so the two documents cannot drift apart.

## A note on what was corrected

The package was red-teamed against primary sources across five challenge lenses and 53
corrections are recorded in the Red Team Audit sheet. The most consequential: **OCC Bulletin 2011-12 / Federal Reserve
SR 11-7 was rescinded on 17 April 2026** and replaced by interagency guidance SR 26-2 /
OCC 2026-13 / FDIC FIL-15-2026, which narrows the model definition, expressly excludes
generative and agentic AI, applies mainly above $30 billion in total assets and is
non-enforceable by its own terms. Drafting that cited the 2011 formulations was repointed
or, where the current US position diverges from what this standard proposes, the divergence
is stated openly rather than concealed behind a citation.
