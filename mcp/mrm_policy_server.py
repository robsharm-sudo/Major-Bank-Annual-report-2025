#!/usr/bin/env python3
"""MCP server for the CPS XXXX / CPG XXXX model risk management package.

Exposes the drafting pipeline as callable tools so the package can be
regenerated, queried, re-verified and re-scored without re-running the
research by hand.

Run directly for stdio transport:

    python mcp/mrm_policy_server.py

Or register it with Claude Code via the .mcp.json at the repository root.

Tools fall into four groups:

  build      regenerate the three deliverables from the content modules
  verify     integrity checks — cross-references, source coverage, live URLs
  query      read the requirement register, sources, principles, audit trail
  score      recompute the gap assessment, optionally with different weights
"""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
BUILD = REPO / "build"
sys.path.insert(0, str(BUILD))

from mcp.server.fastmcp import FastMCP  # noqa: E402

import content_guide as G  # noqa: E402
import content_requirements as R  # noqa: E402
import content_scoring as SC  # noqa: E402
import content_sources as S  # noqa: E402

mcp = FastMCP("mrm-policy")

ARTEFACTS = {
    "standard": REPO / "CPS_XXXX_Model_Risk_Management.docx",
    "guide": REPO / "CPG_XXXX_Model_Risk_Management.docx",
    "workbook": REPO / "MRM_Regulatory_Comparison_and_Improvement_Assessment.xlsx",
}

BUILDERS = {
    "standard": "build_cps_xxxx.py",
    "guide": "build_cpg_xxxx.py",
    "workbook": "build_workbook.py",
}


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #

@mcp.tool()
def build_package(target: str = "all", recalculate: bool = True) -> dict[str, Any]:
    """Regenerate the deliverables from the content modules.

    Args:
        target: "all", "standard", "guide" or "workbook".
        recalculate: for the workbook, run LibreOffice so formula results are
            cached in the file. Requires libreoffice-calc; skip it if the
            environment has no LibreOffice and rely on Excel's calculate-on-load.

    Returns per-target exit status and the builder's stdout.
    """
    targets = list(BUILDERS) if target == "all" else [target]
    unknown = [t for t in targets if t not in BUILDERS]
    if unknown:
        return {"ok": False, "error": f"unknown target(s): {unknown}",
                "valid": list(BUILDERS) + ["all"]}

    results = {}
    for t in targets:
        proc = subprocess.run([sys.executable, BUILDERS[t]], cwd=BUILD,
                              capture_output=True, text=True, timeout=900)
        results[t] = {"exit_code": proc.returncode,
                      "stdout": proc.stdout.strip(),
                      "stderr": proc.stderr.strip()[-2000:] if proc.stderr else ""}

    if recalculate and "workbook" in targets and results["workbook"]["exit_code"] == 0:
        script = Path.home() / ".claude/skills/xlsx/scripts/recalc.py"
        if script.exists():
            proc = subprocess.run(
                [sys.executable, str(script), str(ARTEFACTS["workbook"]), "420"],
                capture_output=True, text=True, timeout=900)
            results["workbook"]["recalc"] = proc.stdout.strip()
        else:
            results["workbook"]["recalc"] = "recalc script not present; skipped"

    return {"ok": all(r["exit_code"] == 0 for r in results.values()), "results": results}


# --------------------------------------------------------------------------- #
# verify
# --------------------------------------------------------------------------- #

@mcp.tool()
def verify_package() -> dict[str, Any]:
    """Run every offline integrity check over the content and the built files.

    Checks requirement/guidance cross-references in both directions, source-ID
    coverage, typography and the bold-means-mandatory invariant, and the
    presence of each artefact. Does not touch the network — use
    check_source_urls for that.
    """
    from docx_common import audit_fonts

    problems: list[str] = []
    _, req_map, chapter_reqs, total_paras = G.numbered()
    req_ids = {r["id"] for r in R.REQUIREMENTS}

    # every requirement has guidance, and no guidance points at a phantom requirement
    missing = sorted(req_ids - set(req_map))
    if missing:
        problems.append(f"requirements with no guidance paragraph: {missing}")
    phantom = sorted(set(req_map) - req_ids)
    if phantom:
        problems.append(f"guidance references unknown requirement IDs: {phantom}")

    # Every source ID relied on must resolve to a real registered entry. Aliases are
    # deliberately not treated as registration: an alias once masked three citations to
    # instruments that either no longer exist or were the wrong document entirely.
    registered = {s["id"] for s in S.SOURCES}
    alias_targets = set(getattr(S, "SOURCE_ALIASES", {}).values())
    dangling = sorted(alias_targets - registered)
    if dangling:
        problems.append(f"source aliases pointing at unregistered entries: {dangling}")

    used: set[str] = set()
    for r in R.REQUIREMENTS:
        used.update(r["sources"])
    for d in SC.DOMAINS:
        used.update(d["sources"])
    unregistered = sorted(used - registered - set(getattr(S, "SOURCE_ALIASES", {})))
    if unregistered:
        problems.append(f"source IDs used but not registered: {unregistered}")

    # Authorities relied on by the principles register and the crosswalk must appear in
    # the source register too, not only those cited by a requirement.
    reg_authorities = {s["authority"] for s in S.SOURCES}
    for fw in S.PRINCIPLE_FRAMEWORKS:
        if fw["authority"] not in reg_authorities and fw["authority"] not in ("EU",):
            problems.append(
                f"principles register cites authority with no registered source: {fw['authority']}")

    # Every requirement must be covered by at least one scoring domain, or the assessment
    # measures something narrower than the standard it is assessing.
    scored = set()
    for d in SC.DOMAINS:
        scored.update(d["reqs"])
    uncovered = sorted({r["id"] for r in R.REQUIREMENTS} - scored)
    if uncovered:
        problems.append(f"requirements covered by no scoring domain: {uncovered}")

    # no requirement may rest on an unverified source
    unverified = {s["id"] for s in S.SOURCES if s["verification"].startswith("Unverified")}
    for r in R.REQUIREMENTS:
        bad = sorted(set(r["sources"]) & unverified)
        if bad:
            problems.append(f"{r['id']} relies on unverified source(s): {bad}")

    # scoring integrity
    for d in SC.DOMAINS:
        for rid in d["reqs"]:
            if rid not in req_ids:
                problems.append(f"gap domain '{d['domain']}' cites unknown requirement {rid}")
        if not 0 <= d["bench"] <= 5 or not 0 <= d["post"] <= 5:
            problems.append(f"gap domain '{d['domain']}' has a score outside 0-5")

    # built artefacts
    artefacts = {}
    for name, path in ARTEFACTS.items():
        if not path.exists():
            problems.append(f"artefact missing: {path.name}")
            artefacts[name] = {"exists": False}
            continue
        entry = {"exists": True, "bytes": path.stat().st_size}
        if path.suffix == ".docx":
            audit = audit_fonts(path)
            entry["requirement_paragraphs"] = audit["requirement_paras"]
            entry["guidance_paragraphs"] = audit["guidance_paras"]
            entry["typography_violations"] = len(audit["violations"])
            if audit["violations"]:
                problems.append(
                    f"{path.name}: {len(audit['violations'])} typography or "
                    f"bold/plain violations")
        artefacts[name] = entry

    return {
        "ok": not problems,
        "problems": problems,
        "counts": {
            "requirements": len(R.REQUIREMENTS),
            "guidance_paragraphs": total_paras,
            "guide_chapters": len(G.GUIDE),
            "scored_domains": len(SC.DOMAINS),
            "registered_sources": len(S.SOURCES),
            "crosswalk_topics": len(S.CROSSWALK_ROWS_FULL),
            "red_team_entries": len(S.REDTEAM_ROWS),
            "ledger_entries": len(S.LEDGER_ROWS),
            "policy_choices": sum(1 for r in R.REQUIREMENTS if r["policy_choice"]),
            "legal_flags": sum(1 for r in R.REQUIREMENTS if r["legal_flag"]),
        },
        "artefacts": artefacts,
    }


@mcp.tool()
def check_source_urls(timeout_seconds: int = 20) -> dict[str, Any]:
    """Fetch every registered source URL and report whether it still resolves.

    Regulatory URLs move and instruments get rescinded, so this is the check
    worth re-running before relying on the package. Reports status per source
    rather than failing on the first error.
    """
    def probe(src: dict) -> dict:
        url = src["url"]
        req = urllib.request.Request(
            url, method="GET",
            headers={"User-Agent": "Mozilla/5.0 (compatible; mrm-policy-check/1.0)"})
        try:
            with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
                return {"id": src["id"], "url": url, "status": resp.status, "ok": True}
        except urllib.error.HTTPError as e:
            return {"id": src["id"], "url": url, "status": e.code, "ok": e.code < 400}
        except Exception as e:
            return {"id": src["id"], "url": url, "status": None, "ok": False,
                    "error": type(e).__name__}

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(probe, S.SOURCES))

    failed = [r for r in results if not r["ok"]]
    return {"ok": not failed, "checked": len(results),
            "failed": failed, "results": results}


# --------------------------------------------------------------------------- #
# query
# --------------------------------------------------------------------------- #

@mcp.tool()
def list_requirements(part: str = "", policy_choices_only: bool = False,
                      legal_flags_only: bool = False) -> list[dict[str, Any]]:
    """List the CPS XXXX requirements, optionally filtered.

    Args:
        part: substring match against the part name, e.g. "Governance".
        policy_choices_only: only requirements not mandated by any comparator.
        legal_flags_only: only requirements carrying a legal-drafting reservation.
    """
    _, req_map, _, _ = G.numbered()
    out = []
    for r in R.REQUIREMENTS:
        if part and part.lower() not in r["part"].lower():
            continue
        if policy_choices_only and not r["policy_choice"]:
            continue
        if legal_flags_only and not r["legal_flag"]:
            continue
        out.append({
            "id": r["id"], "part": r["part"], "section": r["section"],
            "title": r["title"], "requirement": r["requirement"],
            "sources": r["sources"], "principles": r["principles"],
            "provenance": r["provenance"], "policy_choice": r["policy_choice"],
            "legal_flag": r["legal_flag"],
            "guidance_paragraphs": G.ranges(req_map.get(r["id"], [])),
        })
    return out


@mcp.tool()
def get_requirement(requirement_id: str) -> dict[str, Any]:
    """Return one requirement in full, with its guidance paragraphs inlined."""
    match = [r for r in R.REQUIREMENTS if r["id"].upper() == requirement_id.upper()]
    if not match:
        return {"error": f"unknown requirement {requirement_id}",
                "valid_ids": [r["id"] for r in R.REQUIREMENTS]}
    r = dict(match[0])
    flat, req_map, _, _ = G.numbered()
    nums = set(req_map.get(r["id"], []))
    r["guidance"] = [{"paragraph": it["n"], "chapter": it["chapter"], "text": it["t"]}
                     for it in flat if it["k"] == "p" and it.get("n") in nums]
    return r


@mcp.tool()
def list_sources(authority: str = "", unverified_only: bool = False) -> list[dict[str, Any]]:
    """Return the source register, optionally filtered by authority."""
    out = []
    for s in S.SOURCES:
        if authority and authority.lower() not in s["authority"].lower():
            continue
        if unverified_only and not s["verification"].startswith("Unverified"):
            continue
        out.append(s)
    return out


@mcp.tool()
def get_principles(authority: str = "") -> list[dict[str, Any]]:
    """Return the verbatim principles register for one or all authorities.

    Labels and titles are reproduced as printed by the issuing authority, so
    these are safe to cite directly in drafting.
    """
    return [f for f in S.PRINCIPLE_FRAMEWORKS
            if not authority or authority.lower() in f["authority"].lower()]


@mcp.tool()
def get_crosswalk(topic: str = "") -> list[dict[str, Any]]:
    """Return the eight-authority regulatory crosswalk, optionally by topic."""
    cols = ["topic", "APRA_current", "US", "PRA", "OSFI", "ECB", "MAS", "BCBS",
            "FSB", "proposed_CPS_XXXX"]
    out = []
    for row in S.CROSSWALK_ROWS_FULL:
        if topic and topic.lower() not in row[0].lower():
            continue
        out.append(dict(zip(cols, row)))
    return out


@mcp.tool()
def get_audit_trail(severity: str = "") -> dict[str, Any]:
    """Return the red-team correction audit trail and the statement ledger.

    Args:
        severity: filter red-team entries to "High", "Medium" or "Low".
    """
    rt_cols = ["id", "initial_statement", "challenge", "correction", "effect",
               "evidence", "severity", "status"]
    led_cols = ["id", "artefact", "topic", "statement", "provenance",
                "verification", "basis", "correction_trail"]
    rt = [dict(zip(rt_cols, r)) for r in S.REDTEAM_ROWS
          if not severity or r[6].lower() == severity.lower()]
    return {"red_team": rt,
            "statement_ledger": [dict(zip(led_cols, r)) for r in S.LEDGER_ROWS]}


# --------------------------------------------------------------------------- #
# score
# --------------------------------------------------------------------------- #

@mcp.tool()
def score_gaps(weights: dict[str, float] | None = None,
               critical: float = 4.5, high: float = 3.0,
               medium: float = 1.5) -> dict[str, Any]:
    """Recompute the gap assessment, optionally with different domain weights.

    This is the same calculation the workbook performs, exposed so alternative
    weightings can be explored without opening the file.

    Args:
        weights: domain name to weight. Unspecified domains keep their default.
        critical, high, medium: weighted-gap thresholds for the priority bands.
    """
    weights = weights or {}
    unknown = [k for k in weights if k not in {d["domain"] for d in SC.DOMAINS}]
    if unknown:
        return {"error": f"unknown domain(s): {unknown}",
                "valid_domains": [d["domain"] for d in SC.DOMAINS]}

    rows = []
    for d in SC.DOMAINS:
        w = weights.get(d["domain"], d["weight"])
        now = round(sum(d["au"]) / 4.0, 2)
        gap = round(max(0.0, d["bench"] - now) * w, 2)
        band = ("Critical" if gap >= critical else
                "High" if gap >= high else
                "Medium" if gap >= medium else "Low")
        rows.append({
            "domain": d["domain"], "weight": w, "au_score_now": now,
            "benchmark": d["bench"], "benchmark_authority": d["bench_auth"],
            "weighted_gap": gap, "priority": band,
            "expected_after_cps_240": d["post"],
            "uplift": round(d["post"] - now, 2),
            "observed_gap": d["gap"], "recommended_action": d["action"],
            "requirements": d["reqs"], "owner": d["owner"],
        })
    rows.sort(key=lambda r: -r["weighted_gap"])

    return {
        "thresholds": {"critical": critical, "high": high, "medium": medium},
        "summary": {
            "domains": len(rows),
            "mean_au_score_now": round(sum(r["au_score_now"] for r in rows) / len(rows), 2),
            "mean_expected_after": round(sum(r["expected_after_cps_240"] for r in rows) / len(rows), 2),
            "total_weighted_gap": round(sum(r["weighted_gap"] for r in rows), 2),
            "critical": sum(1 for r in rows if r["priority"] == "Critical"),
            "high": sum(1 for r in rows if r["priority"] == "High"),
            "medium": sum(1 for r in rows if r["priority"] == "Medium"),
            "low": sum(1 for r in rows if r["priority"] == "Low"),
        },
        "domains": rows,
    }


@mcp.tool()
def scoring_methodology() -> dict[str, Any]:
    """Return the scoring rubric, dimensions, bands and default weights."""
    return {
        "what_is_scored": (
            "How well the CURRENT Australian prudential framework addresses each "
            "model risk domain, measured against the strongest comparator practice. "
            "Not entity maturity, and not a ranking of comparator authorities."),
        "dimensions": [{"name": n, "question": q} for n, q in SC.DIMENSIONS],
        "rubric": [{"score": s, "label": l, "meaning": m} for s, l, m in SC.RUBRIC],
        "bands": [{"band": b, "weighted_gap_at_or_above": t, "meaning": m}
                  for b, t, m in SC.BANDS],
        "derivation": {
            "domain_score": "mean of the four dimension scores",
            "gap": "max(0, benchmark - domain score)",
            "weighted_gap": "gap x domain weight",
            "priority": "weighted gap banded against the thresholds",
        },
        "default_weights": {d["domain"]: d["weight"] for d in SC.DOMAINS},
        "limitations": [
            "Scores are informed judgements against published instruments, not measurements.",
            "The benchmark is the strongest comparator practice, which is a demanding bar.",
            "Legal status is scored as it stands in the home jurisdiction and implies nothing "
            "about effect in Australia.",
            "The expected post-CPS XXXX score is a design expectation, not an outcome.",
        ],
    }


if __name__ == "__main__":
    mcp.run()
