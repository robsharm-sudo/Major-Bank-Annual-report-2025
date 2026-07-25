"""CPS 240 requirement register — the operative content of the draft standard.

Each entry carries the mandatory sentence (rendered bold), the explanatory guidance
that sits beneath it (rendered plain), the source
IDs relied on, the international principle it maps to, and a provenance label.

Provenance vocabulary, inherited from the AI package supplied as input:
  Extracted            — close reflection of an explicit source requirement
  Extracted + inferred — synthesis across sources, faithful to each
  Inferred             — reasoned construction, no single source states it
  Policy choice        — a proposed requirement not directly mandated by any comparator

"Policy choice" does not mean unsupported. It means the drafter, not a comparator,
is the author of the obligation, and it therefore needs consultation and a
cost-benefit test before issue.
"""

REQUIREMENTS = [
    # ------------------------------------------------------------------ Part A
    {
        "id": "M01",
        "part": "Part A — Application and interpretation",
        "section": "1. Application and scope",
        "title": "Enterprise-wide application and retained accountability",
        "requirement": (
            "An APRA-regulated entity must identify, assess, manage, monitor and report "
            "model risk arising from every model that it develops, acquires, configures, "
            "deploys or relies upon, whether the model is built internally, supplied by a "
            "third party or embedded within another system, and remains accountable for "
            "that model risk irrespective of who developed or operates the model."
        ),
        "guidance": [
            "Model risk arises from the use of a model, not from its authorship. An entity that "
            "buys a model, licenses a platform containing one, inherits one through an acquisition "
            "or relies on a service provider's model is exposed to the consequences of that model "
            "being wrong or being used incorrectly, and cannot transfer that exposure by contract.",
            "Enterprise-wide means across all business lines, legal entities within the APRA-regulated "
            "group, and functions — including models used in finance, treasury, actuarial, capital, "
            "credit, markets, operations, compliance and human resources — and across all purposes, "
            "whether or not the model produces a regulatory number.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "APRA-CPS220", "ECB-GIM"],
        "principles": "US interagency guidance 2026 §III; PRA SS1/23 Principle 1; OSFI E-23 enterprise-wide MRM",
        "provenance": "Extracted",
        "rationale": (
            "Every comparator applies model risk management on an enterprise basis and none permits "
            "accountability to follow the model out of the institution."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M02",
        "part": "Part A — Application and interpretation",
        "section": "1. Application and scope",
        "title": "Definition of a model and of model risk",
        "requirement": (
            "An APRA-regulated entity must apply a documented definition of a model that captures any "
            "quantitative method, system or approach that applies statistical, economic, financial, "
            "actuarial or mathematical theories, techniques or assumptions to process input data into "
            "quantitative estimates, and must treat model risk as the potential for adverse consequences "
            "from decisions based on incorrect or misused model outputs."
        ),
        "guidance": [
            "The definition is deliberately function-based rather than technology-based. Whether the "
            "processing is a regression, a decision tree, a deterministic actuarial formula or a neural "
            "network does not change the analysis. It is also deliberately broad: it captures "
            "deterministic actuarial and financial calculations, which the current United States "
            "guidance excludes, because in an Australian cross-industry context such calculations "
            "determine insurance liabilities and unit prices and carry model risk of the first order.",
            "Model risk has two principal sources: a model may have fundamental errors and produce inaccurate "
            "outputs relative to its design objective and intended use; or a model may be used incorrectly or "
            "inappropriately, including outside the purpose for which it was approved. Both must be managed.",
            "Applying the definition should not become an exercise in avoiding scope. Where it is genuinely "
            "unclear whether a tool is a model, the entity should record the determination and the reasoning, "
            "and should manage the residual risk under this Prudential Standard or under an equivalent control.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23"],
        "principles": "PRA SS1/23 Principle 1.1 Model definition; OSFI E-23 (2027) key terms; US interagency guidance 2026 §II (narrower — excludes deterministic and arithmetic methods)",
        "provenance": "Extracted + inferred",
        "rationale": (
            "A broad, function-based definition follows the PRA and OSFI approach. The United States "
            "narrowed its definition in April 2026 to complex methods only, expressly excluding "
            "spreadsheet arithmetic and deterministic rule-based processes; that narrowing is not "
            "adopted here because it would exclude actuarial and unit pricing calculations central to "
            "the Australian cross-industry perimeter. The divergence is deliberate and recorded."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M03",
        "part": "Part A — Application and interpretation",
        "section": "1. Application and scope",
        "title": "Quantitative tools that are not models",
        "requirement": (
            "An APRA-regulated entity must identify material quantitative decision tools that fall outside its "
            "model definition, record them, and apply controls proportionate to the risk they present."
        ),
        "guidance": [
            "Deterministic calculators, complex spreadsheets, rules engines, allocation keys and end-user computing "
            "tools can drive material decisions and can be wrong in exactly the ways a model can be wrong, without "
            "meeting the definition of a model. Excluding them from the definition should not exclude them from control.",
            "The controls need not be the full model lifecycle. Ownership, documentation, change control, access "
            "control, periodic review and a check that the tool still does what it is meant to do will usually be "
            "sufficient for tools that are not material.",
        ],
        "sources": ["PRA-SS1-23", "OSFI-E23"],
        "principles": "PRA SS1/23 Principle 1 (identification of non-model quantitative methods)",
        "provenance": "Extracted",
        "rationale": (
            "The PRA expressly requires firms to consider quantitative methods that fall outside the model "
            "definition; without this, a narrow model definition becomes a control gap."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M04",
        "part": "Part A — Application and interpretation",
        "section": "2. Proportionality",
        "title": "Proportionality and controlled exceptions",
        "requirement": (
            "An APRA-regulated entity must apply this Prudential Standard in a manner proportionate to the "
            "materiality, complexity, autonomy and criticality of each model and to the size and business mix of "
            "the entity, and must document, time-bound, approve at an authority commensurate with the risk, and "
            "periodically review any exception to or reduction of the controls otherwise required."
        ),
        "guidance": [
            "Proportionality changes the depth, frequency and formality of controls. It does not change whether a "
            "model must be identified, owned, classified or capable of being explained to the Board and to APRA.",
            "A small entity with a handful of vendor models has a materially different obligation from a large "
            "entity operating hundreds of internally developed models across several regulated businesses. Both "
            "must be able to demonstrate that the difference reflects risk rather than convenience.",
            "An exception register that grows without expiry dates is itself an indicator of framework weakness.",
        ],
        "sources": ["PRA-SS1-23", "OSFI-E23", "US-MRM-2026", "APRA-CPS220", "BCBS-239"],
        "principles": "PRA SS1/23 proportionality; OSFI E-23 risk-based application; US interagency guidance 2026 §II",
        "provenance": "Extracted + inferred",
        "rationale": (
            "Proportionality is universal across the comparators; the explicit control of exceptions is drawn from "
            "APRA's existing risk management architecture."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part B
    {
        "id": "M05",
        "part": "Part B — Governance and accountability",
        "section": "3. Board and senior management",
        "title": "Board oversight of model risk",
        "requirement": (
            "The Board of an APRA-regulated entity must approve the model risk management framework and the "
            "entity's appetite for model risk, and must satisfy itself that model risk is being managed within "
            "that appetite and that it receives information sufficient to form that judgement."
        ),
        "guidance": [
            "The Board is not expected to understand the mathematics of individual models. It is expected to "
            "understand what the entity relies on models to do, where reliance is greatest, what could go wrong, "
            "how the entity would know, and what would happen next.",
            "Board reporting should be decision-useful rather than descriptive: aggregate exposure to model risk, "
            "movement in the tiering profile, validation coverage and overdue validations, unresolved high-severity "
            "findings, material limitations accepted, overlays in force and their size, and incidents.",
            "A Board that receives only a model count and a traffic-light summary is unlikely to be positioned to "
            "provide effective challenge.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "APRA-CPS220", "ECB-GIM"],
        "principles": "PRA SS1/23 Principle 2 (governance); US interagency guidance 2026 §VI; OSFI E-23 governance",
        "provenance": "Extracted",
        "rationale": "Board approval of the framework and appetite is common to every comparator.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M06",
        "part": "Part B — Governance and accountability",
        "section": "3. Board and senior management",
        "title": "Senior accountability for the framework",
        "requirement": (
            "An APRA-regulated entity must assign accountability for the design, implementation and effectiveness "
            "of the model risk management framework to a named senior executive with sufficient authority, "
            "independence from model development and business sponsorship, and resources to discharge it."
        ),
        "guidance": [
            "One accountable executive for the framework does not displace accountability for individual models. It "
            "ensures that someone owns the framework itself — its coverage, its consistency and its failures.",
            "The designation should be recorded in the entity's accountability arrangements and should be consistent "
            "with its obligations under the applicable accountability regime.",
        ],
        "sources": ["PRA-SS1-23", "US-MRM-2026", "OSFI-E23", "APRA-CPS220"],
        "principles": "PRA SS1/23 Principle 2 (senior management function accountability); OSFI E-23 accountability",
        "provenance": "Extracted",
        "rationale": (
            "The PRA allocates model risk management to a senior management function; OSFI and the US guidance "
            "require clear senior ownership."
        ),
        "policy_choice": False,
        "legal_flag": True,
    },
    {
        "id": "M07",
        "part": "Part B — Governance and accountability",
        "section": "3. Board and senior management",
        "title": "Model ownership and defined lifecycle roles",
        "requirement": (
            "An APRA-regulated entity must assign, for each model, a model owner accountable for the model "
            "throughout its lifecycle, and must define the roles, responsibilities and required independence of "
            "developers, validators, approvers, users and those responsible for monitoring."
        ),
        "guidance": [
            "The model owner is accountable for the model being fit for its approved purpose, for its documentation "
            "being current, for its performance being monitored, for its limitations being disclosed to users, and "
            "for remediation of findings. Ownership that exists only in the inventory is not ownership.",
            "Where a model is used by more than one business, the entity should be explicit about who owns the model "
            "and who owns each use of it, because the two can fail independently.",
        ],
        "sources": ["US-MRM-2026", "OSFI-E23", "PRA-SS1-23", "ECB-GIM"],
        "principles": "US interagency guidance 2026 §VI roles; OSFI E-23 roles and responsibilities; ECB internal governance",
        "provenance": "Extracted",
        "rationale": "Role definition with named model owners is explicit in the US, Canadian and ECB material.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M08",
        "part": "Part B — Governance and accountability",
        "section": "4. Capability and independence",
        "title": "Capability, resourcing and independence",
        "requirement": (
            "An APRA-regulated entity must maintain personnel, skills, tools and organisational arrangements "
            "sufficient to develop, use, validate, challenge and assure its models, with validation performed by "
            "persons who are independent of, and not accountable to, those who developed the model or who sponsor "
            "its business use."
        ),
        "guidance": [
            "Independence is a matter of incentive as well as reporting line. A validator whose remuneration, "
            "progression or workload depends on the approval of the models they validate is not independent, whatever "
            "the organisational chart shows.",
            "Smaller entities may not be able to maintain a standing validation function. Independence can be achieved "
            "by using suitably qualified persons from elsewhere in the entity or group who were not involved in "
            "development, or by engaging an external provider, provided the entity retains the capability to "
            "understand, direct and challenge the work and does not simply accept its conclusions.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM", "MAS-AIMRM-2024"],
        "principles": "US interagency guidance 2026 §V; PRA SS1/23 Principle 4.1; PRA SS1/23 Principle 4; ECB internal validation",
        "provenance": "Extracted",
        "rationale": "Independent validation is a core element of every comparator regime.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part C
    {
        "id": "M09",
        "part": "Part C — Framework, appetite and policy",
        "section": "5. Model risk management framework",
        "title": "Integrated model risk management framework",
        "requirement": (
            "An APRA-regulated entity must maintain a documented model risk management framework, integrated with "
            "its risk management framework, that covers model identification, inventory, tiering, development, "
            "data, testing, validation, approval, implementation, use, monitoring, change, limitations, remediation, "
            "decommissioning, reporting and assurance."
        ),
        "guidance": [
            "Model risk should be treated as a risk in its own right rather than as a subset of operational risk. "
            "Treating it as an operational risk category tends to produce incident-based management after the event "
            "rather than lifecycle management before it.",
            "Integration means the framework connects to, and does not duplicate, the entity's arrangements for data "
            "risk, information security, operational risk, service provider management, change management and "
            "internal audit.",
        ],
        "sources": ["PRA-SS1-23", "OSFI-E23", "US-MRM-2026", "APRA-CPS220", "APRA-CPS230"],
        "principles": "PRA SS1/23 Principle 2; OSFI E-23 enterprise framework; US interagency guidance 2026 §VI",
        "provenance": "Extracted",
        "rationale": "A documented enterprise framework is required by each of the comparator regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M10",
        "part": "Part C — Framework, appetite and policy",
        "section": "5. Model risk management framework",
        "title": "Model risk appetite and limits",
        "requirement": (
            "An APRA-regulated entity must define its appetite for model risk, express it in terms capable of being "
            "monitored, and establish limits, thresholds and escalation triggers against which model risk is measured "
            "and reported."
        ),
        "guidance": [
            "A model risk appetite expressed only as a statement of intent cannot be breached and therefore cannot be "
            "managed. Measurable expressions include tolerances for validation coverage and overdue validations, the "
            "permissible number and age of high-severity unresolved findings, limits on the aggregate size of overlays "
            "relative to a modelled figure, and constraints on the use of models operating outside approved conditions.",
            "Where an entity cannot yet quantify aggregate model risk, it should say so, use qualitative and coverage-based "
            "measures in the interim, and set out how it intends to close the gap.",
        ],
        "sources": ["PRA-SS1-23", "OSFI-E23", "APRA-CPS220", "US-MRM-2026"],
        "principles": "PRA SS1/23 Principle 2 (risk appetite); OSFI E-23 framework aligned to risk appetite",
        "provenance": "Extracted + inferred",
        "rationale": (
            "Comparators require a risk appetite for model risk; requiring it to be measurable is a drafting choice "
            "that makes the obligation supervisable."
        ),
        "policy_choice": True,
        "legal_flag": False,
    },
    {
        "id": "M11",
        "part": "Part C — Framework, appetite and policy",
        "section": "5. Model risk management framework",
        "title": "Policy, standards and consistency of application",
        "requirement": (
            "An APRA-regulated entity must maintain model risk policies and standards that are approved at an "
            "appropriate authority, applied consistently across the entity, reviewed at least annually, and "
            "version-controlled."
        ),
        "guidance": [
            "Consistency matters most where it is least convenient. Where different businesses apply materially "
            "different development, validation or documentation standards to models of equivalent risk, the entity "
            "should be able to justify the difference on risk grounds.",
        ],
        "sources": ["US-MRM-2026", "OSFI-E23", "PRA-SS1-23", "ECB-GIM"],
        "principles": "US interagency guidance 2026 §VI policies; OSFI E-23 policies and procedures",
        "provenance": "Extracted",
        "rationale": "Policy and standards documentation is an explicit expectation across the comparator set.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M12",
        "part": "Part C — Framework, appetite and policy",
        "section": "6. Reporting and escalation",
        "title": "Management information and escalation",
        "requirement": (
            "An APRA-regulated entity must provide the Board and senior management with timely and accurate "
            "information on model risk, including tiering profile, validation status, unresolved findings, material "
            "limitations, overlays, incidents, exceptions and remediation, and must escalate breaches of model risk "
            "limits and material model failures."
        ),
        "guidance": [
            "Reporting should aggregate. A list of individual model issues does not tell the Board whether model risk "
            "is increasing or decreasing, or where the concentration of reliance sits.",
            "Escalation criteria should be set in advance. Deciding after the event whether a model failure was "
            "material enough to escalate produces predictable results.",
        ],
        "sources": ["PRA-SS1-23", "OSFI-E23", "US-MRM-2026", "BCBS-239", "APRA-CPS220"],
        "principles": "PRA SS1/23 Principle 5; OSFI E-23 reporting; BCBS 239 risk reporting practices",
        "provenance": "Extracted",
        "rationale": "Reporting on model risk to the Board is required or expected by every comparator.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part D
    {
        "id": "M13",
        "part": "Part D — Identification, inventory and tiering",
        "section": "7. Inventory",
        "title": "Model identification and enterprise inventory",
        "requirement": (
            "An APRA-regulated entity must maintain a complete, accurate and current enterprise-wide inventory of "
            "its models, including models supplied by third parties, models embedded in acquired systems, models "
            "under development and models that have been retired but whose outputs remain in use."
        ),
        "guidance": [
            "The inventory is the foundation of the framework: nothing else in this Prudential Standard can be "
            "demonstrated for a model that the entity does not know it has. Annex B sets out the minimum fields.",
            "Identification requires active discovery rather than voluntary registration. Procurement gates, "
            "architecture review, change approval, periodic business attestations and reconciliation to expenditure "
            "and to system inventories are all more reliable than asking business units to self-declare.",
            "Retired models require particular care where a decision, a provision, a capital number or a customer "
            "outcome produced by the model remains in force after the model itself has been switched off.",
        ],
        "sources": ["PRA-SS1-23", "US-MRM-2026", "OSFI-E23", "ECB-GIM", "MAS-AIMRM-2024"],
        "principles": "PRA SS1/23 Principle 1; US interagency guidance 2026 §VI inventory; OSFI E-23 model inventory",
        "provenance": "Extracted",
        "rationale": "A comprehensive inventory is required by every comparator regime without exception.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M14",
        "part": "Part D — Identification, inventory and tiering",
        "section": "8. Tiering",
        "title": "Model risk tiering",
        "requirement": (
            "An APRA-regulated entity must apply a documented and consistently implemented methodology to assign "
            "each model a model risk tier, using both quantitative and qualitative factors, and must use that tier "
            "to determine the intensity of development, documentation, validation, approval, monitoring and "
            "reporting applied to the model."
        ),
        "guidance": [
            "Tiering factors should include the materiality of the decisions or figures the model influences, the "
            "complexity and transparency of the method, the uncertainty in the data and assumptions, the degree of "
            "reliance placed on the output, the extent of automation and the reversibility of the consequence.",
            "A simple model can warrant the highest tier because of what it is used for. Tiering that tracks technical "
            "sophistication rather than consequence will systematically under-govern the models that matter most.",
            "The tier should drive real differences in control. A tiering scheme that produces the same treatment for "
            "every tier is an administrative exercise rather than a risk control.",
        ],
        "sources": ["PRA-SS1-23", "OSFI-E23", "US-MRM-2026", "MAS-AIMRM-2024", "ECB-GIM"],
        "principles": "PRA SS1/23 Principle 1 (model risk classification); OSFI E-23 model risk rating",
        "provenance": "Extracted",
        "rationale": (
            "Risk-based tiering driving control intensity is the mechanism every comparator uses to make "
            "proportionality operational."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M15",
        "part": "Part D — Identification, inventory and tiering",
        "section": "8. Tiering",
        "title": "Reassessment and trigger events",
        "requirement": (
            "An APRA-regulated entity must reassess a model's tier and required controls at a frequency proportionate "
            "to its tier and upon the occurrence of defined trigger events, including material change to the model, "
            "its data, its purpose, its user base, its operating environment or the entity's reliance on it."
        ),
        "guidance": [
            "Trigger events should include changes the entity did not initiate, such as a vendor releasing a new "
            "version, an upstream data source changing definition, or a portfolio migrating into a segment the model "
            "was not developed on.",
        ],
        "sources": ["OSFI-E23", "PRA-SS1-23", "ECB-GIM", "US-MRM-2026"],
        "principles": "OSFI E-23 review triggers; ECB model change management",
        "provenance": "Extracted + inferred",
        "rationale": "Trigger-based reassessment is explicit in OSFI and ECB material.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part E
    {
        "id": "M16",
        "part": "Part E — Development, data and documentation",
        "section": "9. Development",
        "title": "Conceptual soundness and development standards",
        "requirement": (
            "An APRA-regulated entity must ensure that each model is developed in accordance with documented "
            "standards, is conceptually sound, is fit for its intended purpose, and that the design, theory, "
            "methodology, assumptions, variable selection and known limitations are justified and recorded."
        ),
        "guidance": [
            "Conceptual soundness asks whether the approach makes sense for the purpose, not merely whether it fits "
            "the data. A model that performs well in backtesting on a period unrepresentative of the conditions in "
            "which it will be used is not conceptually sound.",
            "Development should include consideration of reasonable alternative approaches and a record of why the "
            "chosen approach was preferred. Where a more transparent method would have performed acceptably, the "
            "entity should be able to explain why a less transparent one was selected.",
            "Developmental evidence should include the testing carried out during development, its results, and the "
            "limitations that testing did not resolve — not only the tests the model passed.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM"],
        "principles": "US interagency guidance 2026 §IV; PRA SS1/23 Principle 3; ECB internal models general topics",
        "provenance": "Extracted",
        "rationale": "Conceptual soundness is the central development concept in the US, UK, Canadian and ECB regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M17",
        "part": "Part E — Development, data and documentation",
        "section": "10. Data",
        "title": "Data quality, provenance and appropriateness",
        "requirement": (
            "An APRA-regulated entity must ensure that data used to develop, calibrate, test, operate and monitor a "
            "model is appropriate for that purpose, of sufficient quality, traceable to source, and that material "
            "data limitations, proxies, adjustments and exclusions are documented and their effect on model output "
            "assessed."
        ),
        "guidance": [
            "Data appropriateness is a question of representativeness as well as accuracy. Data that is accurate but "
            "drawn from a population, product or period unlike the one in which the model will be used will produce "
            "confidently wrong answers.",
            "Where proxy or external data is used because internal data is insufficient, the entity should document "
            "the basis for considering the proxy suitable and should test the sensitivity of the output to that choice.",
            "Synthetic data used for development or testing should be identified as such, with its generation method "
            "and its representativeness assessed.",
        ],
        "sources": ["BCBS-239", "US-MRM-2026", "OSFI-E23", "ECB-GIM", "APRA-CPG235", "ECB-RDARR"],
        "principles": "BCBS 239 risk data aggregation capabilities; US interagency guidance 2026 §IV data; ECB data quality",
        "provenance": "Extracted",
        "rationale": "Data quality and appropriateness obligations are present in all comparator regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M18",
        "part": "Part E — Development, data and documentation",
        "section": "11. Documentation",
        "title": "Documentation sufficient for independent reconstruction",
        "requirement": (
            "An APRA-regulated entity must maintain model documentation sufficient for a competent person "
            "independent of the model's development to understand its purpose, design, data, assumptions, "
            "implementation, limitations, testing, approved conditions of use and performance, and to reproduce its "
            "material results."
        ),
        "guidance": [
            "The reconstruction test is the practical standard: documentation is adequate when someone who was not "
            "there can pick it up and reach the same answer. Documentation that depends on the continued availability "
            "of the person who built the model is a key-person dependency, not documentation.",
            "Documentation should be maintained through the model's life rather than assembled for validation or for "
            "a supervisory request.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "ECB-GIM", "OSFI-E23"],
        "principles": "US interagency guidance 2026 §VI documentation; PRA SS1/23 Principle 3; ECB documentation requirements",
        "provenance": "Extracted",
        "rationale": "The reproducibility standard for documentation is common to the US, UK and ECB regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part F
    {
        "id": "M19",
        "part": "Part F — Testing, validation and approval",
        "section": "12. Testing before use",
        "title": "Pre-implementation testing",
        "requirement": (
            "An APRA-regulated entity must not place a model into use for a material purpose until it has been "
            "tested against its design objective and intended use, the results have been documented, and residual "
            "limitations have been accepted at an appropriate authority."
        ),
        "guidance": [
            "Testing should cover performance under expected conditions and under stressed, boundary and unrepresentative "
            "conditions, sensitivity to key assumptions and inputs, stability, and behaviour at the edges of the "
            "population the model will encounter.",
            "Testing should use data that is sufficiently independent of the data used to build the model. A model "
            "tested only on the data it was fitted to has not been tested.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM", "MAS-AIMRM-2024"],
        "principles": "US interagency guidance 2026 §IV (model testing); PRA SS1/23 Principle 3; ECB pre-approval testing",
        "provenance": "Extracted + inferred",
        "rationale": (
            "Development testing is universal; expressing it as a bar to use for material purposes makes it an "
            "enforceable gate rather than a process expectation."
        ),
        "policy_choice": True,
        "legal_flag": False,
    },
    {
        "id": "M20",
        "part": "Part F — Testing, validation and approval",
        "section": "13. Independent validation",
        "title": "Independent validation",
        "requirement": (
            "An APRA-regulated entity must subject each model to independent validation before it is used for a "
            "material purpose and periodically thereafter at a frequency determined by its tier, and must not treat "
            "validation performed by the model's developer, its business sponsor or its vendor as satisfying this "
            "requirement."
        ),
        "guidance": [
            "Validation is a distinct exercise from development testing. Its purpose is to form an independent view "
            "of whether the model is fit for its intended use, not to confirm that the development team did what it "
            "said it did.",
            "Vendor validation reports, model certifications and audit reports may be used as inputs. They do not "
            "discharge the entity's obligation, because they were not designed around the entity's data, portfolio, "
            "controls or use.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM", "MAS-NOTICE637"],
        "principles": "US interagency guidance 2026 §V; PRA SS1/23 Principle 4; OSFI E-23 independent review; ECB internal validation",
        "provenance": "Extracted",
        "rationale": "Independent validation is a named principle or core element in every comparator regime.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M21",
        "part": "Part F — Testing, validation and approval",
        "section": "13. Independent validation",
        "title": "Scope of validation",
        "requirement": (
            "Validation of a model must address conceptual soundness, outcomes analysis comparing model "
            "outputs with corresponding actual outcomes, and ongoing model monitoring, and must reach an "
            "explicit conclusion on the model's fitness for its intended use together with any conditions "
            "or limitations."
        ),
        "guidance": [
            "These three elements are complementary and none is sufficient alone. Conceptual soundness alone cannot "
            "detect deterioration; outcomes analysis alone cannot explain it.",
            "Validation should assess implementation as well as design — that the model as coded and deployed is the "
            "model as documented and approved.",
            "A validation that records observations without reaching a conclusion leaves the approval decision "
            "without the input it was designed to receive.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM"],
        "principles": "US interagency guidance 2026 §V (components of model validation); PRA SS1/23 Principle 4",
        "provenance": "Extracted",
        "rationale": (
            "The three core elements of validation are the most widely adopted formulation in the discipline and "
            "originate in the US interagency guidance."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M22",
        "part": "Part F — Testing, validation and approval",
        "section": "13. Independent validation",
        "title": "Effective challenge",
        "requirement": (
            "An APRA-regulated entity must ensure that its models are subject to effective challenge — "
            "critical and objective analysis by persons with the expertise to identify model limitations, "
            "sufficient independence to maintain objectivity, and the organisational standing and influence "
            "to effect change."
        ),
        "guidance": [
            "Effective challenge depends on three things together: the challenger must know enough to find the "
            "problem, must be senior and independent enough for the finding to carry weight, and must be rewarded "
            "for raising it rather than for clearing models. Removing any one of the three defeats the control.",
            "Indicators that challenge is not effective include validation findings that are consistently closed by "
            "explanation rather than change, findings downgraded without new evidence, and validation reports whose "
            "conclusions change late in the approval process.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23"],
        "principles": "US interagency guidance 2026 §III (effective challenge); PRA SS1/23 Principle 4",
        "provenance": "Extracted",
        "rationale": (
            "Effective challenge is the organising concept of the US guidance and is adopted in substance by the "
            "PRA and OSFI."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M23",
        "part": "Part F — Testing, validation and approval",
        "section": "14. Approval",
        "title": "Approval and conditions of use",
        "requirement": (
            "An APRA-regulated entity must approve each model for a defined purpose and defined conditions of use at "
            "an authority commensurate with its tier, having considered the validation conclusion, unresolved "
            "findings, limitations, compensating controls and residual model risk, and must record the approved "
            "version, scope, users, limits, monitoring thresholds and review date."
        ),
        "guidance": [
            "Approval should be of a specific version for a specific use. Approval of a model in the abstract leaves "
            "no basis on which to determine later whether it is being used as approved.",
            "Approval notwithstanding unresolved high-severity findings should be exceptional, time-bound, supported by "
            "compensating controls and escalated.",
        ],
        "sources": ["US-MRM-2026", "OSFI-E23", "ECB-GIM", "PRA-SS1-23"],
        "principles": "OSFI E-23 approval; ECB model approval and use; US interagency guidance 2026 §VI",
        "provenance": "Extracted + inferred",
        "rationale": "Approval with defined conditions of use is explicit in the Canadian and ECB regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part G
    {
        "id": "M24",
        "part": "Part G — Implementation, use and change",
        "section": "15. Implementation",
        "title": "Implementation controls",
        "requirement": (
            "An APRA-regulated entity must control the implementation of a model into its production environment, "
            "including verification that the implemented model reproduces the approved model, control over input "
            "data feeds and computing environment, access control, and the ability to revert."
        ),
        "guidance": [
            "Implementation is a recurrent source of model failure that validation focused on methodology does not "
            "detect. Differences between the development environment and production — in data definitions, rounding, "
            "library versions, treatment of missing values or execution order — can change results materially.",
        ],
        "sources": ["US-MRM-2026", "ECB-GIM", "OSFI-E23"],
        "principles": "Former SR 11-7 §IV (implementation); not carried forward in 2026; ECB internal models implementation",
        "provenance": "Extracted",
        "rationale": "Implementation control is explicit in the US guidance and the ECB internal models framework.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M25",
        "part": "Part G — Implementation, use and change",
        "section": "16. Change",
        "title": "Change management and re-approval",
        "requirement": (
            "An APRA-regulated entity must control changes to models, model inputs, assumptions, calibration and "
            "implementation, must assess the materiality of each change, and must re-test, re-validate and re-approve "
            "changes to the extent warranted by that assessment."
        ),
        "guidance": [
            "The materiality assessment should consider the change in isolation and cumulatively. A sequence of "
            "individually immaterial recalibrations can move a model a long way from the version that was validated.",
            "Changes initiated by a vendor, or by an upstream data provider, are changes to the entity's model risk "
            "profile even though the entity did not make them, and should enter the same assessment.",
        ],
        "sources": ["ECB-GIM", "OSFI-E23", "US-MRM-2026", "PRA-SS1-23"],
        "principles": "ECB management of model changes; OSFI E-23 model changes; PRA SS1/23 Principle 3",
        "provenance": "Extracted",
        "rationale": "Model change management is a distinct and detailed obligation in the ECB regime.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M26",
        "part": "Part G — Implementation, use and change",
        "section": "17. Use",
        "title": "Use consistent with approved purpose",
        "requirement": (
            "An APRA-regulated entity must ensure that models are used only for their approved purposes and within "
            "their approved conditions, and that users understand the model's purpose, key assumptions, limitations "
            "and the circumstances in which its output should not be relied upon."
        ),
        "guidance": [
            "Misuse of a sound model is one of the two principal sources of model risk and is frequently the less "
            "well controlled of the two. A model built to rank relative risk being used to set absolute prices, or a "
            "model built for one portfolio being applied to another, are common examples.",
            "Users should receive the limitations, not merely have access to them. Limitations recorded only in a "
            "validation report that users do not read are not disclosed in any meaningful sense.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "ECB-GIM", "OSFI-E23"],
        "principles": "US interagency guidance 2026 §IV (model use); PRA SS1/23 Principle 3; ECB use test",
        "provenance": "Extracted",
        "rationale": "Controlling model use is one of the two limbs of the standard definition of model risk.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M27",
        "part": "Part G — Implementation, use and change",
        "section": "17. Use",
        "title": "Overlays, adjustments and expert judgement",
        "requirement": (
            "An APRA-regulated entity must govern adjustments, overlays and expert judgement applied to model output, "
            "including the basis for the adjustment, its quantification, approval at an authority commensurate with "
            "its size and effect, its documentation, its monitoring and the conditions for its removal."
        ),
        "guidance": [
            "A large or long-standing overlay is evidence about the model. Persistent adjustment in the same direction "
            "usually means the model no longer reflects the exposure and should be redeveloped rather than corrected "
            "in perpetuity.",
            "Overlays should be reported in aggregate to the Board and senior management, because individually approved "
            "adjustments can collectively become the dominant driver of a reported figure.",
        ],
        "sources": ["ECB-GIM", "PRA-SS1-23", "OSFI-E23", "US-MRM-2026"],
        "principles": "PRA SS1/23 Principle 5 (post-model adjustments); ECB margin of conservatism",
        "provenance": "Extracted",
        "rationale": (
            "Post-model adjustments are expressly addressed by the PRA as a model risk mitigant and by the ECB "
            "through the margin of conservatism framework."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M28",
        "part": "Part G — Implementation, use and change",
        "section": "18. Monitoring",
        "title": "Ongoing performance monitoring",
        "requirement": (
            "An APRA-regulated entity must monitor the performance of each model against defined metrics and "
            "thresholds at a frequency proportionate to its tier, and must investigate, escalate and act upon "
            "threshold breaches, deterioration, drift and unexplained changes in behaviour."
        ),
        "guidance": [
            "Monitoring should test whether the assumptions on which the model depends continue to hold, not only "
            "whether the output has moved. A model can remain stable while the conditions that made it valid have gone.",
            "Thresholds should be set in advance and should be linked to a defined response — investigation, "
            "restriction, revalidation, overlay or withdrawal — so that a breach produces an action rather than a note.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM", "MAS-AIMRM-2024"],
        "principles": "US interagency guidance 2026 §V (ongoing model monitoring); PRA SS1/23 Principle 3; OSFI E-23 monitoring",
        "provenance": "Extracted",
        "rationale": "Ongoing monitoring is one of the three core validation elements and is universal.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M29",
        "part": "Part G — Implementation, use and change",
        "section": "18. Monitoring",
        "title": "Limitations, compensating controls and remediation",
        "requirement": (
            "An APRA-regulated entity must record known model limitations and deficiencies, apply compensating "
            "controls where a limitation is material and not immediately resolvable, track remediation to completion "
            "against owners and dates, and escalate overdue or unresolved material findings."
        ),
        "guidance": [
            "Compensating controls should be specific to the limitation they address. A general statement that outputs "
            "are subject to management review does not compensate for a known bias in a particular segment.",
            "The entity should be able to demonstrate that findings are closed because they were fixed, and should "
            "monitor the rate at which findings are closed by rationale, deferral or reclassification.",
        ],
        "sources": ["PRA-SS1-23", "US-MRM-2026", "OSFI-E23", "ECB-GIM"],
        "principles": "PRA SS1/23 Principle 5 (model risk mitigants); OSFI E-23 issue management",
        "provenance": "Extracted",
        "rationale": (
            "Model risk mitigants including restrictions, adjustments and remediation are the subject of a named "
            "PRA principle."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M30",
        "part": "Part G — Implementation, use and change",
        "section": "19. Retirement",
        "title": "Restriction, suspension and decommissioning",
        "requirement": (
            "An APRA-regulated entity must be able to restrict, suspend, replace or decommission a model that is "
            "unfit for its purpose, and must manage decommissioning so that dependent processes, downstream models "
            "and outputs that remain in force are addressed and records are retained."
        ),
        "guidance": [
            "The entity should know, before it needs to act, what it would do if a material model became unusable — "
            "whether an alternative exists, how long it would take to stand up, and what the interim basis for "
            "decisions would be.",
        ],
        "sources": ["OSFI-E23", "PRA-SS1-23", "APRA-CPS230", "ECB-GIM"],
        "principles": "OSFI E-23 decommissioning; CPS 230 critical operations and tolerance levels",
        "provenance": "Extracted + inferred",
        "rationale": "Decommissioning is explicit in OSFI E-23; the continuity dimension links to CPS 230.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part H
    {
        "id": "M31",
        "part": "Part H — Third-party and AI models",
        "section": "20. Third-party models",
        "title": "Vendor and externally developed models",
        "requirement": (
            "An APRA-regulated entity must apply this Prudential Standard to models supplied, hosted or operated by "
            "third parties, and must obtain information sufficient to understand the model's design, data, "
            "assumptions, limitations and performance, or implement compensating controls where that information "
            "cannot be obtained."
        ),
        "guidance": [
            "Where a provider will not disclose methodology, the entity should intensify what it can do itself: "
            "benchmarking against alternatives, outcomes analysis on its own portfolio, sensitivity testing through "
            "controlled input variation, and tighter conditions of use.",
            "The entity should not accept a level of opacity for a high-tier model that it would not accept from an "
            "internal development team.",
        ],
        "sources": ["US-MRM-2026", "OSFI-E23", "BCBS-TPRM", "APRA-CPS230", "PRA-SS1-23"],
        "principles": "US interagency guidance 2026 §VII (vendor and other third-party products); OSFI E-23 third-party models; BCBS third-party principles",
        "provenance": "Extracted",
        "rationale": "Vendor models are expressly within scope of the US, Canadian and UK regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M32",
        "part": "Part H — Third-party and AI models",
        "section": "20. Third-party models",
        "title": "Information rights, concentration and substitutability",
        "requirement": (
            "An APRA-regulated entity must maintain contractual and governance arrangements giving it timely access "
            "to the information and assurance it needs to meet its obligations in relation to a material third-party "
            "model, and must identify and manage concentration and substitutability risk arising from common models, "
            "data sources, platforms and providers."
        ),
        "guidance": [
            "Information rights should be practically usable rather than nominally present. A right to audit that the "
            "entity has no capacity to exercise provides little assurance.",
            "Concentration should be assessed at entity level and, so far as the entity can observe it, at industry "
            "level. Widespread reliance on the same external model or data source can produce correlated error across "
            "firms even where each firm's own governance is sound.",
        ],
        "sources": ["APRA-CPS230", "BCBS-TPRM", "FSB-AI-2024", "OSFI-E23"],
        "principles": "CPS 230 service provider management; BCBS third-party principles; FSB concentration analysis",
        "provenance": "Extracted + inferred",
        "rationale": (
            "Third-party risk principles and financial-stability analysis both identify concentration in externally "
            "supplied models as a distinct risk."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M33",
        "part": "Part H — Third-party and AI models",
        "section": "21. AI and machine learning models",
        "title": "Additional controls for AI and machine learning models",
        "requirement": (
            "Where a model uses artificial intelligence or machine learning techniques, an APRA-regulated entity "
            "must address the additional risks arising from those techniques, including limited explainability, "
            "sensitivity to data drift, instability under retraining, feature leakage, potential for biased outcomes, "
            "and dependence on externally supplied models whose construction the entity cannot inspect."
        ),
        "guidance": [
            "AI and machine learning models are models. They are subject to every requirement in this Prudential "
            "Standard. This paragraph adds to those requirements; it does not create a separate regime.",
            "Where explainability is limited, the entity should intensify outcomes-based controls rather than treat "
            "the limitation as a reason to reduce them. Suitable measures include benchmark comparison against a more "
            "transparent model, stability testing across retraining cycles, subgroup outcome analysis and tighter "
            "conditions of use.",
            "Where a model retrains automatically, the entity should define the operating envelope within which "
            "retraining is authorised, and should treat movement outside that envelope as a model change.",
        ],
        "sources": ["OSFI-E23", "MAS-AIMRM-2024", "BCBS-DIGI", "PRA-SS1-23", "FSB-AI-2024"],
        "principles": "OSFI E-23 AI/ML considerations; MAS AI model risk management observations; BCBS digitalisation report",
        "provenance": "Extracted",
        "rationale": (
            "OSFI expressly extends model risk management to AI/ML and MAS has published detailed observed practice "
            "for AI model risk management."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M34",
        "part": "Part H — Third-party and AI models",
        "section": "21. AI and machine learning models",
        "title": "Boundary with the AI risk management framework",
        "requirement": (
            "An APRA-regulated entity must apply this Prudential Standard to any artificial intelligence system that "
            "meets the definition of a model, must apply its AI risk management arrangements to the wider risks of "
            "that system, and must ensure that no material AI system falls between the two."
        ),
        "guidance": [
            "The two regimes address different risks in the same system. This Prudential Standard governs whether the "
            "quantitative output is fit to be relied on. AI risk management governs the wider consequences of the "
            "system's operation — security, autonomy, data handling, human oversight and resilience.",
            "A generative or agentic system that produces no quantitative estimate for decision-making is generally "
            "not a model, but remains subject to the entity's AI risk management arrangements. A generative system "
            "used to produce an estimate that drives a material decision is both.",
            "The entity should maintain a single register that records, for each AI system, which regime or regimes "
            "apply, so that the boundary is a documented determination rather than an assumption.",
        ],
        "sources": ["OSFI-E23", "MAS-AIMRM-2024", "FSB-AI-2024"],
        "principles": "OSFI E-23 single framework for models including AI",
        "provenance": "Policy choice",
        "rationale": (
            "No comparator operates parallel model risk and AI risk instruments, so the boundary rule is an APRA "
            "drafting choice required by the proposed two-instrument architecture."
        ),
        "policy_choice": True,
        "legal_flag": True,
    },

    # ------------------------------------------------------------------ Part I
    {
        "id": "M35",
        "part": "Part I — Specialist model classes",
        "section": "22. Regulatory capital models",
        "title": "Models used to determine regulatory capital",
        "requirement": (
            "An APRA-regulated entity that uses a model to determine a regulatory capital requirement must satisfy "
            "the requirements of the applicable prudential standard for that model in addition to this Prudential "
            "Standard, must not change an approved model without APRA's approval where the applicable standard so "
            "requires, and must ensure the model is used in the entity's internal risk management."
        ),
        "guidance": [
            "This Prudential Standard does not alter or displace the model approval requirements in the capital "
            "standards. Where the two overlap, the more specific requirement in the capital standard prevails.",
            "The requirement that an approved capital model be used in internal risk management is longstanding and "
            "substantive. A model maintained for regulatory reporting while the business is run on a different basis "
            "indicates that one of the two is not trusted.",
        ],
        "sources": ["APRA-APS113", "ECB-GIM", "ECB-CRR", "BCBS-FW", "PRA-SS1-23"],
        "principles": "ECB Guide to internal models; CRR internal model requirements; APS 113 model requirements",
        "provenance": "Extracted",
        "rationale": (
            "Regulatory capital models are subject to a distinct approval regime in Australia, the EU and the UK "
            "which this Prudential Standard must sit alongside rather than duplicate."
        ),
        "policy_choice": False,
        "legal_flag": True,
    },
    {
        "id": "M36",
        "part": "Part I — Specialist model classes",
        "section": "23. Valuation and financial reporting models",
        "title": "Valuation and financial reporting models",
        "requirement": (
            "An APRA-regulated entity must apply this Prudential Standard to models used to value assets and "
            "liabilities, to determine expected credit losses and to produce financial and regulatory reporting, and "
            "must ensure independent price verification and independent review of material valuation inputs and "
            "assumptions."
        ),
        "guidance": [
            "Valuation models concentrate model risk because the output is the reported number rather than an input "
            "to a decision that a human subsequently makes. Level 3 valuations, illiquid exposures and modelled "
            "expected credit loss are the areas of greatest sensitivity to assumption choice.",
            "Independent price verification is a distinct control from validation and both are required for material "
            "valuation models.",
        ],
        "sources": ["BCBS-FVP", "ECB-GIM", "APRA-CPS220", "US-MRM-2026"],
        "principles": "BCBS supervisory guidance on fair value practices; ECB internal models market risk",
        "provenance": "Extracted",
        "rationale": "Valuation model governance and independent price verification are established supervisory expectations.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M37",
        "part": "Part I — Specialist model classes",
        "section": "24. Actuarial and insurance models",
        "title": "Actuarial, reserving and insurance liability models",
        "requirement": (
            "An APRA-regulated insurer must apply this Prudential Standard to models used to determine insurance "
            "liabilities, premiums, reinsurance recoveries and capital, and must ensure that the role of the "
            "Appointed Actuary and this Prudential Standard's validation requirements operate together without gaps "
            "in independent review."
        ),
        "guidance": [
            "The Appointed Actuary provides a form of independent professional review that is well established and, "
            "for many actuarial models, will satisfy a substantial part of the validation expectation. It does not "
            "automatically satisfy all of it, particularly in respect of implementation verification and data quality.",
            "The insurer should map which elements of validation are discharged through the actuarial control cycle "
            "and which require separate work, rather than assuming complete overlap in either direction.",
        ],
        "sources": ["APRA-CPS320", "APRA-GPS320", "APRA-LPS320", "OSFI-E23"],
        "principles": "APRA Appointed Actuary framework; OSFI E-23 application to insurers",
        "provenance": "Extracted + inferred",
        "rationale": (
            "OSFI's expansion of E-23 to insurers establishes the precedent; the interaction with the Australian "
            "Appointed Actuary framework is an Australian drafting question."
        ),
        "policy_choice": False,
        "legal_flag": True,
    },
    {
        "id": "M38",
        "part": "Part I — Specialist model classes",
        "section": "25. Superannuation models",
        "title": "Models used by RSE licensees",
        "requirement": (
            "An RSE licensee must apply this Prudential Standard to models used in investment strategy, asset "
            "valuation, liquidity management, insurance in superannuation, fee and cost determination, unit pricing "
            "and member outcomes assessment."
        ),
        "guidance": [
            "Unit pricing and valuation models directly determine amounts credited to member accounts. An error is "
            "realised as a transfer of value between members and is frequently difficult to reverse, which places "
            "these models at the higher end of any reasonable tiering assessment.",
            "Liquidity stress models used to support investment strategy should be tested against the conditions in "
            "which they would actually be relied upon.",
        ],
        "sources": ["APRA-SPS220", "APRA-SPS530", "APRA-SPS515"],
        "principles": "SPS 530 investment governance; SPS 515 business performance review",
        "provenance": "Inferred",
        "rationale": (
            "No comparator addresses superannuation model risk; cross-industry application to RSE licensees requires "
            "the standard to name the model classes that matter in that sector."
        ),
        "policy_choice": True,
        "legal_flag": True,
    },
    {
        "id": "M39",
        "part": "Part I — Specialist model classes",
        "section": "26. Stress testing and scenario models",
        "title": "Stress testing, scenario and capital planning models",
        "requirement": (
            "An APRA-regulated entity must apply this Prudential Standard to models used for stress testing, scenario "
            "analysis and capital planning, and must ensure that the limitations of those models are made explicit to "
            "those relying on their results."
        ),
        "guidance": [
            "Stress testing models are used precisely where historical data is least informative, so their results "
            "depend heavily on assumption and expert judgement. That does not make them exempt from governance; it "
            "makes the governance of their assumptions the principal control.",
            "Forward-looking scenario models addressing risks with limited historical precedent, including climate "
            "scenarios, should be used with explicit acknowledgement of the uncertainty in their outputs, and should "
            "not be presented to decision-makers with a precision the method cannot support.",
        ],
        "sources": ["BCBS-STRESS", "PRA-SS1-23", "ECB-GIM", "APRA-CPS220"],
        "principles": "BCBS stress testing principles; PRA SS1/23 application to stress testing models",
        "provenance": "Extracted",
        "rationale": "The BCBS stress testing principles establish governance expectations for these models.",
        "policy_choice": False,
        "legal_flag": False,
    },

    # ------------------------------------------------------------------ Part J
    {
        "id": "M40",
        "part": "Part J — Aggregate risk, records and assurance",
        "section": "27. Aggregate model risk",
        "title": "Aggregate assessment of model risk",
        "requirement": (
            "An APRA-regulated entity must assess model risk in aggregate across its model portfolio, must consider "
            "the effect of that aggregate risk in its internal capital assessment, and must be able to explain the "
            "basis and limitations of the assessment."
        ),
        "guidance": [
            "Aggregate assessment need not be a single number. Concentration of reliance, correlation of methodology "
            "and data across models, common assumptions and the extent of unvalidated or overdue models are all "
            "informative and are usually available before a quantification capability exists.",
            "Where an entity concludes that no capital is required in respect of model risk, that conclusion should be "
            "reasoned and documented rather than reached by omission.",
        ],
        "sources": ["PRA-SS1-23", "ECB-GIM", "US-MRM-2026", "APRA-CPS220"],
        "principles": "PRA SS1/23 Principle 5 (aggregate model risk); ECB model risk in the SREP",
        "provenance": "Extracted",
        "rationale": (
            "Aggregate model risk assessment and its capital implications are addressed by the PRA and by the ECB "
            "supervisory review process."
        ),
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M41",
        "part": "Part J — Aggregate risk, records and assurance",
        "section": "28. Records",
        "title": "Records and reconstructability",
        "requirement": (
            "An APRA-regulated entity must retain records sufficient to reconstruct, for a material model, what it "
            "produced, on what data and version, on what basis it was approved, how it performed, what limitations "
            "applied and what adjustments were made."
        ),
        "guidance": [
            "Reconstructability is what allows a supervisor, an auditor, an actuary or a court to establish what the "
            "entity knew and when. It should be designed into the model's operation rather than reassembled later.",
            "Retention periods should align with the entity's other prudential record-keeping obligations and with the "
            "period over which the decisions the model informed remain material.",
        ],
        "sources": ["US-MRM-2026", "ECB-GIM", "OSFI-E23", "APRA-CPS220"],
        "principles": "US interagency guidance 2026 §VI documentation and records; ECB documentation",
        "provenance": "Extracted + inferred",
        "rationale": "Record-keeping is explicit across comparators; the reconstruction standard is a drafting choice.",
        "policy_choice": False,
        "legal_flag": True,
    },
    {
        "id": "M42",
        "part": "Part J — Aggregate risk, records and assurance",
        "section": "29. Assurance",
        "title": "Internal audit and independent assurance",
        "requirement": (
            "An APRA-regulated entity must ensure that internal audit, or another independent function with "
            "equivalent standing, periodically assesses the design and operating effectiveness of the model risk "
            "management framework, including the effectiveness of validation and of challenge, and reports the "
            "results to the Board Audit Committee."
        ),
        "guidance": [
            "Internal audit's role is to assess whether the framework works, not to re-perform validation. Testing "
            "whether validation findings are genuinely resolved, whether tiering is applied consistently and whether "
            "the inventory is complete will usually be more informative than re-examining model methodology.",
            "Where internal audit lacks the technical capability to assess validation quality, the entity should "
            "obtain that capability rather than narrow the scope of the assurance.",
        ],
        "sources": ["US-MRM-2026", "PRA-SS1-23", "OSFI-E23", "ECB-GIM"],
        "principles": "US interagency guidance 2026 §VI internal audit; ECB internal audit of internal models",
        "provenance": "Extracted",
        "rationale": "Internal audit coverage of the model risk framework is explicit in the US and ECB regimes.",
        "policy_choice": False,
        "legal_flag": False,
    },
    {
        "id": "M43",
        "part": "Part J — Aggregate risk, records and assurance",
        "section": "30. APRA engagement",
        "title": "Notification and provision of information to APRA",
        "requirement": (
            "An APRA-regulated entity must notify APRA of a model failure or model risk event that has, or is likely "
            "to have, a material impact on its financial position, its regulatory reporting or its ability to meet "
            "its prudential obligations, and must provide APRA with information relating to its models and model risk "
            "management on request."
        ),
        "guidance": [
            "Where a model failure is also an operational risk incident or an information security incident, the "
            "notification requirements of the applicable prudential standards apply and this paragraph does not "
            "create an additional or conflicting deadline.",
            "Early engagement is expected where an entity identifies a material weakness in a model used for "
            "regulatory capital, reserving or reporting, rather than at the point the correction is finalised.",
        ],
        "sources": ["APRA-CPS230", "APRA-CPS234", "APRA-CPS220", "OSFI-E23"],
        "principles": "CPS 230 incident notification; OSFI E-23 supervisory engagement",
        "provenance": "Extracted + inferred; legal drafting required",
        "rationale": (
            "Deliberately cross-references existing notification architecture rather than proposing a separate "
            "model risk deadline that would conflict with it."
        ),
        "policy_choice": False,
        "legal_flag": True,
    },
]

# Sanity checks used by the builders and the integrity test.
IDS = [r["id"] for r in REQUIREMENTS]
assert len(IDS) == len(set(IDS)), "duplicate requirement IDs"
assert all(r["requirement"].strip().endswith(".") for r in REQUIREMENTS), "requirement not a full sentence"
assert all(" must " in r["requirement"] or r["requirement"].startswith("The Board must")
           or " must" in r["requirement"] for r in REQUIREMENTS), "requirement lacks mandatory verb"

PARTS = []
for _r in REQUIREMENTS:
    if _r["part"] not in PARTS:
        PARTS.append(_r["part"])

SECTIONS = []
for _r in REQUIREMENTS:
    if _r["section"] not in SECTIONS:
        SECTIONS.append(_r["section"])
