"""Source register, crosswalk, principles register and audit trail content.

Verification vocabulary used throughout:
    Verified — primary source                  read in the issuing authority's own document
    Verified — secondary source                confirmed only from a reputable third party
    Unverified — not independently confirmed   could not be confirmed; not relied upon for
                                               any statement of requirement

Anything carrying the third label is excluded from the requirement register's
evidential base and appears in the documents only where the label travels with it.
"""

CHECKED = "25 Jul 2026"

V_PRIMARY = "Verified — primary source"
V_SECONDARY = "Verified — secondary source"
V_NONE = "Unverified — not independently confirmed"

# --------------------------------------------------------------------------- #
# Source register
# --------------------------------------------------------------------------- #

SOURCES = [
    # ---------------------------------------------------------------- US
    {
        "id": "US-MRM-2026", "authority": "OCC / FRB / FDIC",
        "title": "Supervisory Guidance on Model Risk Management — interagency guidance issued as "
                 "Federal Reserve SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026",
        "published": "17 April 2026", "effective": "17 April 2026",
        "date": "17 Apr 2026",
        "status": "Interagency supervisory guidance. Expressly non-enforceable: it 'does not set "
                  "forth enforceable standards or prescriptive requirements' and non-compliance "
                  "'will not result in supervisory criticism'. US supervisory guidance does not "
                  "have the force and effect of law.",
        "scope": "Expected to be most relevant to banking organisations with over $30 billion in "
                 "total assets. Organisations at or below that threshold are generally excluded, "
                 "though the guidance may still be relevant where model exposure is significant. "
                 "Generative AI and agentic AI models are expressly outside scope.",
        "relevant": "Current US framework. Seven sections: introduction; purpose and scope; "
                    "overview of model risk and model risk management; model development and "
                    "model use; model validation and monitoring; governance and controls; and "
                    "vendor and other third-party products. Retains effective challenge and the "
                    "three components of validation, and expressly addresses aggregate model risk.",
        "url": "https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "US-MRM-2011", "authority": "OCC / FRB",
        "title": "OCC Bulletin 2011-12 / Federal Reserve SR 11-7 — Supervisory Guidance on Model "
                 "Risk Management",
        "published": "4 April 2011",
        "effective": "Rescinded and superseded 17 April 2026",
        "date": "4 Apr 2011 (rescinded)",
        "status": "Superseded supervisory guidance. Rescinded by OCC Bulletin 2026-13 and "
                  "superseded by Federal Reserve SR 26-2 on 17 April 2026. Was never a "
                  "regulation. Retained here for provenance because it originated most of the "
                  "discipline's architecture.",
        "scope": "Applied to all banking organisations supervised by the Federal Reserve and the "
                 "OCC, taking into account size, nature and complexity. Adopted by the FDIC in "
                 "June 2017 via FIL-22-2017.",
        "relevant": "The originating framework: the three-component description of a model, the "
                    "two sources of model risk, effective challenge, conceptual soundness, the "
                    "three core elements of validation, inventory, documentation and vendor "
                    "models. Its broad model definition is NOT carried forward into the 2026 "
                    "guidance, which is narrower.",
        "url": "https://www.occ.gov/static/rescinded-bulletins/bulletin-2011-12.pdf",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "US-SG-STATUS", "authority": "OCC / FRB / FDIC",
        "title": "Use of supervisory guidance — 12 CFR Part 4 Subpart F (OCC), 12 CFR §262.7 and "
                 "Part 262 Appendix A (Board), 12 CFR Part 302 Appendix A (FDIC)",
        "published": "Codified 2021, following the 2018 interagency statement",
        "effective": "In force",
        "date": "2021",
        "status": "Codified regulation. Binding on the agencies, not on supervised institutions. "
                  "Provides that supervisory guidance does not have the force and effect of law "
                  "and that the agencies do not take enforcement action on the basis of guidance.",
        "scope": "The OCC, the Federal Reserve Board and the FDIC and their supervised "
                 "institutions.",
        "relevant": "Establishes definitively that the US model risk guidance is not law. This is "
                    "the single binding instrument in the US part of this evidence base, and it "
                    "binds the regulators rather than the banks.",
        "url": "https://www.ecfr.gov/current/title-12/chapter-I/part-4/subpart-F",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "OCC-CB-2025", "authority": "OCC",
        "title": "OCC Bulletin 2025-26 — Model Risk Management: Clarification for Community Banks",
        "published": "6 October 2025", "effective": "On issue",
        "date": "6 Oct 2025",
        "status": "Bulletin clarifying the application of existing supervisory guidance. Not a "
                  "regulation. Not rescinded by OCC Bulletin 2026-13.",
        "scope": "OCC-supervised community banks.",
        "relevant": "States that OCC guidance does not require community banks to perform annual "
                    "model validation, and that the OCC will not give negative supervisory "
                    "feedback solely for the frequency or scope of validation a bank reasonably "
                    "determined on a risk basis. Directly relevant to proportionality drafting.",
        "url": "https://www.occ.gov/news-issuances/bulletins/2025/bulletin-2025-26.html",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "OCC-HANDBOOK", "authority": "OCC",
        "title": "Comptroller's Handbook — Model Risk Management booklet",
        "published": "August 2021",
        "effective": "Rescinded 17 April 2026",
        "date": "Aug 2021 (rescinded)",
        "status": "Examiner handbook booklet, rescinded by OCC Bulletin 2026-13. Was guidance for "
                  "OCC examiners, not a regulation.",
        "scope": "OCC examiners assessing model risk management at supervised banks, including "
                 "community banks.",
        "relevant": "Existence, issuance and rescission are confirmed. The booklet itself is no "
                    "longer retrievable from an official domain and no statement about its "
                    "contents is relied upon anywhere in this package.",
        "url": "https://www.occ.gov/news-issuances/bulletins/2021/bulletin-2021-39.html",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- UK
    {
        "id": "PRA-SS1-23", "authority": "PRA",
        "title": "SS1/23 — Model risk management principles for banks",
        "published": "17 May 2023; current version dated 16 April 2026",
        "effective": "17 May 2024",
        "date": "17 May 2023; upd. 16 Apr 2026",
        "status": "Supervisory statement setting out PRA expectations. Not a PRA Rulebook "
                  "instrument and not binding law.",
        "scope": "UK-incorporated banks, building societies and PRA-designated investment firms "
                 "with internal model approval to calculate regulatory capital requirements. Does "
                 "not apply to insurers, credit unions, third-country branches or firms without "
                 "internal model approval.",
        "relevant": "Five principles with 23 sub-principles: model identification and model risk "
                    "classification; governance; model development, implementation, and use; "
                    "independent model validation; and model risk mitigants.",
        "url": "https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "PRA-PS6-23", "authority": "PRA",
        "title": "PS6/23 — Model risk management principles for banks (Policy Statement)",
        "published": "17 May 2023", "effective": "17 May 2024",
        "date": "17 May 2023",
        "status": "Policy statement. Explains the final policy and feedback; the operative "
                  "expectations sit in SS1/23.",
        "scope": "As for SS1/23.",
        "relevant": "Confirms the twelve-month implementation period and the restriction of scope "
                    "to firms with internal model approval.",
        "url": "https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "PRA-SS3-18", "authority": "PRA",
        "title": "SS3/18 — Model risk management principles for stress testing",
        "published": "April 2018; current version dated April 2026",
        "effective": "April 2018",
        "date": "Apr 2018; upd. Apr 2026",
        "status": "Supervisory statement. PRA expectations, not binding law.",
        "scope": "Firms in scope of the PRA's stress testing framework.",
        "relevant": "Model risk management expectations specific to stress testing models, "
                    "including governance of assumptions and expert judgement.",
        "url": "https://www.bankofengland.co.uk/prudential-regulation/publication/2018/model-risk-management-principles-for-stress-testing-ss",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- Canada
    {
        "id": "OSFI-E23", "authority": "OSFI",
        "title": "Guideline E-23 — Model Risk Management (2027)",
        "published": "11 September 2025", "effective": "1 May 2027",
        "date": "11 Sep 2025; eff. 1 May 2027",
        "status": "Final supervisory guideline. Not yet in effect at the as-of date. Sound "
                  "Business and Financial Practices category.",
        "scope": "Banks, foreign bank branches, life insurance and fraternal companies, property "
                 "and casualty companies, and trust and loan companies. Does not apply to "
                 "federally regulated pension plans.",
        "relevant": "Three outcomes and twelve principles numbered 1.1 to 3.6, covering enterprise-wide model risk management, a risk-based approach, and model lifecycle management. Appendix 1, Information tracking for models, sets out minimum model inventory content. Expressly covers AI and machine learning models.",
        "url": "https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "OSFI-E23-2017", "authority": "OSFI",
        "title": "Guideline E-23 — Enterprise-Wide Model Risk Management for Deposit-Taking "
                 "Institutions (2017)",
        "published": "30 September 2017", "effective": "On issue",
        "date": "Sep 2017 (superseded)",
        "status": "Supervisory guideline. OSFI's guidance library presents the 2027 guideline as its replacement from 1 May 2027, but no express supersession clause was located in either the 2027 guideline or its covering letter, so the relationship is stated as OSFI presents it rather than as a quoted provision.",
        "scope": "Federally regulated deposit-taking institutions only.",
        "relevant": "The predecessor framework, structured as numbered sections rather than "
                    "principles. Included for contrast with the expanded 2027 scope.",
        "url": "https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/enterprise-wide-model-risk-management-deposit-taking-institutions",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "OSFI-B10", "authority": "OSFI",
        "title": "Guideline B-10 — Third-Party Risk Management",
        "published": "April 2023", "effective": "1 May 2024",
        "date": "Apr 2023; eff. 1 May 2024",
        "status": "Supervisory guideline.",
        "scope": "Federally regulated financial institutions.",
        "relevant": "Third-party arrangements including externally supplied models and the "
                    "information rights needed to govern them.",
        "url": "https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/third-party-risk-management-guideline",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- EU
    {
        "id": "ECB-GIM", "authority": "ECB",
        "title": "ECB Guide to internal models",
        "published": "Consolidated guide; current version June 2026 (release 4.1)",
        "effective": "Applies to ECB supervisory assessment of internal models",
        "date": "Jun 2026 (rel. 4.1)",
        "status": "Supervisory guide. Sets out how the ECB understands and applies binding EU law; "
                  "the guide itself is not a legal act and does not create obligations beyond "
                  "the CRR.",
        "scope": "Significant institutions directly supervised by the ECB that use internal models "
                 "for regulatory capital.",
        "relevant": "Five chapters: overarching principles for internal models, credit risk, market "
                    "risk under CRR2, market risk under CRR3, and counterparty credit risk. The "
                    "overarching principles chapter has twelve sections including documentation, "
                    "data governance, implementation of a model risk management framework, "
                    "internal validation, internal audit, the use of machine learning techniques "
                    "in internal models, model change and third-party involvement.",
        "url": "https://www.bankingsupervision.europa.eu/activities/internal_models/html/index.en.html",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "ECB-CRR", "authority": "EU",
        "title": "Regulation (EU) No 575/2013 (Capital Requirements Regulation), internal model "
                 "provisions: Article 174 Use of models, Article 179 Overall requirements for "
                 "estimation, Article 185 Validation of internal estimates, Article 188 "
                 "Validation and documentation, Article 189 Corporate governance, Article 191 "
                 "Internal audit",
        "published": "26 June 2013, as amended", "effective": "In force",
        "date": "2013, as amended",
        "status": "Binding EU regulation, directly applicable in Member States. This is the "
                  "binding law that the ECB guide interprets.",
        "scope": "Credit institutions and investment firms in the European Union.",
        "relevant": "Legal requirements for internal model validation, the use test, model "
                    "governance and the review of estimates.",
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "ECB-RDARR", "authority": "ECB",
        "title": "Guide on effective risk data aggregation and risk reporting",
        "published": "3 May 2024", "effective": "On issue",
        "date": "May 2024",
        "status": "Supervisory guide. Sets out ECB expectations; not a legal act.",
        "scope": "Significant institutions directly supervised by the ECB.",
        "relevant": "Data governance, data quality and the reliability of risk data feeding "
                    "models and risk reporting.",
        "url": "https://www.bankingsupervision.europa.eu/framework/legal-framework/public-consultations/html/rdarr.en.html",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- Singapore
    {
        "id": "MAS-AIMRM-2024", "authority": "MAS",
        "title": "Artificial Intelligence Model Risk Management — Observations from a Thematic "
                 "Review",
        "published": "December 2024", "effective": "n/a",
        "date": "Dec 2024",
        "status": "Information paper describing observed good practices. Not mandatory guidelines "
                  "and not a Notice.",
        "scope": "Banks selected for the MAS thematic review; of general interest more broadly.",
        "relevant": "Governance and oversight, key risk management systems and processes, and "
                    "development and deployment controls for AI models, including generative AI.",
        "url": "https://www.mas.gov.sg/publications/monographs-or-information-paper/2024/artificial-intelligence-model-risk-management",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "MAS-FEAT", "authority": "MAS",
        "title": "Principles to Promote Fairness, Ethics, Accountability and Transparency (FEAT) "
                 "in the Use of Artificial Intelligence and Data Analytics in Singapore's "
                 "Financial Sector",
        "published": "12 November 2018", "effective": "n/a",
        "date": "Nov 2018",
        "status": "Voluntary principles. Not binding.",
        "scope": "Financial institutions in Singapore, on a voluntary basis.",
        "relevant": "Fairness, ethics, accountability and transparency principles applied to "
                    "analytics and AI-driven decisions.",
        "url": "https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/feat",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "MAS-NOTICE637", "authority": "MAS",
        "title": "MAS Notice 637 — Risk Based Capital Adequacy Requirements for Banks Incorporated "
                 "in Singapore",
        "published": "As amended", "effective": "In force",
        "date": "As amended",
        "status": "Binding Notice issued under the Banking Act. Legally enforceable in Singapore.",
        "scope": "Banks incorporated in Singapore.",
        "relevant": "Internal ratings-based and internal models provisions, including model "
                    "validation, independent review and the use test for regulatory capital models.",
        "url": "https://www.mas.gov.sg/regulation/notices/notice-637",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- BCBS
    {
        "id": "BCBS-239", "authority": "BCBS",
        "title": "Principles for effective risk data aggregation and risk reporting (BCBS 239)",
        "published": "January 2013", "effective": "1 January 2016 for G-SIBs",
        "date": "Jan 2013",
        "status": "BIS-classified Guidelines, not a Standard. Not directly binding; effect "
                  "depends on domestic implementation by national authorities.",
        "scope": "Global systemically important banks, and domestic systemically important banks "
                 "at national discretion.",
        "relevant": "Fourteen principles on governance, data architecture, accuracy, "
                    "completeness, timeliness and adaptability of risk data, and on risk "
                    "reporting practices.",
        "url": "https://www.bis.org/publ/bcbs239.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "BCBS-STRESS", "authority": "BCBS",
        "title": "Stress testing principles",
        "published": "October 2018", "effective": "n/a",
        "date": "Oct 2018",
        "status": "BIS-classified Guidelines. The document expressly states that the principles do not constitute Standards, for which the Basel Committee expects full implementation. Domestic effect depends on implementation by national authorities.",
        "scope": "Banks and supervisors, applied proportionately.",
        "relevant": "Nine principles on stress testing governance, including the models used and "
                    "the assumptions and expert judgement embedded in them.",
        "url": "https://www.bis.org/bcbs/publ/d450.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "BCBS-FVP", "authority": "BCBS",
        "title": "Supervisory guidance for assessing banks' financial instrument fair value "
                 "practices",
        "published": "April 2009", "effective": "n/a",
        "date": "Apr 2009",
        "status": "Supervisory guidance. Effect depends on domestic implementation.",
        "scope": "Banks and supervisors.",
        "relevant": "Valuation governance, valuation model validation, independent price "
                    "verification and the treatment of valuation uncertainty.",
        "url": "https://www.bis.org/publ/bcbs153.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "BCBS-DIGI", "authority": "BCBS",
        "title": "Digitalisation of finance",
        "published": "May 2024", "effective": "n/a",
        "date": "May 2024",
        "status": "Analytical report. Not a standard and not binding.",
        "scope": "Banks and supervisors.",
        "relevant": "Observations on AI and machine learning, model risk, explainability, data "
                    "and third-party dependencies in banking.",
        "url": "https://www.bis.org/bcbs/publ/d575.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "BCBS-AIML", "authority": "BCBS",
        "title": "Newsletter on artificial intelligence and machine learning",
        "published": "16 March 2022", "effective": "n/a",
        "date": "16 Mar 2022",
        "status": "Supervisory newsletter. Not a standard.",
        "scope": "Banks and supervisors.",
        "relevant": "Early supervisory observations on AI/ML model risk, explainability and "
                    "governance.",
        "url": "https://www.bis.org/publ/bcbs_nl27.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "BCBS-TPRM", "authority": "BCBS",
        "title": "Principles for the sound management of third-party risk (BCBS d605)",
        "published": "2025", "effective": "n/a",
        "date": "2025",
        "status": "BIS-classified Guidelines, not a Standard. Domestic effect depends on implementation by national authorities.",
        "scope": "Primarily internationally active banks and their supervisors.",
        "relevant": "Twelve principles covering governance, risk management and strategy, risk "
                    "assessment, due diligence, contracting, onboarding, ongoing monitoring, "
                    "business continuity, termination and the role of supervisors — applicable "
                    "to externally supplied models.",
        "url": "https://www.bis.org/bcbs/publ/d605.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- FSB
    {
        "id": "FSB-SP-2026", "authority": "FSB",
        "title": "Sound Practices for Responsible Adoption of Artificial Intelligence — "
                 "consultation report",
        "published": "10 June 2026", "effective": "n/a",
        "date": "Jun 2026 (consultation)",
        "status": "Consultation report. The FSB states expressly that the sound practices are not "
                  "intended to establish an international standard. Not binding anywhere.",
        "scope": "Financial institutions of all types, applied proportionately.",
        "relevant": "Twelve sound practices spanning strategic direction and oversight, governance "
                    "and accountability, risk management framework, organisational adaptability, "
                    "materiality and risk assessment, selection, data governance, explainability "
                    "and transparency, performance management, human oversight, cyber and ICT "
                    "risk, and third-party AI risk. Addresses AI rather than model risk generally, "
                    "and is used here only as comparative input.",
        "url": "https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai/",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "FSB-AI-2024", "authority": "FSB",
        "title": "The Financial Stability Implications of Artificial Intelligence",
        "published": "14 November 2024", "effective": "n/a",
        "date": "14 Nov 2024",
        "status": "Analytical report. Expressly not a standard.",
        "scope": "The global financial system.",
        "relevant": "Vulnerabilities including third-party dependencies, service provider "
                    "concentration, correlated model behaviour, market correlation and cyber risk.",
        "url": "https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "FSB-AI-2017", "authority": "FSB",
        "title": "Artificial intelligence and machine learning in financial services",
        "published": "1 November 2017", "effective": "n/a",
        "date": "1 Nov 2017",
        "status": "Analytical report. Not a standard.",
        "scope": "The global financial system.",
        "relevant": "Early identification of model risk, opacity and third-party concentration "
                    "arising from AI adoption in finance.",
        "url": "https://www.fsb.org/2017/11/artificial-intelligence-and-machine-learning-in-financial-service/",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- APRA
    {
        "id": "BCBS-ECL-2015", "authority": "BCBS",
        "title": "Guidance on credit risk and accounting for expected credit losses (BCBS d350)",
        "published": "18 December 2015", "effective": "n/a",
        "date": "18 Dec 2015",
        "status": "BIS-classified Guidelines. Supervisory guidance intended not to contradict "
                  "applicable accounting standards. Domestic effect depends on implementation; in "
                  "Australia APG 220 directs ADIs to have regard to it.",
        "scope": "Banks and banking supervisors. Written around IFRS 9-type expected credit loss "
                 "accounting frameworks.",
        "relevant": "Eleven principles. Principles 1 to 8 address banks: board and management "
                    "responsibilities; sound ECL methodologies; credit risk rating process and "
                    "grouping; adequacy of the allowance; ECL model validation; experienced credit "
                    "judgment; common data; and disclosure. Principles 9 to 11 address supervisors: "
                    "periodic evaluation of credit risk practices; satisfaction that ECL "
                    "measurement methods are appropriate; and consideration of credit risk "
                    "practices in assessing capital adequacy. Principle 5 is the direct antecedent "
                    "of the ECL model validation obligation in APS 220.",
        "url": "https://www.bis.org/bcbs/publ/d350.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "BCBS-CR-NL-2023", "authority": "BCBS",
        "title": "Newsletter on credit risk issues (bcbs_nl32)",
        "published": "4 July 2023", "effective": "n/a",
        "date": "4 Jul 2023",
        "status": "Supervisory newsletter. Not a standard and not binding.",
        "scope": "Banks and supervisors.",
        "relevant": "Supervisory observations on credit risk practices, including expected credit "
                    "loss provisioning. Cited by APRA's October 2023 letter on provisioning "
                    "practices as reinforcing the same observations.",
        "url": "https://www.bis.org/publ/bcbs_nl32.htm",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-APS220", "authority": "APRA",
        "title": "Prudential Standard APS 220 Credit Risk Management",
        "published": "Current at the as-of date", "effective": "Commenced 1 January 2023",
        "date": "Commenced 1 Jan 2023",
        "status": "Binding prudential standard.",
        "scope": "Authorised deposit-taking institutions.",
        "relevant": "Credit risk management framework, classification of exposures and provisions, "
                    "and a dedicated section on credit risk and accounting for expected credit "
                    "losses which requires an ADI to have sound policies and processes in place to "
                    "appropriately validate models used to assess and measure expected credit "
                    "losses. Also contains the Special purpose engagements provision under which "
                    "APRA may require an ADI to appoint an independent party to review and report "
                    "to APRA on its credit risk management, including provisioning practices.",
        "url": "https://www.apra.gov.au/standards/aps-220",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-APS310",
        "authority": "APRA",
        "title": "Prudential Standard APS 310 Audit and Related Matters",
        "published": "Current at the as-of date",
        "effective": "Commenced 1 January 2023",
        "date": "Commenced 1 Jan 2023",
        "status": "Binding prudential standard.",
        "scope": "Authorised deposit-taking institutions.",
        "relevant": "Contains a Special purpose engagements provision under which APRA may require an "
                    "ADI, by notice in writing, to appoint an auditor to report on a particular aspect "
                    "of the ADI's operations, prudential reporting, risk management systems or "
                    "financial position, at the ADI's expense. The reference to risk management "
                    "systems is the express basis on which a review of model risk management may be "
                    "required of an ADI.",
        "url": "https://www.apra.gov.au/standards/aps-310",
        "verification": "Verified — primary source",
        "checked": "25 Jul 2026",
    },
    {
        "id": "APRA-GPS310",
        "authority": "APRA",
        "title": "Prudential Standard GPS 310 Audit and Related Matters",
        "published": "Current at the as-of date",
        "effective": "Commenced 1 October 2024",
        "date": "Commenced 1 Oct 2024",
        "status": "Binding prudential standard.",
        "scope": "General insurers and Level 2 insurance groups.",
        "relevant": "Where APRA specifies in writing, the Appointed Auditor must undertake a special "
                    "purpose review of matters relating to the insurer's operations, risk management "
                    "or financial affairs, at the insurer's expense, reporting within three months.",
        "url": "https://www.apra.gov.au/standards/gps-310",
        "verification": "Verified — primary source",
        "checked": "25 Jul 2026",
    },
    {
        "id": "APRA-LPS310",
        "authority": "APRA",
        "title": "Prudential Standard LPS 310 Audit and Related Matters",
        "published": "Current at the as-of date",
        "effective": "Commenced 18 December 2023",
        "date": "Commenced 18 Dec 2023",
        "status": "Binding prudential standard.",
        "scope": "Life companies, including friendly societies.",
        "relevant": "Provides for a special purpose engagement relating to matters set out in writing "
                    "by APRA concerning the life company's operations, risk management or financial "
                    "affairs, at the life company's expense.",
        "url": "https://www.apra.gov.au/standards/lps-310",
        "verification": "Verified — primary source",
        "checked": "25 Jul 2026",
    },
    {
        "id": "APRA-HPS310",
        "authority": "APRA",
        "title": "Prudential Standard HPS 310 Audit and Related Matters",
        "published": "Current at the as-of date",
        "effective": "Commenced 1 July 2023",
        "date": "Commenced 1 Jul 2023",
        "status": "Binding prudential standard.",
        "scope": "Private health insurers.",
        "relevant": "Provides for a special purpose engagement relating to matters set out in writing "
                    "by APRA concerning the private health insurer's operations, risk management or "
                    "financial affairs, at the insurer's expense.",
        "url": "https://www.apra.gov.au/standards/hps-310",
        "verification": "Verified — primary source",
        "checked": "25 Jul 2026",
    },
    {
        "id": "APRA-SPS310",
        "authority": "APRA",
        "title": "Prudential Standard SPS 310 Audit and Related Matters",
        "published": "Current at the as-of date",
        "effective": "Commenced 30 June 2024",
        "date": "Commenced 30 Jun 2024",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "APRA may require an RSE licensee to engage an auditor, being the existing RSE "
                    "auditor or another auditor specified by APRA, to report on a particular aspect of "
                    "the RSE licensee's business operations, compliance with prudential requirements "
                    "or the RSE licensee's risk management framework, at the RSE licensee's expense.",
        "url": "https://www.apra.gov.au/standards/sps-310",
        "verification": "Verified — primary source",
        "checked": "25 Jul 2026",
    },
    {
        "id": "APRA-APG220", "authority": "APRA",
        "title": "Prudential Practice Guide APG 220 Credit Risk Management",
        "published": "Current at the as-of date", "effective": "n/a",
        "date": "Current",
        "status": "Prudential practice guide. Non-enforceable guidance.",
        "scope": "ADIs implementing APS 220.",
        "relevant": "Guidance on the APS 220 credit risk framework. Expressly states that the "
                    "Basel Committee's Guidance on credit risk and accounting for expected credit "
                    "losses of 18 December 2015 sets out guidance on sound credit risk practices "
                    "associated with expected credit loss accounting frameworks, and that APRA "
                    "expects ADIs to have regard to it.",
        "url": "https://www.apra.gov.au/practice-guides/apg-220",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-PROV-2023", "authority": "APRA",
        "title": "Letter — Credit risk provisioning practices for locally incorporated "
                 "authorised deposit-taking institutions",
        "published": "19 October 2023", "effective": "n/a",
        "date": "19 Oct 2023",
        "status": "Letter to industry. Supervisory observations and expectations; not a "
                  "prudential standard.",
        "scope": "Locally incorporated ADIs.",
        "relevant": "Sets out APRA's observations on expected credit loss provisioning across "
                    "three areas: controls around model risk management, including judgement-based "
                    "adjustments and overlays; capturing economic uncertainty through sensitivity "
                    "analysis; and identifying credit deterioration in vulnerable sectors and "
                    "borrowers, including the indicators used to transfer exposures to Stage 2 "
                    "under AASB 9. The principal source for the review focus areas in Annex G.",
        "url": "https://www.apra.gov.au/credit-risk-provisioning-practices-for-locally-incorporated-authorised-deposit-taking-institutions",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "AASB-9", "authority": "AASB",
        "title": "AASB 9 Financial Instruments",
        "published": "As amended", "effective": "In force",
        "date": "As amended",
        "status": "Australian Accounting Standard. Binding for financial reporting purposes under "
                  "the Corporations Act; not a prudential instrument.",
        "scope": "Entities preparing financial statements under Australian Accounting Standards.",
        "relevant": "The expected credit loss impairment model, including the three-stage "
                    "approach and the assessment of significant increases in credit risk. APS 220 "
                    "requires provisions to be adequate and consistent with the objectives of "
                    "Australian Accounting Standards.",
        "url": "https://www.aasb.gov.au/pronouncements/accounting-standards/",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPG110", "authority": "APRA",
        "title": "Prudential Practice Guide CPG 110 Internal Capital Adequacy Assessment Process "
                 "and Supervisory Review",
        "published": "Current at the as-of date", "effective": "n/a",
        "date": "Current",
        "status": "Prudential practice guide. Non-enforceable guidance.",
        "scope": "APRA-regulated entities conducting an ICAAP.",
        "relevant": "Guidance on the internal capital adequacy assessment process and on stress "
                    "testing, which APRA's provisioning letter directs ADIs to follow when "
                    "conducting sensitivity analysis on expected credit losses.",
        "url": "https://www.apra.gov.au/practice-guides/cpg-110",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS001", "authority": "APRA",
        "title": "Prudential Standard CPS 001 Defined terms",
        "published": "Current at the as-of date", "effective": "In force at the as-of date",
        "date": "In force; commencement not separately verified",
        "status": "Binding prudential standard.",
        "scope": "APRA-regulated entities, as the source of cross-industry defined terms.",
        "relevant": "The centralised definitions instrument. Paragraph A6 provides that a term not "
                    "defined in Annex A takes its meaning from CPS 001, so the two must be "
                    "reconciled before issue.",
        "url": "https://www.apra.gov.au/standards/cps-001",
        "verification": "Verified — secondary source", "checked": "25 Jul 2026",
    },
    {
        "id": "APRA-CPS220", "authority": "APRA",
        "title": "Prudential Standard CPS 220 Risk Management",
        "published": "July 2019 text", "effective": "Commenced 1 July 2019",
        "date": "Commenced 1 Jul 2019",
        "status": "Binding cross-industry prudential standard.",
        "scope": "APRA-regulated entities as defined in CPS 220. SPS 220 is the RSE licensee "
                 "counterpart.",
        "relevant": "Risk management framework, risk appetite, Board and senior management "
                    "responsibilities. Does not name model risk as a distinct risk type.",
        "url": "https://www.apra.gov.au/standards/cps-220",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS220", "authority": "APRA",
        "title": "Prudential Standard SPS 220 Risk Management",
        "published": "January 2023 text", "effective": "Commenced 1 January 2023",
        "date": "Commenced 1 Jan 2023",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Risk management framework and governance obligations for superannuation.",
        "url": "https://www.apra.gov.au/standards/sps-220",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS230", "authority": "APRA",
        "title": "Prudential Standard CPS 230 Operational Risk Management",
        "published": "Current determination made 23 April 2026", "effective": "1 July 2026",
        "date": "Determined 23 Apr 2026; commences 1 Jul 2026",
        "status": "Binding cross-industry prudential standard. The current determination revokes and replaces the 2023 determination, under which CPS 230 commenced on 1 July 2025.",
        "scope": "APRA-regulated entities as defined in CPS 230.",
        "relevant": "Operational risk controls, critical operations and tolerance levels, incident "
                    "management and notification, and service provider management.",
        "url": "https://www.apra.gov.au/standards/cps-230",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS234", "authority": "APRA",
        "title": "Prudential Standard CPS 234 Information Security",
        "published": "July 2019 text", "effective": "Commenced 1 July 2019",
        "date": "Commenced 1 Jul 2019",
        "status": "Binding cross-industry prudential standard.",
        "scope": "APRA-regulated entities as defined in CPS 234.",
        "relevant": "Information security capability, control testing, incident notification and "
                    "assurance.",
        "url": "https://www.apra.gov.au/standards/cps-234",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPG235", "authority": "APRA",
        "title": "Prudential Practice Guide CPG 235 Managing Data Risk",
        "published": "September 2013", "effective": "n/a",
        "date": "Sep 2013",
        "status": "Prudential practice guide. Non-enforceable guidance.",
        "scope": "APRA-regulated entities.",
        "relevant": "Data governance, data lifecycle, data quality and controls. Predates modern "
                    "model data concerns such as proxy and synthetic data.",
        "url": "https://www.apra.gov.au/system/files/Prudential-Practice-Guide-CPG-235-Managing-Data-Risk_1.pdf",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-APS113", "authority": "APRA",
        "title": "Prudential Standard APS 113 Capital Adequacy: Internal Ratings-based Approach "
                 "to Credit Risk",
        "published": "Final released 4 June 2026", "effective": "Commenced 30 June 2026",
        "date": "Released 4 Jun 2026; commenced 30 Jun 2026",
        "status": "Binding prudential standard.",
        "scope": "ADIs approved by APRA to use the internal ratings-based approach.",
        "relevant": "The most developed model governance requirements in the Australian framework: "
                    "model approval, independent review, validation, the use test and model change.",
        "url": "https://www.apra.gov.au/standards/aps-113",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS320", "authority": "APRA",
        "title": "Prudential Standard CPS 320 Actuarial and Related Matters",
        "published": "Determination made 29 April 2026", "effective": "Commenced 1 July 2026",
        "date": "Determined 29 Apr 2026; commenced 1 Jul 2026",
        "status": "Binding prudential standard.",
        "scope": "Insurers as defined in the standard.",
        "relevant": "Appointed Actuary role, actuarial advice framework, Financial Condition Report and Actuarial Valuation Report — a form of independent professional review of actuarial models. The commencement and structure of the current version were confirmed from the APRA standards page; the in-force PDF could not be downloaded, so paragraph references are taken from the July 2019 text and should be re-checked against the 1 July 2026 version.",
        "url": "https://www.apra.gov.au/standards/cps-320",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS530", "authority": "APRA",
        "title": "Prudential Standard SPS 530 Investment Governance",
        "published": "January 2023 text", "effective": "Commenced 1 January 2023",
        "date": "Commenced 1 Jan 2023",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Investment governance, valuation, liquidity management and stress testing "
                    "obligations that rely on models.",
        "url": "https://www.apra.gov.au/standards/sps-530",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-HPS110", "authority": "APRA",
        "title": "Prudential Standard HPS 110 Capital Adequacy (private health insurance)",
        "published": "Current at the as-of date", "effective": "In force at the as-of date",
        "date": "In force; commencement not separately verified",
        "status": "Binding prudential standard.",
        "scope": "Private health insurers.",
        "relevant": "Capital adequacy for private health insurers. Named here because private "
                    "health insurance is within the enabling authority for this Prudential "
                    "Standard and its liability and risk equalisation calculations are modelled.",
        "url": "https://www.apra.gov.au/standards/hps-110",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS114", "authority": "APRA",
        "title": "Prudential Standard SPS 114 Operational Risk Financial Requirement",
        "published": "Current at the as-of date", "effective": "In force at the as-of date",
        "date": "In force; commencement not separately verified",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Determination and maintenance of the operational risk financial requirement "
                    "target amount — the superannuation counterpart to an internal capital "
                    "assessment, and therefore the place where aggregate model risk is considered "
                    "for an RSE licensee.",
        "url": "https://www.apra.gov.au/standards/sps-114",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS515", "authority": "APRA",
        "title": "Prudential Standard SPS 515 Strategic Planning and Member Outcomes",
        "published": "Current at the as-of date", "effective": "In force at the as-of date",
        "date": "In force; commencement not separately verified",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Business performance review and member outcomes assessment, which rely on "
                    "modelled projections.",
        "url": "https://www.apra.gov.au/standards/sps-515",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
]

# Some requirement source IDs are aliases of registered sources.
# No aliases. Every source ID cited by a requirement resolves to a registered entry,
# so nothing can be cited that does not appear in Annex E.
SOURCE_ALIASES = {}


# --------------------------------------------------------------------------- #
# Annex content for the standard
# --------------------------------------------------------------------------- #

DEFINITIONS = [
    ["Model", "A quantitative method, system or approach that applies statistical, economic, "
              "financial, actuarial or mathematical theories, techniques or assumptions to process "
              "input data into quantitative estimates."],
    ["Model risk", "The potential for adverse consequences from decisions based on incorrect or "
                   "misused model outputs. Model risk arises where a model has fundamental errors "
                   "and produces inaccurate outputs relative to its design objective and intended "
                   "use, or where a model is used incorrectly or inappropriately."],
    ["Material model", "A model that is used for a material purpose, or whose failure or misuse "
                       "could otherwise have a material effect on the entity's financial position, "
                       "its regulatory obligations, its critical operations, or amounts or "
                       "entitlements attributable to its customers or beneficiaries."],
    ["Model owner", "The person accountable for a model being fit for its approved purpose "
                    "throughout its lifecycle, including its documentation, performance monitoring, "
                    "communication of limitations and remediation of findings."],
    ["Model risk tier", "The classification assigned to a model under the entity's tiering "
                        "methodology, which determines the intensity of controls applied to it."],
    ["Independent validation", "An assessment of a model's fitness for its intended use performed "
                               "by persons who did not develop the model and who are not "
                               "accountable to those who developed it or who sponsor its use."],
    ["Effective challenge", "Critical and objective analysis by persons with the expertise to "
                            "identify model limitations, sufficient independence to maintain "
                            "objectivity, and the organisational standing and influence to effect "
                            "change."],
    ["Conceptual soundness", "The quality of a model's design, theory, methodology and assumptions "
                             "as appropriate for the purpose for which the model will be used."],
    ["Outcomes analysis", "Comparison of model outputs with corresponding actual outcomes, used to "
                          "assess whether a model continues to perform as intended."],
    ["Overlay", "An adjustment applied to a model's output before it is used, including management "
                "overlays, post-model adjustments and model overrides."],
    ["Quantitative decision tool", "A quantitative method that materially informs a decision but "
                                   "does not meet the definition of a model."],
    ["De minimis model", "A model that the entity has determined, and documented, could not have a "
                          "material effect on its financial position, its regulatory obligations, its "
                          "critical operations, or amounts or entitlements attributable to its customers "
                          "or beneficiaries if it were wrong or misused. A de minimis model remains "
                          "subject to identification, inventory, ownership, classification and "
                          "reassessment."],
    ["Material purpose", "A purpose where an incorrect or misused model output could have a "
                         "material effect on the entity's financial position, its regulatory "
                         "obligations, its critical operations, or amounts or entitlements "
                         "attributable to its customers or beneficiaries."],
    ["Ongoing model monitoring", "Evaluation of whether a model continues to perform as expected "
                                 "given changes in products, exposures, activities, customers, data "
                                 "relevance or market conditions."],
    ["Independent price verification", "Verification of valuation inputs and prices by a function "
                                       "independent of the business that originated the position, "
                                       "distinct from validation of the valuation model itself."],
    ["Model failure", "An event in which a model produces materially incorrect output, is materially "
                      "misused, or becomes unavailable, in each case in circumstances affecting a "
                      "material purpose."],
    ["Artificial intelligence system", "A machine-based system that infers from inputs how to "
                                       "generate outputs such as predictions, content, "
                                       "recommendations, decisions or actions. An artificial "
                                       "intelligence system that produces quantitative estimates "
                                       "relied upon for a material purpose is a model."],
    ["Third-party model", "A model developed, supplied, hosted or operated by a party other than "
                          "the entity, including a model embedded in a supplied system."],
]

PROVENANCE_TERMS = [
    ["Extracted", "A close reflection of an explicit requirement or expectation in a source "
                  "instrument."],
    ["Extracted + inferred", "A synthesis across sources that is faithful to each of them."],
    ["Inferred", "A reasoned construction where no single source states the proposition."],
    ["Policy choice", "A proposed requirement not directly mandated by any comparator authority. "
                      "The drafter, not a comparator, is the author of the obligation. This does "
                      "not mean the requirement is unsupported; it means it requires consultation "
                      "and cost-benefit testing before issue."],
    ["Verified — primary source", "Confirmed by reading the issuing authority's own document."],
    ["Verified — secondary source", "Confirmed only from a reputable third party, not from the "
                                    "issuing authority's own document."],
    ["Unverified — not independently confirmed", "Could not be confirmed from an official source "
                                                 "and is not relied upon for any statement of "
                                                 "requirement."],
]

INVENTORY_FIELDS = [
    ["Identity", "Unique identifier; model name; version; status; owning business unit; legal "
                 "entity."],
    ["Purpose and use", "Intended purpose; approved uses and users; approved conditions and limits; "
                        "processes, products, customers or beneficiaries affected."],
    ["Accountability", "Model owner; accountable executive; developer; validator; approver; "
                       "operator; provider."],
    ["Method", "Model type and technique; whether AI or machine learning techniques are used; "
               "whether the model adapts or retrains in production; degree of automation."],
    ["Data", "Material development, calibration, test and operational data; sources; use of proxy, "
             "external or synthetic data; sensitivity; lineage reference."],
    ["Dependencies", "Upstream and downstream models; provider; hosting; material data sources; "
                     "critical libraries and nth-party dependencies."],
    ["Risk", "Model risk tier; rationale; date assigned; linkage to a critical operation; key "
             "limitations and the compensating controls relied upon."],
    ["Governance", "Approval date, authority and conditions; validation status and date; next "
                   "validation due; open findings by severity; exceptions in force."],
    ["Performance", "Monitoring metrics and thresholds; latest performance assessment; overlays in "
                    "force and their size; breaches and actions taken."],
    ["Change and retirement", "Version history; material changes and their assessment; provider "
                              "updates; decommission date; disposition of records, data and "
                              "outputs still in force."],
]

TIER_INDICATORS = [
    "Determines or materially influences a regulatory capital requirement, a provision, a "
    "technical or insurance liability, or a valuation reported in the financial statements.",
    "Determines or materially influences an amount credited to or debited from a customer or "
    "member account, including unit prices and fee calculations.",
    "Makes, recommends or materially influences decisions affecting a person's access to a "
    "financial product, a claim, a benefit or a price.",
    "Supports a critical operation, or its failure could cause a tolerance level under CPS 230 to "
    "be breached.",
    "Is applied automatically at volume, or its output is acted upon without effective human "
    "review.",
    "Is opaque to the extent that the drivers of an individual output cannot be attributed, and "
    "compensating controls are not yet demonstrated to be effective.",
    "Depends on sparse, proxy, external or unrepresentative data, or on data whose provenance the "
    "entity cannot establish.",
    "Adapts, retrains or changes behaviour in production without a controlled approval step.",
    "Relies on a provider, foundation model, platform or data source for which no practical "
    "substitute exists within the relevant time horizon.",
    "Produces an error that would be difficult to detect, difficult to reverse, or would "
    "crystallise a transfer of value between customers or members.",
]

LEGAL_SETTLEMENT = [
    ["Instrument numbering and enabling authority",
     "Confirm the instrument number and determine whether one cross-industry standard can be made "
     "for ADIs, insurers and RSE licensees, or whether companion instruments are required. 'CPS "
     "XXXX' is a drafting placeholder only."],
    ["Sectoral application",
     "Settle application to each regulated industry, to foreign ADIs and branches, to "
     "non-operating holding companies and at Level 1, Level 2 and Level 3."],
    ["Definitions",
     "Settle the definitions of model, model risk, material model and model risk tier, and their "
     "interaction with the definitions used in the capital, actuarial and investment governance "
     "standards."],
    ["Interaction with capital standards",
     "Confirm that APS 113 and the other capital standards prevail on model approval and change "
     "where they are more specific, and that no inconsistency is created."],
    ["Interaction with the Appointed Actuary framework",
     "Settle how the independent validation requirement operates alongside CPS 320 and the "
     "sectoral actuarial standards, and confirm that no gap in independent review arises."],
    ["Application to RSE licensees",
     "Confirm the model classes named for RSE licensees and the interaction with SPS 530, "
     "SPS 515 and SPS 114, the last of which governs the operational risk financial "
     "requirement that paragraph M42 refers to."],
    ["Accountability regime",
     "Settle the designation of the accountable senior executive and its interaction with the "
     "applicable accountability regime."],
    ["Notification",
     "Confirm that CPS 230 and CPS 234 remain the primary notification requirements, and settle "
     "whether any model-specific notification trigger is justified."],
    ["APRA powers",
     "Settle the powers to require information, restriction of model use and remediation, and "
     "ensure procedural fairness. Independent review is dealt with separately below. "
     "Paragraph A5 confers the adjustment and "
     "exclusion power and the Interpretation section requires every power under this Prudential "
     "Standard to be exercised in writing; the procedural requirements attaching to each need "
     "settlement."],
    ["Independent review and special purpose engagements",
     "Settle how M45 interacts with the special purpose engagement powers that already exist. The "
     "Audit and Related Matters standards carry one in every industry this Prudential Standard "
     "covers — APS 310, GPS 310, LPS 310, HPS 310 and SPS 310 — each reaching the entity's risk "
     "management, and APS 220 carries a narrower one for ADIs confined to credit risk management "
     "including provisioning practices. No new power is therefore needed. What needs settling is "
     "whether M45's supporting obligation belongs in this Prudential Standard at all or is better "
     "left to those standards; whether the reviewer under the 310 standards must be the Appointed "
     "Auditor, who may not hold model risk expertise, and if not how an alternative is agreed; and "
     "whether the three-month reporting period in those standards is workable for a review of a "
     "material model estate."],
    ["Interaction with APS 220",
     "Settle how this Prudential Standard interacts with the expected credit loss provisions of "
     "APS 220 for ADIs, which already require sound policies and processes to validate expected "
     "credit loss models. The drafting treats the two as cumulative, with this Prudential Standard "
     "supplying the validation discipline that APS 220 does not define. Confirm that reading, and "
     "confirm the position for non-ADIs that determine provisions on a modelled basis and to whom "
     "APS 220 does not apply."],
    ["Commencement and transition",
     "Set commencement, transitional milestones for inventory, tiering and validation coverage, "
     "and the treatment of models already in use. Paragraph A4 splits entity-level from "
     "model-level obligations; the periods for each require settlement."],
    ["De minimis and simplified compliance",
     "Paragraph M05 provides a de minimis exception at model level: a model of no material "
     "consequence attracts only identification, inventory, ownership, classification and "
     "reassessment. Settle the drafting of the prohibited classes, whether the aggregate test "
     "should carry a stated threshold, and the approval authority for a determination. Separately, "
     "decide whether an entity-level threshold or simplified pathway is also warranted; the United "
     "States has taken that route by confining its guidance to institutions above a size "
     "threshold. The entity-level question is not settled in this draft."],
    ["Foreign ADIs and branches",
     "Confirm the read-down in paragraph A6 for foreign ADIs, and settle whether the standard "
     "reaches models operated outside Australia that affect Australian operations."],
    ["Records and privacy",
     "Balance the reconstructability requirement against data minimisation, security and technical "
     "feasibility."],
    ["Boundary with the AI instrument",
     "Settle the boundary rule between this standard and any AI risk management instrument so that "
     "no material system falls outside both."],
]


# --------------------------------------------------------------------------- #
# Principles register — labels and titles as printed by the issuing authority
# --------------------------------------------------------------------------- #

# BCBS d350 principles, verbatim. Principles 1-8 address banks; 9-11 address supervisors.
BCBS_ECL_PRINCIPLES = [
    ["Principle 1", "A bank's board of directors (or equivalent) and senior management are responsible for ensuring that the bank has appropriate credit risk practices, including an effective system of internal control, to consistently determine adequate allowances in accordance with the bank's stated policies and procedures, the applicable accounting framework and relevant supervisory guidance."],
    ["Principle 2", "A bank should adopt, document and adhere to sound methodologies that address policies, procedures and controls for assessing and measuring credit risk on all lending exposures. The measurement of allowances should build upon those robust methodologies and result in the appropriate and timely recognition of expected credit losses in accordance with the applicable accounting framework."],
    ["Principle 3", "A bank should have a credit risk rating process in place to appropriately group lending exposures on the basis of shared credit risk characteristics."],
    ["Principle 4", "A bank's aggregate amount of allowances, regardless of whether allowance components are determined on a collective or an individual basis, should be adequate and consistent with the objectives of the applicable accounting framework."],
    ["Principle 5", "A bank should have policies and procedures in place to appropriately validate models used to assess and measure expected credit losses."],
    ["Principle 6", "A bank's use of experienced credit judgment, especially in the robust consideration of reasonable and supportable forward-looking information, including macroeconomic factors, is essential to the assessment and measurement of expected credit losses."],
    ["Principle 7", "A bank should have a sound credit risk assessment and measurement process that provides it with a strong basis for common systems, tools and data to assess credit risk and to account for expected credit losses."],
    ["Principle 8", "A bank's public disclosures should promote transparency and comparability by providing timely, relevant and decision-useful information."],
    ["Principle 9", "Banking supervisors should periodically evaluate the effectiveness of a bank's credit risk practices."],
    ["Principle 10", "Banking supervisors should be satisfied that the methods employed by a bank to determine accounting allowances lead to an appropriate measurement of expected credit losses in accordance with the applicable accounting framework."],
    ["Principle 11", "Banking supervisors should consider a bank's credit risk practices when assessing a bank's capital adequacy."],
]

PRINCIPLE_FRAMEWORKS = [
    {
        "authority": "PRA", "confidence": V_PRIMARY,
        "instrument": "PRA SS1/23 — Model risk management principles for banks",
        "note": "Five principles, each with numbered sub-principles. Titles are printed with an "
                "en dash after the principle number; sub-principles are printed without one.",
        "items": [
            ["Principle 1", "Model identification and model risk classification"],
            ["Principle 1.1", "Model definition"],
            ["Principle 1.2", "Model inventory"],
            ["Principle 1.3", "Model tiering"],
            ["Principle 2", "Governance"],
            ["Principle 2.1", "Board of directors’ responsibilities"],
            ["Principle 2.2", "SMF accountability for model risk management framework"],
            ["Principle 2.3", "Policies and procedures"],
            ["Principle 2.4", "Roles and responsibilities"],
            ["Principle 2.5", "Internal Audit"],
            ["Principle 2.6", "Use of externally developed models, third-party vendor products"],
            ["Principle 3", "Model development, implementation, and use"],
            ["Principle 3.1", "Model purpose and design"],
            ["Principle 3.2", "The use of data"],
            ["Principle 3.3", "Model development testing"],
            ["Principle 3.4", "Model adjustments and expert judgement"],
            ["Principle 3.5", "Model development documentation"],
            ["Principle 3.6", "Supporting systems"],
            ["Principle 4", "Independent model validation"],
            ["Principle 4.1", "The independent validation function"],
            ["Principle 4.2", "Independent review"],
            ["Principle 4.3", "Process verification"],
            ["Principle 4.4", "Model performance monitoring"],
            ["Principle 4.5", "Periodic revalidation"],
            ["Principle 5", "Model risk mitigants"],
            ["Principle 5.1", "Process for applying post-model adjustments"],
            ["Principle 5.2", "Restrictions on model use"],
            ["Principle 5.3", "Exceptions and escalations"],
        ],
    },
    {
        "authority": "OSFI", "confidence": V_PRIMARY,
        "instrument": "OSFI Guideline E-23 — Model Risk Management (2027)",
        "note": "Structured as three outcomes, each heading a group of principles numbered X.Y where X is the parent outcome. Twelve principles in total. A mapping that treats E-23 as having only three citable units under-represents it by twelve. The guideline also carries Appendix 1, Information tracking for models, which sets out minimum inventory content and informed Annex B. Section A.4 defines six stakeholder roles — Model Owner, Model Developer, Model Reviewer, Model Approver, Model User and Model Stakeholder. Principle 2.1 covers all models in use or recently decommissioned: models of negligible risk are not outside the identification obligation, only outside the heavier controls.",
        "items": [
            ["Outcome 1", "Model risk is well understood and managed across the enterprise."],
            ["Principle 1.1", "Effective reporting structures and proper resourcing should enable sound model governance."],
            ["Principle 1.2", "The MRM framework should align risk-taking activities to strategic objectives and risk appetite."],
            ["Principle 1.3", "Models should be appropriate for their business purposes."],
            ["Outcome 2", "Model risk is managed using a risk-based approach."],
            ["Principle 2.1", "Institutions should identify and track all models in use or recently decommissioned."],
            ["Principle 2.2", "Institutions should establish a model risk rating approach that assesses key dimensions of model risk."],
            ["Principle 2.3", "The scope, scale, and intensity of MRM should be commensurate with the risk introduced by the model."],
            ["Outcome 3", "Model governance covers the entire model lifecycle."],
            ["Principle 3.1", "MRM policies, procedures, and controls should be robust, flexible, and lead to effective requirements applied across the model lifecycle."],
            ["Principle 3.2", "Data used to develop the model should be suitable for the intended use."],
            ["Principle 3.3", "Institutions should have model development processes that set clear standards for performance and documentation."],
            ["Principle 3.4", "Institutions should have a process to independently assess conceptual soundness and performance of models."],
            ["Principle 3.5", "Models should be deployed in an environment with quality and change control processes."],
            ["Principle 3.6", "Institutions should have defined standards for model monitoring, and model decommission."],
        ],
    },
    {
        "authority": "OCC / FRB / FDIC", "confidence": V_PRIMARY,
        "instrument": "US interagency Supervisory Guidance on Model Risk Management "
                      "(SR 26-2 / OCC 2026-13 / FDIC FIL-15-2026, 17 April 2026)",
        "note": "Seven sections. Expressly non-enforceable and most relevant to banking "
                "organisations above $30 billion in total assets. Generative and agentic AI are "
                "outside scope. Replaced the 2011 guidance, which was rescinded.",
        "items": [
            ["I", "INTRODUCTION"],
            ["II", "PURPOSE AND SCOPE"],
            ["III", "OVERVIEW OF MODEL RISK AND MODEL RISK MANAGEMENT"],
            ["IV", "MODEL DEVELOPMENT AND MODEL USE"],
            ["IV — sub", "Model Development; Model Use"],
            ["V", "MODEL VALIDATION AND MONITORING"],
            ["V — sub", "Components of Model Validation; Conceptual Soundness; Outcomes Analysis; Ongoing Model Monitoring"],
            ["VI", "GOVERNANCE AND CONTROLS"],
            ["VI — sub", "Roles and Responsibilities; Model Inventory; Documentation"],
            ["VII", "VENDOR AND OTHER THIRD-PARTY PRODUCTS"],
        ],
    },
    {
        "authority": "ECB", "confidence": V_PRIMARY,
        "instrument": "ECB guide to internal models (June 2026, release 4.1) — overarching "
                      "principles chapter",
        "note": "Five chapters overall: overarching principles for internal models; credit risk; "
                "market risk under CRR2; market risk under CRR3; counterparty credit risk. The "
                "sections below are those of the overarching principles chapter.",
        "items": [
            ["Section 1", "Guidelines at consolidated and subsidiary levels"],
            ["Section 2", "Documentation of internal models"],
            ["Section 3", "Data governance"],
            ["Section 4", "Implementation of a model risk management framework"],
            ["Section 5", "Identification of management body and senior management"],
            ["Section 6", "General principles for internal validation"],
            ["Section 7", "General principles for internal audit"],
            ["Section 8", "General principles on climate-related and environmental risks"],
            ["Section 9", "The use of machine learning techniques in internal models"],
            ["Section 10", "General principles for the implementation of a changed or extended model"],
            ["Section 11", "Third-party involvement"],
            ["Section 12", "Internal models in the context of consolidations"],
        ],
    },
    {
        "authority": "EU", "confidence": V_PRIMARY,
        "instrument": "Regulation (EU) No 575/2013 (CRR) — binding internal model articles",
        "note": "Directly applicable EU law. These are the binding obligations that the ECB guide "
                "interprets; the guide itself is not a legal act.",
        "items": [
            ["Article 174", "Use of models"],
            ["Article 179", "Overall requirements for estimation"],
            ["Article 185", "Validation of internal estimates"],
            ["Article 188", "Validation and documentation"],
            ["Article 189", "Corporate Governance"],
            ["Article 191", "Internal Audit"],
        ],
    },
    {
        "authority": "BCBS", "confidence": V_PRIMARY,
        "instrument": "BCBS 239 — Principles for effective risk data aggregation and risk reporting",
        "note": "Fourteen principles. Principles 1–2 cover governance and infrastructure, 3–6 risk "
                "data aggregation capabilities, 7–11 risk reporting practices, and 12–14 "
                "supervisory review. Not directly binding; effect depends on domestic "
                "implementation.",
        "items": [
            ["Principle 1", "Governance"],
            ["Principle 2", "Data architecture and IT infrastructure"],
            ["Principle 3", "Accuracy and Integrity"],
            ["Principle 4", "Completeness"],
            ["Principle 5", "Timeliness"],
            ["Principle 6", "Adaptability"],
            ["Principle 7", "Accuracy"],
            ["Principle 8", "Comprehensiveness"],
            ["Principle 9", "Clarity and usefulness"],
            ["Principle 10", "Frequency"],
            ["Principle 11", "Distribution"],
            ["Principle 12", "Review"],
            ["Principle 13", "Remedial actions and supervisory measures"],
            ["Principle 14", "Home/host cooperation"],
        ],
    },
    {
        "authority": "BCBS", "confidence": V_PRIMARY,
        "instrument": "BCBS Guidance on credit risk and accounting for expected credit losses (d350, "
                      "18 December 2015)",
        "note": "Eleven principles. Principles 1 to 8 address banks; Principles 9 to 11 address "
                "supervisors. Principle 5 is the direct antecedent of the expected credit loss "
                "model validation obligation in APS 220, which transposes it in near-identical "
                "binding language. APG 220 directs ADIs to have regard to this guidance.",
        "items": [[lab, st] for lab, st in BCBS_ECL_PRINCIPLES],
    },
    {
        "authority": "BCBS", "confidence": V_PRIMARY,
        "instrument": "BCBS Stress testing principles (d450, October 2018)",
        "note": "Nine principles. Principles 7 and 8 bear directly on model risk in stress testing.",
        "items": [
            ["Principle 1", "Stress testing frameworks should have clearly articulated and formally adopted objectives"],
            ["Principle 2", "Stress testing frameworks should include an effective governance structure"],
            ["Principle 3", "Stress testing should be used as a risk management tool and to inform business decisions"],
            ["Principle 4", "Stress testing frameworks should capture material and relevant risks and apply stresses that are sufficiently severe"],
            ["Principle 5", "Resources and organisational structures should be adequate to meet the objectives of the stress testing framework"],
            ["Principle 6", "Stress tests should be supported by accurate and sufficiently granular data and by robust IT systems"],
            ["Principle 7", "Models and methodologies to assess the impacts of scenarios and sensitivities should be fit for purpose"],
            ["Principle 8", "Stress testing models, results and frameworks should be subject to challenge and regular review"],
            ["Principle 9", "Stress testing practices and findings should be communicated within and across jurisdictions"],
        ],
    },
    {
        "authority": "BCBS", "confidence": V_PRIMARY,
        "instrument": "BCBS Principles for the sound management of third-party risk (d605)",
        "note": "Twelve principles grouped under governance and strategy, the third-party "
                "lifecycle, and the role of supervisors. Relevant to externally supplied models.",
        "items": [
            ["Principles 1–2", "Governance, risk management and strategy"],
            ["Principle 3", "Risk assessment"],
            ["Principle 4", "Due diligence"],
            ["Principle 5", "Contracting"],
            ["Principle 6", "Onboarding"],
            ["Principle 7", "Ongoing monitoring"],
            ["Principle 8", "Business continuity management"],
            ["Principle 9", "Termination"],
            ["Principles 10–12", "Role of supervisors"],
        ],
    },
    {
        "authority": "MAS", "confidence": V_PRIMARY,
        "instrument": "MAS Notice 637 — internal model validation provisions",
        "note": "Binding Notice. Section 7 sets model validation requirements; paragraphs 2.5 and "
                "2.6 of Section 2 cover internal validation and its independent review. The "
                "numbered paragraphs carry no printed titles.",
        "items": [
            ["Section 7, paras 7.1–7.6", "Model Validation Requirements"],
            ["Section 2, para 2.5(a)–(c)", "Internal Validation"],
            ["Section 2, para 2.6(a)–(e)", "Independent Review of Internal Validation"],
        ],
    },
    {
        "authority": "MAS", "confidence": V_PRIMARY,
        "instrument": "MAS FEAT Principles (November 2018) and the Artificial Intelligence Model "
                      "Risk Management information paper (December 2024)",
        "note": "FEAT comprises fourteen voluntary principles across fairness, ethics, "
                "accountability and transparency; several carry no printed sub-heading. The 2024 "
                "information paper describes observed good practice and is not mandatory.",
        "items": [
            ["FEAT 1–2", "Justifiability"],
            ["FEAT 3–4", "Accuracy and Bias"],
            ["FEAT 5–6", "Ethics (no printed sub-heading)"],
            ["FEAT 7–9", "Internal Accountability"],
            ["FEAT 10–11", "External Accountability"],
            ["FEAT 12–14", "Transparency (no printed sub-heading)"],
            ["Info paper §4", "Governance and Oversight"],
            ["Info paper §5", "Key Risk Management Systems and Processes"],
            ["Info paper §6", "Development and Deployment"],
        ],
    },
    {
        "authority": "FSB", "confidence": V_PRIMARY,
        "instrument": "FSB Sound Practices for Responsible Adoption of Artificial Intelligence — "
                      "consultation report",
        "note": "Twelve sound practices. A consultation report, expressly not intended to "
                "establish an international standard. Addresses AI rather than model risk "
                "generally, and is used here only as comparative input.",
        "items": [
            ["Sound Practice 1", "Strategic direction and oversight"],
            ["Sound Practice 2", "Governance and accountability"],
            ["Sound Practice 3", "Incorporation of AI risks into risk management framework"],
            ["Sound Practice 4", "Organisational adaptability"],
            ["Sound Practice 5", "Materiality and risk assessment"],
            ["Sound Practice 6", "Selection"],
            ["Sound Practice 7", "Data governance"],
            ["Sound Practice 8", "Explainability and transparency"],
            ["Sound Practice 9", "Performance management"],
            ["Sound Practice 10", "Human oversight"],
            ["Sound Practice 11", "Cyber and ICT risk management"],
            ["Sound Practice 12", "Third-party AI risk management"],
        ],
    },
    {
        "authority": "FSB", "confidence": V_PRIMARY,
        "instrument": "FSB, The Financial Stability Implications of Artificial Intelligence "
                      "(14 November 2024) — identified vulnerabilities",
        "note": "An analytical report, not a standard. Section 4.2 identifies financial sector "
                "vulnerabilities.",
        "items": [
            ["§4.2.1", "Third-party dependencies and service provider concentration"],
            ["§4.2.2", "Market correlations"],
            ["§4.2.3", "Cyber"],
            ["§4.2.4", "Model risk, data, and governance"],
            ["§4.2.5", "Other vulnerabilities"],
        ],
    },
    {
        "authority": "APRA", "confidence": V_PRIMARY,
        "instrument": "Australian instruments carrying model governance obligations",
        "note": "APRA has no model risk prudential standard and no enumerated model risk "
                "principles. Model governance obligations are distributed across instruments "
                "written for other purposes, and cannot be mapped one-to-one against a comparator "
                "principle set. That distribution is the gap CPS XXXX addresses. Paragraph "
                "references below were read from the primary instruments.",
        "items": [
            ["APS 113 paras 15–19", "Key principles"],
            ["APS 113 paras 20–23", "Governance and oversight"],
            ["APS 113 para 27", "Independent review"],
            ["APS 113 paras 42–56", "IRB approval, initial approval, phased roll-out, permanent partial use and ongoing requirements"],
            ["APS 113 Att. D paras 29–35", "Use of statistical models in the rating process"],
            ["APS 113 Att. D paras 67–68", "Use of internal ratings (the use test)"],
            ["APS 113 Att. D paras 103–109", "Validation of internal estimates"],
            ["APG 113 Chapter 7", "Validation of rating systems and risk estimates"],
            ["CPS 220 paras 19–26", "Risk management framework"],
            ["CPS 220 paras 27–28", "Risk appetite"],
            ["CPS 220 paras 44–51", "Review of the risk management framework"],
            ["CPS 230 paras 11–14", "Key principles"],
            ["CPS 230 paras 28–30", "Operational risk controls"],
            ["CPS 230 paras 34–38", "Critical operations and tolerance levels"],
            ["CPS 234", "Information security controls, testing and incident notification"],
            ["CPG 235", "Managing data risk — practice guide, non-enforceable"],
            ["CPS 320 paras 22–23", "Actuarial advice framework"],
            ["CPS 320 paras 24–33", "Financial Condition Report and Actuarial Valuation Report"],
            ["CPS 320 paras 35–40", "Actuarial reviews required by APRA"],
            ["SPS 530 paras 10–15", "Investment governance framework"],
            ["SPS 530 paras 30–35", "Investment stress testing"],
            ["SPS 515", "Strategic planning and member outcomes"],
        ],
    },
]


# --------------------------------------------------------------------------- #
# Regulatory crosswalk
# Columns: domain | APRA current | US | PRA | OSFI | ECB | MAS | BCBS | FSB |
#          proposed CPS XXXX
# --------------------------------------------------------------------------- #

CROSSWALK_ROWS_FULL = [
    ["Legal character of the framework",
     "Binding prudential standards, but none addresses model risk as such.",
     "Supervisory guidance only, expressly non-enforceable; the sole binding instrument makes guidance non-binding.",
     "Supervisory statement; expectations, not Rulebook rules.",
     "Supervisory guideline; final but not effective until 1 May 2027.",
     "Supervisory guide interpreting binding CRR articles; the CRR is the law, the guide is not.",
     "Binding Notice for capital models; information paper and voluntary principles for AI.",
     "International principles; effect depends on domestic implementation.",
     "Analytical and consultative reports; expressly not standards.",
     "Binding cross-industry prudential standard, deliberately enforceable rather than advisory."],

    ["Definition of a model",
     "Not defined on a cross-industry basis.",
     "Narrowed in April 2026 to complex methods applying statistical, economic or financial theories; excludes spreadsheet arithmetic, deterministic rules, and generative and agentic AI.",
     "Principle 1.1(a) sets out a definition firms should adopt as the basis for the scope of their framework, and expects consideration of quantitative methods falling outside it.",
     "Model definition expressly includes AI and machine learning.",
     "Internal models for regulatory capital; machine learning addressed as a technique within them.",
     "Capital models defined in Notice 637; AI models addressed separately.",
     "No general definition; BCBS 239 addresses risk data rather than models.",
     "Uses the OECD AI definition rather than a model definition.",
     "Broad function-based definition capturing deterministic actuarial and pricing calculations, which the US now excludes."],

    ["Non-model quantitative tools",
     "Not addressed.",
     "Expressly excluded from the model definition; no control obligation stated in the 2026 guidance.",
     "Principle 1.1 expects firms to consider quantitative methods falling outside the model definition.",
     "Addressed through the risk-based approach.",
     "Not separately addressed.",
     "Not separately addressed.",
     "Not addressed.",
     "Not addressed.",
     "Express requirement to identify material tools outside the definition and control them proportionately."],

    ["Enterprise-wide scope",
     "Implicit in CPS 220 but model risk is not named as a material risk.",
     "Applies across the organisation; most relevant above $30bn total assets.",
     "Enterprise-wide, but only for firms with internal model approval.",
     "Enterprise-wide across all models regardless of source or purpose.",
     "Limited to internal models used for regulatory capital.",
     "Capital models; AI practices observed more broadly.",
     "Not applicable.",
     "Not applicable.",
     "Enterprise-wide across all models, all business lines and all APRA-regulated industries."],

    ["Proportionality",
     "General principle across all standards; not linked to model risk.",
     "Risk-based; a 2025 bulletin confirms community banks need not validate annually.",
     "Tiering drives control intensity.",
     "Scope, scale and intensity commensurate with model risk (Principle 2.3).",
     "Materiality of the model within the capital framework.",
     "Risk materiality drives control intensity.",
     "Principles applied proportionately.",
     "Explicit proportionality by institution and use-case materiality.",
     "Proportionate by tier, with exceptions documented, time-bound, approved and reviewed."],

    ["De minimis and scope relief",
     "No mechanism; model requirements apply only where a capital or actuarial standard reaches them.",
     "Models deemed immaterial may attract only identification and monitoring of the conditions under which their use could become material; the guidance also applies mainly above a $30bn entity threshold.",
     "Tiering determines control intensity; no separate de minimis category.",
     "Principle 2.3 scales scope, scale and intensity to model risk, but Principle 2.1 keeps all models within identification.",
     "Materiality assessment within the internal model framework; no de minimis category.",
     "Risk materiality drives control intensity.",
     "Not addressed.",
     "Proportionality by use-case materiality.",
     "Express de minimis determination at model level, confined to identification, inventory, ownership, classification and reassessment, with prohibited classes, an aggregate test and an anti-disaggregation limb."],
    ["Model inventory",
     "No cross-industry obligation.",
     "Described as common industry practice rather than an expectation.",
     "Principle 1.2 requires a model inventory.",
     "Principle 2.1 requires identification and tracking of all models in use or recently decommissioned.",
     "Model register expected for internal models.",
     "Expected for capital models; inventories observed in AI practice.",
     "Not addressed.",
     "Documentation of AI identified as a sound practice.",
     "Complete, current, controlled enterprise inventory including embedded, third-party and recently decommissioned models, with minimum fields prescribed."],

    ["Risk tiering",
     "No taxonomy; APS 113 distinguishes only by capital treatment.",
     "Model risk framed as inherent risk in the context of materiality, itself a function of exposure and purpose.",
     "Principle 1.3 model tiering.",
     "Principle 2.2 requires a model risk rating approach assessing key dimensions.",
     "Materiality assessment within the internal model framework.",
     "Risk materiality assessment central to AI control intensity.",
     "Not addressed.",
     "Materiality and risk assessment at inception and thereafter.",
     "Documented tiering on quantitative and qualitative factors, driving validation, monitoring, approval and reporting intensity."],

    ["Board and senior accountability",
     "CPS 220 gives the Board the risk management framework; model risk not named.",
     "Roles and responsibilities with defined accountability, including conflicts between development and validation.",
     "Principle 2.1 Board responsibilities and 2.2 SMF accountability for the framework.",
     "Principle 1.1 on reporting structures and resourcing.",
     "Section 5 identification of management body and senior management.",
     "Board and senior management oversight in observed AI practice.",
     "Governance is BCBS 239 Principle 1.",
     "Sound Practices 1 and 2 on strategic direction, oversight, governance and accountability.",
     "Board approves the framework and appetite; a named senior executive is accountable for the framework; every model has a named owner."],

    ["Development and conceptual soundness",
     "APS 113 for IRB models only.",
     "Section IV on model development, including purpose statement, user input and testing.",
     "Principle 3.1 model purpose and design; 3.3 development testing.",
     "Principle 3.3 on development processes with clear standards.",
     "Documentation and data governance sections of the overarching principles chapter.",
     "Notice 637 for capital models.",
     "Not addressed directly.",
     "Sound Practice 6 on selection.",
     "Documented development standards, conceptual soundness, consideration of alternatives, and recorded limitations for all material models."],

    ["Data",
     "CPG 235 is a non-enforceable guide dating from 2013.",
     "Data quality, relevance and inputs assessed within development testing.",
     "Principle 3.2 the use of data.",
     "Principle 3.2 requires data suitable for the intended use.",
     "Section 3 data governance; separate guide on risk data aggregation and reporting.",
     "Data quality and representativeness prominent in AI practice.",
     "BCBS 239 sets fourteen principles on risk data aggregation and reporting.",
     "Sound Practice 7 on data governance.",
     "Data appropriateness as well as quality, lineage to source, and documented treatment of proxy, external and synthetic data."],

    ["Documentation",
     "Only within APS 113 and actuarial standards.",
     "Reduced in 2026 to a statement that adequate documentation helps support model risk management.",
     "Principle 3.5 model development documentation.",
     "Principle 3.3 covers documentation standards.",
     "Section 2 documentation of internal models; CRR Article 188 makes it binding.",
     "Required for capital models under Notice 637.",
     "Not addressed.",
     "Documentation identified as a sound practice.",
     "Reconstruction standard: sufficient for an independent competent person to reproduce material results."],

    ["Testing before use",
     "Only within capital model approval.",
     "Validation generally occurs before first use, but use before validation is permitted for urgent business need with compensating controls.",
     "Principle 3.3 model development testing.",
     "Within the model review and approval lifecycle stages.",
     "Pre-approval assessment by the supervisor for capital models.",
     "Pre-deployment validation expected for higher-risk AI.",
     "Not addressed.",
     "Performance assessment proportionate to risk.",
     "Express bar: a model must not be used for a material purpose until tested and residual limitations accepted at an appropriate authority."],

    ["Independent validation",
     "APS 113 for IRB; the Appointed Actuary provides a different form of independent review.",
     "Quality of validation depends on the rigour of the review rather than on organisational structure — a softening from the 2011 text.",
     "Principle 4 independent model validation, with five sub-principles.",
     "Principle 3.4 requires a process to independently assess conceptual soundness and performance.",
     "Section 6 internal validation; CRR Articles 185 and 188 make validation binding.",
     "Notice 637 paragraphs 2.5 and 2.6 on internal validation and its independent review.",
     "Not addressed.",
     "Performance management, with independence left flexible.",
     "Independent validation required for material models, with vendor or sponsor validation expressly insufficient."],

    ["Components of validation",
     "Not specified.",
     "Conceptual soundness, outcomes analysis, and ongoing model monitoring.",
     "Principles 4.2 independent review, 4.3 process verification, 4.4 performance monitoring, 4.5 periodic revalidation.",
     "Conceptual soundness and performance under Principle 3.4.",
     "Validation covering methodology, data and performance.",
     "Validation requirements in Section 7 of Notice 637.",
     "Not addressed.",
     "Not addressed.",
     "Conceptual soundness, outcomes analysis and ongoing model monitoring, with an explicit conclusion on fitness for use."],

    ["Effective challenge",
     "Concept absent from the framework.",
     "Retained and reformulated: expertise, sufficient independence, and organisational standing and influence to effect change.",
     "Embedded in Principle 4 as ongoing, independent and effective challenge.",
     "Implicit in the independent assessment principle.",
     "Internal validation and internal audit principles.",
     "Independent review under Notice 637.",
     "Not addressed.",
     "Not addressed.",
     "Express requirement, with an expectation that entities test whether challenge is operating effectively."],

    ["Model use and misuse",
     "Use test in APS 113 only.",
     "Recognised that a sound model can carry high model risk if misapplied or misused.",
     "Principle 3 covers model use.",
     "Principle 1.3 models should be appropriate for their business purposes.",
     "Credit risk chapter, general topics Section 6 model use; CRR Article 174 use of models is binding.",
     "Use test for capital models.",
     "Not addressed.",
     "Human oversight sound practice.",
     "Use confined to approved purpose and conditions, with limitations communicated to users rather than merely recorded."],

    ["Overlays and expert judgement",
     "Not governed generally.",
     "Overlays and adjustments referenced within monitoring.",
     "Principle 3.4 model adjustments and expert judgement; Principle 5.1 post-model adjustments.",
     "Addressed within model monitoring standards.",
     "Margin of conservatism framework for internal models.",
     "Not addressed generally.",
     "Not addressed.",
     "Not addressed.",
     "Governance of basis, quantification, approval, duration and removal, with aggregate reporting of overlays in force."],

    ["Change management",
     "APS 113 for capital models only.",
     "Frequency and scope of model changes inform validation timing.",
     "Within Principle 3 and Principle 4.5 periodic revalidation.",
     "Principle 3.5 deployment with quality and change control processes.",
     "Section 10 on implementation of a changed or extended model; a detailed model change regime.",
     "Change control for capital models.",
     "Not addressed.",
     "Organisational adaptability sound practice.",
     "Materiality assessment of changes individually and cumulatively, with provider-initiated change treated as an entity change event."],

    ["Monitoring and drift",
     "Limited to specific model classes.",
     "Ongoing model monitoring as a named validation component.",
     "Principle 4.4 model performance monitoring.",
     "Principle 3.6 standards for model monitoring and decommission.",
     "Within internal validation and model change provisions.",
     "Post-deployment monitoring in observed AI practice.",
     "Not addressed.",
     "Sound Practice 9 performance management.",
     "Tier-based monitoring frequency with pre-set thresholds linked to investigation, restriction, revalidation or withdrawal."],

    ["Decommissioning",
     "Not addressed.",
     "Not separately addressed.",
     "Not separately addressed.",
     "Principle 3.6 expressly covers model decommission.",
     "Not separately addressed.",
     "Not addressed.",
     "Not addressed.",
     "Not addressed.",
     "Managed decommissioning covering downstream models, outputs still in force, records and data disposition."],

    ["Third-party and vendor models",
     "CPS 230 governs the provider, not the model.",
     "Section VII on vendor and other third-party products, including validation and ongoing monitoring of vendor models.",
     "Principle 2.6 use of externally developed models and third-party vendor products.",
     "All models in scope regardless of source; B-10 applies to the arrangement.",
     "Section 11 third-party involvement.",
     "Provider opacity and contingency prominent in AI practice.",
     "Twelve third-party risk principles covering the full lifecycle.",
     "Sound Practice 12 third-party AI risk management.",
     "Full framework applied to third-party models, with usable information rights and compensating controls where information is unavailable."],

    ["Concentration and substitutability",
     "Bilateral service provider assessment under CPS 230.",
     "Not addressed as a systemic matter.",
     "Not AI-specific.",
     "Interconnectedness is a proportionality factor.",
     "Not addressed as a systemic matter.",
     "Provider concentration highlighted in AI practice.",
     "Concentration addressed in the third-party principles.",
     "Third-party dependencies and service provider concentration identified as a financial stability vulnerability.",
     "Entity-level concentration assessment, with support for sector-wide monitoring of common model and data dependencies."],

    ["AI and machine learning models",
     "Addressed through a separate AI workstream, not as a model class.",
     "Traditional and non-generative, non-agentic AI models in scope; generative and agentic AI expressly excluded.",
     "Covered where AI meets the firm's model definition; a 2025 roundtable considered AI and ML in model risk.",
     "Model definition expressly includes AI and machine learning.",
     "Section 9 on the use of machine learning techniques in internal models.",
     "Detailed observed practice for AI model risk management, including generative AI.",
     "Analytical work on digitalisation and an AI/ML newsletter; no dedicated standard.",
     "Twelve sound practices for AI adoption, expressly not a standard.",
     "AI models within the framework as a model class, with an express boundary rule against the separate AI instrument."],

    ["Expected credit loss and provisioning models",
     "APS 220 requires sound policies and processes to appropriately validate ECL models, sound measurement methodologies, adequate aggregate provisions and experienced credit judgement. APG 220 directs ADIs to have regard to the Basel guidance. APRA's October 2023 letter sets out observed practice.",
     "Not addressed as a distinct model class in the model risk guidance; ECL sits in the accounting and credit supervision streams.",
     "Covered where an ECL model falls within the firm's model definition; no dedicated ECL provision in SS1/23.",
     "Covered by the general model definition; no dedicated ECL principle.",
     "IFRS 9 ECL models fall within the internal models and credit risk supervisory frameworks; no dedicated chapter in the internal models guide.",
     "Not addressed as a distinct model class.",
     "Dedicated guidance: eleven principles on credit risk and accounting for expected credit losses, including Principle 5 on ECL model validation and Principles 9 to 11 on supervisory evaluation.",
     "Not addressed.",
     "Express requirement that ECL and provisioning models are within the model risk framework, with judgement-based adjustments, overlays, assumptions and scenarios governed with the same discipline as the models, and a set of review focus areas in Annex G."],
    ["Aggregate model risk",
     "Not required.",
     "Sound practice to assess model risk individually and in aggregate, reflecting interactions, dependencies and reliance on common assumptions, data or methodologies.",
     "Principle 2.1 board responsibilities, covering understanding and reporting of model risk in aggregate.",
     "Outcome 1 requires model risk to be understood across the enterprise.",
     "Model risk considered in supervisory review.",
     "Not addressed.",
     "Prudent valuation guidance (CAP50) and the Pillar 3 prudent valuation template may bear on aggregate model risk adjustment and disclosure; not confirmed from primary text at the as-of date.",
     "Not addressed.",
     "Aggregate assessment required and considered in internal capital assessment, with qualitative measures permitted where quantification is not yet feasible."],

    ["Internal audit and assurance",
     "General internal audit obligations only.",
     "Internal audit evaluates whether model risk management practices are rigorous and effective, rather than duplicating validation.",
     "Principle 2.5 Internal Audit.",
     "Addressed within governance expectations.",
     "Section 7 internal audit; CRR Article 191 makes it binding.",
     "Independent review under Notice 637.",
     "Three lines concepts apply generally.",
     "Governance sound practices.",
     "Periodic independent assessment of framework design and operating effectiveness, including the effectiveness of validation and challenge, reported to the Board Audit Committee."],

    ["Supervisory notification",
     "CPS 230 and CPS 234 set materiality criteria and timeframes.",
     "No model-specific notification requirement.",
     "Escalation within the framework; no notification rule.",
     "Supervisory engagement expected.",
     "Model change approval required from the supervisor for capital models.",
     "Notification for capital model changes.",
     "Not addressed.",
     "Not addressed.",
     "Cross-references CPS 230 and CPS 234 rather than creating a separate deadline, with early engagement expected on material model weakness."],
]

# The Word annex omits the 'APRA current' column and leads with the proposal.
CROSSWALK_ROWS = [[r[0], r[9], r[2], r[3], r[4], r[5], r[6], r[7], r[8]]
                  for r in CROSSWALK_ROWS_FULL]


# --------------------------------------------------------------------------- #
# Requirement-by-authority challenge
#
# Support is derived mechanically from the source IDs each requirement relies
# on, then overridden where verification showed the authority diverges or is
# silent. The derivation rule is stated on the sheet so a reader can check it.
# --------------------------------------------------------------------------- #

_AUTHORITY_SOURCES = {
    "APRA": ("APRA-",),
    "OCC/Fed": ("US-MRM-", "US-SG-", "OCC-"),
    "PRA": ("PRA-",),
    "OSFI": ("OSFI-",),
    "ECB": ("ECB-",),
    "MAS": ("MAS-",),
    "BCBS": ("BCBS-",),
    "FSB": ("FSB-",),
}

STRONG = "Strong support"
MODERATE = "Moderate support"
LIMITED = "Limited / indirect"
SILENT = "Not addressed"
DIVERGES = "Diverges"

# Where verification showed the authority takes a different position, or is
# silent notwithstanding a citation elsewhere in the requirement.
_OVERRIDES = {
    ("M02", "OCC/Fed"): (DIVERGES, "The April 2026 guidance narrows the definition to complex "
                                   "methods and excludes spreadsheet arithmetic, deterministic "
                                   "rules and generative and agentic AI. CPS XXXX does not follow."),
    ("M03", "OCC/Fed"): (DIVERGES, "Expressly excludes such tools from the model definition and "
                                   "states no control obligation for them."),
    ("M21", "OCC/Fed"): (MODERATE, "Retains validation but states its quality depends on the "
                                   "rigour of review rather than organisational structure, a "
                                   "softening from the rescinded 2011 text."),
    ("M20", "OCC/Fed"): (MODERATE, "Validation generally precedes first use, but use before "
                                   "validation is permitted for urgent business need with "
                                   "compensating controls."),
    ("M34", "OCC/Fed"): (DIVERGES, "Generative and agentic AI are expressly outside scope; "
                                   "non-generative AI models are in scope."),
    ("M35", "OCC/Fed"): (SILENT, "No parallel AI instrument, so no boundary rule arises."),
    ("M35", "OSFI"): (STRONG, "Single framework covering models including AI removes the boundary "
                              "problem entirely — the alternative architecture to the one proposed."),
    ("M40", "OSFI"): (SILENT, "Superannuation is outside OSFI's perimeter; federally regulated "
                              "pension plans are expressly excluded from E-23."),
    ("M14", "OCC/Fed"): (MODERATE, "Describes a comprehensive inventory as common industry "
                                   "practice rather than stating it as an expectation."),
    ("M19", "OCC/Fed"): (MODERATE, "Reduced in 2026 to a statement that adequate documentation "
                                   "helps support model risk management."),
    ("M31", "OSFI"): (STRONG, "Principle 3.6 expressly covers model decommission — the only "
                              "comparator that does."),
    ("M42", "OCC/Fed"): (STRONG, "Expressly requires assessment of model risk individually and in "
                                 "aggregate, reflecting interactions and common dependencies."),
}

_OVERALL = {
    True: "Pass as policy proposal — consult and cost-benefit test",
    False: "Pass — supported and status-qualified",
}


def _support_for(req, authority):
    key = (req["id"], authority)
    if key in _OVERRIDES:
        return _OVERRIDES[key]
    prefixes = _AUTHORITY_SOURCES[authority]
    if any(s.startswith(prefixes) for s in req["sources"]):
        return (STRONG, "")
    return (SILENT, "")


def build_requirement_test(requirements):
    rows = []
    for r in requirements:
        cells = []
        notes = []
        for auth in _AUTHORITY_SOURCES:
            level, why = _support_for(r, auth)
            cells.append(level)
            if why:
                notes.append(f"{auth}: {why}")
        overall = _OVERALL[r["policy_choice"]]
        if r["legal_flag"]:
            overall = "Conditional pass — legal drafting required"
        rows.append([r["id"], r["title"], *cells, overall,
                     ", ".join(r["sources"]) + ("  |  " + "  ".join(notes) if notes else "")])
    return rows


# --------------------------------------------------------------------------- #
# Statement provenance ledger
# --------------------------------------------------------------------------- #

LEDGER_ROWS = [
    ["ST-01", "CPS XXXX / CPG XXXX", "US legal status",
     "The United States model risk guidance is supervisory guidance and does not have the force "
     "and effect of law.",
     "Extracted", V_PRIMARY,
     "12 CFR Part 4 Subpart F (OCC), 12 CFR §262.7 and Part 262 Appendix A (Board), 12 CFR Part "
     "302 Subpart A (FDIC), codifying the 2018 interagency statement. SR 26-2 repeats the "
     "disclaimer on its face.",
     "None required."],
    ["ST-02", "All artefacts", "US currency",
     "OCC Bulletin 2011-12 and Federal Reserve SR 11-7 were rescinded and superseded on 17 April "
     "2026 by SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026.",
     "Extracted", V_PRIMARY,
     "SR 26-2 cover letter supersession statement; the four-item rescission list in OCC Bulletin "
     "2026-13; FDIC FIL-15-2026; and the 'RESCINDED — Replaced, see OCC 2026-13' watermark on the "
     "OCC copy of the 2011 attachment.",
     "Corrected. The package initially cited SR 11-7 as current throughout. See RT-01."],
    ["ST-03", "CPS XXXX M02", "US model definition",
     "The current US definition is narrower than the definition adopted in CPS XXXX and excludes "
     "spreadsheet arithmetic, deterministic rule-based processes, and generative and agentic AI.",
     "Extracted", V_PRIMARY,
     "SR 26-2 §II and footnote 3.",
     "Corrected. The draft initially attributed a broad three-part definition to current US "
     "guidance. See RT-02."],
    ["ST-04", "CPS XXXX M23 / CPG XXXX", "Effective challenge",
     "Effective challenge survives in the 2026 US guidance, reformulated around expertise, "
     "sufficient independence, and organisational standing and influence to effect change.",
     "Extracted", V_PRIMARY,
     "SR 26-2 §III. The rescinded 2011 formulation was a combination of incentives, competence "
     "and influence.",
     "Corrected. The draft initially used the 2011 formulation. See RT-03."],
    ["ST-05", "CPS XXXX M22 / CPG XXXX", "Components of validation",
     "The components of validation are conceptual soundness, outcomes analysis and ongoing model "
     "monitoring.",
     "Extracted", V_PRIMARY,
     "SR 26-2 §V, sub-headings 'Components of Model Validation', 'Conceptual Soundness', "
     "'Outcomes Analysis', 'Ongoing Model Monitoring'.",
     "Corrected from the 2011 naming and ordering. See RT-04."],
    ["ST-06", "All artefacts", "PRA principle structure",
     "PRA SS1/23 has five principles and 23 sub-principles. Principle 5 is 'Model risk mitigants'.",
     "Extracted", V_PRIMARY,
     "SS1/23 primary text, principle and sub-principle headings transcribed verbatim.",
     "Corrected. A predecessor document in this project described Principle 5 as 'reporting'. "
     "See RT-05."],
    ["ST-07", "All artefacts", "OSFI structure",
     "OSFI Guideline E-23 (2027) is structured as three outcomes and twelve principles numbered "
     "1.1 to 3.6.",
     "Extracted", V_PRIMARY,
     "E-23 (2027) sections A.5, B, C and D, principle headings transcribed verbatim.",
     "Corrected. A predecessor document described E-23 as having three outcomes only, which "
     "under-represents it by twelve citable units. See RT-06."],
    ["ST-08", "All artefacts", "OSFI status and scope",
     "E-23 (2027) was published on 11 September 2025 and takes effect on 1 May 2027. It covers "
     "banks, foreign bank branches, life and fraternal companies, property and casualty companies "
     "and trust and loan companies, and does not apply to federally regulated pension plans.",
     "Extracted", V_PRIMARY,
     "OSFI guidance library entry for E-23 (2027) and the covering letter.",
     "None required."],
    ["ST-09", "All artefacts", "ECB currency",
     "The ECB guide to internal models is at its June 2026 release, whose overarching principles "
     "chapter includes a section on implementation of a model risk management framework and a "
     "section on the use of machine learning techniques in internal models.",
     "Extracted", V_PRIMARY,
     "ECB guide to internal models, chapter and section headings.",
     "Corrected from an initial citation of the February 2024 release. See RT-07."],
    ["ST-10", "CPG XXXX Annex", "CRR binding articles",
     "The binding EU obligations on internal models sit in CRR Articles 174, 179, 185, 188, 189 "
     "and 191; the ECB guide interprets them and is not itself a legal act.",
     "Extracted", V_PRIMARY,
     "Regulation (EU) No 575/2013, article headings.",
     "None required."],
    ["ST-11", "All artefacts", "FSB status",
     "The FSB sound practices for responsible adoption of AI are a consultation report comprising "
     "twelve sound practices and are expressly not intended to establish an international standard.",
     "Extracted", V_PRIMARY,
     "FSB consultation report, sound practice headings and the report's own statement of status.",
     "None required."],
    ["ST-12", "All artefacts", "BCBS third-party principles",
     "The BCBS principles for the sound management of third-party risk comprise twelve principles "
     "and are published as BCBS d605.",
     "Extracted", V_PRIMARY,
     "BIS publication d605, principle headings.",
     "Corrected from an initial reference to d588. See RT-08."],
    ["ST-13", "CPS XXXX M40 / CPG XXXX", "Superannuation",
     "No comparator authority addresses model risk in superannuation.",
     "Inferred", V_PRIMARY,
     "Scope statements of each comparator instrument. OSFI expressly excludes federally regulated "
     "pension plans.",
     "None required. Recorded as a policy design choice with no benchmark."],
    ["ST-14", "CPS XXXX M45 / CPG XXXX", "Notification",
     "No comparator authority imposes a model-risk-specific supervisory notification deadline.",
     "Inferred", V_PRIMARY,
     "Review of each comparator instrument. CPS 230 and CPS 234 provide the Australian "
     "notification architecture.",
     "A model-specific deadline was drafted and then removed as conflicting. See RT-09."],
    ["ST-15", "CPG XXXX", "Community bank proportionality",
     "The OCC has confirmed that its guidance does not require community banks to perform annual "
     "model validation.",
     "Extracted", V_PRIMARY,
     "OCC Bulletin 2025-26.",
     "None required. Informs the proportionality drafting rather than a requirement."],
    ["ST-18", "CPS XXXX M05 / CPG XXXX", "De minimis exception",
     "A model of no material consequence attracts only identification, inventory, ownership, "
     "classification and reassessment.",
     "Extracted + inferred", V_PRIMARY,
     "US interagency guidance 2026 §III states that where models are deemed immaterial, model risk "
     "management may consist of identifying those models and monitoring the conditions under which "
     "their use may become material. OSFI E-23 Principle 2.3 scales scope, scale and intensity to "
     "model risk while Principle 2.1 keeps all models within identification.",
     "The prohibited classes, the aggregate test and the anti-disaggregation limb are Australian "
     "drafting choices, not comparator requirements, and are labelled as a policy choice. See "
     "RT-50."],
    ["ST-17", "Workbook / crosswalk", "BCBS and aggregate model risk",
     "The crosswalk originally recorded the BCBS position on aggregate model risk as 'not "
     "addressed'. Adversarial review suggested the Basel Framework's prudent valuation guidance "
     "(CAP50) and the Pillar 3 prudent valuation template may require a model risk valuation "
     "adjustment and its disclosure.",
     "Unverified", V_NONE,
     "The BIS Basel Framework chapter pages load their text client-side and could not be "
     "retrieved in this session; the chapter's existence and title are confirmed but its "
     "provisions were not read. Neither the original negative nor the suggested positive is "
     "asserted.",
     "The cell now records the lead and its unverified status instead of asserting a negative. "
     "See RT-49. This should be resolved from the primary chapter before consultation."],
    ["ST-16", "Workbook", "Validation frequencies",
     "The validation frequencies shown by tier are illustrative drafting, not derived from any "
     "comparator instrument.",
     "Policy choice", V_PRIMARY,
     "No comparator prescribes frequencies on a cross-industry basis; the rescinded 2011 US "
     "guidance contained an at-least-annual periodic review expectation which the 2026 guidance "
     "does not carry forward.",
     "Labelled as illustrative in both the guide and the workbook. See RT-10."],
]


# --------------------------------------------------------------------------- #
# Red-team audit trail
# --------------------------------------------------------------------------- #

REDTEAM_ROWS = [
    ["RT-01",
     "The package cited OCC Bulletin 2011-12 / Federal Reserve SR 11-7 as the current United "
     "States model risk guidance, and used it as the primary authority for thirty-three "
     "requirement citations.",
     "Is the 2011 guidance still current as at July 2026? Supervisory guidance is periodically "
     "revised and the drafter's knowledge may predate any revision.",
     "The 2011 guidance was rescinded and superseded on 17 April 2026 by interagency guidance "
     "issued as Federal Reserve SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026. All citations "
     "were repointed to the 2026 guidance, the 2011 instrument was retained in the source "
     "register marked as rescinded for provenance, and the substantive divergences were assessed "
     "individually.",
     "Affected the source register, thirty-three requirement citations, sixteen guidance "
     "attribution lines and five scoring benchmarks.",
     "SR 26-2 cover letter; OCC Bulletin 2026-13 rescission list; FDIC FIL-15-2026; rescission "
     "watermark on the OCC copy of the 2011 attachment.",
     "High", "Closed — correction incorporated"],

    ["RT-02",
     "CPS XXXX's model definition was presented as following the established three-part US "
     "formulation, implying current US support for a broad definition.",
     "Does the current US guidance still support a broad definition? If not, the standard is "
     "claiming alignment it does not have.",
     "The 2026 US guidance narrows the definition to a 'complex' quantitative method applying "
     "statistical, economic or financial theories and expressly excludes simple arithmetic such "
     "as spreadsheet calculations, deterministic rule-based processes, and generative and agentic "
     "AI. CPS XXXX retains the broad definition — deliberately, because the narrow one would "
     "exclude actuarial and unit pricing calculations central to the Australian cross-industry "
     "perimeter — and the divergence is now stated openly rather than concealed by a citation.",
     "M02 rewritten; its provenance changed from Extracted to Extracted + inferred; the "
     "benchmark authority for the definition domain moved from the US to the PRA and OSFI.",
     "SR 26-2 §II and footnote 3.",
     "High", "Closed — correction incorporated"],

    ["RT-03",
     "Effective challenge was drafted as requiring 'competence, influence and incentive'.",
     "Is that the current formulation, or the rescinded one?",
     "That was the 2011 formulation. The 2026 guidance reformulates effective challenge around "
     "expertise to identify limitations, sufficient independence to maintain objectivity, and "
     "organisational standing and influence to effect change. M23 was redrafted to the current "
     "formulation; incentives are retained in the practice guide as a practical consideration "
     "rather than presented as part of the definition.",
     "M23 and the corresponding guidance paragraph rewritten.",
     "SR 26-2 §III; rescinded 2011 attachment §III for the superseded wording.",
     "Medium", "Closed — correction incorporated"],

    ["RT-04",
     "Validation scope was drafted as 'conceptual soundness, ongoing monitoring including process "
     "verification and benchmarking, and outcomes analysis'.",
     "Are those the current component names and does benchmarking sit where the draft places it?",
     "The 2026 guidance names the components conceptual soundness, outcomes analysis and ongoing "
     "model monitoring, in that order, and locates benchmarking under conceptual soundness rather "
     "than ongoing monitoring. M22 and the guidance were realigned.",
     "M22 and two guidance paragraphs rewritten.",
     "SR 26-2 §V sub-headings.",
     "Medium", "Closed — correction incorporated"],

    ["RT-05",
     "A predecessor document in this project described PRA SS1/23 Principle 5 as 'reporting'.",
     "Verify the five principle titles against the primary supervisory statement.",
     "Principle 5 is 'Model risk mitigants'. Reporting is embedded across the principles and is "
     "not a standalone principle. All five titles and all 23 sub-principle titles were "
     "transcribed verbatim from the primary text and carried into the principles register.",
     "Principles register, guidance attribution lines and the requirement-to-principle mapping.",
     "PRA SS1/23 primary text.",
     "High", "Closed — correction incorporated"],

    ["RT-06",
     "A predecessor document described OSFI E-23 as having three outcomes.",
     "Is that the whole structure? A three-unit framework would be unusually sparse for a "
     "lifecycle guideline.",
     "E-23 (2027) is structured as three outcomes AND twelve principles numbered 1.1 to 3.6. "
     "Treating it as three citable units under-represents it by twelve. The full structure is now "
     "reproduced in the principles register and used for attribution.",
     "Principles register, crosswalk and requirement-to-principle mapping.",
     "OSFI E-23 (2027) sections A.5, B, C and D.",
     "High", "Closed — correction incorporated"],

    ["RT-07",
     "The ECB guide to internal models was cited at its February 2024 release.",
     "Has the guide been revised since?",
     "The current release is June 2026. Its overarching principles chapter adds a section on "
     "implementation of a model risk management framework and a section on the use of machine "
     "learning techniques in internal models — both directly relevant to this standard and absent "
     "from the earlier release. The source register and the principles register were updated.",
     "Source register, principles register and two crosswalk cells.",
     "ECB guide to internal models, chapter and section headings.",
     "Medium", "Closed — correction incorporated"],

    ["RT-08",
     "The BCBS third-party risk principles were cited as publication d588.",
     "Confirm the publication number and principle count.",
     "The principles are published as d605 and comprise twelve principles. The source register "
     "URL and the principle count were corrected, and the source moved from unverified to "
     "verified against the primary publication.",
     "Source register and principles register.",
     "BIS publication d605.",
     "Medium", "Closed — correction incorporated"],

    ["RT-09",
     "An early draft proposed a model-risk-specific supervisory notification deadline.",
     "Is such a deadline supported by any comparator, and would it conflict with existing "
     "Australian notification architecture?",
     "No comparator imposes a model-specific notification deadline, and a new one risked "
     "conflicting with the materiality criteria and timeframes in CPS 230 and CPS 234. M45 now "
     "cross-references the existing architecture and expects early engagement on material model "
     "weakness instead.",
     "M45 redrafted; the notification domain scored against the existing architecture rather than "
     "a new obligation.",
     "CPS 230; CPS 234; comparator review.",
     "High", "Closed — correction incorporated"],

    ["RT-10",
     "Validation frequencies by tier were presented in the practice guide without qualification.",
     "Are these frequencies drawn from any comparator instrument?",
     "They are not. The rescinded 2011 US guidance contained an at-least-annual periodic review "
     "expectation which the 2026 guidance does not carry forward, and the OCC has since confirmed "
     "that community banks are not required to validate annually. The table is now labelled as "
     "illustrative drafting and identified as a policy design choice.",
     "Practice guide validation table caption and verification annotation; statement ledger entry "
     "ST-16.",
     "OCC Bulletin 2025-26; SR 26-2 §V; rescinded 2011 attachment §V.",
     "Medium", "Closed — correction incorporated"],

    ["RT-11",
     "An early draft required all models to be fully explainable.",
     "Is an absolute explainability requirement achievable, and is it supported?",
     "It is neither. Comparator authorities consistently frame explainability as fit for purpose "
     "and permit compensating controls where full explainability is not achievable. The guidance "
     "now requires explainability to be assessed against what the entity needs to do with the "
     "model, and requires outcome-based controls to be intensified where explainability is limited.",
     "Chapter 12 of the practice guide.",
     "Comparator review; ECB guide section on machine learning techniques.",
     "Medium", "Closed — correction incorporated"],

    ["RT-12",
     "An early draft required annual independent validation of every model.",
     "Is that proportionate, and is it supported?",
     "No comparator requires it universally, and the OCC has expressly confirmed that community "
     "banks need not validate annually. Validation frequency is now set by tier, with the "
     "highest tier at least annually and lower tiers on a risk-based cycle.",
     "M21 and M25; the validation intensity table in the practice guide.",
     "OCC Bulletin 2025-26; PRA SS1/23 Principle 4.5; OSFI E-23 Principle 2.3.",
     "Medium", "Closed — correction incorporated"],

    ["RT-13",
     "An early draft required contractual access to vendor source code and training data for "
     "third-party models.",
     "Is that achievable, and is it required by any comparator?",
     "It is frequently impracticable and raises intellectual property and security issues. No "
     "comparator requires it; the 2026 US guidance expressly acknowledges that proprietary "
     "components may not be disclosed while maintaining that the principles still apply. M32 and "
     "M33 now require sufficient information or compensating controls, expressed as an outcome.",
     "M32 and M33; chapter 11 of the practice guide.",
     "SR 26-2 §VII; PRA SS1/23 Principle 2.6; BCBS d605.",
     "High", "Closed — correction incorporated"],

    ["RT-14",
     "The scoring initially recorded the United States as the benchmark authority in seven "
     "domains, on the strength of the 2011 guidance.",
     "Does the 2026 guidance still set the benchmark in those domains?",
     "In several it does not. The 2026 text reduces documentation to a permissive statement, "
     "describes the inventory as common industry practice rather than an expectation, de-emphasises "
     "organisational independence in validation, and permits use before validation on urgent "
     "business need. The benchmark moved to the PRA, OSFI or ECB in five domains. The US remains "
     "the benchmark for effective challenge and aggregate model risk, where its articulation is "
     "still the strongest.",
     "Five benchmark authorities changed in the gap assessment, changing the priority ordering.",
     "SR 26-2 §§V and VI compared against PRA SS1/23, OSFI E-23 (2027) and the ECB guide.",
     "High", "Closed — correction incorporated"],

    ["RT-15",
     "The draft applies a single cross-industry standard to ADIs, insurers and RSE licensees.",
     "Can one instrument do that, and does it create gaps against the Appointed Actuary framework "
     "and the capital standards?",
     "The question cannot be resolved by drafting alone. The standard now expressly preserves the "
     "capital standards where more specific, requires insurers to map which validation elements "
     "the actuarial control cycle discharges, and flags enabling authority, sectoral application "
     "and instrument numbering for legal settlement in Annex F.",
     "M36, M39, Annex F; seven requirements carry a legal flag.",
     "APS 113; CPS 320; SPS 530; comparator review.",
     "High", "Open — referred for legal settlement"],

    ["RT-16",
     "The draft creates a boundary between this standard and a separate AI risk instrument.",
     "Does any comparator operate parallel model risk and AI instruments, and could a system fall "
     "between them?",
     "No comparator does. OSFI deliberately brought AI within a single model risk guideline, and "
     "the 2026 US guidance excludes generative and agentic AI from model risk scope without "
     "putting anything in its place. The boundary rule in M35 is therefore an Australian design "
     "choice, is labelled as one, and requires a single register recording which regime applies to "
     "each AI system so that the boundary is a documented determination.",
     "M35 marked as a policy choice and carrying a legal flag; chapter 12 of the practice guide.",
     "OSFI E-23 (2027) scope; SR 26-2 footnote 3.",
     "High", "Open — referred for consultation"],

    ["RT-17",
     "The claim that no comparator addresses superannuation model risk.",
     "Verify rather than assume — an unverified negative is as unsafe as an unverified positive.",
     "Confirmed. OSFI expressly excludes federally regulated pension plans from E-23; the PRA "
     "framework covers banks with internal model approval; the US guidance covers banking "
     "organisations. The superannuation domain is scored with no benchmark and the requirement is "
     "labelled a policy design choice.",
     "M40; the superannuation domain carries no benchmark authority in the gap assessment.",
     "Scope statements of each comparator instrument.",
     "Medium", "Closed — verified, no correction required"],

    ["RT-19",
     "APRA and several other source URLs were recorded from expected URL patterns rather than "
     "from a successful fetch.",
     "Do the registered URLs actually resolve? A source register whose links are dead is not an "
     "evidence base.",
     "Eleven of thirty-four URLs returned HTTP 404 on the first automated check — all nine APRA "
     "entries plus the ECB risk data aggregation guide and the MAS AI model risk information "
     "paper. Correct URLs were located on each official domain and substituted. All thirty-four "
     "now resolve, and the affected sources moved from secondary to primary verification.",
     "Source register URLs and verification labels; thirty-three of thirty-four sources are now "
     "verified from primary text.",
     "Automated fetch of every registered URL; re-run at any time through the check_source_urls "
     "tool on the accompanying MCP server.",
     "High", "Closed — correction incorporated"],

    ["RT-20",
     "BCBS stress testing principles and third-party principles were described as international "
     "principles without qualification.",
     "Does the BIS classify these as Standards, and do they carry their own status disclaimers?",
     "Neither is a Standard. The BIS classifies both as Guidelines, and the stress testing "
     "principles carry an express statement that they do not constitute Standards, for which the "
     "Committee expects full implementation. Both entries were requalified.",
     "Legal status matrix and source register entries for the two BCBS instruments.",
     "BCBS d450 introduction; BIS publication classification for d450 and d605.",
     "Medium", "Closed — correction incorporated"],

    ["RT-21",
     "The superseded OSFI E-23 (2017) was described as 'superseded by the 2027 guideline with "
     "effect from 1 May 2027'.",
     "Is there an express supersession clause, or is that an inference from the guidance library?",
     "No express supersession clause was located in either the 2027 guideline or its covering "
     "letter. The entry now states the relationship as OSFI presents it in its guidance library "
     "rather than quoting a provision that does not exist.",
     "Source register entry for the 2017 guideline.",
     "OSFI E-23 (2027) body and covering letter; OSFI guidance library.",
     "Low", "Closed — correction incorporated"],

    ["RT-22",
     "CPS 230 was recorded as commencing 1 July 2025.",
     "Is that the current instrument? A superseded commencement date would misstate the "
     "Australian baseline the whole assessment is measured against.",
     "The current CPS 230 determination was made on 23 April 2026 and commences 1 July 2026, "
     "revoking and replacing the 2023 determination under which CPS 230 first commenced on "
     "1 July 2025. The source register now records both.",
     "Source register and legal status matrix entry for CPS 230.",
     "APRA CPS 230 determination, 23 April 2026.",
     "Medium", "Closed — correction incorporated"],

    ["RT-23",
     "The APRA entry in the principles register listed instruments by name only, implying a "
     "loose mapping.",
     "Can APRA's distributed model governance obligations be located precisely, or is the claim "
     "that they are scattered itself unevidenced?",
     "They can. Paragraph-level anchors were read from the primary instruments — including "
     "APS 113 paragraph 27 on independent review, Attachment D paragraphs 103 to 109 on "
     "validation of internal estimates and paragraphs 67 to 68 on the use test, APG 113 "
     "Chapter 7, CPS 320 paragraphs 22 to 40, and SPS 530 paragraphs 30 to 35. The entry now "
     "carries 22 paragraph-level references, and independent verification confirmed that APRA "
     "has no model risk prudential standard and no enumerated model risk principles.",
     "Principles register; strengthens the evidential basis for the central premise of the "
     "package.",
     "APS 113, APG 113, CPS 220, CPS 230, CPS 320 and SPS 530 primary text.",
     "Medium", "Closed — verified, register strengthened"],

    ["RT-24",
     "The Australian instruments the standard sits alongside were recorded as 'current at the "
     "as-of date' without commencement dates.",
     "Which version of each is actually in force, and has any been remade recently? The "
     "Australian baseline is what the whole assessment is measured against, so a stale version "
     "would distort every score.",
     "Three of the nine had been remade in 2026 and the register did not say so. APS 113 — the "
     "instrument carrying Australia's strongest existing model governance requirements — was "
     "released in final form on 4 June 2026 and commenced 30 June 2026. CPS 320 was determined "
     "on 29 April 2026 and commenced 1 July 2026. CPS 230's current determination was made on "
     "23 April 2026 and commences 1 July 2026. Commencement dates were added for every APRA "
     "instrument, and SPS 515 is marked as not separately verified rather than asserted.",
     "Source register and legal status matrix; the gap assessment's Australian baseline is now "
     "anchored to identified versions rather than to 'current'.",
     "APRA standards pages and determinations for each instrument.",
     "High", "Closed — correction incorporated"],

    ["RT-25",
     "CPS 320 paragraph references were taken from the instrument's structure.",
     "Was the in-force text actually retrieved, or is the structure inferred from a landing page?",
     "The 1 July 2026 in-force PDF could not be downloaded from apra.gov.au — the link is "
     "rendered client-side and the legislation register record is a JavaScript application. "
     "Title, commencement, status, instrument reference, scope and section headings were "
     "confirmed from the APRA standards page; paragraph-level references come from the July 2019 "
     "text. The register now says so, and flags that they should be re-checked against the "
     "current version.",
     "Source register entry for CPS 320; the paragraph anchors in the principles register carry "
     "the same caveat.",
     "APRA standards page for CPS 320; July 2019 primary PDF.",
     "Medium", "Closed — limitation disclosed rather than concealed"],

    ["RT-26",
     "The standard opened at 'Objectives and key requirements' with no Authority, Application, "
     "Commencement or Adjustments and exclusions paragraphs.",
     "Every APRA prudential standard carries this front matter. Without an adjustments and "
     "exclusions paragraph there is no lawful route for APRA to vary a requirement for an "
     "individual entity, making the instrument more rigid than every standard it sits alongside. "
     "Without a transitional paragraph, requirements expressed as a bar on use would on "
     "commencement prohibit continued use of models entities already rely on.",
     "Paragraphs A1 to A6 were added: authority, application, commencement, transitional "
     "arrangements for models already in use, adjustments and exclusions, and interpretation. "
     "Each carries a note identifying what requires legal settlement.",
     "Six new mandatory paragraphs; the standard is now structurally complete as an instrument.",
     "CPS 230 paragraphs 1 to 11 as the structural precedent.",
     "High", "Closed — correction incorporated"],

    ["RT-27",
     "M04 required an entity to document and approve 'any exception to or reduction of the "
     "controls otherwise required' by the standard.",
     "The controls otherwise required are the mandatory paragraphs. As drafted, a proportionality "
     "clause purported to let an entity except itself from the instrument's own requirements at "
     "its own approval authority.",
     "M04 was split in substance: it now requires the entity to demonstrate that control intensity "
     "reflects the model's tier and that equivalent models are treated consistently, and confines "
     "the exception machinery to departures from the entity's own policies and standards. The "
     "guidance states plainly that only APRA may adjust or exclude a requirement, under A5.",
     "M04 redrafted; its guidance rewritten; the adjustment power now sits in A5 where it belongs.",
     "Internal analysis of the interaction between M04 and the mandatory paragraphs.",
     "High", "Closed — correction incorporated"],

    ["RT-28",
     "M22 required validation to address outcomes analysis comparing model outputs with "
     "corresponding actual outcomes, without qualification.",
     "For several model classes the standard expressly brings into scope — stress testing, "
     "scenario analysis, capital planning and forward-looking climate models — no corresponding "
     "actual outcome exists. The requirement was impossible to satisfy for them.",
     "M22 now requires outcomes analysis to the extent outcomes are observable and sufficient for "
     "the purpose, and requires alternative evidence of performance — benchmarking, sensitivity "
     "analysis and assessment of assumptions — where they are not.",
     "M22 redrafted; the validation intensity table in the guide realigned.",
     "M41 scope; BCBS stress testing principles 7 and 8.",
     "High", "Closed — correction incorporated"],

    ["RT-29",
     "M21 barred use of a model for a material purpose until independent validation was complete, "
     "with no exception path.",
     "The current US guidance expressly contemplates use before validation on urgent business "
     "need with compensating controls. An absolute bar with no exception and no transition would "
     "on commencement prohibit continued use of every insufficiently validated model in the "
     "industry.",
     "M21 now permits use before validation completes where there is an urgent business need, "
     "subject to approval at an authority commensurate with tier, compensating controls, informing "
     "users of the limitation and completing validation within a defined period. Paragraph A4 "
     "provides the transition for models already in use.",
     "M21 redrafted; A4 added.",
     "US interagency guidance 2026 §V.",
     "High", "Closed — correction incorporated"],

    ["RT-30",
     "M42 required every APRA-regulated entity to consider aggregate model risk in its internal "
     "capital assessment.",
     "RSE licensees have no internal capital assessment. The requirement was inapplicable to an "
     "entire regulated industry the standard purports to cover.",
     "M42 now refers to the internal capital adequacy assessment or, for an RSE licensee, to "
     "determining the operational risk financial requirement target amount.",
     "M42 redrafted sector-neutrally.",
     "Superannuation prudential framework; SPS 114 operational risk financial requirement.",
     "High", "Closed — correction incorporated"],

    ["RT-31",
     "M14 required a complete, accurate and current inventory in absolute terms; M32's "
     "compensating-control escape reached only the information limb; M33 had no transition for "
     "contracts already on foot; and M39 left the Appointed Actuary conflict to the guide.",
     "Absolute completeness is not demonstrable and not testable. A hosted vendor model cannot be "
     "subjected to the entity's own implementation controls. Existing contracts cannot be reopened "
     "on commencement. And for most insurers the Appointed Actuary sets the assumptions, so M09 "
     "and M21 would disqualify the very review CPS 320 requires.",
     "M14 now requires the inventory plus processes designed to ensure completeness. M32's escape "
     "extends to any obligation the entity cannot itself discharge for a third-party model, with a "
     "record of which are met that way. M33 applies to existing arrangements from the earlier of "
     "renewal, material variation or the end of the transition period. M39 resolves the actuarial "
     "interaction in the standard: CPS 320 review satisfies independent validation to the extent "
     "the reviewer did not develop the model or set its assumptions.",
     "Four requirements redrafted.",
     "CPS 230 transitional precedent for service provider arrangements; CPS 320.",
     "High", "Closed — correction incorporated"],

    ["RT-32",
     "The practice guide's validation intensity table prescribed 'at least annually' for the "
     "highest tier and 'every two to three years' for the second, while its own caption called the "
     "frequencies illustrative.",
     "A table that states an interval will be read as the expectation whatever the caption says. "
     "No comparator prescribes cross-industry validation frequencies, and the OCC has expressly "
     "confirmed that its guidance does not require annual validation.",
     "The frequency cells now state the drivers rather than intervals, and the caption and "
     "verification note explain why no interval is given.",
     "Chapter 8 of the practice guide.",
     "OCC Bulletin 2025-26; US interagency guidance 2026 §V; PRA SS1/23 Principle 4.5.",
     "Medium", "Closed — correction incorporated"],

    ["RT-33",
     "M45 created a notification obligation with no timeframe and no threshold beyond 'material', "
     "while the guidance beneath it told entities to use CPS 230 and CPS 234 timeframes.",
     "The requirement and its guidance said different things, and the requirement as drafted was "
     "not testable.",
     "M45 now states the timing expectation on the face of the requirement and ties it to the "
     "CPS 230 and CPS 234 timeframes where the event falls within those standards, resolving the "
     "inconsistency without creating a competing deadline.",
     "M45 redrafted.",
     "CPS 230; CPS 234.",
     "Medium", "Closed — correction incorporated"],

    ["RT-34",
     "M03 identified non-model quantitative tools by example only — spreadsheets, rules engines, "
     "allocation keys — with no stated criterion.",
     "Examples cannot draw a perimeter. A complex spreadsheet running a regression is a model; a "
     "complex spreadsheet applying documented arithmetic is not. The examples invited the wrong "
     "reading.",
     "M03 now states the criterion on the face of the requirement: a tool falls outside the model "
     "definition only where its output is fully determined by its inputs and documented rules, "
     "without estimation, statistical inference or an embedded assumption about an uncertain "
     "quantity.",
     "M03 redrafted.",
     "PRA SS1/23 Principle 1.1; US interagency guidance 2026 §II exclusions.",
     "Medium", "Closed — correction incorporated"],

    ["RT-35",
     "Annex A defined effective challenge as competence, standing and incentives, and defined a "
     "model with a three-component sentence that M02 does not contain.",
     "The Annex A definitions are operative. Leaving the rescinded 2011 formulation there meant "
     "the standard defined its own central concept two different ways in two places, and the "
     "definition that would be applied is the one in the Annex.",
     "The Annex A definition of effective challenge now matches M23 word for word. The "
     "three-component sentence was removed from the Annex A definition of a model, so it matches "
     "M02; the description survives in the practice guide where it is explanatory.",
     "Annex A of the standard; the glossary sheet.",
     "US interagency guidance 2026 §III; M23 and M02 as drafted.",
     "High", "Closed — correction incorporated"],

    ["RT-36",
     "Aggregate model risk and board reporting were attributed to PRA SS1/23 Principle 5 in four "
     "places.",
     "Principle 5 is 'Model risk mitigants' — post-model adjustments, restrictions on model use, "
     "and exceptions and escalations. It says nothing about aggregate model risk or board "
     "reporting, which sit under Principle 2.1.",
     "M13 and M42 now cite Principle 2.1. M42's rationale was rewritten to lead with the 2026 US "
     "guidance, which does expressly call for model risk to be assessed individually and in "
     "aggregate reflecting common assumptions, data and methodologies.",
     "M13 and M42 principle mappings and M42's rationale.",
     "PRA SS1/23 Principle 5 and Principle 2.1 primary text; US interagency guidance 2026 §III.",
     "High", "Closed — correction incorporated"],

    ["RT-37",
     "M39 cited GPS 320 and LPS 320; M36 cited a Basel Framework identifier that the alias map "
     "silently resolved to BCBS 239.",
     "GPS 320 and LPS 320 were replaced by CPS 320 in 2019 and no longer exist. BCBS 239 concerns "
     "risk data aggregation and says nothing about internal model approval or the use test. The "
     "integrity check passed because it treated aliases as registered sources, so three citations "
     "appeared in the requirements register that had no entry in the source register.",
     "All three citations were removed and the alias map was deleted entirely. Every source ID "
     "cited by a requirement now resolves to a registered entry, so nothing can be cited that "
     "does not appear in Annex E. The integrity check was tightened to match.",
     "M36 and M39 sources; SOURCE_ALIASES removed; verify_package strengthened.",
     "APRA instrument history for GPS/LPS 320; BCBS 239 subject matter.",
     "High", "Closed — correction incorporated"],

    ["RT-38",
     "The scoring rubric defined 5 and 4 as 'addressed in a binding instrument', while 25 of the "
     "33 benchmarks were set by supervisory guidance that is not binding anywhere.",
     "The rubric contradicted its own application. Read literally, no comparator could score above "
     "3 in most domains, which would have inverted every gap in the assessment.",
     "The rubric now scores the quality and specificity of the expectation irrespective of "
     "instrument type, and the enforceability dimension is stated to apply to Australia only — "
     "which is what the assessment was actually measuring.",
     "Scoring methodology sheet and the rubric shown in the workbook.",
     "Internal consistency analysis of the rubric against the benchmark assignments.",
     "High", "Closed — correction incorporated"],

    ["RT-39",
     "The superannuation domain was scored with a benchmark of 0 because no comparator addresses "
     "superannuation model risk.",
     "A zero benchmark floors the gap at zero, which returned a priority of 'Low' — published as "
     "meaning 'broadly comparable to international practice'. The domain with no international "
     "coverage at all was therefore reported as the least urgent.",
     "The domain is now benchmarked at 5 against the standard's own cross-industry objective, with "
     "the benchmark authority recorded as 'No comparator'. It now scores 4.38 weighted and ranks "
     "High, which reflects the position.",
     "Gap assessment and areas for improvement ranking.",
     "Scope statements of each comparator; the methodology's own treatment of absent benchmarks.",
     "High", "Closed — correction incorporated"],

    ["RT-40",
     "M09, M10 and M12 — capability and independence, the integrated framework, and policies and "
     "standards — were cited by no scoring domain.",
     "The framework obligation itself was unscored, so the assessment measured the parts of model "
     "risk management without measuring whether there is a framework at all.",
     "A 'MRM framework, policies and capability' domain was added covering all three, benchmarked "
     "against PRA Principle 2 and OSFI Principle 3.1. Every requirement is now covered by at least "
     "one domain.",
     "Gap assessment gains a 34th domain; the executive summary counts update automatically.",
     "Coverage check of scoring domains against the requirement register.",
     "Medium", "Closed — correction incorporated"],

    ["RT-41",
     "Annex C directed the highest tier where a model influences 'an employment outcome', and M01 "
     "extended enterprise scope to human resources models. M34 required entities to address the "
     "'potential for biased outcomes'.",
     "APRA is a prudential regulator. Employment decisions and unbounded bias obligations sit with "
     "other regulators and other legislation, and asserting them here would invite a scope "
     "objection that would distract from the prudential case.",
     "Employment outcomes were removed from the Annex C indicator and human resources from M01's "
     "guidance. M34's limb was recast in model-performance terms: systematic differences in model "
     "performance across segments of the population to which the model is applied.",
     "Annex C, M01 guidance and M34.",
     "Prudential remit analysis.",
     "High", "Closed — correction incorporated"],

    ["RT-42",
     "M45 imposed a standing duty to provide APRA with information 'on request', open as to scope, "
     "form and requester. M35 required entities to apply AI risk management arrangements that "
     "nothing obliged them to have. M42's RSE limb referred to the operational risk financial "
     "requirement without citing the standard that governs it.",
     "An open-ended information duty with no stated legal form is not how the other cross-industry "
     "standards are drafted. M35 assumed an instrument that does not exist. M42 pointed at a "
     "determination made under an uncited standard.",
     "M45 now applies where APRA requires information in writing, and its notification trigger "
     "covers amounts credited to or debited from customer and beneficiary accounts. M35 gains a "
     "limb for entities with no separate AI arrangements. M42 cites SPS 114, which is now "
     "registered as a source. An interpretation clause was added requiring every APRA power under "
     "the standard to be exercised in writing.",
     "M35, M42, M45, the Interpretation section and the source register.",
     "CPS 230 drafting form for information powers; SPS 114.",
     "High", "Closed — correction incorporated"],

    ["RT-43",
     "The FSB sound practices supplied twelve entries of the principles register, were cited in "
     "eight crosswalk cells and were the subject of a statement-ledger entry, but had no entry in "
     "the source register.",
     "A source relied on that heavily with no registered entry has no recorded status, date or "
     "URL, and a reader cannot check what it is or whether it binds anything.",
     "Registered as FSB-SP-2026 with its consultation status recorded — the FSB states expressly "
     "that the practices are not intended to establish an international standard. The integrity "
     "check now covers sources cited by the principles register and the crosswalk, not only those "
     "cited by requirements.",
     "Source register, legal status matrix and the integrity check.",
     "FSB consultation report.",
     "Medium", "Closed — correction incorporated"],

    ["RT-44",
     "Five source attribution lines in the practice guide used a status code, '[B where "
     "implemented]', that appears in neither the guide's legend nor Annex D.",
     "A reader cannot interpret a status code that is not defined, and the code implied a degree "
     "of bindingness that BIS guidelines do not have.",
     "The four BCBS instruments now carry [G], with the domestic-implementation qualification "
     "carried in the prose of the attribution line. BCBS 239's register status was corrected from "
     "'International standard' to BIS-classified Guidelines.",
     "Practice guide attribution lines; BCBS 239 source register entry.",
     "BIS publication classification for bcbs239, d450, d516 and d605.",
     "Medium", "Closed — correction incorporated"],

    ["RT-45",
     "Annex B opened 'An APRA-regulated entity's model inventory must record at least the "
     "following', in the guidance style.",
     "The build audit forbids bold text in a guidance paragraph, so the only statement making "
     "Annex B mandatory was rendered as explanatory text. On the standard's own reading rule, "
     "Annex B imposed nothing.",
     "M14 now requires the inventory to record at least the fields set out in Annex B, so the "
     "obligation sits in a bold mandatory paragraph. Annex B's opening line was reworded to point "
     "back at M14.",
     "M14 and Annex B.",
     "The standard's own interpretation rule that only bold paragraphs are mandatory.",
     "High", "Closed — correction incorporated"],

    ["RT-46",
     "Every governance obligation was expressed in terms of 'the Board'; private health insurance "
     "appeared nowhere despite being in the enabling authority; A4's transition reached only "
     "model-level obligations; and Annex A's bespoke definitions were not tied to CPS 001.",
     "A foreign ADI has no Australian Board, so those obligations were incapable of performance by "
     "a branch. A named industry with no coverage would not survive consultation. Entity-level "
     "obligations with no transition would all fall due on commencement. And bespoke definitions "
     "floating free of CPS 001 invite inconsistency with the rest of the framework.",
     "A6 now reads down 'the Board' for foreign ADIs and ties undefined terms to CPS 001. A4 was "
     "split into entity-level obligations from commencement and model-level obligations on a "
     "remediation plan. M39 now names private health insurers, deferred claims liabilities and "
     "risk equalisation, and cites HPS 110. Annex F gained items for foreign ADIs and for whether "
     "a simplified pathway for smaller entities is warranted.",
     "A4, A6, M39, Annex F and the source register.",
     "Cross-industry drafting practice in CPS 220, CPS 230 and CPS 234; the enabling authority in A1.",
     "High", "Closed — correction incorporated"],

    ["RT-47",
     "M03's carve-out excluded any tool whose output is fully determined by its inputs and "
     "documented rules.",
     "A unit price calculation is fully determined by its inputs. The carve-out would therefore "
     "have excluded the very models M02 and M40 were drafted to capture — the ones whose errors "
     "transfer value between members irreversibly.",
     "M03's test now turns on consequence as well as method: a tool is outside the definition only "
     "where it also does not determine a regulatory figure, a reported valuation or an amount "
     "attributable to a customer or beneficiary.",
     "M03; resolves a direct contradiction with M02 and M40.",
     "Internal consistency analysis across M02, M03 and M40.",
     "High", "Closed — correction incorporated"],

    ["RT-48",
     "No requirement addressed the outputs a failed model had already produced, and M31 conferred "
     "a power to suspend a model without requiring anything to fall back on. Group and offshore "
     "model governance was unaddressed.",
     "Remediating a finding is not the same as remediating its consequences: a model that "
     "mispriced units or understated a provision leaves balances and figures that need "
     "correcting. A power to suspend a model the entity has no alternative to is not usable. And "
     "for many Australian entities the model is built and validated by an offshore parent.",
     "M30 now requires the entity, on identifying a material error or failure, to determine its "
     "cause, assess whether the weakness affects other models, and address the effect on figures, "
     "balances and customer or beneficiary amounts already produced. M31 requires an identified "
     "alternative basis for highest-tier models. M08 requires the entity to satisfy itself about "
     "group-performed work and retain the ability to direct and challenge it.",
     "M08, M30 and M31.",
     "ECB guide on group-level model governance; OSFI E-23 lifecycle stages.",
     "High", "Closed — correction incorporated"],

    ["RT-49",
     "The crosswalk asserted that the BCBS does not address aggregate model risk.",
     "An asserted negative is a claim like any other. Adversarial review suggested the Basel "
     "Framework's prudent valuation guidance and Pillar 3 prudent valuation template may in fact "
     "require a model risk valuation adjustment and its public disclosure, which would make the "
     "negative wrong.",
     "The claim could not be resolved either way: the BIS Basel Framework chapter pages render "
     "their text client-side and could not be retrieved. Rather than keep an unverified negative "
     "or adopt an unverified positive, the cell now records the lead and its status. Ledger entry "
     "ST-17 marks it for resolution from the primary chapter before consultation.",
     "One crosswalk cell; one statement-ledger entry. No requirement relies on the point.",
     "BIS Basel Framework CAP50 chapter listing (title confirmed, text not retrievable).",
     "Medium", "Open — unresolved, disclosed"],

    ["RT-50",
     "The standard applied all requirements to every model, with proportionality operating only on "
     "control intensity. Annex F recorded a de minimis exception as an open policy question.",
     "Without a de minimis mechanism, a model that could not matter attracts the same lifecycle as "
     "one that determines regulatory capital. Every comparator relieves low-consequence models of "
     "the full lifecycle, and the 2026 US guidance says so expressly: where models are deemed "
     "immaterial, model risk management may consist of identifying them and monitoring the "
     "conditions under which their use may become material.",
     "A de minimis exception was added at model level as M05. A model determined to be de minimis "
     "attracts only identification, inventory, ownership, classification and reassessment. Three "
     "anti-abuse limbs were drafted with it: prohibited classes that can never be de minimis "
     "(regulatory capital, provisions, insurance liabilities, reported valuations, unit prices and "
     "other customer or beneficiary amounts, and models supporting a critical operation); an "
     "aggregate test, because a population of individually immaterial models sharing an assumption "
     "may not be immaterial together; and a bar on disaggregating a model to bring its components "
     "under the threshold. The exception deliberately does not release a model from the inventory, "
     "since an entity that has removed a model cannot demonstrate the determination was ever made.",
     "New requirement M05; six new guidance paragraphs; a new Annex A definition; a new crosswalk "
     "topic; the proportionality scoring domain updated. Marked as a policy choice requiring "
     "consultation and cost-benefit testing.",
     "US interagency guidance 2026 §III; OSFI E-23 (2027) Principles 2.1 and 2.3; PRA SS1/23 "
     "Principle 1.3.",
     "High", "Closed — requirement added"],

    ["RT-51",
     "Inserting M05 into Part A shifted every subsequent requirement identifier.",
     "An audit trail that references identifiers is only useful if those references still resolve. "
     "Leaving the earlier entries pointing at pre-insertion numbers would have silently "
     "misdirected every correction recorded before this one.",
     "All identifiers from the former M05 onward were resequenced upward by one across the "
     "requirement register, the practice guide, the scoring model, the crosswalk, this audit "
     "trail and the statement ledger. The concordance is simply: M01 to M04 unchanged; former Mnn "
     "for nn of 05 or above is now M(nn+1). References in this audit trail and the ledger have "
     "been updated to current identifiers, so an entry describing a correction to the former M13 "
     "now reads M14.",
     "Every artefact. The integrity check confirms that no guidance paragraph, scoring domain or "
     "cross-reference points at an identifier that does not exist.",
     "Automated resequencing with verification by the package integrity check.",
     "Medium", "Closed — resequenced and verified"],

    ["RT-52",
     "Full adversarial verification of the five red-team lenses returned 57 findings, of which 31 "
     "were refuted outright and 24 were reduced to a smaller residual.",
     "Most findings were raised against snapshots of the package taken before earlier corrections "
     "landed. Verifiers repeatedly established that a quoted defect no longer existed, and that "
     "the proposed fix would either be a no-op or would reopen a closed correction. Acting on the "
     "raw findings would have undone RT-27, RT-31, RT-33, RT-34, RT-42, RT-46 and RT-47.",
     "Only the verified residuals were applied. M23's explanatory paragraph stated a different "
     "three-limb test from its own bold paragraph and reintroduced incentives as a co-equal limb; "
     "it now tracks the requirement and demotes incentives to a practical condition. M22 now "
     "prints the validation components in the order the current US guidance uses. M36's approval "
     "and use-test limbs are now expressly conditional on the applicable capital standard. Annex "
     "A's model definition carried a sentence M02 does not contain, and 'material model' used a "
     "non-negligible-effect trigger where 'material purpose' used a material-effect one; both are "
     "aligned. Three stale attributions in the practice guide were corrected: PRA Principle 5 for "
     "aggregate model risk, the exception paragraph reading as though it could except a "
     "requirement, and the superseded bias phrasing in the AI chapter.",
     "M22, M23, M36, two Annex A definitions and three practice guide paragraphs; CPS 001 and "
     "SPS 114 registered; two Annex F items extended.",
     "PRA SS1/23 Principles 2.1 and 5; US interagency guidance 2026 §§III and V; the package's own "
     "closed audit entries.",
     "High", "Closed — verified residuals applied"],

    ["RT-53",
     "Two findings survived verification intact rather than being reduced.",
     "The Annex A model definition retained a three-component sentence that the operative "
     "definition in M02 does not contain, so the defined term and the requirement said different "
     "things; and M36 imposed an unconditional obligation to obtain APRA approval for model "
     "change and to use the model in internal risk management, where those duties arise only "
     "where the applicable capital standard imposes them.",
     "Both were applied as verified. The definition now matches M02 word for word, with the "
     "three-component description retained in the practice guide where it is explanatory. M36's "
     "limbs are now conditional on the applicable prudential standard.",
     "Annex A and M36.",
     "Independent verification at the locus; APS 113 and the ECB internal models framework.",
     "High", "Closed — correction incorporated"],

    ["RT-54",
     "M37 and M38 both brought expected credit loss models into the scope of the Prudential "
     "Standard. M37 applied it to models used 'to determine expected credit losses'; M38 applied "
     "it to models used 'to assess and measure expected credit losses and to determine "
     "provisions'.",
     "Two mandatory paragraphs scoping the same models is a drafting defect. An entity cannot "
     "tell which paragraph governs, and a duplicated scoping obligation invites the argument that "
     "the two differ in some intended way.",
     "The expected credit loss limb was removed from M37, leaving M38 as the single scoping "
     "paragraph for expected credit loss and provisioning models. M37 now governs valuation and "
     "financial and regulatory reporting models, with guidance signposting paragraph 38 and "
     "confirming that both apply where one model serves both purposes.",
     "M37 and M38.",
     "Both requirement texts read at the locus.",
     "Medium", "Closed — correction incorporated"],

    ["RT-55",
     "M45's independent review limb was drafted as applying where APRA requires a review of 'an "
     "aspect of its model risk management, including its provisioning practices'.",
     "Does the APS 220 Special purpose engagements provision, on which the limb rests, bear that "
     "weight? Its verbatim words extend to 'all or a particular aspect of the ADI's credit risk "
     "management, including provisioning practices'.",
     "It does not. The drafting substituted model risk management for credit risk management as "
     "the genus, converting a credit risk power into a model risk power, and did so in a "
     "cross-industry instrument when APS 220 applies to ADIs only. M45 now states an entity's "
     "obligation to support a review where the power is conferred by another instrument, without "
     "purporting to confer the power itself, and preserves the APS 220 formulation accurately as "
     "a separate limb. Guidance states expressly that the APS 220 provision does not reach model "
     "risk management at large and supplies no basis at all for an insurer or RSE licensee.",
     "M45 and its guidance; a new Annex F entry on independent review and special purpose "
     "engagements.",
     "APS 220 Special purpose engagements, verbatim; the drafting precedent set by RT-42, that "
     "the package must not assume a power no cited instrument supplies.",
     "High", "Closed — correction incorporated"],

    ["RT-56",
     "The practice guide stated that where this Prudential Standard and APS 220 overlap, 'APS 220 "
     "prevails as the more specific instrument'.",
     "Is that precedence rule established anywhere, and what would it do if this Prudential "
     "Standard required more of a model than APS 220 does?",
     "It is established nowhere. The standard's Interpretation section creates no such rule, and "
     "as drafted the sentence would read down this Prudential Standard wherever it imposed the "
     "higher obligation — the opposite of the intent. The guidance now states that the two are "
     "cumulative, that neither reads down the other, and that the higher obligation is the one to "
     "meet, with the formal interaction recorded in Annex F for settlement.",
     "The expected credit loss chapter of the guide; a new Annex F entry on interaction with "
     "APS 220.",
     "The Interpretation section of the standard; APS 220.",
     "Medium", "Closed — correction incorporated"],

    ["RT-57",
     "Annex G set out twelve focus areas for a review of expected credit loss models.",
     "Would the annex let a reviewer appointed under a special purpose engagement form a view on "
     "whether the reported provision is supportable?",
     "Not on the measurement itself. The annex addressed framework, governance, staging, "
     "segmentation, scenarios, overlays and data, but omitted the mechanics where expected credit "
     "loss estimates actually fail: the component models and their validation, the lifetime "
     "probability of default term structure, loss given default and collateral realisation, "
     "exposure at default and credit conversion factors for undrawn commitments, behavioural life "
     "and prepayment, discounting, back-testing of the estimate against realised losses, "
     "individually assessed exposures, the interaction of hardship, forbearance and write-off "
     "with measurement, and externally sourced components. Four new areas were added and the "
     "sequence reordered to follow the order in which an engagement would work through them.",
     "Annex G, which gained four focus areas.",
     "Assessed against the measurement requirements of AASB 9 and the matters BCBS d350 and "
     "APRA's October 2023 letter direct to validation and credit judgement.",
     "High", "Closed — correction incorporated"],

    ["RT-58",
     "Annex F stated that \'CPS 240\' is a drafting placeholder only, after the package had been "
     "renumbered to CPS XXXX.",
     "Did the renumbering reach every occurrence?",
     "All but one. The string was split across two source lines, so it survived a search for the "
     "whole phrase and remained in the one annex whose purpose is to record that the number is a "
     "placeholder. Corrected, and the check was re-run over the assembled content of every module "
     "rather than over the source lines, which is the only form of the check that would have "
     "caught it.",
     "Annex F.",
     "Whole-package scan of assembled string values, which now reports no stale instrument "
     "numbers.",
     "Low", "Closed — correction incorporated"],

    ["RT-59",
     "The RT-56 correction was applied to the practice guide but not to the standard. M38's "
     "guidance still read that 'where the two overlap the more specific requirement in APS 220 "
     "prevails', while the guide had been changed to say the two are cumulative.",
     "Found on re-executing the pipeline after RT-56. Two questions: did the correction reach "
     "every locus, and is the precedence formulation right anywhere it appears?",
     "It had not, and it was not. The two documents contradicted each other, and the formulation "
     "was actively wrong for M38 — it would let an ADI satisfy the bare APS 220 validation "
     "obligation and disregard the validation discipline M38 exists to supply. M38 now carries "
     "the cumulative formulation. M36's parallel deference to the capital standards was kept, "
     "because APS 113 contains a complete and more demanding model regime where APS 220 contains "
     "a bare obligation, but it was made precise: the capital standard governs approval, change "
     "and conditions of use, and does not relieve the entity of the framework obligations it does "
     "not address. The valuation scoring action was also still referring to expected credit loss "
     "models after RT-54 moved them to M38.",
     "M36, M38, and two recommended actions in the scoring model.",
     "Detected by rebuilding from source and reading the assembled output rather than the diff.",
     "High", "Closed — correction incorporated"],

    ["RT-60",
     "The package asserted that no special purpose engagement power reached an insurer or an RSE "
     "licensee, and that APS 220 was the only instrument conferring one. M45, its guidance, "
     "Annex F, Annex G and the practice guide were all drafted on that footing.",
     "Raised by an independent red-team lens as an asserted negative from an unexamined field — "
     "the same defect class as RT-42 — and then put directly by the reviewer, who asked whether "
     "APS 220 or APS 310 allows expected credit loss models to be looked at.",
     "The assertion was wrong. A special purpose engagement power exists in every industry this "
     "Prudential Standard covers, in the Audit and Related Matters standards: APS 310 for ADIs "
     "(operations, prudential reporting, risk management systems or financial position), GPS 310 "
     "for general insurers, LPS 310 for life companies and HPS 310 for private health insurers "
     "(operations, risk management or financial affairs), and SPS 310 for RSE licensees (business "
     "operations, compliance with prudential requirements or the risk management framework). Each "
     "was read from the primary instrument and each is in force. Because they reach risk "
     "management rather than credit risk management, they are a better fit for a model risk "
     "review than APS 220, which remains the narrower ADI-only basis for the credit risk and "
     "provisioning aspects. M45 now rests on the 310 standards with APS 220 as a second basis; "
     "Annex F's question changes from whether to confer a power to how M45 interacts with the "
     "powers that exist; Annex G gains a table of the provisions; and the guide chapter and "
     "scoring action were rewritten.",
     "M45 and its guidance, two Annex F entries, the Annex G callout and a new table, the guide "
     "chapter, the ECL scoring domain, and five new source register entries.",
     "APS 310, GPS 310, LPS 310, HPS 310 and SPS 310 read from apra.gov.au on 25 July 2026.",
     "High", "Closed — correction incorporated"],

    ["RT-61",
     "M45's limb required access to whatever \'the review requires\', and described the engagement "
     "as one APRA may \'commission\'.",
     "Independent lens: who fixes the scope of the obligation, and who appoints and pays?",
     "Both were wrong. The extent of a binding obligation was left to a privately appointed "
     "reviewer rather than to the matters APRA specifies; the limb now reads \'reasonably required "
     "for the matters APRA has specified\'. And under every one of these provisions APRA requires "
     "the entity to appoint and the entity bears the cost, so \'commission\' — the ordinary word "
     "for engaging and paying a reviewer — told entities the opposite of what the provisions do. "
     "Corrected in the Annex G callout, the guide and the scoring action. The limb was also "
     "conditioned on \'a prudential standard\', which on its face included this one, making the "
     "paragraph arguably its own enabling provision; it now reads \'another prudential standard\'.",
     "M45; the Annex G callout; the guide chapter; the ECL scoring domain.",
     "The verbatim provisions; the drafting principle applied at RT-55.",
     "High", "Closed — correction incorporated"],

    ["RT-62",
     "The Annex G callout and M45's guidance said a review of the whole of Annex G was the kind of "
     "engagement the APS 220 provision contemplates.",
     "Independent lens: RT-55 narrowed M45 to respect the APS 220 genus, and RT-57 enlarged Annex "
     "G in the same revision, but nobody re-tested the enlarged Annex against the narrowed genus.",
     "The over-claim had survived at a different locus, and in the standard rather than the guide. "
     "The focus areas on model risk framework coverage, on third-party and vendor components and "
     "on interaction with regulatory capital and reporting are none of them credit risk "
     "management. With APS 310 now "
     "identified the problem largely dissolves, because the 310 standards reach risk management "
     "generally; the callout and the guide now attribute the credit risk and provisioning areas "
     "to APS 220 and the remainder to APS 310. Recorded because the pattern — a correction that "
     "is right where it is applied and does not travel — is the same one as RT-59 and is now the "
     "package's most frequent defect.",
     "The Annex G callout; M45's guidance; the guide chapter.",
     "Independent red-team lens on the special purpose engagement power.",
     "High", "Closed — correction incorporated"],

    ["RT-63",
     "The pre-existing Annex F entry \'APRA powers\' listed independent review among the powers to "
     "be settled, and the new entry on special purpose engagements owned the same decision.",
     "Independent lens: two entries in one settlement register owning one decision, neither "
     "cross-referencing the other.",
     "Annex F is a work allocation to APRA Legal and the Office of Parliamentary Counsel, and "
     "duplicated ownership invites either duplicated work or divergent resolution. Independent "
     "review was struck from the general powers entry, which now points to the dedicated entry.",
     "Two Annex F entries.",
     "Independent red-team lens; the same reasoning applied at RT-54.",
     "Low", "Closed — correction incorporated"],

    ["RT-64",
     "The two \'Capturing economic uncertainty\' paragraphs in the expected credit loss chapter of "
     "the practice guide were tagged to requirements M38 and M40.",
     "Independent lens: inserting M38 renumbered the requirements above it, so does M40 still mean "
     "what the chapter was drafted against?",
     "It does not. Before the insertion M40 was stress testing; after it, M40 is \'Models used by "
     "RSE licensees\' and stress testing became M41. The guide chapter was drafted against the "
     "pre-insertion numbering, so the superannuation requirement\'s guidance pointer reached two "
     "paragraphs about expected credit loss sensitivity analysis and internal capital adequacy "
     "assessment, and the stress testing requirement lost them. Both tags corrected to M41. "
     "M40 now resolves to paragraphs 116 to 117 and M41 to 118 to 119 and 126 to 127. "
     "This class of error passes every existing check: both identifiers exist, so the "
     "cross-reference verification confirms the pointer resolves while it points at the wrong "
     "requirement. It was found only by an independent reader asking what the identifier now "
     "means.",
     "Two guide paragraphs; the guidance cross-references under M40 and M41 in the standard.",
     "content_guide.numbered() before and after; the diff of the commit that introduced M38.",
     "High", "Closed — correction incorporated"],

    ["RT-65",
     "The Annex G focus area on staging tested the indicators used to transfer exposures into "
     "Stage 2 and the "
     "sensitivity of the provision to staging thresholds.",
     "Independent lens: does the Annex ever test the measurement consequence of the transfer, as "
     "distinct from its trigger?",
     "It did not. A search of the whole package returned no occurrence of \'12-month\', "
     "\'credit-impaired\', \'definition of default\' or \'cure\'. The point of a Stage 2 transfer is "
     "that it changes the measurement basis from twelve-month to lifetime expected credit losses, "
     "and a review that tested only the trigger would not reach the consequence that makes the "
     "trigger matter. That area was retitled and now tests whether the staging outcome selects the "
     "correct measurement basis through all three stages, and whether the definitions of default "
     "and cure are consistent with those used in credit risk management and regulatory capital. "
     "Evidence now includes a stage reconciliation with movements explained.",
     "The Annex G focus area on staging, significant increase in credit risk and measurement basis.",
     "AASB 9 measurement requirements; absence confirmed by search across all content modules.",
     "High", "Closed — correction incorporated"],

    ["RT-66",
     "The Annex G focus area on outcomes analysis asked whether the entity compares expected "
     "credit losses previously "
     "recognised against losses actually realised.",
     "Independent lens: an AASB 9 estimate is a probability-weighted expectation across scenarios, "
     "so is single-period comparison against outcomes a coherent test at all?",
     "Partly. Verification rejected the wider claim — the area asks for bias identified across "
     "periods, not single-period falsification — but confirmed a real defect inside it: the area "
     "did not require the comparison to be made on a matched horizon, and a lifetime estimate "
     "compared against one year of write-offs is not a test of anything. The area now requires "
     "twelve-month estimates to be compared against the following twelve months and lifetime "
     "estimates only over multi-period cohorts, states expressly that a single period falsifies "
     "nothing, and adds comparison of realised macroeconomic conditions against the scenario set.",
     "The Annex G focus area on outcomes analysis and back-testing of the estimate.",
     "Adversarial verification of an overstated finding, which reduced it to the part that held.",
     "Medium", "Closed — correction incorporated"],

    ["RT-67",
     "Annex G never established the perimeter of the review.",
     "Independent lens: could a reviewer conclude on whether the reported provision is "
     "supportable without first knowing what is inside the estimate? \'Level 2\', \'subsidiar\' and "
     "\'solo\' returned no hit in any focus area.",
     "No. A new area, Perimeter and completeness of coverage, was added second, testing whether "
     "every portfolio contributing to the provision is measured by a model within the framework, "
     "whether every entity is identified including branches, offshore operations and run-off "
     "books, whether any material portfolio is measured on a non-modelled or legacy basis, and "
     "whether methodology differences across the group are deliberate. Evidence includes a "
     "reconciliation from the reported provision to the models producing it, with any residual "
     "measured outside a model quantified.",
     "Annex G.",
     "Independent red-team lens on review utility; absence confirmed by search.",
     "High", "Closed — correction incorporated"],

    ["RT-68",
     "Annex G tested the models but never the plumbing that runs them.",
     "Independent lens: is the model that produced the reported number the model that was "
     "validated? A keyword scan returned no hit for implementation, production, ledger, "
     "reconciliation, version or spreadsheet outside unrelated contexts.",
     "A validated methodology and a correct reported number are different things, and the gap "
     "between them is where end-user computing, unapproved versions and manual journals sit. A "
     "new area, Implementation and production controls, was added after Aggregate effect of "
     "adjustments, testing version control, implementation verification against the approved "
     "model, end-user computing in the production path, authorisation of post-calculation manual "
     "journals, and reconciliation from engine output to general ledger to reported provision. "
     "It seats there because the preceding area requires the Board to see modelled result, "
     "adjustments and final provision as three figures, and this is the test that the plumbing "
     "producing them holds.",
     "Annex G, now eighteen focus areas.",
     "Independent red-team lens on review utility; M25 and M29 of this Prudential Standard.",
     "High", "Closed — correction incorporated"],

    ["RT-69",
     "The expected credit loss scoring domain was scored au=(4, 4, 5, 4) — cell for cell "
     "identical to the regulatory capital domain — and banded Low.",
     "Independent lens: Specificity 4 means clear expectations with minor gaps, but the domain\'s "
     "own gap text says the validation obligation exists without a framework defining what "
     "validation consists of, who performs it and what follows a finding. Is that a minor gap? "
     "And can a domain band Low while the change proposes a new mandatory paragraph for it?",
     "Verification confirmed the narrower point and rejected the wider one. Specificity was "
     "reduced from 4 to 3; Coverage 4, Enforceability 5 and Alignment 4 stand, because the "
     "near-verbatim transposition of BCBS d350 Principle 5 into a binding standard supports "
     "them. Specificity 2 was expressly rejected as describing a general obligation not specific "
     "to model risk, which is the opposite of what APS 220 does, and the overlays domain was not "
     "rescored because its Specificity 1 measures a different deficiency. The domain now scores "
     "4.00 against a benchmark of 5, weighted gap 1.50, band Medium, which is consistent with an "
     "action proposing a new mandatory paragraph, a guide chapter and an annex. Note that 1.50 "
     "sits exactly on the Medium threshold, which is user-editable in the workbook.",
     "The expected credit loss scoring domain.",
     "The rubric in content_scoring.py read against the domain\'s own gap narrative and against "
     "how comparable domains are scored.",
     "Medium", "Closed — correction incorporated"],

    ["RT-70",
     "The audit trail cited Annex G areas by number — \'sixteen focus areas\', \'Focus area 1 ... "
     "area 13 ... area 15\', \'focus area 5\', \'focus area 4\'.",
     "Raised by the lens proposing two new areas: inserting them would renumber everything below "
     "and silently invalidate every one of those citations.",
     "This is the RT-64 defect class — a pointer that still resolves while pointing at the wrong "
     "thing — and it would have been introduced by the very change that fixed two other defects. "
     "Rather than renumber the references, every numeric citation of an Annex G area in the audit "
     "trail was replaced with the area\'s name, so no future insertion can invalidate them. "
     "Recorded separately because the structural fix, not the individual corrections, is the "
     "point: this is the third appearance of the class after RT-59, RT-62 and RT-64.",
     "Four entries in the red-team audit trail.",
     "Anticipated by the lens before the change was made; verified by search for residual "
     "numeric references, which returns none.",
     "Medium", "Closed — correction incorporated"],

    ["RT-18",
     "The Comptroller's Handbook model risk management booklet was cited as a source.",
     "Is it retrievable, and is it current?",
     "It was rescinded on 17 April 2026 and its PDF no longer resolves on an official domain. Its "
     "existence, issuance and rescission are verified from two reachable OCC sources, but nothing "
     "about its contents is asserted anywhere in this package.",
     "Source register entry retained with a verification caveat; no requirement relies on it.",
     "OCC Bulletin 2021-39; OCC Bulletin 2026-13 rescission list.",
     "Low", "Closed — correction incorporated"],
]


# Bound at import time so the workbook builder can consume it directly.
from content_requirements import REQUIREMENTS as _REQS  # noqa: E402

REQUIREMENT_TEST_ROWS = build_requirement_test(_REQS)


# --------------------------------------------------------------------------- #
# Annex G — focus areas for an APRA review of expected credit loss models
#
# Drawn from APRA's October 2023 letter on provisioning practices, the expected
# credit loss provisions of APS 220, and BCBS d350, which APG 220 directs ADIs to
# have regard to. Each row states what the area is, what a review would test, and
# what evidence would ordinarily demonstrate it.
# --------------------------------------------------------------------------- #

ECL_REVIEW_FOCUS = [
    ["1. Model risk framework coverage",
     "Whether expected credit loss models are within the entity's model risk framework in "
     "substance and not only on the register — tiered, owned, validated and monitored on the "
     "same basis as other models of equivalent consequence.",
     "Inventory entries with tier and owner; validation status and dates; evidence that ECL "
     "models are not carved out of framework reporting."],

    ["2. Perimeter and completeness of coverage",
     "Whether every portfolio whose exposures contribute to the reported provision is measured "
     "by a model within the framework, and whether every entity whose exposures are included "
     "is identified — including branches, offshore operations and recently acquired or run-off "
     "books. Whether any material portfolio is measured on a non-modelled, legacy or locally "
     "developed basis, and whether methodology differences between entities in the group are "
     "deliberate and justified rather than unreconciled.",
     "A reconciliation from the reported provision to the models that produce it, with any "
     "residual measured outside a model identified and quantified; the list of entities and "
     "portfolios in scope at Level 1 and Level 2; the basis on which offshore operations apply "
     "the group methodology or a local one, and the approval of any departure."],

    ["3. Validation of ECL models",
     "Whether validation addresses conceptual soundness, outcomes analysis and ongoing "
     "monitoring, is performed by persons independent of development and of the provisioning "
     "outcome, and reaches an explicit conclusion on fitness for use.",
     "Validation reports with conclusions and conditions; independence assessment; findings "
     "register with severity, owner and closure evidence."],

    ["4. Component models and measurement mechanics",
     "Whether each component of the estimate is validated in its own right rather than only "
     "the consolidated output — the probability of default and its lifetime term structure, "
     "loss given default including collateral valuation and realisation assumptions, and "
     "exposure at default including credit conversion factors for undrawn and "
     "off-balance-sheet commitments. Whether the behavioural life and prepayment assumptions "
     "used for revolving and open-ended facilities are supportable, and whether discounting is "
     "applied at the correct rate over the correct horizon.",
     "Component-level validation reports; the derivation of the lifetime PD term structure; "
     "collateral haircut and time-to-realisation evidence; credit conversion factor "
     "calibration; behavioural life studies; the discounting methodology and its "
     "reconciliation to the effective interest rate."],

    ["5. Outcomes analysis and back-testing of the estimate",
     "Whether the entity compares expected credit losses previously recognised against losses "
     "actually realised on a like-for-like horizon — twelve-month estimates against the "
     "following twelve months, and lifetime estimates only over multi-period cohorts — at a "
     "granularity that can identify bias, and whether persistent over- or under-estimation has "
     "been acted upon rather than observed. An expected credit loss estimate is a "
     "probability-weighted expectation across scenarios, so a single period's outcome "
     "falsifies nothing on its own; what a review looks for is bias that persists once the "
     "horizon is matched.",
     "Back-testing of ECL against realised write-offs and recoveries by portfolio and vintage, "
     "with the estimation horizon stated; measures of bias and their trend; comparison of "
     "realised macroeconomic conditions against the scenario set used; the entity's response "
     "where bias was identified."],

    ["6. Staging, significant increase in credit risk and measurement basis",
     "Whether the indicators used to transfer exposures into Stage 2 are validated as models "
     "in their own right, whether they operate for vulnerable sectors, and what the provision "
     "would be under alternative reasonable staging criteria. Whether the staging outcome "
     "selects the correct measurement basis — twelve-month expected credit losses before a "
     "significant increase in credit risk, lifetime losses after it, and lifetime losses with "
     "interest revenue on the net carrying amount once an exposure is credit-impaired — since "
     "the transfer changes what is measured and not only how much. Whether the definitions of "
     "default and of cure are consistent with those used in credit risk management and in "
     "regulatory capital.",
     "Staging criteria and their validation; transfer volumes and triggers; sector-level "
     "staging outcomes; sensitivity of the provision to staging thresholds; reconciliation of "
     "exposures and provisions by stage, with movements between stages explained; the default "
     "and cure definitions and evidence they are applied consistently."],

    ["7. Segmentation and collective assessment",
     "Whether segmentation is granular enough for the portfolio's risk profile, whether "
     "collective assessment groupings share genuine credit risk characteristics, and whether "
     "emerging sectoral risk is identified systematically rather than manually.",
     "Segmentation design and review; grouping rationale; systematic identification processes "
     "for vulnerable sectors; evidence sectoral risk reaches loss estimates."],

    ["8. Individually assessed exposures and account treatments",
     "Whether individually assessed provisions are supported by documented cash flow scenarios "
     "and probability weights rather than a single view, whether the boundary between "
     "individual and collective assessment is applied consistently, and whether hardship, "
     "forbearance, restructuring and write-off policies interact correctly with the "
     "measurement of expected credit losses rather than masking deterioration.",
     "Individual assessment files with scenarios, weights and approvals; the individual versus "
     "collective boundary and its application; hardship and forbearance flags and their effect "
     "on staging and measurement; write-off policy and its timing."],

    ["9. Forward-looking information and scenarios",
     "Whether macroeconomic scenarios, their weights and the process for setting them are "
     "governed, documented and challenged; and whether the scenario set remains reasonable and "
     "supportable in current conditions.",
     "Scenario governance papers; weighting rationale and approvals; challenge records; "
     "back-testing of prior scenario judgements."],

    ["10. Sensitivity analysis",
     "Whether comprehensive sensitivity analysis is performed regularly and timely across "
     "portfolios and segments, and whether its results reach the Board in a form that supports "
     "a provisioning decision.",
     "Sensitivity analysis by segment, industry and geography; frequency evidence; the "
     "reporting in which results were presented; linkage to ICAAP and risk appetite review."],

    ["11. Judgement-based adjustments and overlays",
     "Whether the basis, quantification, approval, duration and removal conditions of each "
     "overlay are documented; whether overlays are monitored; and whether persistent "
     "same-direction adjustment has triggered redevelopment rather than repetition.",
     "Overlay register with quantification and approver; period-on-period movement and "
     "direction; supporting analysis; senior management oversight records; redevelopment "
     "plans."],

    ["12. Aggregate effect of adjustments",
     "Whether the entity reports the aggregate size and direction of overlays against the "
     "modelled result, so the Board can see how much of the provision is model output and how "
     "much is judgement.",
     "Board and committee reporting showing modelled result, adjustments and final provision "
     "as separate figures over time."],

    ["13. Implementation and production controls",
     "Whether the model that produced the reported number is the model that was validated — "
     "that the calculation engine reproduces the approved methodology, that the version in "
     "production is the version approved, and that changes since the last validation have been "
     "assessed. What end-user computing sits in the production run, how post-calculation "
     "manual journals are authorised and controlled, and whether the engine output reconciles "
     "to the general ledger and to the provision as reported.",
     "Version control and release records for the production engine; implementation "
     "verification against the approved model; the inventory of spreadsheets and other "
     "end-user computing in the production path, with their controls; the manual journal log "
     "with approvals; the reconciliation from engine output to general ledger to reported "
     "provision."],

    ["14. Data",
     "Whether the data used to develop, calibrate and run ECL models is appropriate, complete "
     "and traceable to source, and whether known data limitations are the reason for overlays "
     "that could instead be resolved.",
     "Data lineage; quality metrics; documented limitations; the link between identified data "
     "gaps and adjustments made in their place."],

    ["15. Third-party and vendor components",
     "Whether externally sourced models, scores, macroeconomic forecasts or calibration data "
     "used in the estimate are understood, validated and monitored by the entity itself, and "
     "whether the entity could continue to measure expected credit losses if the provider "
     "withdrew.",
     "Vendor model documentation and the entity's own validation of it; the basis on which "
     "external forecasts are selected and challenged; contractual access to methodology and "
     "data; substitution arrangements."],

    ["16. Governance, accountability and reporting",
     "Whether accountability for the provision is clear, whether the Board receives "
     "information sufficient to challenge it, and whether the entity's own committees have "
     "exercised that challenge.",
     "Accountability map; Board and committee papers and minutes showing challenge; escalation "
     "of model performance issues."],

    ["17. Interaction with regulatory capital and reporting",
     "Whether provisioning outcomes flow correctly into regulatory capital and prudential "
     "reporting, and whether any prescribed provisioning requirement is correctly applied.",
     "Reconciliation between accounting provisions and regulatory treatment; reporting "
     "controls; evidence of correct classification of exposures."],

    ["18. Remediation and responsiveness",
     "Whether previously identified weaknesses in ECL models have been remediated, and whether "
     "the entity has acted on APRA's published observations on provisioning practice.",
     "Findings closure evidence; internal audit coverage; the entity's own assessment against "
     "APRA's October 2023 observations."],
]

# The Special purpose engagements provision, quoted verbatim from APS 220.
APS220_SPECIAL_PURPOSE = (
    "APRA may require an ADI to appoint an independent party to review and provide a report to "
    "APRA on all or a particular aspect of the ADI's credit risk management, including "
    "provisioning practices. APRA may, however, request such a report without prior consultation "
    "with an ADI. APRA may set the terms of the review and at the ADI's expense."
)

# The expected credit loss provisions of APS 220, quoted verbatim.
APS220_ECL = [
    "An ADI must adopt, document and adhere to sound methodologies that address policies, "
    "processes and controls for assessing and measuring credit losses on all exposures. The "
    "measurement of provisions must build on robust methodologies and result in the appropriate "
    "and timely recognition of expected credit losses in accordance with Australian Accounting "
    "Standards.",
    "An ADI's aggregate amount of provisions must be adequate and consistent with the objectives "
    "of Australian Accounting Standards.",
    "An ADI must have sound policies and processes in place to appropriately validate models used "
    "to assess and measure expected credit losses.",
    "An ADI must use experienced credit judgement, particularly in the robust consideration of "
    "reasonable and supportable forward-looking information, including macroeconomic factors, in "
    "its assessment and measurement of expected credit losses.",
    "An ADI must have an appropriate credit risk assessment and measurement process that provides "
    "it with a sound basis for common systems, tools and data to assess credit risk and to account "
    "for expected credit losses.",
]



# --------------------------------------------------------------------------- #
# The Audit and Related Matters standards, which carry a special purpose
# engagement power in every industry this Prudential Standard applies to. Each
# was read from the primary instrument on 25 July 2026. The subject matter is
# quoted as the instrument expresses it; the wording differs between industries
# and the differences matter, so they are not paraphrased into a single form.
# --------------------------------------------------------------------------- #

SPECIAL_PURPOSE_POWERS = [
    ["APS 310", "ADIs", "Commenced 1 Jan 2023",
     "A particular aspect of the ADI's operations, prudential reporting, risk management systems "
     "or financial position.",
     "APRA may require the ADI, by notice in writing, to appoint an auditor — the existing "
     "Appointed Auditor or another auditor. At the ADI's expense."],
    ["GPS 310", "General insurers and Level 2 insurance groups", "Commenced 1 Oct 2024",
     "Matters specified by APRA relating to the insurer's operations, risk management or "
     "financial affairs.",
     "Where APRA specifies in writing, the Appointed Auditor or Group Auditor undertakes the "
     "review. At the insurer's expense. Report to APRA and the insurer within three months."],
    ["LPS 310", "Life companies", "Commenced 18 Dec 2023",
     "Matters set out in writing by APRA relating to the life company's operations, risk "
     "management or financial affairs.",
     "Ordinarily the Appointed Auditor; another auditor where APRA agrees in writing. At the life "
     "company's expense. Report within three months."],
    ["HPS 310", "Private health insurers", "Commenced 1 Jul 2023",
     "Matters set out in writing by APRA relating to the private health insurer's operations, "
     "risk management or financial affairs.",
     "Ordinarily the Appointed Auditor; another auditor only where APRA agrees in writing. At the "
     "insurer's expense."],
    ["SPS 310", "RSE licensees", "Commenced 30 Jun 2024",
     "A particular aspect of the RSE licensee's business operations, compliance with prudential "
     "requirements or the RSE licensee's risk management framework.",
     "APRA may require the RSE licensee to engage the existing RSE auditor or another auditor "
     "specified by APRA. At the RSE licensee's expense."],
    ["APS 220", "ADIs", "Commenced 1 Jan 2023",
     "All or a particular aspect of the ADI's credit risk management, including provisioning "
     "practices.",
     "APRA may require the ADI to appoint an independent party, and may request the report "
     "without prior consultation. APRA may set the terms of the review, at the ADI's expense."],
]
