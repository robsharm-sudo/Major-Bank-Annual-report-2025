"""
Pulls the verified register out of the workflow run journal.

    python3 extract_research.py <journal.jsonl> <out.json>

The fact-check stage is split across four agents, each returning one slice of
the register (issues / framework / audit trail / red-team disposition), because
a single combined output exceeds the model's output-token ceiling. This stitches
the slices back together by key, taking the LAST result that carries each key so
a resumed run supersedes the draft it replaced.

Missing slices are reported loudly rather than silently emitted as empty - an
absent audit trail must never look like a clean one.
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


def last_with(key):
    """Last result carrying key, so a resumed pass supersedes the draft."""
    for r in reversed(results):
        if r.get(key):
            return r
    return None


SLICES = {
    "issues": ["issues"],
    "framework_verdicts": ["framework_verdicts", "headline_numbers", "open_consultation_asks"],
    "audit_trail": ["audit_trail", "residual_uncertainties"],
    "redteam_disposition": ["redteam_disposition"],
}

final, missing = {}, []
for anchor, keys in SLICES.items():
    src = last_with(anchor)
    if src is None:
        missing.append(anchor)
        continue
    for k in keys:
        if src.get(k):
            final[k] = src[k]

if "issues" not in final:
    sys.exit("FATAL: no issue register found in journal — nothing to build from")

sources = []
for r in results:
    for s in r.get("key_sources", []):
        if s not in sources:
            sources.append(s)

json.dump({"final": final, "sources": sources}, open(out, "w"), indent=2)

iss = final["issues"]
print(f"extracted -> {out}")
print(f"  issues {len(iss)}  "
      f"A={sum(1 for i in iss if i.get('grade') == 'A')} "
      f"B={sum(1 for i in iss if i.get('grade') == 'B')} "
      f"C={sum(1 for i in iss if i.get('grade') == 'C')}")
print(f"  framework verdicts    {len(final.get('framework_verdicts', []))}")
print(f"  headline numbers      {len(final.get('headline_numbers', []))}")
print(f"  consultation asks     {len(final.get('open_consultation_asks', []))}")
print(f"  audit rows            {len(final.get('audit_trail', []))}")
print(f"  red-team dispositions {len(final.get('redteam_disposition', []))}")
print(f"  residual uncertainties{len(final.get('residual_uncertainties', []))}")
print(f"  sources               {len(sources)}")
if missing:
    print(f"\n  *** MISSING SLICES: {', '.join(missing)} — the brief must not claim these were verified.")
