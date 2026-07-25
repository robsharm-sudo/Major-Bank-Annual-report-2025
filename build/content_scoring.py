"""Gap scoring model for the model risk management assessment workbook.

The question the scoring answers is narrow and stated deliberately:

    Against the strongest comparator practice, how well does the *current*
    Australian prudential framework address each model risk domain, and how
    much of that gap would the proposed CPS 240 close?

It does not score entity maturity, and it does not rank the comparator
authorities against one another. A low Australian score is a statement about
the framework as it stands today, before CPS 240, and is the basis for the
"areas for improvement" register.

Scoring runs on four dimensions, each 0-5:

  COVERAGE       Is the domain addressed at all?
  SPECIFICITY    Is the expectation stated precisely enough to be supervised
                 and evidenced, rather than as a general principle?
  ENFORCEABILITY Does it sit in a binding instrument, or in guidance?
  ALIGNMENT      Does it match what the strongest comparator does?

Each domain carries a weight reflecting prudential significance. The weighted
priority is  (benchmark - australia_now) x weight, banded into Critical / High /
Medium / Low. Weights and band thresholds are live inputs in the workbook so a
reader can re-weight and watch priorities move.
"""

RUBRIC = [
    (5, "Leading practice",
     "Addressed comprehensively in a binding instrument, with expectations specific enough to be "
     "evidenced and supervised. Matches or exceeds the strongest comparator."),
    (4, "Strong",
     "Addressed in a binding instrument with clear expectations. Minor gaps in specificity or in "
     "coverage of edge cases relative to the strongest comparator."),
    (3, "Adequate",
     "Addressed, but either in guidance rather than a binding instrument, or in a binding "
     "instrument at a level of generality that leaves material discretion."),
    (2, "Partial",
     "Addressed indirectly or by implication, through a general obligation not specific to model "
     "risk. Compliance would be difficult to evidence or to supervise consistently."),
    (1, "Incidental",
     "Touched on only for a narrow class of models or entities, or mentioned without expectation."),
    (0, "Absent",
     "Not addressed in the framework at all."),
]

DIMENSIONS = [
    ("Coverage", "Is the domain addressed at all in the framework?"),
    ("Specificity", "Is the expectation precise enough to be evidenced and supervised?"),
    ("Enforceability", "Binding instrument, guidance, or nothing?"),
    ("Alignment", "Does it match the strongest comparator practice?"),
]

BANDS = [
    ("Critical", 4.5, "Framework gap of a kind that could permit material unmanaged model risk. "
                      "Address before or at consultation."),
    ("High", 3.0, "Significant divergence from the strongest comparator with a clear prudential "
                  "rationale for closing it."),
    ("Medium", 1.5, "Meaningful but not urgent. Suitable for the practice guide or for supervisory "
                    "attention rather than a new obligation."),
    ("Low", 0.0, "Broadly comparable to international practice. No action proposed."),
]

# --------------------------------------------------------------------------- #
# Domain assessment
#
# au = (coverage, specificity, enforceability, alignment) for the Australian
#      framework AS IT STANDS TODAY, before CPS 240.
# post = expected weighted domain score once CPS 240 and CPG 240 are in force.
# bench = the strongest comparator score, with the authority that sets it.
# --------------------------------------------------------------------------- #

DOMAINS = [
    {
        "domain": "Definition of a model and of model risk",
        "weight": 1.50,
        "au": (1, 1, 2, 1),
        "bench": 5, "bench_auth": "PRA / OSFI",
        "post": 4.5,
        "reqs": ["M02", "M03"],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23"],
        "gap": "No APRA instrument defines a model or model risk on a cross-industry basis. Model "
               "requirements exist only inside the capital and actuarial standards and apply only "
               "to the models those standards cover.",
        "action": "Adopt a broad function-based definition of a model and of model risk on a "
                  "cross-industry basis, with an express obligation to identify and control "
                  "quantitative tools falling outside it. Do not follow the April 2026 United "
                  "States narrowing, which would exclude actuarial and unit pricing calculations.",
        "owner": "Policy",
    },
    {
        "domain": "Enterprise-wide scope and retained accountability",
        "weight": 1.25,
        "au": (2, 2, 3, 2),
        "bench": 5, "bench_auth": "OSFI",
        "post": 4.5,
        "reqs": ["M01"],
        "sources": ["OSFI-E23", "US-MRM-2026", "APRA-CPS220"],
        "gap": "CPS 220 requires a risk management framework covering material risks but does not "
               "name model risk, so enterprise-wide coverage depends on each entity's own "
               "characterisation.",
        "action": "State enterprise-wide application expressly and confirm that accountability is "
                  "retained where a model is supplied or operated by another party.",
        "owner": "Policy",
    },
    {
        "domain": "Model inventory",
        "weight": 1.25,
        "au": (1, 1, 2, 1),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M13"],
        "sources": ["PRA-SS1-23", "OSFI-E23", "US-MRM-2026"],
        "gap": "No cross-industry inventory obligation. Without one, no other model risk obligation "
               "can be evidenced as complete, and APRA cannot assess sector-wide reliance.",
        "action": "Require a complete, current, controlled enterprise inventory including embedded, "
                  "third-party and recently decommissioned models, with minimum fields specified.",
        "owner": "Policy + Supervision",
    },
    {
        "domain": "Model risk tiering and proportionality",
        "weight": 1.25,
        "au": (2, 1, 3, 2),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M04", "M14", "M15"],
        "sources": ["PRA-SS1-23", "OSFI-E23"],
        "gap": "Proportionality is a general principle across APRA standards but there is no model "
               "risk classification taxonomy, so control intensity is not systematically linked to "
               "model risk.",
        "action": "Require a documented tiering methodology using quantitative and qualitative "
                  "factors that demonstrably drives validation, monitoring and approval intensity.",
        "owner": "Policy",
    },
    {
        "domain": "Board oversight of model risk",
        "weight": 1.50,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M05", "M12"],
        "sources": ["PRA-SS1-23", "OSFI-E23", "APRA-CPS220"],
        "gap": "CPS 220 gives the Board responsibility for the risk management framework, but model "
               "risk is not identified as a risk requiring Board attention in its own right and no "
               "reporting content is specified.",
        "action": "Require Board approval of the model risk framework and appetite, supported by "
                  "aggregate, decision-useful reporting rather than model counts.",
        "owner": "Policy",
    },
    {
        "domain": "Senior accountability for the framework",
        "weight": 1.25,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M06", "M07"],
        "sources": ["PRA-SS1-23", "OSFI-E23"],
        "gap": "No named accountability for model risk as a discipline. Accountability for "
               "individual models is implicit in business ownership but framework-level failures "
               "have no owner.",
        "action": "Require a named senior executive accountable for the framework, plus a named "
                  "owner for each model, and settle the interaction with the accountability regime.",
        "owner": "Policy + Legal",
    },
    {
        "domain": "Model risk appetite",
        "weight": 1.00,
        "au": (2, 1, 3, 2),
        "bench": 4, "bench_auth": "PRA",
        "post": 4.0,
        "reqs": ["M10"],
        "sources": ["PRA-SS1-23", "OSFI-E23", "APRA-CPS220"],
        "gap": "Risk appetite obligations are general. Model risk is rarely expressed in appetite "
               "statements in monitorable terms, so it cannot be breached or escalated.",
        "action": "Require an appetite for model risk expressed so that it can be measured, with "
                  "limits, thresholds and escalation triggers.",
        "owner": "Policy",
    },
    {
        "domain": "Development and conceptual soundness",
        "weight": 1.25,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "US interagency (OCC/FRB/FDIC)",
        "post": 4.5,
        "reqs": ["M16"],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "ECB-GIM"],
        "gap": "Development standards exist only for capital models under APS 113 and for actuarial "
               "work. Models outside those regimes have no development expectation.",
        "action": "Require documented development standards, conceptual soundness, consideration of "
                  "alternatives and recording of limitations across all material models.",
        "owner": "Policy",
    },
    {
        "domain": "Data quality, provenance and appropriateness",
        "weight": 1.25,
        "au": (3, 2, 3, 3),
        "bench": 5, "bench_auth": "BCBS / ECB",
        "post": 4.5,
        "reqs": ["M17"],
        "sources": ["BCBS-239", "ECB-RDARR", "APRA-CPG235", "OSFI-E23"],
        "gap": "CPG 235 provides a data governance foundation but is a practice guide, is dated, and "
               "does not address model-specific concerns such as proxy data, representativeness or "
               "synthetic data.",
        "action": "Require model data to be assessed for appropriateness as well as quality, with "
                  "lineage to source and documented treatment of proxies and synthetic data.",
        "owner": "Policy + Data",
    },
    {
        "domain": "Documentation and reproducibility",
        "weight": 1.00,
        "au": (2, 2, 3, 2),
        "bench": 5, "bench_auth": "ECB / PRA",
        "post": 4.5,
        "reqs": ["M18"],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "ECB-GIM"],
        "gap": "No cross-industry documentation standard for models. Documentation adequacy is "
               "assessed only where a capital or actuarial standard applies.",
        "action": "Adopt the reconstruction test: documentation sufficient for an independent "
                  "competent person to reproduce material results.",
        "owner": "Policy",
    },
    {
        "domain": "Pre-implementation testing",
        "weight": 1.25,
        "au": (2, 1, 3, 2),
        "bench": 5, "bench_auth": "PRA / ECB",
        "post": 4.5,
        "reqs": ["M19"],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23"],
        "gap": "No general bar on using an untested model. Testing expectations exist only within "
               "the capital model approval process.",
        "action": "Establish an explicit gate: a model must not be used for a material purpose until "
                  "tested and residual limitations accepted.",
        "owner": "Policy",
    },
    {
        "domain": "Independent validation",
        "weight": 1.50,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "PRA",
        "post": 5.0,
        "reqs": ["M20", "M21", "M24"],
        "sources": ["PRA-SS1-23", "US-MRM-2026", "OSFI-E23", "ECB-GIM"],
        "gap": "Independent validation is required for IRB models under APS 113 and, in a different "
               "form, through the Appointed Actuary. There is no general requirement, so a model "
               "driving material decisions outside those regimes may never be independently "
               "reviewed.",
        "action": "Require independent validation for material models, structured around conceptual "
                  "soundness, ongoing monitoring and outcomes analysis, at an intensity set by tier.",
        "owner": "Policy + Supervision",
    },
    {
        "domain": "Effective challenge",
        "weight": 1.50,
        "au": (1, 1, 2, 1),
        "bench": 5, "bench_auth": "US interagency (OCC/FRB/FDIC)",
        "post": 4.5,
        "reqs": ["M22"],
        "sources": ["US-MRM-2026", "PRA-SS1-23"],
        "gap": "The concept is absent from the Australian framework. Validation can exist on paper "
               "without the competence, standing or incentives that make it effective, and nothing "
               "currently requires an entity to test whether challenge works.",
        "action": "Require effective challenge expressly, and expect entities to assess whether it "
                  "is operating through finding closure routes and severity migration.",
        "owner": "Policy + Supervision",
    },
    {
        "domain": "Approval and conditions of use",
        "weight": 1.00,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "ECB",
        "post": 4.5,
        "reqs": ["M23"],
        "sources": ["ECB-GIM", "OSFI-E23", "US-MRM-2026"],
        "gap": "Approval requirements exist for capital models only. Elsewhere, models enter use "
               "without a recorded approval of version, purpose or conditions.",
        "action": "Require version-specific approval for a defined purpose and conditions, recording "
                  "limits, thresholds, accepted limitations and review date.",
        "owner": "Policy",
    },
    {
        "domain": "Implementation controls",
        "weight": 1.00,
        "au": (1, 1, 3, 1),
        "bench": 5, "bench_auth": "ECB",
        "post": 4.0,
        "reqs": ["M24"],
        "sources": ["ECB-GIM", "US-MRM-2026", "OSFI-E23"],
        "gap": "Nothing requires verification that the deployed model reproduces the approved one. "
               "This is a recurrent source of failure that methodological validation does not catch.",
        "action": "Require pre-production verification against the approved model and re-verification "
                  "after material infrastructure or pipeline change.",
        "owner": "Policy + Technology",
    },
    {
        "domain": "Change management and re-approval",
        "weight": 1.25,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "ECB",
        "post": 4.5,
        "reqs": ["M25"],
        "sources": ["ECB-GIM", "OSFI-E23", "PRA-SS1-23"],
        "gap": "Model change control is prescribed only for capital models. Cumulative change and "
               "vendor-initiated change are not addressed anywhere in the framework.",
        "action": "Require materiality assessment of changes individually and cumulatively, and "
                  "treat provider-initiated change as an entity change event.",
        "owner": "Policy",
    },
    {
        "domain": "Model use and misuse",
        "weight": 1.25,
        "au": (1, 1, 3, 1),
        "bench": 5, "bench_auth": "US interagency / ECB",
        "post": 4.5,
        "reqs": ["M26"],
        "sources": ["US-MRM-2026", "ECB-GIM", "PRA-SS1-23"],
        "gap": "Misuse is one of the two recognised sources of model risk and is entirely unaddressed "
               "outside the capital use test. Nothing requires users to be told a model's limitations.",
        "action": "Require use within approved purpose and conditions, and require limitations to be "
                  "communicated to users rather than merely recorded.",
        "owner": "Policy",
    },
    {
        "domain": "Overlays, adjustments and expert judgement",
        "weight": 1.25,
        "au": (2, 1, 3, 2),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M27"],
        "sources": ["PRA-SS1-23", "ECB-GIM"],
        "gap": "Post-model adjustments can become the dominant driver of a reported figure without "
               "any single approval considering that effect. No Australian instrument governs them "
               "generally or requires aggregate reporting.",
        "action": "Require governance of the basis, quantification, approval, duration and removal of "
                  "overlays, and aggregate reporting of them.",
        "owner": "Policy",
    },
    {
        "domain": "Ongoing monitoring and drift",
        "weight": 1.25,
        "au": (2, 2, 3, 2),
        "bench": 5, "bench_auth": "US interagency / OSFI",
        "post": 4.5,
        "reqs": ["M28"],
        "sources": ["US-MRM-2026", "OSFI-E23", "PRA-SS1-23"],
        "gap": "Monitoring expectations are limited to specific model classes. Thresholds are rarely "
               "linked to a defined response, so deterioration produces reporting rather than action.",
        "action": "Require monitoring at tier-based frequency with pre-set thresholds linked to "
                  "investigation, restriction, revalidation or withdrawal.",
        "owner": "Policy + Risk",
    },
    {
        "domain": "Limitations, mitigants and remediation",
        "weight": 1.00,
        "au": (2, 1, 3, 2),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M29"],
        "sources": ["PRA-SS1-23", "US-MRM-2026"],
        "gap": "No requirement to record model limitations, apply compensating controls or track "
               "remediation to completion. Findings can be closed by explanation without change.",
        "action": "Require recorded limitations, specific compensating controls, tracked remediation "
                  "and escalation of overdue material findings.",
        "owner": "Policy",
    },
    {
        "domain": "Decommissioning and retirement",
        "weight": 0.75,
        "au": (1, 1, 2, 1),
        "bench": 4, "bench_auth": "OSFI",
        "post": 4.0,
        "reqs": ["M30"],
        "sources": ["OSFI-E23", "APRA-CPS230"],
        "gap": "Retired models whose outputs remain in force — provisions, capital numbers, unit "
               "prices, insurance liabilities — are not addressed anywhere.",
        "action": "Require managed decommissioning covering downstream models, outputs still in "
                  "force, records and data disposition.",
        "owner": "Policy",
    },
    {
        "domain": "Third-party and vendor models",
        "weight": 1.25,
        "au": (2, 2, 4, 2),
        "bench": 5, "bench_auth": "US interagency / PRA",
        "post": 4.5,
        "reqs": ["M31", "M32"],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "BCBS-TPRM", "APRA-CPS230"],
        "gap": "CPS 230 governs service providers but not the model risk in a supplied model. "
               "Opacity is commonly accepted from vendors at a level that would not be accepted "
               "internally.",
        "action": "Apply the full framework to third-party models, require usable information rights "
                  "without mandating source-code access, and require compensating controls where "
                  "information is unavailable.",
        "owner": "Policy + Operational Risk",
    },
    {
        "domain": "Concentration and substitutability",
        "weight": 1.00,
        "au": (2, 1, 3, 2),
        "bench": 4, "bench_auth": "FSB / BCBS",
        "post": 4.0,
        "reqs": ["M32"],
        "sources": ["FSB-AI-2024", "BCBS-TPRM", "APRA-CPS230"],
        "gap": "Bilateral service provider assessment does not capture correlated reliance on a "
               "common external model, data source or platform across the industry.",
        "action": "Require entity-level concentration assessment and support sector-wide monitoring "
                  "of common model and data dependencies.",
        "owner": "Supervision + Data",
    },
    {
        "domain": "AI and machine learning models",
        "weight": 1.25,
        "au": (2, 2, 3, 2),
        "bench": 5, "bench_auth": "OSFI",
        "post": 4.5,
        "reqs": ["M33", "M34"],
        "sources": ["OSFI-E23", "MAS-AIMRM-2024", "BCBS-DIGI", "FSB-AI-2024"],
        "gap": "AI model risk is being addressed through a separate AI workstream, creating a risk "
               "that a model built with AI techniques is governed as an AI system but not as a "
               "model, or the reverse.",
        "action": "Bring AI models within the model risk framework as a model class, with an "
                  "explicit boundary rule against the AI risk instrument so nothing falls between.",
        "owner": "Policy",
    },
    {
        "domain": "Regulatory capital and internal models",
        "weight": 1.50,
        "au": (4, 4, 5, 4),
        "bench": 5, "bench_auth": "ECB",
        "post": 4.75,
        "reqs": ["M35"],
        "sources": ["APRA-APS113", "ECB-GIM", "ECB-CRR", "PRA-SS1-23"],
        "gap": "This is the strongest part of the Australian framework. The residual gap is the "
               "absence of a general model risk discipline around the capital model estate, and "
               "less developed guidance on model change than the ECB provides.",
        "action": "Preserve the capital standards unchanged and position CPS 240 to sit alongside "
                  "them, with the more specific requirement prevailing.",
        "owner": "Policy + Capital",
    },
    {
        "domain": "Valuation and financial reporting models",
        "weight": 1.25,
        "au": (2, 2, 3, 2),
        "bench": 4, "bench_auth": "BCBS",
        "post": 4.0,
        "reqs": ["M36"],
        "sources": ["BCBS-FVP", "ECB-GIM"],
        "gap": "Valuation model governance and independent price verification are not addressed on a "
               "cross-industry basis, despite the output being the reported number itself.",
        "action": "Bring valuation and expected credit loss models expressly within scope and require "
                  "independent price verification as a control distinct from validation.",
        "owner": "Policy",
    },
    {
        "domain": "Actuarial and insurance models",
        "weight": 1.25,
        "au": (3, 3, 4, 3),
        "bench": 4, "bench_auth": "OSFI",
        "post": 4.5,
        "reqs": ["M37"],
        "sources": ["APRA-CPS320", "OSFI-E23"],
        "gap": "The Appointed Actuary framework is a genuine strength but was not designed as model "
               "risk management. Implementation verification and data quality assessment are not "
               "reliably covered.",
        "action": "Require insurers to map which validation elements the actuarial control cycle "
                  "discharges and which need separate work.",
        "owner": "Policy + Insurance",
    },
    {
        "domain": "Superannuation models",
        "weight": 1.25,
        "au": (1, 1, 3, 1),
        "bench": 0, "bench_auth": "No comparator",
        "post": 4.0,
        "reqs": ["M38"],
        "sources": ["APRA-SPS530", "APRA-SPS515"],
        "gap": "No comparator authority addresses superannuation model risk, so there is no "
               "benchmark. Unit pricing and valuation models determine amounts credited to member "
               "accounts and errors transfer value between members irreversibly.",
        "action": "Name the RSE model classes expressly. Scored against the cross-industry benchmark "
                  "rather than a comparator, because none exists.",
        "owner": "Policy + Superannuation",
        "no_benchmark": True,
    },
    {
        "domain": "Stress testing and scenario models",
        "weight": 1.00,
        "au": (3, 2, 4, 3),
        "bench": 5, "bench_auth": "PRA / BCBS",
        "post": 4.5,
        "reqs": ["M39"],
        "sources": ["BCBS-STRESS", "PRA-SS3-18", "APRA-CPS220"],
        "gap": "APRA conducts stress testing but there is no standard governing the models used, "
               "whereas the PRA maintains a dedicated supervisory statement on model risk in stress "
               "testing.",
        "action": "Bring stress testing, scenario and capital planning models within scope, with "
                  "explicit treatment of assumption governance and of uncertainty disclosure.",
        "owner": "Policy + Supervision",
    },
    {
        "domain": "Aggregate model risk and capital",
        "weight": 1.25,
        "au": (1, 1, 2, 1),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.0,
        "reqs": ["M40"],
        "sources": ["PRA-SS1-23", "ECB-GIM"],
        "gap": "Nothing requires an entity to form a view of model risk in aggregate or to consider "
               "it in internal capital assessment, so correlated failure across models sharing data, "
               "vendors or assumptions is invisible.",
        "action": "Require aggregate assessment and consideration in internal capital assessment, "
                  "permitting qualitative measures where quantification is not yet feasible.",
        "owner": "Policy + Capital",
    },
    {
        "domain": "Records and reconstructability",
        "weight": 1.00,
        "au": (2, 2, 4, 2),
        "bench": 4, "bench_auth": "ECB",
        "post": 4.0,
        "reqs": ["M41"],
        "sources": ["ECB-GIM", "US-MRM-2026", "APRA-CPS220"],
        "gap": "General record-keeping obligations do not specify what must be retained to "
               "reconstruct a model's output, approval basis and performance.",
        "action": "Specify reconstructability for material models, with retention aligned to the "
                  "period over which the decisions informed remain material.",
        "owner": "Policy + Legal",
    },
    {
        "domain": "Independent assurance and internal audit",
        "weight": 1.25,
        "au": (3, 2, 4, 3),
        "bench": 5, "bench_auth": "PRA",
        "post": 4.5,
        "reqs": ["M42"],
        "sources": ["PRA-SS1-23", "US-MRM-2026", "ECB-GIM", "APRA-CPS220"],
        "gap": "Internal audit obligations are general. Audit of the model risk framework, and in "
               "particular of whether challenge is effective, is not specified and frequently "
               "lacks the technical capability to be meaningful.",
        "action": "Require periodic independent assessment of framework design and operating "
                  "effectiveness, including the effectiveness of validation and challenge.",
        "owner": "Policy + Assurance",
    },
    {
        "domain": "Supervisory engagement and notification",
        "weight": 1.00,
        "au": (3, 3, 4, 3),
        "bench": 4, "bench_auth": "OSFI",
        "post": 4.25,
        "reqs": ["M43"],
        "sources": ["APRA-CPS230", "APRA-CPS234", "OSFI-E23"],
        "gap": "Notification architecture is sound but does not identify model failure as a "
               "notifiable event, so a material model error may not be reported unless it also "
               "constitutes an operational incident.",
        "action": "Cross-reference existing CPS 230 and CPS 234 timeframes rather than create a "
                  "conflicting deadline, and expect early engagement on material model weakness.",
        "owner": "Policy + Legal",
    },
]


def au_score(d):
    """Unweighted mean of the four dimension scores."""
    return sum(d["au"]) / 4.0


def summary():
    rows = []
    for d in DOMAINS:
        now = au_score(d)
        gap = max(0.0, d["bench"] - now)
        rows.append({
            "domain": d["domain"],
            "now": now,
            "bench": d["bench"],
            "gap": gap,
            "weighted": gap * d["weight"],
            "post": d["post"],
        })
    return rows


assert len({d["domain"] for d in DOMAINS}) == len(DOMAINS), "duplicate domain"
assert all(0 <= v <= 5 for d in DOMAINS for v in d["au"]), "score out of range"
assert all(0 <= d["bench"] <= 5 for d in DOMAINS), "benchmark out of range"
assert all(0 <= d["post"] <= 5 for d in DOMAINS), "post score out of range"
