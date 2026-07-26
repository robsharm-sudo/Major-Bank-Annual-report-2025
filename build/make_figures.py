"""
Renders every figure in the brief from the assembled data file.

    python3 make_figures.py <assembled.json>

Figures 1 and 4 are fixed infographics (the rate structure and the runway);
figures 2, 3, 5 and 6 are driven by the verified register, so re-running this
after the register changes keeps the visuals and the tables in agreement.
"""
import json
import sys
import os
import apra_viz as v

DATA = json.load(open(sys.argv[1]))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
issues = DATA.get("issues", [])
fw = DATA.get("framework_verdicts", [])
fig = DATA.get("figure_inputs", {})


def p(name):
    return os.path.join(OUT, name)


# --- Figure 1: what the tax charges, and on which slice -----------------------
v.fig_tier_ladder(p("fig1_tiers.png"), [
    dict(band="Up to $3m", sub="Standard super\nearnings tax", rate=15,
         width=34, color=v.COBALT, extra=None),
    dict(band="$3m – $10m", sub="Division 296 adds 15%\non earnings from this slice",
         rate=30, width=33, color=v.ORANGE, extra="15% fund tax\n+ 15% Div 296"),
    dict(band="Above $10m", sub="Division 296 adds 25%\non earnings from this slice",
         rate=40, width=33, color=v.MAGENTA, extra="15% fund tax\n+ 25% Div 296"),
], note=("Rates shown for accumulation-phase earnings. Retirement-phase earnings are untaxed in the fund, so the Division 296\n"
         "charge there is the full 15% or 25% rather than an increment. Both thresholds are indexed. The charge applies only to\n"
         "earnings attributable to the slice of a balance above each threshold, not to the whole balance."))

# --- Figure 2: the graded issue map ------------------------------------------
if issues:
    v.fig_grade_map(p("fig2_grade_map.png"), issues,
                    note=fig.get("fig2_note", ""), show_title=False)

# --- Figure 3: what the framework needs --------------------------------------
# Counts, not an instrument-by-instrument map: with 27 verdicts the map renders
# far taller than a page. The full per-instrument detail is Annex B.
if fw:
    ORDER = [
        ("no-change", "No change needed", "#B8B7B0"),
        ("supervisory-practice-only", "Supervisory\nattention only", v.TEAL),
        ("update-guidance", "Updated\nguidance", v.COBALT),
        ("amend-standard", "Amend a\nstandard", v.MAGENTA),
    ]
    counts = [dict(label=lab, n=sum(1 for x in fw if x.get("verdict") == key), color=col)
              for key, lab, col in ORDER]
    counts = [c for c in counts if c["n"] > 0]
    amend = [x["instrument"] for x in fw if x.get("verdict") == "amend-standard"]
    v.fig_verdict_summary(
        p("fig3_framework.png"), counts,
        callout=(f"The one amendment: {amend[0].split('(')[0].strip()}" if amend else None),
        note=fig.get("fig3_note", ""))

# --- Figure 4: the runway ----------------------------------------------------
v.fig_timeline(p("fig4_timeline.png"), [
    dict(x=5,  date="13 Mar 2026", label="Royal Assent", color=v.MUTED, done=True),
    dict(x=19, date="1 Apr 2026",  label="Division 296\ncommences", color=v.MUTED, done=True),
    dict(x=33, date="1 Jul 2026",  label="2026–27 income year:\nfirst measurement\nyear begins", color=v.COBALT, done=True),
    dict(x=55, date="2026–27",     label="ATO co-design group\nsettles calculation\nand attribution", color=v.ORANGE),
    dict(x=73, date="30 Jun 2027", label="First measurement\nof balances", color=v.TEAL),
    dict(x=93, date="2027–28",     label="First assessments\n& release authorities", color=v.MAGENTA),
], today_x=38, note=fig.get("fig4_note", ""))

# --- Figure 5: the perimeter -------------------------------------------------
per = fig.get("perimeter")
if per:
    v.fig_perimeter(p("fig5_perimeter.png"), [
        dict(pct=per["smsf_pct"], label="In SMSFs",
             sub="ATO-regulated —\noutside APRA's perimeter", color=v.ORANGE),
        dict(pct=per["apra_pct"], label="In APRA-regulated funds",
             sub="Where APRA's standards\nand data apply", color=v.COBALT),
    ], title=per.get("title", ""), subtitle=per.get("subtitle", ""),
       note=per.get("note", ""))

# --- Figure 6: whose lever is it ---------------------------------------------
if issues:
    def n_for(kinds):
        return sum(1 for i in issues if i.get("action_type") in kinds)
    counts = [
        dict(label="APRA can act directly — guidance or supervision",
             n=n_for({"new-or-updated-guidance", "supervisory-practice"}), color=v.COBALT),
        dict(label="Needs a change to a prudential standard",
             n=n_for({"standard-amendment"}), color=v.TEAL),
        dict(label="Treasury or ATO policy — outside APRA's control",
             n=n_for({"legislative-change"}), color=v.ORANGE),
        dict(label="Monitor only", n=n_for({"no-change-monitor"}), color="#B8B7B0"),
    ]
    counts = [c for c in counts if c["n"] > 0]
    if counts:
        v.fig_action_split(p("fig6_split.png"), counts,
                           note=fig.get("fig6_note", ""))

print("figures rendered ->", os.path.normpath(OUT))
