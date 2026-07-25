"""CPG XXXX practice guide content.

Structure mirrors APG 250, which was supplied as a model: numbered "should"
paragraphs, a cross-reference strip at the head of each chapter, source
attribution lines carrying legal-status codes, and amber verification
annotations recording what is extracted, inferred or unverified.

Paragraph numbers are assigned at build time from the order of this list, and
the cross-references in both directions are derived from the ``req`` tags. Nothing
is hand-numbered, so the two documents cannot drift apart.

Entry kinds:
    p      numbered guidance paragraph; ``req`` lists the CPS XXXX requirements it supports
    src    source attribution line, attaches to the preceding paragraph
    ver    verification annotation, rendered amber
    h      sub-heading within a chapter
    tbl    table: {"headers": [...], "rows": [[...]], "widths": [...], "caption": str}
    bul    bullet list attaching to the preceding paragraph

Status codes used in ``src`` lines:
    [B]  binding in its home jurisdiction
    [SE] supervisory expectation, not binding law
    [G]  guidance
    [PB] proposed / consultative
    [A]  analytical or advisory
"""

GUIDE = [
 # ================================================================ Chapter 1
 {"chapter": "Introduction",
  "intro": "This Prudential Practice Guide assists an APRA-regulated entity to comply with "
           "Prudential Standard CPS XXXX Model Risk Management. It uses 'should' to indicate "
           "expectations. Compliance with this guide is not itself mandatory; CPS XXXX uses "
           "'must' for requirements.",
  "items": [
   {"k": "p", "req": [], "t": "This guide is structured to follow CPS XXXX. Each chapter opens with the requirements it supports, so that a reader working from the standard can find the corresponding guidance, and a reader working from the guidance can identify the obligation it explains."},
   {"k": "p", "req": [], "t": "Guidance in this guide is drawn from Australian prudential requirements and from the model risk frameworks of comparable authorities. International sources are labelled by legal status: [B] binding in its home jurisdiction, [SE] supervisory expectation, [G] guidance, [PB] proposed or consultative, and [A] analytical or advisory. An overseas instrument is not binding in Australia whatever its status at home, and is used here only to inform expectations under CPS XXXX."},
   {"k": "src", "t": "Status classification follows Annex D of this guide and the source register in the accompanying assessment workbook."},
   {"k": "p", "req": [], "t": "APRA expects this guide to be applied proportionately. An entity with a small number of vendor models and one with several hundred internally developed models across banking, insurance and superannuation businesses face the same obligations but will meet them very differently."},
   {"k": "p", "req": [], "t": "This guide does not create obligations, does not vary CPS XXXX, and does not limit APRA's discretion in supervising an entity. Where this guide and CPS XXXX appear to differ, CPS XXXX prevails."},
   {"k": "h", "t": "Why model risk warrants a dedicated standard"},
   {"k": "p", "req": [], "t": "Regulated entities have increased their reliance on models faster than they have increased their capacity to govern them. Models now determine capital, provisions, valuations, insurance liabilities, unit prices, credit decisions, fraud interventions and member outcomes. The consequence of a model being wrong has grown with the consequence of the decisions it drives."},
   {"k": "p", "req": [], "t": "Model risk has historically been managed inside the frameworks for the risks the models measure — credit models under credit risk, valuation models under market risk — with the result that no one is accountable for the risk that the measurement itself is wrong. Comparable authorities have moved model risk into its own discipline for this reason."},
   {"k": "src", "t": "Source: PRA SS1/23 [SE]. OSFI Guideline E-23 (2027) [SE]. US interagency guidance on model risk management, SR 26-2 / OCC 2026-13 / FDIC FIL-15-2026 [SE]."},
   {"k": "p", "req": [], "t": "The most consequential failures observed internationally have rarely been mathematical. They have been failures of scope, where a model was not known to exist; of use, where a sound model was applied to a purpose it was not built for; of implementation, where the deployed model differed from the approved one; and of challenge, where a weakness was identified and not acted upon."},
  ]},

 # ================================================================ Chapter 2
 {"chapter": "Scope — what is a model",
  "items": [
   {"k": "p", "req": ["M02"], "t": "An entity should adopt a single enterprise definition of a model and apply it consistently. Fragmented definitions applied differently by business line produce inconsistent coverage and make aggregate model risk impossible to assess."},
   {"k": "p", "req": ["M02"], "t": "It is useful to think of a model as having three parts: an information input component that delivers data and assumptions, a processing component that transforms inputs into estimates, and a reporting component that translates the estimates into information a business can use. Each part can fail independently, and a failure in the first or third is as consequential as a failure in the second."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 1.1 Model definition [SE]. OSFI Guideline E-23 (2027), key terms [SE]. The three-component description originated in the 2011 United States interagency guidance, which was rescinded on 17 April 2026; the description remains analytically useful and is retained here on that basis rather than as a current citation."},
   {"k": "ver", "t": "Verification: the United States interagency guidance was revised on 17 April 2026 (SR 26-2, OCC Bulletin 2026-13, FDIC FIL-15-2026), rescinding the 2011 guidance. The 2026 definition is narrower — a 'complex' quantitative method applying statistical, economic or financial theories, expressly excluding simple arithmetic such as spreadsheet calculations and deterministic rule-based processes, and expressly excluding generative and agentic AI. CPS XXXX does not adopt that narrowing, for the reasons given in the standard. The divergence is deliberate."},
   {"k": "p", "req": ["M02"], "t": "The definition is function-based. Whether the processing component is a linear regression, a deterministic actuarial projection, a decision tree, a gradient-boosted ensemble or a large language model does not change whether the tool is a model. Defining scope by technology creates a perimeter that moves every time the technology does."},
   {"k": "p", "req": ["M02"], "t": "Quantitative estimates include forecasts, valuations, risk measures, scores, rankings, classifications and probabilities. A tool that produces a categorical output is a model where the classification rests on an estimate of an uncertain quantity — a score, a probability or a predicted class. A tool that reaches a categorical output by applying documented rules to its inputs, with no such estimate, falls outside the definition and is dealt with under M03."},
   {"k": "h", "t": "Applying the definition at the margin"},
   {"k": "p", "req": ["M02", "M03"], "t": "Entities should expect genuine borderline cases and should decide them on a documented basis. The practical question is whether uncertainty in the method could produce a materially wrong answer that a user would not detect. Where it could, the tool should generally be managed as a model."},
   {"k": "p", "req": ["M03"], "t": "Tools that fall outside the definition but drive material decisions should still be controlled. Complex spreadsheets, rules engines, allocation keys, pricing calculators and end-user computing tools fail in the same ways models fail — stale assumptions, broken links, undocumented changes, key-person dependency — without the benefit of the model lifecycle."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 1.1, which expects firms to consider quantitative methods falling outside the model definition [SE]."},
   {"k": "ver", "t": "Verification: PRA SS1/23's five principles and 23 sub-principles were extracted verbatim from the primary supervisory statement. Principle 1 is 'Model identification and model risk classification' and Principle 5 is 'Model risk mitigants'. An earlier draft in this project described Principle 5 as 'reporting'; that was incorrect and has been corrected here."},
   {"k": "p", "req": ["M03"], "t": "Controls for non-model quantitative tools need not replicate the model lifecycle. Identified ownership, version control, access restriction, documented logic, change control and periodic verification that the tool still performs as intended will usually be proportionate."},
   {"k": "h", "t": "Models the entity did not build"},
   {"k": "p", "req": ["M01", "M32"], "t": "A model is within scope because the entity relies on its output, not because the entity wrote it. Vendor models, models embedded in core banking, actuarial or treasury platforms, models inherited through acquisition, models operated by a service provider and models supplied by a parent or affiliate are all within scope."},
   {"k": "p", "req": ["M01"], "t": "Entities should be alert to models that arrive without a procurement decision — a feature enabled in an existing platform, an analytics capability switched on by a provider, or a tool adopted by a business team. These are the models least likely to appear in the inventory and least likely to have been assessed."},
  ]},

 # ================================================================ Chapter 3
 {"chapter": "Proportionality and model risk tiering",
  "items": [
   {"k": "p", "req": ["M04", "M15"], "t": "Tiering is the mechanism by which proportionality is made operational. It converts a general statement that controls should reflect risk into a specific determination of how much development evidence, validation depth, monitoring frequency, approval seniority and reporting each model attracts."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 1.3 Model tiering [SE]. OSFI Guideline E-23 (2027) Principle 2.2, on establishing a model risk rating approach that assesses key dimensions of model risk [SE]."},
   {"k": "p", "req": ["M15"], "t": "A tiering methodology should combine quantitative and qualitative factors. Quantitative factors typically include the size of the exposure, balance, provision, capital number or customer population the model influences. Qualitative factors include complexity, transparency, data quality, degree of automation, reversibility of the consequence and the availability of an alternative."},
   {"k": "p", "req": ["M15"], "t": "Materiality of use should dominate technical complexity. A simple deterministic calculation that sets a regulatory capital figure or a unit price warrants a higher tier than a sophisticated model used for internal management reporting. Tiering schemes anchored to methodological sophistication systematically under-govern the models that matter most."},
   {"k": "tbl", "caption": "Indicative tiering factors and how they translate into control intensity. Entities should calibrate to their own circumstances.",
    "headers": ["Factor", "Lower tier indicator", "Higher tier indicator"],
    "widths": [4.6, 6.0, 6.0],
    "rows": [
      ["Consequence of error", "Internal management information; readily corrected", "Regulatory capital, provisions, unit price, insurance liability or customer outcome"],
      ["Reliance", "Output is one input among several to a human decision", "Output is determinative or applied automatically at volume"],
      ["Transparency", "Method and drivers can be explained to a non-specialist", "Method is opaque; drivers cannot be readily attributed"],
      ["Data", "Ample, directly relevant internal data", "Sparse, proxy, external or unrepresentative data"],
      ["Reversibility", "Error detectable and correctable within a reporting period", "Error crystallises value transfer or is difficult to unwind"],
      ["Alternatives", "A credible fallback exists and has been tested", "No practical alternative; entity is dependent on the model"],
      ["Change dynamics", "Stable method, infrequent recalibration", "Frequent retraining, adaptive behaviour or vendor-driven change"],
    ]},
   {"k": "p", "req": ["M15"], "t": "The number of tiers matters less than the difference between them. Three tiers applied with genuine differentiation are more useful than five tiers that attract broadly similar treatment. If the tiering scheme does not change what actually happens to a model, it is documentation rather than control."},
   {"k": "p", "req": ["M15"], "t": "Entities should monitor the distribution of models across tiers over time. A population that migrates steadily downward, or in which very few models occupy the highest tier, warrants examination of whether the criteria are being applied as designed."},
   {"k": "h", "t": "De minimis models"},
   {"k": "p", "req": ["M05"], "t": "CPS XXXX permits an entity to determine that a model is de minimis and to apply to it only the identification, inventory, ownership, classification and reassessment requirements. The determination turns on consequence: whether the entity could be materially wrong, or materially unfair to a customer or beneficiary, if the model were wrong and the error went undetected."},
   {"k": "p", "req": ["M05"], "t": "It is not a determination about size, complexity, cost or how long a model has been in use. A simple model that has run without incident for a decade is not de minimis if an error in it would misstate a provision. Conversely a sophisticated model used to prioritise internal workflow may well be."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §III, which states that where models are deemed immaterial, model risk management may consist of identifying those models and monitoring the conditions under which their use may become material [SE]. OSFI Guideline E-23 (2027) Principle 2.3, read with Principle 2.1 [SE]. PRA SS1/23 Principle 1.3 Model tiering [SE]."},
   {"k": "p", "req": ["M05", "M14"], "t": "A de minimis model stays in the inventory. That is the point on which the exception depends: an entity that has removed a model from the inventory cannot demonstrate that the determination was ever made, still less that it remains correct. Entities should treat the de minimis population as a reportable category rather than as an absence."},
   {"k": "p", "req": ["M05"], "t": "Certain models cannot be de minimis whatever the entity's assessment. These are models determining a regulatory capital requirement, a provision, a technical or insurance liability, a valuation reported in the financial statements, a unit price or another amount attributable to a customer or beneficiary, and models supporting a critical operation. The consequence of error in these classes is realised directly and is frequently irreversible."},
   {"k": "p", "req": ["M05"], "t": "Two failure modes deserve specific attention. The first is aggregation: models that are individually immaterial can matter collectively, particularly where they feed the same process, share a data source or rest on a common assumption. The entity should examine the population, not only the individual determinations. The second is disaggregation: splitting a model so that each component falls below the threshold, which defeats the exception rather than satisfying it."},
   {"k": "p", "req": ["M05", "M16"], "t": "A determination attaches to a use, not to a model in the abstract. Where a model that was de minimis for one purpose begins to be relied on for another, the determination should be revisited before the new use begins rather than at the next scheduled review."},
   {"k": "ver", "t": "Verification: the de minimis mechanism is drawn from the treatment of immaterial models in the 2026 United States interagency guidance and from OSFI Principles 2.1 and 2.3, which relieve low-risk models of the full lifecycle while keeping them within identification. The prohibited classes, the aggregate test and the anti-disaggregation limb are Australian drafting choices and are identified as a policy design choice in the assessment workbook."},
   {"k": "h", "t": "Controlled exceptions"},
   {"k": "p", "req": ["M04"], "t": "Reduced controls should be a decision rather than an omission. An exception should identify the provision of the entity's own policies or standards not being met, the reason, the compensating control, the approver, the expiry date and the review point. It cannot except the entity from a requirement of CPS XXXX: only APRA may do that, under paragraph A5."},
   {"k": "p", "req": ["M04"], "t": "An exception register in which items have no expiry, or are routinely extended, indicates that the entity has adopted a lower standard rather than granted an exception. APRA supervisors may examine the age profile of exceptions as an indicator of framework effectiveness."},
   {"k": "ver", "t": "Verification: proportionality is expressly provided for in the PRA, OSFI and US frameworks. The specific expectation that exceptions be time-bound with recorded compensating controls is drawn from APRA's existing risk management architecture rather than from a comparator instrument, and is identified in the assessment workbook as a policy design choice."},
   {"k": "h", "t": "Reassessment"},
   {"k": "p", "req": ["M16"], "t": "Tiers should be reassessed on a defined cycle and on the occurrence of trigger events. Triggers should include material change to the model, its data, its purpose or its user base; significant growth in the exposure or population it covers; deterioration in performance; and changes the entity did not initiate, such as a vendor version release or a change in an upstream data definition."},
   {"k": "p", "req": ["M16"], "t": "Reliance can grow without any change to the model. A model built for a small portfolio that is progressively applied to a larger one has become more material without being touched, and a reassessment cycle driven only by model change will not detect this."},
  ]},

 # ================================================================ Chapter 4
 {"chapter": "Governance and accountability",
  "items": [
   {"k": "p", "req": ["M06"], "t": "The Board should understand what the entity relies on models to do, where that reliance is concentrated, what the consequences of failure would be, how failure would be detected, and what would happen next. It is not expected to understand model methodology."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 2 Governance, and Principle 2.1 Board of directors' responsibilities [SE]. OSFI Guideline E-23 (2027) Outcome 1 and Principle 1.1 [SE]. US interagency guidance 2026 §VI, governance and controls [SE]. CPS 220 Risk Management [B]."},
   {"k": "p", "req": ["M06", "M13"], "t": "Board reporting should support that understanding. Useful content includes the tiering profile and its movement, validation coverage and overdue validations against tier, unresolved high-severity findings and their age, material limitations accepted and the compensating controls relied on, the aggregate size and direction of overlays, model incidents, and concentration of reliance on individual providers or methods."},
   {"k": "p", "req": ["M13"], "t": "Reporting should aggregate rather than enumerate. A schedule of individual model issues does not tell the Board whether model risk is rising or falling. Trend, concentration and coverage are more informative than counts."},
   {"k": "p", "req": ["M06"], "t": "For a smaller entity, model risk reporting may sit within existing risk reporting rather than in a standalone pack, provided the Board receives the substance and can identify model risk as a distinct matter."},
   {"k": "h", "t": "Senior accountability"},
   {"k": "p", "req": ["M07"], "t": "A single senior executive should be accountable for the framework itself — its coverage, its consistency of application and its effectiveness. This is distinct from accountability for individual models, and exists so that framework-level failures have an owner."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 2.2, SMF accountability for the model risk management framework [SE]. OSFI Guideline E-23 (2027) Principle 1.1 [SE]."},
   {"k": "p", "req": ["M07"], "t": "The accountable executive should be positioned to require change. Accountability without the authority to direct remediation, or without independence from the businesses whose models are being governed, is unlikely to be effective."},
   {"k": "ver", "t": "Verification: the PRA allocates model risk management framework accountability to a designated senior management function. The precise interaction with the Australian accountability regime requires legal settlement and is flagged in Annex F of CPS XXXX."},
   {"k": "h", "t": "Model ownership"},
   {"k": "p", "req": ["M08"], "t": "Each model should have a named owner accountable for it being fit for its approved purpose, for its documentation being current, for its performance being monitored, for its limitations being communicated to users, and for the remediation of findings. Ownership recorded in the inventory but not exercised is not ownership."},
   {"k": "p", "req": ["M08"], "t": "Where several businesses use the same model, the entity should distinguish ownership of the model from ownership of each use. The model can be sound while a particular use of it is not, and the two failures require different responses."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §VI, roles and responsibilities [SE]. OSFI Guideline E-23 (2027) Principle 1.1 [SE]. ECB Guide to internal models, internal governance [SE]."},
   {"k": "h", "t": "Capability and independence"},
   {"k": "p", "req": ["M09"], "t": "Validation should be performed by people who did not build the model and who do not report to those who did or to the business sponsoring its use. Where a standing independent validation function is not practicable, independence can still be achieved — by drawing on qualified people elsewhere in the entity or group who were not involved in development, by engaging an external provider, or by escalating the review to a forum that is independent of the sponsoring business."},
   {"k": "p", "req": ["M09"], "t": "Independence is a matter of incentive as much as of reporting line. Where a validator's workload, progression or remuneration depends on models being approved, the control is compromised regardless of the organisational structure."},
   {"k": "p", "req": ["M09"], "t": "Smaller entities may achieve independence by using qualified people from elsewhere in the entity or group who were not involved in development, or by engaging an external provider. An entity that outsources validation should retain enough capability to scope the work, understand the findings and challenge the conclusions."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §V [SE]. PRA SS1/23 Principle 4.1 The independent validation function [SE]. ECB Guide to internal models, internal validation [SE]."},
  ]},

 # ================================================================ Chapter 5
 {"chapter": "Framework, appetite and policy",
  "items": [
   {"k": "p", "req": ["M10"], "t": "The framework should treat model risk as a risk in its own right. Treating it as a category of operational risk tends to produce incident-driven management after a failure rather than lifecycle management designed to prevent one."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 2 [SE]. OSFI Guideline E-23 (2027) Outcome 1, that model risk is well understood and managed across the enterprise [SE]. CPS 220 Risk Management [B]."},
   {"k": "p", "req": ["M10"], "t": "The framework should connect to, rather than duplicate, the entity's arrangements for data risk, information security, operational risk, change management, service provider management and internal audit. Where an entity operates a separate AI risk framework, the boundary between the two should be explicit."},
   {"k": "h", "t": "Model risk appetite"},
   {"k": "p", "req": ["M11"], "t": "A model risk appetite should be capable of being breached. An appetite expressed only as a statement of intent cannot be monitored and therefore cannot constrain behaviour."},
   {"k": "p", "req": ["M11"], "t": "Measurable expressions available to most entities include tolerance for the proportion of high-tier models with a current validation, the permitted number and age of unresolved high-severity findings, limits on the aggregate size of overlays relative to the modelled figure, and constraints on models operating outside approved conditions of use."},
   {"k": "p", "req": ["M11", "M42"], "t": "Entities that cannot yet quantify aggregate model risk should say so, use coverage and qualitative measures in the interim, and set out how they intend to develop the capability. An appetite deferred until quantification is available is an appetite that does not exist."},
   {"k": "ver", "t": "Verification: a model risk appetite is expected by the PRA and OSFI. Requiring it to be expressed in monitorable terms is a drafting choice that makes the obligation supervisable, and is identified as a policy design choice in the assessment workbook."},
   {"k": "h", "t": "Policies and standards"},
   {"k": "p", "req": ["M12"], "t": "Policies and standards should be applied consistently across the entity. Where different businesses apply materially different development, documentation or validation standards to models of equivalent tier, the entity should be able to justify the difference on risk grounds rather than on history or convenience."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 2.3 Policies and procedures [SE]. OSFI Guideline E-23 (2027) Principle 3.1 [SE]. US interagency guidance 2026 §VI, governance and controls [SE]."},
   {"k": "p", "req": ["M12"], "t": "Policies should be reviewed at least annually and version-controlled, with the substance of changes recorded. A policy library in which the current version cannot be established, or in which superseded versions remain in circulation, undermines the framework it documents."},
  ]},

 # ================================================================ Chapter 6
 {"chapter": "Identification and inventory",
  "items": [
   {"k": "p", "req": ["M14"], "t": "The inventory is the foundation of the framework. No requirement in CPS XXXX can be demonstrated for a model the entity does not know it has, and inventory completeness is therefore the first thing an entity should be able to evidence."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 1.2 Model inventory [SE]. OSFI Guideline E-23 (2027) Principle 2.1, on identifying and tracking all models in use or recently decommissioned [SE]. US interagency guidance 2026 §VI, model inventory [SE]."},
   {"k": "p", "req": ["M14"], "t": "Identification requires active discovery. Voluntary registration reliably under-reports, because the models least likely to be declared are those adopted without formal approval — precisely the population of greatest concern."},
   {"k": "p", "req": ["M14"], "t": "Discovery mechanisms that entities have found effective include:"},
   {"k": "bul", "items": [
     "procurement and vendor onboarding gates that ask directly whether a product contains or provides a model",
     "architecture and change approval gates applied to model deployment",
     "periodic attestation by business unit heads, naming the models their unit relies on",
     "reconciliation of the inventory against system inventories, data flows and expenditure",
     "review of material spreadsheets and end-user computing registers",
     "targeted enquiry following an acquisition or a platform upgrade",
   ]},
   {"k": "p", "req": ["M14"], "t": "The inventory should record decommissioned models where outputs they produced remain in force. A retired model that set a provision, a capital number, a customer price or an insurance liability that has not yet run off continues to carry model risk after the model itself has been switched off."},
   {"k": "p", "req": ["M14"], "t": "Annex B of CPS XXXX sets out the minimum inventory fields. Entities should treat these as a floor. The inventory should be maintained as a controlled record with defined update responsibilities rather than as a periodically refreshed spreadsheet."},
   {"k": "ver", "t": "Verification: inventory obligations were confirmed from the primary text of the PRA, OSFI and US instruments. OSFI's express inclusion of recently decommissioned models is extracted from Principle 2.1 of Guideline E-23 (2027)."},
  ]},

 # ================================================================ Chapter 7
 {"chapter": "Development, data and documentation",
  "items": [
   {"k": "p", "req": ["M17"], "t": "Conceptual soundness asks whether the chosen approach is appropriate for the intended purpose, given the data available and the conditions in which the model will operate. It is not answered by goodness of fit. A model that fits its development sample closely may be conceptually unsound if that sample is unrepresentative of the conditions of use."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §IV, model development and model use [SE]. PRA SS1/23 Principle 3.1 Model purpose and design [SE]. OSFI Guideline E-23 (2027) Principle 3.3 [SE]."},
   {"k": "p", "req": ["M17"], "t": "Development should record the purpose the model is being built for, the design decisions taken, the theory or empirical basis for them, the variables considered and why they were retained or rejected, the assumptions on which the model depends, and the limitations that development did not resolve."},
   {"k": "p", "req": ["M17"], "t": "Reasonable alternatives should be considered and the choice recorded. Where a more transparent method would have performed acceptably, the entity should be able to explain why a less transparent one was preferred. This is not a presumption against complex methods; it is a record that the trade-off was made deliberately."},
   {"k": "p", "req": ["M17"], "t": "Development evidence should include the tests that were run and their results, including tests the model did not pass and how that was resolved. Documentation presenting only successful tests gives validation and approval an incomplete picture."},
   {"k": "h", "t": "Data"},
   {"k": "p", "req": ["M18"], "t": "Data should be assessed for appropriateness as well as accuracy. Accurate data drawn from a population, product, geography or period unlike the one in which the model will be used produces confident and wrong answers, and is a more common failure than poor data quality."},
   {"k": "src", "t": "Source: BCBS 239 Principles for effective risk data aggregation and risk reporting [G]. OSFI Guideline E-23 (2027) Principle 3.2, that data used to develop the model should be suitable for the intended use [SE]. CPG 235 Managing Data Risk [G]. ECB Guide on effective risk data aggregation and risk reporting [SE]."},
   {"k": "p", "req": ["M18"], "t": "Entities should document data lineage to source for material models, so that a change in an upstream system or definition can be traced to the models it affects. Lineage that stops at the data warehouse does not support that assessment."},
   {"k": "p", "req": ["M18"], "t": "Where proxy or external data substitutes for insufficient internal data, the basis for considering the proxy suitable should be recorded and the sensitivity of the output to that choice should be tested. Proxies adopted at development frequently persist long after internal data has become available."},
   {"k": "p", "req": ["M18", "M34"], "t": "Synthetic data used in development or testing should be identified as such, with its generation method documented and its representativeness assessed. Testing a model on synthetic data generated from the same assumptions used to build it does not test those assumptions."},
   {"k": "h", "t": "Documentation"},
   {"k": "p", "req": ["M19"], "t": "The practical standard for documentation is reconstruction: a competent person who was not involved in the model's development should be able to pick up the documentation and reproduce its material results. Documentation that depends on the continued availability of the developer is a key-person dependency."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §VI, documentation [SE]. PRA SS1/23 Principle 3.5 Model development documentation [SE]. ECB Guide to internal models, documentation [SE]."},
   {"k": "p", "req": ["M19"], "t": "Documentation should be maintained through the model's life. Documentation assembled in response to a validation cycle or a supervisory request describes the model as it is remembered rather than as it was built and changed."},
  ]},

 # ================================================================ Chapter 8
 {"chapter": "Testing, validation and approval",
  "items": [
   {"k": "p", "req": ["M20"], "t": "Development testing and validation are different exercises with different purposes. Development testing establishes whether the model works as its developers intended. Validation forms an independent view of whether it is fit to be relied upon."},
   {"k": "p", "req": ["M20"], "t": "Pre-implementation testing should cover performance under expected conditions and under stressed, boundary and unrepresentative conditions; sensitivity to key assumptions and inputs; stability over time and across segments; and behaviour at the edges of the population the model will encounter."},
   {"k": "p", "req": ["M20"], "t": "Testing should use data sufficiently independent of the data used to fit the model. Out-of-sample and, where possible, out-of-time testing should be standard for higher-tier models."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §IV, model testing [SE]. PRA SS1/23 Principle 3.3 Model development testing [SE]."},
   {"k": "h", "t": "The three elements of validation"},
   {"k": "p", "req": ["M22"], "t": "Validation should address three complementary components: conceptual soundness, including assessment of model design, key modelling choices, assumptions, data selection, construction and developmental evidence; outcomes analysis, comparing model outputs with corresponding real-world outcomes; and ongoing model monitoring, evaluating whether the model continues to perform as expected as products, exposures, activities, clients, data relevance or market conditions change."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §V, components of model validation [SE]. PRA SS1/23 Principle 4.2 Independent review, 4.3 Process verification and 4.4 Model performance monitoring [SE]. OSFI Guideline E-23 (2027) Principle 3.4 [SE]."},
   {"k": "p", "req": ["M22"], "t": "No component is sufficient alone. Conceptual soundness cannot detect deterioration after implementation. Outcomes analysis can detect deterioration but not explain it. Verification that the model was built and deployed as documented says nothing about whether the design was appropriate in the first place."},
   {"k": "p", "req": ["M22", "M25"], "t": "Validation should test implementation as well as design — that the model as coded and running in production is the model as documented and approved. Differences in data definitions, rounding, treatment of missing values, library versions or execution order between environments can change results materially and are not detected by methodological review."},
   {"k": "p", "req": ["M22"], "t": "A validation report should reach an explicit conclusion on fitness for the intended use, with any conditions or limitations stated. A report that records observations without a conclusion leaves the approval decision without the input it was designed to receive."},
   {"k": "tbl", "caption": "Indicative validation intensity by tier. This table deliberately states the drivers rather than fixed intervals: no comparator authority prescribes validation frequencies on a cross-industry basis, and the OCC has confirmed that its guidance does not require annual validation. Entities should set their own cycle lengths and trigger events, and be able to justify them by tier.",
    "headers": ["Element", "Tier 1 (highest)", "Tier 2", "Tier 3 (lowest)"],
    "widths": [4.2, 4.4, 4.0, 4.0],
    "rows": [
      ["Independent validation before use", "Full, by a function independent of development", "Full, proportionate scope", "Review by a competent person not involved in development"],
      ["Periodic revalidation", "Short cycle, and on any trigger event", "Longer cycle, and on material trigger events", "Extended cycle, and on material change"],
      ["Outcomes analysis", "Frequent, with formal backtesting where outcomes are observable", "Periodic; alternative evidence where outcomes are not observable", "Periodic, may be qualitative"],
      ["Benchmarking", "Against an alternative model or challenger where practicable", "Where practicable", "Not ordinarily required"],
      ["Process verification", "Full, including code and environment review", "Targeted", "Confirmation of implementation"],
      ["Approval authority", "Board committee or designated senior forum", "Senior executive or model risk committee", "Delegated within policy"],
    ]},
   {"k": "ver", "t": "Verification: the three components of validation are extracted from the current US interagency guidance, which is supervisory guidance rather than a regulation and is non-enforceable by its own terms. No fixed validation frequency is stated in this guide: the rescinded 2011 US guidance contained an at-least-annual periodic review expectation which the April 2026 guidance does not carry forward, and OCC Bulletin 2025-26 confirms that community banks are not required to validate annually. Setting cycle lengths is left to the entity, by tier."},
   {"k": "h", "t": "Effective challenge"},
   {"k": "p", "req": ["M23"], "t": "Effective challenge is critical and objective analysis by people with three attributes together: the expertise to identify model limitations, sufficient independence to maintain objectivity, and the organisational standing and influence to bring about change. Removing any one defeats the control while leaving its documentation intact. Entities should also attend to incentives, since a challenger rewarded for clearing models will not challenge for long."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §III, effective challenge [SE]. PRA SS1/23 Principle 4 Independent model validation [SE]."},
   {"k": "p", "req": ["M23"], "t": "Indicators that challenge is not effective include findings consistently closed by explanation rather than by change, findings downgraded in severity without new evidence, validation conclusions that soften late in the approval process, and validation functions whose resourcing is set by the businesses whose models they review."},
   {"k": "p", "req": ["M23", "M44"], "t": "Entities should periodically assess whether challenge is working, rather than assuming it from the existence of a validation function. Analysis of finding closure routes, severity migration and elapsed time to remediation is more informative than validation completion rates."},
   {"k": "h", "t": "Vendor validation"},
   {"k": "p", "req": ["M21", "M32"], "t": "Vendor validation reports, certifications and third-party audit opinions may inform the entity's validation. They do not discharge it, because they are not designed around the entity's data, portfolio, controls or intended use. An entity relying on them should record what they cover and what remains for the entity to test."},
   {"k": "h", "t": "Approval"},
   {"k": "p", "req": ["M24"], "t": "Approval should be of a specific model version for a specific purpose under specific conditions. Approval expressed in general terms leaves no basis on which to determine later whether the model is being used as approved."},
   {"k": "p", "req": ["M24"], "t": "The approval record should identify the approved version, the permitted uses and users, any limits on application, the monitoring thresholds that apply, the limitations accepted and the compensating controls relied upon, and the date by which the model must be reviewed."},
   {"k": "src", "t": "Source: OSFI Guideline E-23 (2027), model approval within the model lifecycle [SE]. ECB Guide to internal models [SE]."},
   {"k": "p", "req": ["M24", "M30"], "t": "Approval despite unresolved high-severity findings should be exceptional, time-bound, supported by compensating controls and escalated to the forum that set the model risk appetite."},
  ]},

 # ================================================================ Chapter 9
 {"chapter": "Implementation, use and change",
  "items": [
   {"k": "p", "req": ["M25"], "t": "Implementation is an under-appreciated source of model failure. Validation focused on methodology will not detect that the production model differs from the approved one, and such differences arise routinely from environment, data pipeline and configuration differences rather than from deliberate change."},
   {"k": "p", "req": ["M25"], "t": "Entities should verify, before a model is relied upon in production, that it reproduces the approved model's results on a controlled set of cases, and should repeat that verification after material infrastructure or data pipeline change."},
   {"k": "src", "t": "Source: Former SR 11-7 §IV, implementation — not carried forward as a separate heading in the 2026 guidance [SE]. OSFI Guideline E-23 (2027) Principle 3.5, that models should be deployed in an environment with quality and change control processes [SE]. PRA SS1/23 Principle 3.6 Supporting systems [SE]."},
   {"k": "h", "t": "Change"},
   {"k": "p", "req": ["M26"], "t": "Change assessment should consider the change both in isolation and cumulatively. A sequence of individually immaterial recalibrations can move a model materially away from the version that was validated, and change frameworks that assess only the increment will not detect this."},
   {"k": "p", "req": ["M26"], "t": "Changes the entity did not initiate are still changes to its model risk profile. A vendor version release, a change in an upstream data definition, a change in the composition of a portfolio the model is applied to, or a change in the regulatory basis of a calculation should each enter the change assessment."},
   {"k": "src", "t": "Source: ECB Guide to internal models, management of model changes [SE]. OSFI Guideline E-23 (2027) Principle 3.5 [SE]."},
   {"k": "h", "t": "Use"},
   {"k": "p", "req": ["M27"], "t": "Misuse of a sound model is one of the two recognised sources of model risk and is frequently the less well controlled. Common patterns include applying a model built to rank relative risk to set absolute prices, applying a model developed on one portfolio to another, and continuing to rely on a model in conditions it was known not to cover."},
   {"k": "src", "t": "Source: Former SR 11-7 §III, the two sources of model risk — the 2026 guidance retains the misuse limb [SE]. PRA SS1/23 Principle 3 [SE]. ECB Guide to internal models, use test [SE]."},
   {"k": "p", "req": ["M27"], "t": "Users should be given the model's limitations, not merely have access to them. Limitations recorded in a validation report that users do not read are not communicated. Entities should consider embedding limitations and conditions of use in the systems through which users receive model output."},
   {"k": "h", "t": "Overlays and expert judgement"},
   {"k": "p", "req": ["M28"], "t": "Adjustments to model output should be governed with the same discipline as the model. The basis, the quantification, the approver, the duration and the conditions for removal should each be recorded."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 5.1 Process for applying post-model adjustments [SE]. ECB Guide to internal models, margin of conservatism [SE]."},
   {"k": "p", "req": ["M28"], "t": "A persistent overlay in a consistent direction is evidence about the model rather than a correction to it. Where an entity has adjusted a model's output in the same direction for successive periods, the appropriate response is usually redevelopment rather than continued adjustment."},
   {"k": "p", "req": ["M28", "M13"], "t": "Overlays should be reported in aggregate. Individually approved adjustments can collectively become the dominant driver of a reported figure without any single approval having considered that effect."},
   {"k": "ver", "t": "Verification: post-model adjustments are addressed expressly by PRA SS1/23 Principle 5.1, which defines them to include model overlays, management overlays and model overrides. The ECB addresses the same issue through the margin of conservatism framework for internal models."},
  ]},

 # ================================================================ Chapter 10
 {"chapter": "Monitoring, mitigants and retirement",
  "items": [
   {"k": "p", "req": ["M29"], "t": "Monitoring should test whether the conditions that made the model valid continue to hold, not only whether its output has moved. A model can produce stable output while the relationships it depends on have broken down."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §V, ongoing model monitoring [SE]. PRA SS1/23 Principle 4.4 Model performance monitoring [SE]. OSFI Guideline E-23 (2027) Principle 3.6 [SE]."},
   {"k": "p", "req": ["M29"], "t": "Thresholds should be set in advance and linked to a defined response — investigation, escalation, restriction of use, revalidation, overlay or withdrawal. A threshold that produces a note rather than an action is not a control."},
   {"k": "p", "req": ["M29"], "t": "Monitoring should cover input data as well as output. Shifts in the distribution, completeness or definition of inputs frequently precede deterioration in output and provide earlier warning."},
   {"k": "h", "t": "Limitations and remediation"},
   {"k": "p", "req": ["M30"], "t": "Compensating controls should be specific to the limitation they address. A general statement that outputs are subject to management review does not compensate for a known bias in a particular segment, because it does not direct attention to that segment."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 5 Model risk mitigants, and Principle 5.2 Restrictions on model use [SE]."},
   {"k": "p", "req": ["M30"], "t": "Entities should monitor how findings are closed. A high proportion closed by rationale, deferral or reclassification rather than by change indicates that remediation is not functioning, even where closure rates appear satisfactory."},
   {"k": "h", "t": "Restriction, suspension and retirement"},
   {"k": "p", "req": ["M31"], "t": "An entity should know in advance what it would do if a material model became unusable — whether an alternative exists, how long it would take to bring into service, and what the interim basis for decisions would be. For models supporting a critical operation, this should be tested."},
   {"k": "src", "t": "Source: OSFI Guideline E-23 (2027) Principle 3.6, model decommission [SE]. CPS 230 Operational Risk Management [B]."},
   {"k": "p", "req": ["M31"], "t": "Decommissioning should address downstream models that consume the retired model's output, decisions and balances that remain in force, retained records, and the disposition of data. Retirement that switches off the model without addressing its residue leaves risk in place without an owner."},
  ]},

 # ================================================================ Chapter 11
 {"chapter": "Third-party models",
  "items": [
   {"k": "p", "req": ["M32"], "t": "A third-party model is subject to the same framework as an internally developed one. The entity's ability to inspect it is lower, which increases rather than reduces the work required to gain assurance."},
   {"k": "src", "t": "Source: US interagency guidance 2026 §VII, vendor and other third-party products [SE]. PRA SS1/23 Principle 2.6 Use of externally developed models, third-party vendor products [SE]. OSFI Guideline E-23 (2027), third-party models [SE]."},
   {"k": "p", "req": ["M32"], "t": "Where a provider will not disclose methodology, the entity should intensify what it can do independently: benchmarking against an alternative, outcomes analysis on its own portfolio, sensitivity testing through controlled variation of inputs, and tighter conditions of use. Opacity should narrow the approved use, not widen the tolerance."},
   {"k": "p", "req": ["M32"], "t": "An entity should not accept from a provider a level of opacity it would not accept from an internal development team for a model of the same tier."},
   {"k": "h", "t": "Information rights"},
   {"k": "p", "req": ["M33"], "t": "Information rights should be usable in practice. A contractual audit right the entity has neither the capability nor the intention to exercise provides little assurance. Rights to timely notice of material model change, to performance information and to incident notification are generally more valuable."},
   {"k": "src", "t": "Source: CPS 230 Operational Risk Management, service provider management [B]. BCBS Principles for the sound management of third-party risk [G]."},
   {"k": "p", "req": ["M33"], "t": "CPS XXXX does not require access to vendor source code or training data. It requires sufficient information, or sufficient compensating control, for the entity to form a view on fitness for its own use."},
   {"k": "h", "t": "Concentration"},
   {"k": "p", "req": ["M33"], "t": "Concentration should be assessed at entity level and, so far as observable, across the industry. Widespread reliance on the same external model, data source or platform can produce correlated error across firms even where each firm's own governance is sound, and this is a supervisory concern that no individual firm's controls address."},
   {"k": "src", "t": "Source: FSB, The Financial Stability Implications of Artificial Intelligence [A]. BCBS Principles for the sound management of third-party risk [G]."},
  ]},

 # ================================================================ Chapter 12
 {"chapter": "Artificial intelligence and machine learning models",
  "items": [
   {"k": "p", "req": ["M34"], "t": "An artificial intelligence or machine learning model is a model. Every requirement of CPS XXXX applies to it. This chapter addresses the respects in which those requirements are harder to satisfy, not a separate regime."},
   {"k": "src", "t": "Source: OSFI Guideline E-23 (2027), which expressly brings AI and machine learning models within model risk management [SE]. MAS, Artificial Intelligence Model Risk Management information paper [G]. BCBS, Digitalisation of finance [A]."},
   {"k": "p", "req": ["M34"], "t": "The characteristic difficulties are limited explainability, sensitivity to data drift, instability across retraining cycles, susceptibility to feature leakage, systematic differences in model performance across segments of the population to which the model is applied, and dependence on externally supplied models whose construction cannot be inspected."},
   {"k": "h", "t": "Explainability"},
   {"k": "p", "req": ["M34"], "t": "Explainability should be assessed against what the entity actually needs to do: satisfy itself the model is sound, monitor it, explain an outcome to a person affected by it, and meet applicable legal obligations. These require different depths of explanation and an absolute standard is neither achievable nor useful."},
   {"k": "p", "req": ["M34"], "t": "Where explainability is limited, outcome-based controls should be intensified rather than relaxed. Suitable measures include comparison against a more transparent benchmark model, stability testing across retraining cycles, subgroup outcome analysis, monitoring of input distribution shift, and narrower conditions of use."},
   {"k": "ver", "t": "Verification: an absolute explainability requirement was considered and rejected. Comparator authorities consistently frame explainability as fit-for-purpose and permit compensating controls where full explainability is not achievable. This is recorded in the red-team audit trail."},
   {"k": "h", "t": "Retraining and adaptive behaviour"},
   {"k": "p", "req": ["M34", "M26"], "t": "Where a model retrains automatically, the entity should define the envelope within which retraining is authorised — the data it may use, the performance bounds it must remain within, and the parameters it may adjust — and should treat movement outside that envelope as a model change requiring assessment."},
   {"k": "p", "req": ["M34"], "t": "Retraining should be monitored for stability. A model whose behaviour changes materially between retraining cycles on similar data is exhibiting a form of instability that periodic validation will not detect."},
   {"k": "h", "t": "Boundary with AI risk management"},
   {"k": "p", "req": ["M35"], "t": "Where an entity operates a separate AI risk management framework, the two address different risks in the same system. CPS XXXX governs whether a quantitative output is fit to be relied upon. AI risk management governs the wider consequences of the system's operation, including security, autonomy, data handling, human oversight and resilience."},
   {"k": "p", "req": ["M35"], "t": "A generative or agentic system that produces no quantitative estimate used in decision-making is generally not a model, but remains subject to the entity's AI risk arrangements. A generative system used to produce an estimate that drives a material decision falls within both."},
   {"k": "p", "req": ["M35"], "t": "The entity should record, for each AI system, which framework or frameworks apply, so that the boundary is a documented determination that can be reviewed rather than an assumption that can leave a system ungoverned."},
   {"k": "ver", "t": "Verification: no comparator authority operates parallel model risk and AI risk instruments; OSFI deliberately brought AI within a single model risk guideline. The boundary rule in CPS XXXX is therefore an Australian drafting choice arising from the proposed two-instrument architecture, and is identified as a policy design choice requiring consultation."},
  ]},

 # ================================================================ Chapter 13
 {"chapter": "Specialist model classes",
  "items": [
   {"k": "p", "req": ["M36"], "t": "Models used to determine a regulatory capital requirement remain subject to the approval and change requirements of the applicable capital standard. CPS XXXX sits alongside those requirements and does not displace them; where the two overlap, the more specific requirement prevails."},
   {"k": "src", "t": "Source: APS 113 Capital Adequacy: Internal Ratings-based Approach to Credit Risk [B]. ECB Guide to internal models [SE], interpreting binding Capital Requirements Regulation provisions [B]. PRA SS1/23, which applies to firms with internal model approval [SE]."},
   {"k": "p", "req": ["M36"], "t": "The requirement that an approved capital model be used in internal risk management is substantive rather than formal. Where a model is maintained for regulatory reporting while the business is managed on a different basis, one of the two is not trusted, and the entity should be able to explain which and why."},
   {"k": "h", "t": "Valuation and financial reporting"},
   {"k": "p", "req": ["M37"], "t": "Valuation models concentrate model risk because the output is the reported number rather than an input to a decision a person subsequently makes. Level 3 valuations, illiquid exposures and modelled expected credit loss are the most sensitive to assumption choice and warrant the most independent scrutiny."},
   {"k": "src", "t": "Source: BCBS, Supervisory guidance for assessing banks' financial instrument fair value practices [G]."},
   {"k": "p", "req": ["M37"], "t": "Independent price verification is a distinct control from model validation. Both are expected for material valuation models, and an entity should not treat the presence of one as satisfying the other."},
   {"k": "h", "t": "Actuarial and insurance models"},
   {"k": "p", "req": ["M39"], "t": "For an insurer, the Appointed Actuary framework already provides a form of independent professional review that will discharge a substantial part of the validation expectation for many actuarial models. It does not automatically discharge all of it, particularly implementation verification and data quality assessment."},
   {"k": "p", "req": ["M39"], "t": "Insurers should map which elements of CPS XXXX validation are met through the actuarial control cycle and which require separate work, rather than assuming complete overlap in either direction. The mapping should be documented and reviewed."},
   {"k": "ver", "t": "Verification: OSFI's extension of Guideline E-23 (2027) to life and property and casualty insurers establishes the precedent for applying model risk management to insurance models. The specific interaction with the Australian Appointed Actuary framework is an Australian drafting question flagged for legal settlement."},
   {"k": "h", "t": "Superannuation models"},
   {"k": "p", "req": ["M40"], "t": "For an RSE licensee, unit pricing and asset valuation models directly determine amounts credited to member accounts. An error is realised as a transfer of value between members and is frequently difficult to reverse, which places these models at the higher end of any reasonable tiering assessment."},
   {"k": "p", "req": ["M40"], "t": "Liquidity models supporting investment strategy should be tested against the conditions in which they would actually be relied upon, rather than against normal conditions in which liquidity is not in question."},
   {"k": "ver", "t": "Verification: no comparator authority addresses superannuation model risk. Application to RSE licensees is an Australian policy design choice arising from the cross-industry scope of the proposed standard, and is identified as such in the assessment workbook."},
   {"k": "h", "t": "Stress testing and scenario models"},
   {"k": "p", "req": ["M41"], "t": "Stress testing models are used where historical data is least informative, so their results depend heavily on assumption and expert judgement. That makes the governance of assumptions the principal control rather than a reason to reduce governance."},
   {"k": "src", "t": "Source: BCBS Stress testing principles [G]. CPS 220 Risk Management [B]."},
   {"k": "p", "req": ["M41"], "t": "Forward-looking scenario models addressing risks with limited historical precedent, including climate scenarios, should be presented to decision-makers with the uncertainty in their outputs made explicit, and should not be reported with a precision the method cannot support."},
  ]},

 # ================================================================ Chapter 13A
 {"chapter": "Expected credit loss and provisioning models",
  "intro": "This chapter addresses models used to assess and measure expected credit losses and to "
           "determine provisions, and sets out the focus areas APRA would expect a review of those "
           "models to cover.",
  "items": [
   {"k": "p", "req": ["M38"], "t": "Expected credit loss models occupy a distinctive position. For most models the output informs a decision that a person then makes; for an expected credit loss model the output is the provision itself. An error is realised immediately in the financial statements, in regulatory capital and in the reported credit quality of the portfolio, and it is realised at the level of the aggregate rather than one exposure at a time."},
   {"k": "p", "req": ["M38"], "t": "The Australian obligation already exists and is binding. APS 220 requires an ADI to have sound policies and processes in place to appropriately validate models used to assess and measure expected credit losses, to adopt sound methodologies for assessing and measuring credit losses, to hold aggregate provisions that are adequate and consistent with the objectives of Australian Accounting Standards, and to use experienced credit judgement in the robust consideration of reasonable and supportable forward-looking information."},
   {"k": "src", "t": "Source: APS 220, Credit risk and accounting for expected credit losses [B]. APG 220, which states that the Basel Committee's Guidance on credit risk and accounting for expected credit losses of 18 December 2015 sets out guidance on sound credit risk practices and that APRA expects ADIs to have regard to it [G]. BCBS d350 [G]."},
   {"k": "ver", "t": "Verification: the APS 220 obligation to validate expected credit loss models is a near-verbatim transposition of BCBS d350 Principle 5, which reads 'A bank should have policies and procedures in place to appropriately validate models used to assess and measure expected credit losses.' Both texts were read in the primary instruments. This is one of the few domains in which the Australian framework already carries an international model risk principle in binding form."},
   {"k": "p", "req": ["M38"], "t": "What APS 220 does not supply is the content of that validation — what it consists of, who may perform it, how often, and what follows when it finds something. CPS XXXX supplies exactly that. The two are complementary: APS 220 states the obligation, this Prudential Standard states the discipline, and where they overlap APS 220 prevails as the more specific instrument."},

   {"k": "h", "t": "Judgement-based adjustments and overlays"},
   {"k": "p", "req": ["M38", "M28"], "t": "APRA has observed that many ADIs continue to apply sizeable judgement-based adjustments to compensate for model and data limitations. Adjustments have a legitimate role: models alone may not be calibrated to capture every driver of credit risk, particularly where conditions have moved outside the estimation window. But an overlay is a statement that the model is wrong, and it should be governed as such."},
   {"k": "src", "t": "Source: APRA, Credit risk provisioning practices for locally incorporated authorised deposit-taking institutions, 19 October 2023 [G]. BCBS Newsletter on credit risk issues, 4 July 2023 [A]."},
   {"k": "p", "req": ["M38", "M28"], "t": "Where judgemental adjustments are made, APRA expects them to be supported by documented analysis and robust controls and governance, including sound processes for their application, controls over the efficacy of the output, and senior management oversight and accountabilities. An entity should also be able to show that it is monitoring and improving model performance rather than allowing overlays to become a permanent substitute for recalibration."},
   {"k": "p", "req": ["M38", "M28"], "t": "The practical test is direction and persistence. An overlay applied in the same direction across successive reporting periods is evidence that the model no longer reflects the exposure. A reviewer would expect to see either a redevelopment plan or a reasoned explanation of why the condition being corrected is genuinely temporary."},

   {"k": "h", "t": "Capturing economic uncertainty"},
   {"k": "p", "req": ["M38", "M40"], "t": "Sensitivity analysis is how an entity demonstrates that it understands what its provision depends on. APRA expects comprehensive sensitivity analysis to be performed on a regular and timely basis across credit portfolios, segmented by industry, geography and other relevant dimensions, so that management and the Board can see how provisions respond to changes in the key underlying drivers of credit risk."},
   {"k": "p", "req": ["M38", "M40"], "t": "This analysis can form part of the entity's broader stress testing capability and inform the internal capital adequacy assessment process and risk appetite review. The same governance expectations apply to it as to the models: clear accountabilities, robust controls and oversight over both the process and the decisions taken from it."},
   {"k": "src", "t": "Source: APRA provisioning letter, 19 October 2023 [G]. CPG 110 Internal Capital Adequacy Assessment Process and Supervisory Review [G]."},

   {"k": "h", "t": "Identifying credit deterioration"},
   {"k": "p", "req": ["M38"], "t": "APRA has observed that many ADIs continue to rely on manually intensive and judgement-driven processes to capture the effect of emerging risks on vulnerable borrowers and sectors, and has encouraged investment in systematic processes that identify vulnerable sectors and factor sectoral risk into loss estimates."},
   {"k": "p", "req": ["M38"], "t": "Three things carry most of the weight here: the use of collective assessments, the level of segmentation in the models and the data behind them, and the indicators used to transfer exposures in vulnerable sectors into Stage 2 under AASB 9. The staging decision is a modelled judgement with a direct and often large effect on the reported provision, and it should be validated with that in mind."},

   {"k": "h", "t": "Focus areas for a review of expected credit loss models"},
   {"k": "p", "req": ["M38", "M45"], "t": "Annex G of CPS XXXX sets out the focus areas APRA would expect a review of expected credit loss models to cover. They are drawn from APRA's own published observations on provisioning practice, from the requirements of APS 220, and from the Basel guidance that APG 220 directs ADIs to have regard to."},
   {"k": "p", "req": ["M38", "M45"], "t": "The focus areas are not a checklist to be completed. A review that confirms each item exists without forming a view on whether the provision is right will not have answered the question. The purpose of each area is to test whether the number the entity has reported is supportable."},

   {"k": "h", "t": "Special purpose engagements under APS 220"},
   {"k": "p", "req": ["M45"], "t": "APS 220 contains a Special purpose engagements provision under which APRA may require an ADI to appoint an independent party to review and provide a report to APRA on all or a particular aspect of the ADI's credit risk management, including provisioning practices. APRA may request such a report without prior consultation with the ADI, may set the terms of the review, and may do so at the ADI's expense."},
   {"k": "src", "t": "Source: APS 220, Special purpose engagements [B]. The provision is quoted in full in Annex G of CPS XXXX."},
   {"k": "p", "req": ["M45"], "t": "A review of expected credit loss models along the lines set out in Annex G is precisely the kind of engagement that provision contemplates, and entities should expect that APRA may commission one on that basis. The terms of reference would be set by APRA rather than negotiated, and the report would be provided to APRA."},
   {"k": "p", "req": ["M45"], "t": "An entity that maintains its expected credit loss models in accordance with this Prudential Standard should be able to support such an engagement from existing records rather than by assembling evidence in response to it. Where an entity could not, that is itself informative about the state of its model risk management."},
   {"k": "ver", "t": "Verification: the Special purpose engagements provision was read verbatim from APS 220. Paragraph numbers are not asserted because the published rendering of the standard used for verification does not carry them; the provision is cited by its section heading. The proposition that APRA may commission an expected credit loss model review under it is a reading of the provision's express words, which extend to 'all or a particular aspect of the ADI's credit risk management, including provisioning practices'."},
  ]},

 # ================================================================ Chapter 14
 {"chapter": "Aggregate model risk, records and assurance",
  "items": [
   {"k": "p", "req": ["M42"], "t": "Aggregate assessment need not begin with quantification. Concentration of reliance, correlation of method and data across models, common assumptions, and the extent of unvalidated or overdue models are all informative and are generally available before a quantification capability exists."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 2.1 Board of directors' responsibilities, which covers understanding and reporting of model risk both individually and in aggregate [SE]. US interagency guidance 2026 §III [SE]. ECB supervisory review of model risk [SE]."},
   {"k": "p", "req": ["M42"], "t": "Where an entity concludes that no capital is warranted in respect of model risk, that conclusion should be reasoned and recorded. Reaching it by omission is not a conclusion."},
   {"k": "p", "req": ["M42"], "t": "Correlation deserves particular attention. Models that share a data source, a vendor, a core assumption or a development team can fail together, and an aggregate view built by summing independent assessments will understate that exposure."},
   {"k": "h", "t": "Records"},
   {"k": "p", "req": ["M43"], "t": "Reconstructability allows a supervisor, auditor, actuary or court to establish what the entity knew and when. It should be designed into the model's operation rather than assembled after the event, because the records that matter most are usually those not retained by default."},
   {"k": "p", "req": ["M43"], "t": "Retention periods should align with the entity's other prudential record-keeping obligations and with the period over which the decisions the model informed remain material. For long-tail insurance liabilities and superannuation member outcomes, that period can be considerably longer than for credit decisions."},
   {"k": "h", "t": "Assurance"},
   {"k": "p", "req": ["M44"], "t": "Internal audit's role is to assess whether the framework works, not to re-perform validation. Testing whether findings are genuinely resolved, whether tiering is applied consistently across businesses, and whether the inventory is complete is generally more informative than re-examining model methodology."},
   {"k": "src", "t": "Source: PRA SS1/23 Principle 2.5 Internal Audit [SE]. US interagency guidance 2026 §VI, roles and responsibilities [SE]. ECB Guide to internal models, internal audit [SE]."},
   {"k": "p", "req": ["M44"], "t": "Where internal audit lacks the technical capability to assess validation quality, the entity should obtain that capability, through co-sourcing or specialist recruitment, rather than narrow the scope of the assurance to what the existing team can cover."},
   {"k": "h", "t": "Engagement with APRA"},
   {"k": "p", "req": ["M45"], "t": "Early engagement is expected where an entity identifies a material weakness in a model used for regulatory capital, reserving or reporting. Engagement at the point the correction is finalised gives APRA no opportunity to consider the issue while options remain open."},
   {"k": "p", "req": ["M45"], "t": "Where a model failure is also an operational risk or information security incident, the notification requirements of the applicable prudential standards apply. CPS XXXX does not create a separate or conflicting deadline."},
   {"k": "ver", "t": "Verification: the decision not to introduce a model-risk-specific notification deadline was deliberate. Introducing one risked conflicting with existing materiality criteria and timeframes, and is recorded as a correction in the red-team audit trail."},
  ]},

 # ================================================================ Chapter 15
 {"chapter": "Implementation",
  "items": [
   {"k": "p", "req": [], "t": "APRA recognises that meeting CPS XXXX will require material uplift for many entities, particularly in inventory completeness, tiering consistency and validation coverage. The following phasing is indicative and would be settled through consultation."},
   {"k": "tbl", "caption": "Indicative implementation phasing. Dates are illustrative and subject to consultation and to the commencement provisions ultimately settled.",
    "headers": ["Phase", "Focus", "Indicative activities"],
    "widths": [3.4, 4.0, 9.2],
    "rows": [
      ["Phase 1", "Foundation", "Designate the accountable executive. Adopt the model definition. Establish the framework and policy. Begin enterprise discovery and populate the inventory."],
      ["Phase 2", "Classification and coverage", "Complete the inventory. Apply tiering across the population. Establish validation arrangements for the highest tier. Set model risk appetite and reporting."],
      ["Phase 3", "Full operation", "Validation coverage complete for material models. Monitoring, change control and overlay governance operating. Independent assurance performed. Aggregate reporting to the Board established."],
    ]},
   {"k": "p", "req": [], "t": "Entities should sequence by risk rather than by convenience. Establishing validation for the highest-tier models before completing the inventory of the lowest is generally the better order, provided discovery continues in parallel."},
   {"k": "p", "req": [], "t": "Comparable transitions internationally have allowed extended lead times. OSFI's Guideline E-23 (2027) was published on 11 September 2025 with effect from 1 May 2027, providing approximately eighteen months. The PRA's SS1/23 was published in May 2023 with effect from 17 May 2024, providing twelve months."},
   {"k": "ver", "t": "Verification: both transition periods were confirmed from the primary instruments. The phasing in the table above is illustrative APRA drafting and is not derived from any comparator instrument."},
  ]},
]


def numbered():
    """Assign paragraph numbers and return (flat_items, req_to_paragraph_map)."""
    flat = []
    n = 0
    for ch_i, ch in enumerate(GUIDE):
        flat.append({"k": "chapter", "t": ch["chapter"], "intro": ch.get("intro"),
                     "index": ch_i})
        for it in ch["items"]:
            item = dict(it)
            if it["k"] == "p":
                n += 1
                item["n"] = n
            item["chapter"] = ch["chapter"]
            flat.append(item)

    req_map = {}
    for it in flat:
        if it["k"] == "p":
            for r in it.get("req", []):
                req_map.setdefault(r, []).append(it["n"])

    chapter_reqs = {}
    for it in flat:
        if it["k"] == "p":
            chapter_reqs.setdefault(it["chapter"], set()).update(it.get("req", []))

    return flat, req_map, chapter_reqs, n


def ranges(nums):
    """Compress [5,6,7,11] into '5-7, 11' for readable cross-references."""
    if not nums:
        return ""
    nums = sorted(set(nums))
    out, start, prev = [], nums[0], nums[0]
    for x in nums[1:]:
        if x == prev + 1:
            prev = x
            continue
        out.append((start, prev))
        start = prev = x
    out.append((start, prev))
    return ", ".join(str(a) if a == b else f"{a}–{b}" for a, b in out)
