"""
APRA-branded chart harness for the Division 296 prudential brief.

Palette is APRA's own brand identity (from the APRA template), snapped to steps
that pass the dataviz colour checks:

    Core series (validated all-pairs, any chart form):
        cobalt #0072CE, orange #E87722, teal #00B398
    Extended (adjacent-pairs only; ships with direct labels):
        + magenta #B03A75, indigo #454E93

Relief rule: orange and teal sit below 3:1 on white, so every chart here ships
visible direct labels. Do not remove them.

Typeface: Liberation Sans (metric-compatible with Arial, APRA's brand font).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe

# ---------------------------------------------------------------- palette ----
NAVY       = "#012169"   # APRA navy - headings and ink
COBALT     = "#0072CE"   # accent1  - series 1
TEAL       = "#00B398"   # accent2  - series 3
ORANGE     = "#E87722"   # accent4  - series 2
MAGENTA    = "#890C58"   # accent5  - dark anchor
MAGENTA_LT = "#B03A75"   # lightened magenta - series 4 (passes lightness band)
INDIGO     = "#454E93"   # accent6  - series 5
LIGHTBLUE  = "#B5D5EE"   # fill tint only, never a series
PALEBLUE   = "#E3F3FA"
NEARWHITE  = "#F4F9FC"

SERIES = [COBALT, ORANGE, TEAL, MAGENTA_LT, INDIGO]

# ink / chrome
TEXT_PRIMARY   = "#1A1A1A"
TEXT_SECONDARY = "#52514E"
MUTED          = "#898781"
GRID           = "#E1E0D9"
BASELINE       = "#C3C2B7"
SURFACE        = "#FFFFFF"

# Grade ramp - ORDINAL, single warm hue family, light to dark.
# Severity reads as depth; the letter label always accompanies it, so colour
# never carries the meaning alone.
GRADE_COLOR = {"A": MAGENTA, "B": ORANGE, "C": "#C9A227"}
GRADE_FILL  = {"A": "#F2E1EA", "B": "#FCEADC", "C": "#F7F1DC"}

# Verdict colours for the framework map - categorical, from the core three
VERDICT_COLOR = {
    "amend-standard":           MAGENTA,
    "update-guidance":          COBALT,
    "supervisory-practice-only": TEAL,
    "no-change":                "#B8B7B0",
}
VERDICT_LABEL = {
    "amend-standard":           "Amend standard",
    "update-guidance":          "Update guidance",
    "supervisory-practice-only": "Supervisory practice",
    "no-change":                "No change",
}

# --- dollar-sign guard -------------------------------------------------------
# Matplotlib treats a PAIR of $ as LaTeX mathtext, so "$3m - $10m" silently
# renders in italic math. Every label in this brief is full of dollar amounts,
# and the data comes from research output we do not control, so escape centrally
# at the draw call rather than trusting each call site.
import matplotlib.axes as _maxes
import matplotlib.text as _mtext


def esc(s):
    """Escape $ so matplotlib renders it literally instead of entering mathtext."""
    if isinstance(s, str) and "$" in s:
        return s.replace("\\$", "$").replace("$", r"\$")
    return s


for _cls, _meth in ((_maxes.Axes, "text"), (_maxes.Axes, "set_title"),
                    (_maxes.Axes, "set_xlabel"), (_maxes.Axes, "set_ylabel"),
                    (_mtext.Text, "set_text")):
    def _wrap(orig):
        def inner(self, *a, **kw):
            a = list(a)
            for i, val in enumerate(a):
                if isinstance(val, str):
                    a[i] = esc(val)
                    break
            if "label" in kw:
                kw["label"] = esc(kw["label"])
            return orig(self, *a, **kw)
        return inner
    setattr(_cls, _meth, _wrap(getattr(_cls, _meth)))


plt.rcParams.update({
    "font.family":      "Liberation Sans",
    "font.size":        9,
    "text.color":       TEXT_PRIMARY,
    "axes.labelcolor":  TEXT_SECONDARY,
    "axes.edgecolor":   BASELINE,
    "xtick.color":      MUTED,
    "ytick.color":      MUTED,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "figure.facecolor": SURFACE,
    "axes.facecolor":   SURFACE,
    "savefig.facecolor": SURFACE,
    "savefig.dpi":      300,
    "figure.dpi":       300,
})


def _save(fig, path):
    fig.savefig(path, bbox_inches="tight", pad_inches=0.06, facecolor=SURFACE)
    plt.close(fig)
    print(f"  wrote {path}")


def _title(ax, title, subtitle=None):
    # Subtitle sits just above the axes; the title is padded clear ABOVE it.
    # (set_title's pad is measured from the axes, not from the subtitle, so the
    # pad must exceed the subtitle's own height or the two overlap.)
    ax.set_title(title, loc="left", fontsize=11, fontweight="bold",
                 color=NAVY, pad=26 if subtitle else 8)
    if subtitle:
        ax.text(0, 1.012, subtitle, transform=ax.transAxes, fontsize=8,
                color=TEXT_SECONDARY, va="bottom", ha="left")


# ============================================================ FIGURE 1 =======
def fig_tier_ladder(path, tiers, note=None):
    """The regime at a glance: marginal tax rate by balance band.

    tiers: list of dicts {band, rate, extra, color_key, width}
    A stepped ladder, not a chart - each step direct-labelled with its rate.
    """
    fig, ax = plt.subplots(figsize=(7.2, 2.35))
    ax.set_xlim(0, 100); ax.set_ylim(0, 46)
    ax.axis("off")

    x = 0.0
    for i, t in enumerate(tiers):
        w = t["width"]
        col = t["color"]
        # step block, thin mark with rounded top corners
        ax.add_patch(FancyBboxPatch(
            (x + 0.6, 0), w - 1.2, t["rate"],
            boxstyle="round,pad=0,rounding_size=1.1",
            linewidth=0, facecolor=col, mutation_aspect=0.34, zorder=2))
        # rate label sits inside the block when tall enough, above when not
        cx = x + w / 2
        if t["rate"] >= 16:
            ax.text(cx, t["rate"] - 4.6, f"{t['rate']}%", ha="center", va="center",
                    fontsize=15, fontweight="bold", color="white", zorder=4)
        else:
            ax.text(cx, t["rate"] + 2.4, f"{t['rate']}%", ha="center", va="bottom",
                    fontsize=15, fontweight="bold", color=col, zorder=4)
        # the Division 296 increment, called out
        if t.get("extra"):
            ax.text(cx, t["rate"] - 11.5, t["extra"], ha="center", va="center",
                    fontsize=7.4, color="white", zorder=4, linespacing=1.35)
        # band label under the baseline
        ax.text(cx, -2.6, t["band"], ha="center", va="top", fontsize=8.4,
                fontweight="bold", color=NAVY)
        ax.text(cx, -7.4, t["sub"], ha="center", va="top", fontsize=7.2,
                color=TEXT_SECONDARY, linespacing=1.35)
        x += w

    ax.plot([0, 100], [0, 0], color=BASELINE, lw=1.2, zorder=3)
    ax.text(0, 43.5, "Tax rate on earnings", fontsize=8, color=TEXT_SECONDARY)
    if note:
        ax.text(0, -16.5, note, fontsize=7, color=MUTED, va="top", linespacing=1.4)
    _save(fig, path)


# ============================================================ FIGURE 2 =======
def fig_grade_map(path, issues, note=None):
    """Graded prudential issue map.

    x = how directly it is APRA's lever, y = prudential materiality,
    bubble size = likelihood, colour+letter = grade. Every point direct-labelled.
    """
    fig, ax = plt.subplots(figsize=(7.2, 4.3))

    # quadrant wash - recessive, purely orienting
    ax.add_patch(Rectangle((3.0, 3.0), 2.6, 2.6, facecolor=PALEBLUE,
                           edgecolor="none", zorder=0, alpha=0.75))
    # anchored bottom-right of the wash, clear of the y=5 / x=5 bubble lanes
    ax.text(5.60, 3.10, "APRA's own lever\nand highly material",
            ha="right", va="bottom", fontsize=7.2, color=COBALT,
            style="italic", linespacing=1.4, zorder=1)

    for i in (1, 2, 3, 4, 5):
        ax.axhline(i, color=GRID, lw=0.6, zorder=1)
        ax.axvline(i, color=GRID, lw=0.6, zorder=1)

    # Issues sharing a cell would stack invisibly - fan them around the point
    # so every bubble stays readable and none is hidden.
    from collections import defaultdict
    cells = defaultdict(list)
    for it in issues:
        cells[(it["apra_proximity"], it["materiality"])].append(it)

    import math
    for (px, py), group in cells.items():
        n = len(group)
        for j, it in enumerate(group):
            if n == 1:
                dx = dy = 0.0
            else:
                ang = 2 * math.pi * j / n + math.pi / 4
                r = 0.20 if n <= 4 else 0.26
                dx, dy = r * math.cos(ang), r * math.sin(ang)
            col = GRADE_COLOR[it["grade"]]
            size = (150 + (it["likelihood"] ** 2) * 26) * (0.62 if n > 1 else 1.0)
            ax.scatter(px + dx, py + dy, s=size, facecolor=col,
                       edgecolor="white", linewidth=2.0, zorder=4, alpha=0.94)
            ax.text(px + dx, py + dy, it["id"], ha="center", va="center",
                    fontsize=6.6 if n > 1 else 7.4, fontweight="bold",
                    color="white", zorder=5)

    ax.set_xlim(0.45, 5.75); ax.set_ylim(0.45, 5.75)
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_xlabel("How directly APRA can act on it  →", fontsize=8.4)
    ax.set_ylabel("Prudential materiality  →", fontsize=8.4)
    ax.tick_params(length=0)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(BASELINE)

    handles = [Line2D([], [], marker="o", linestyle="none", markersize=9,
                      markerfacecolor=GRADE_COLOR[g], markeredgecolor="white",
                      markeredgewidth=1.4,
                      label={"A": "Grade A — raise in this meeting",
                             "B": "Grade B — press and monitor",
                             "C": "Grade C — watch"}[g])
               for g in ("A", "B", "C")]
    handles.append(Line2D([], [], marker="o", linestyle="none", markersize=6,
                          markerfacecolor=MUTED, markeredgecolor="white",
                          label="Bubble size = likelihood"))
    ax.legend(handles=handles, loc="lower left", frameon=False, fontsize=7.6,
              handletextpad=0.5, borderpad=0.2, labelspacing=0.5)

    _title(ax, "Where the prudential risk actually sits",
           "Bubble size shows likelihood. Letters are issue IDs — see the table.")
    if note:
        ax.text(0, -0.175, note, transform=ax.transAxes, fontsize=7,
                color=MUTED, va="top", linespacing=1.4)
    _save(fig, path)


# ============================================================ FIGURE 3 =======
def fig_framework_map(path, verdicts, note=None):
    """What the prudential framework actually needs - one row per instrument.

    Text is wrapped to its column and row heights follow the tallest cell, so
    long instrument names or stress descriptions never run into the verdict.
    """
    import textwrap

    order = ["amend-standard", "update-guidance",
             "supervisory-practice-only", "no-change"]
    verdicts = sorted(verdicts, key=lambda v: order.index(v["verdict"]))

    # column geometry on a 0-10 canvas
    X_MARK, X_INST, X_STRESS, X_VERD = 0.06, 0.62, 4.15, 9.94
    WRAP_INST, WRAP_STRESS = 32, 50

    rows = []
    for v in verdicts:
        inst = textwrap.wrap(v["instrument"], WRAP_INST) or [""]
        stress = textwrap.wrap(v["div296_stress"], WRAP_STRESS) or [""]
        rows.append((v, inst, stress, max(len(inst), len(stress))))

    LINE_H = 0.30            # height of one text line, in canvas units
    PAD = 0.22               # padding above+below the text block
    heights = [n * LINE_H + PAD for _, _, _, n in rows]
    total = sum(heights)

    fig, ax = plt.subplots(figsize=(7.2, total * 0.62 + 1.05))
    ax.set_xlim(0, 10)

    y = 0.0
    for (v, inst, stress, nlines), h in zip(reversed(rows), reversed(heights)):
        col = VERDICT_COLOR[v["verdict"]]
        top, bot = y + h, y
        mid = y + h / 2
        ax.add_patch(Rectangle((0, bot + 0.05), 10, h - 0.10,
                               facecolor=NEARWHITE, edgecolor="none", zorder=1))
        ax.add_patch(FancyBboxPatch((X_MARK, bot + 0.13), 0.30, h - 0.26,
                                    boxstyle="round,pad=0,rounding_size=0.09",
                                    facecolor=col, edgecolor="none", zorder=2))

        def block(x, lines, **kw):
            y0 = mid + (len(lines) - 1) * LINE_H / 2
            for j, ln in enumerate(lines):
                ax.text(x, y0 - j * LINE_H, ln, va="center", zorder=3, **kw)

        block(X_INST, inst, ha="left", fontsize=8.2, fontweight="bold", color=NAVY)
        block(X_STRESS, stress, ha="left", fontsize=7.5, color=TEXT_SECONDARY)
        ax.text(X_VERD, mid, VERDICT_LABEL[v["verdict"]], va="center",
                ha="right", fontsize=7.5, fontweight="bold", color=col, zorder=3)
        y += h

    ax.set_ylim(-0.55, total + 0.62)
    ax.axis("off")
    hy = total + 0.20
    ax.text(X_INST, hy, "Prudential instrument", fontsize=7.3,
            fontweight="bold", color=MUTED, va="center")
    ax.text(X_STRESS, hy, "What Division 296 stresses", fontsize=7.3,
            fontweight="bold", color=MUTED, va="center")
    ax.text(X_VERD, hy, "Verdict", fontsize=7.3, fontweight="bold",
            color=MUTED, ha="right", va="center")
    if note:
        ax.text(0, -0.30, note, fontsize=7, color=MUTED, va="top",
                linespacing=1.4)
    _save(fig, path)


# ============================================================ FIGURE 4 =======
def fig_timeline(path, events, today_x=None, note=None):
    """Implementation runway - what happens when, and APRA's windows to act.

    Markers are drawn with plot(marker=...) in POINT units, not Circle patches in
    data units: the axes scales differ by ~30x, so data-unit circles render as
    ellipses.  Past events are filled; future events are hollow.
    """
    fig, ax = plt.subplots(figsize=(7.2, 2.7))
    ax.set_xlim(0, 100); ax.set_ylim(-3.6, 3.6)
    ax.axis("off")

    # spine: solid through elapsed time, lighter ahead of today
    if today_x is not None:
        ax.plot([2, today_x], [0, 0], color=COBALT, lw=3.0, alpha=0.30,
                solid_capstyle="round", zorder=1)
        ax.plot([today_x, 98], [0, 0], color=LIGHTBLUE, lw=3.0,
                solid_capstyle="round", zorder=1)
    else:
        ax.plot([2, 98], [0, 0], color=LIGHTBLUE, lw=3.0,
                solid_capstyle="round", zorder=1)

    for i, e in enumerate(events):
        x = e["x"]
        up = (i % 2 == 0)
        col = e.get("color", COBALT)
        done = e.get("done", False)
        stem = 0.78 if up else -0.78
        ax.plot([x, x], [0, stem], color=col, lw=1.5, zorder=2, alpha=0.8)
        ax.plot([x], [0], marker="o", markersize=11,
                markerfacecolor=col if done else "white",
                markeredgecolor=col, markeredgewidth=2.0, zorder=4)

        # date always sits nearest the spine; label reads outward from it
        va = "bottom" if up else "top"
        d = 1 if up else -1
        ax.text(x, 1.05 * d, e["date"], ha="center", va=va, fontsize=7.9,
                fontweight="bold", color=col, zorder=5)
        ax.text(x, 1.62 * d, e["label"], ha="center", va=va, fontsize=7.2,
                color=TEXT_SECONDARY, linespacing=1.45, zorder=5)

    # "you are here"
    if today_x is not None:
        ax.plot([today_x, today_x], [-0.55, 0.55], color=NAVY, lw=1.8,
                zorder=6, solid_capstyle="round")
        ax.text(today_x, 0.85, "TODAY", ha="center", va="bottom", fontsize=6.8,
                fontweight="bold", color=NAVY, zorder=6,
                path_effects=[pe.withStroke(linewidth=2.6, foreground="white")])

    if note:
        ax.text(2, -3.15, note, fontsize=7, color=MUTED, va="top",
                linespacing=1.4)
    _save(fig, path)


# ============================================================ FIGURE 5 =======
def fig_perimeter(path, segments, note=None, title="", subtitle=""):
    """Single stacked bar - where the affected balances sit, and who supervises.

    Direct-labelled (relief rule) with a 2px surface gap between segments.
    """
    fig, ax = plt.subplots(figsize=(7.2, 1.95))
    ax.set_xlim(0, 100); ax.set_ylim(-1.9, 1.55)
    ax.axis("off")

    x = 0.0
    for s in segments:
        w = s["pct"]
        ax.add_patch(FancyBboxPatch((x + 0.16, -0.32), max(w - 0.32, 0.4), 0.64,
                                    boxstyle="round,pad=0,rounding_size=0.09",
                                    facecolor=s["color"], edgecolor="none",
                                    zorder=2))
        if w >= 9:
            ax.text(x + w / 2, 0, f"{s['pct']:g}%", ha="center", va="center",
                    fontsize=11, fontweight="bold", color="white", zorder=3)
        ax.text(x + w / 2, 0.52, s["label"], ha="center", va="bottom",
                fontsize=8, fontweight="bold", color=s["color"], zorder=3)
        ax.text(x + w / 2, -0.50, s["sub"], ha="center", va="top", fontsize=7.2,
                color=TEXT_SECONDARY, linespacing=1.4, zorder=3)
        x += w

    if title:
        ax.text(0, 1.42, title, fontsize=11, fontweight="bold", color=NAVY,
                va="top")
    if subtitle:
        ax.text(0, 1.02, subtitle, fontsize=8, color=TEXT_SECONDARY, va="top")
    if note:
        ax.text(0, -1.42, note, fontsize=7, color=MUTED, va="top",
                linespacing=1.4)
    _save(fig, path)


# ============================================================ FIGURE 6 =======
def fig_action_split(path, counts, note=None):
    """How many issues fall to APRA vs Treasury/ATO - a small honest tally."""
    fig, ax = plt.subplots(figsize=(3.4, 2.2))
    labels = [c["label"] for c in counts]
    vals   = [c["n"] for c in counts]
    cols   = [c["color"] for c in counts]
    ypos   = range(len(labels))[::-1]

    for y, v, c, l in zip(ypos, vals, cols, labels):
        ax.add_patch(FancyBboxPatch((0, y - 0.22), v, 0.44,
                                    boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=c, edgecolor="none", zorder=2))
        ax.text(v + 0.18, y, str(v), va="center", ha="left", fontsize=9,
                fontweight="bold", color=c, zorder=3)
        ax.text(0, y + 0.40, l, va="bottom", ha="left", fontsize=7.6,
                color=TEXT_SECONDARY, zorder=3)

    ax.set_xlim(0, max(vals) * 1.35); ax.set_ylim(-0.7, len(labels) - 0.18)
    ax.axis("off")
    if note:
        ax.text(0, -0.62, note, fontsize=7, color=MUTED, va="top")
    _save(fig, path)
