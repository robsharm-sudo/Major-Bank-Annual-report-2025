"""
Pulls the workflow's final verified register out of the run journal.

    python3 extract_research.py <journal.jsonl> <out.json>

The journal records one entry per agent return. The final register is the last
entry carrying an audit_trail, which only the fact-check agent produces. Falling
back to the last entry with issues lets us still salvage the pre-fact-check
register if that final agent died, rather than silently emitting nothing.
"""
import json
import sys

journal, out = sys.argv[1], sys.argv[2]

results = []
for line in open(journal):
    try:
        d = json.loads(line)
    except ValueError:
        continue
    if d.get("type") != "result":
        continue
    r = d.get("result", d.get("value"))
    if isinstance(r, str):
        try:
            r = json.loads(r)
        except ValueError:
            continue
    if isinstance(r, dict):
        results.append(r)

verified = [r for r in results if r.get("audit_trail")]
if verified:
    final, stage = verified[-1], "fact-checked"
else:
    drafts = [r for r in results if r.get("issues")]
    if not drafts:
        sys.exit("no register found in journal — nothing to extract")
    final, stage = drafts[-1], "DRAFT (fact-check missing)"

# Sources are spread across the research streams, not repeated in the register.
sources = []
for r in results:
    for s in r.get("key_sources", []):
        if s not in sources:
            sources.append(s)

json.dump({"final": final, "sources": sources}, open(out, "w"), indent=2)

iss = final.get("issues", [])
print(f"extracted [{stage}] -> {out}")
print(f"  issues {len(iss)}  "
      f"A={sum(1 for i in iss if i.get('grade') == 'A')} "
      f"B={sum(1 for i in iss if i.get('grade') == 'B')} "
      f"C={sum(1 for i in iss if i.get('grade') == 'C')}")
print(f"  framework verdicts {len(final.get('framework_verdicts', []))}")
print(f"  audit rows {len(final.get('audit_trail', []))}")
print(f"  red-team dispositions {len(final.get('redteam_disposition', []))}")
print(f"  residual uncertainties {len(final.get('residual_uncertainties', []))}")
print(f"  sources {len(sources)}")
