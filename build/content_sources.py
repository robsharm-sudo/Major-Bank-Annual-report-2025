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
        "relevant": "Three outcomes and twelve principles numbered 1.1 to 3.6, covering "
                    "enterprise-wide model risk management, a risk-based approach, and model "
                    "lifecycle management. Expressly covers AI and machine learning models.",
        "url": "https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "OSFI-E23-2017", "authority": "OSFI",
        "title": "Guideline E-23 — Enterprise-Wide Model Risk Management for Deposit-Taking "
                 "Institutions (2017)",
        "published": "30 September 2017", "effective": "On issue",
        "date": "Sep 2017 (superseded)",
        "status": "Supervisory guideline, superseded by the 2027 guideline with effect from "
                  "1 May 2027.",
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
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- EU
    {
        "id": "ECB-GIM", "authority": "ECB",
        "title": "ECB Guide to internal models",
        "published": "Consolidated guide; most recent revision published February 2024",
        "effective": "Applies to ECB supervisory assessment of internal models",
        "date": "Feb 2024 revision",
        "status": "Supervisory guide. Sets out how the ECB understands and applies binding EU law; "
                  "the guide itself is not a legal act and does not create obligations beyond "
                  "the CRR.",
        "scope": "Significant institutions directly supervised by the ECB that use internal models "
                 "for regulatory capital.",
        "relevant": "General topics chapter covering overarching principles, internal governance, "
                    "internal validation, internal audit, model use, management of model changes "
                    "and third-party involvement, followed by credit risk, market risk and "
                    "counterparty credit risk chapters.",
        "url": "https://www.bankingsupervision.europa.eu/activities/internal_models/html/index.en.html",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "ECB-CRR", "authority": "EU",
        "title": "Regulation (EU) No 575/2013 (Capital Requirements Regulation), internal model "
                 "provisions including Articles 174, 179, 185 and 189",
        "published": "26 June 2013, as amended", "effective": "In force",
        "date": "2013, as amended",
        "status": "Binding EU regulation, directly applicable in Member States. This is the "
                  "binding law that the ECB guide interprets.",
        "scope": "Credit institutions and investment firms in the European Union.",
        "relevant": "Legal requirements for internal model validation, the use test, model "
                    "governance and the review of estimates.",
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "ECB-RDARR", "authority": "ECB",
        "title": "Guide on effective risk data aggregation and risk reporting",
        "published": "May 2024", "effective": "On issue",
        "date": "May 2024",
        "status": "Supervisory guide. Sets out ECB expectations; not a legal act.",
        "scope": "Significant institutions directly supervised by the ECB.",
        "relevant": "Data governance, data quality and the reliability of risk data feeding "
                    "models and risk reporting.",
        "url": "https://www.bankingsupervision.europa.eu/press/pr/date/2024/html/ssm.pr240503~9c07f30f24.en.html",
        "verification": V_SECONDARY, "checked": CHECKED,
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
        "url": "https://www.mas.gov.sg/publications/monographs-or-information-paper/2024/information-paper-on-ai-model-risk-management",
        "verification": V_SECONDARY, "checked": CHECKED,
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
        "verification": V_SECONDARY, "checked": CHECKED,
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
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- BCBS
    {
        "id": "BCBS-239", "authority": "BCBS",
        "title": "Principles for effective risk data aggregation and risk reporting (BCBS 239)",
        "published": "January 2013", "effective": "1 January 2016 for G-SIBs",
        "date": "Jan 2013",
        "status": "International standard. Not directly binding; effect depends on domestic "
                  "implementation by national authorities.",
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
        "status": "International principles. Effect depends on domestic implementation.",
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
        "verification": V_SECONDARY, "checked": CHECKED,
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
        "title": "Principles for the sound management of third-party risk",
        "published": "July 2025", "effective": "n/a",
        "date": "2025",
        "status": "International principles. Effect depends on domestic implementation.",
        "scope": "Primarily internationally active banks and their supervisors.",
        "relevant": "Third-party lifecycle, nth-party dependencies, concentration, contractual "
                    "provisions, monitoring and exit — applicable to externally supplied models.",
        "url": "https://www.bis.org/bcbs/publ/d588.htm",
        "verification": V_NONE, "checked": CHECKED,
    },
    # ---------------------------------------------------------------- FSB
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
        "id": "APRA-CPS220", "authority": "APRA",
        "title": "Prudential Standard CPS 220 Risk Management",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding cross-industry prudential standard.",
        "scope": "APRA-regulated entities as defined in CPS 220. SPS 220 is the RSE licensee "
                 "counterpart.",
        "relevant": "Risk management framework, risk appetite, Board and senior management "
                    "responsibilities. Does not name model risk as a distinct risk type.",
        "url": "https://www.apra.gov.au/prudential-standard-cps-220-risk-management",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS220", "authority": "APRA",
        "title": "Prudential Standard SPS 220 Risk Management",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Risk management framework and governance obligations for superannuation.",
        "url": "https://www.apra.gov.au/prudential-standard-sps-220-risk-management",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS230", "authority": "APRA",
        "title": "Prudential Standard CPS 230 Operational Risk Management",
        "published": "Current at the as-of date", "effective": "1 July 2025",
        "date": "Eff. 1 Jul 2025",
        "status": "Binding cross-industry prudential standard.",
        "scope": "APRA-regulated entities as defined in CPS 230.",
        "relevant": "Operational risk controls, critical operations and tolerance levels, incident "
                    "management and notification, and service provider management.",
        "url": "https://www.apra.gov.au/prudential-standard-cps-230-operational-risk-management",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS234", "authority": "APRA",
        "title": "Prudential Standard CPS 234 Information Security",
        "published": "Current at the as-of date", "effective": "1 July 2019",
        "date": "Eff. 1 Jul 2019",
        "status": "Binding cross-industry prudential standard.",
        "scope": "APRA-regulated entities as defined in CPS 234.",
        "relevant": "Information security capability, control testing, incident notification and "
                    "assurance.",
        "url": "https://www.apra.gov.au/prudential-standard-cps-234-information-security",
        "verification": V_SECONDARY, "checked": CHECKED,
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
        "url": "https://www.apra.gov.au/prudential-practice-guide-cpg-235-managing-data-risk",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-APS113", "authority": "APRA",
        "title": "Prudential Standard APS 113 Capital Adequacy: Internal Ratings-based Approach "
                 "to Credit Risk",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding prudential standard.",
        "scope": "ADIs approved by APRA to use the internal ratings-based approach.",
        "relevant": "The most developed model governance requirements in the Australian framework: "
                    "model approval, independent review, validation, the use test and model change.",
        "url": "https://www.apra.gov.au/prudential-standard-aps-113-capital-adequacy-internal-ratings-based-approach-to-credit-risk",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-CPS320", "authority": "APRA",
        "title": "Prudential Standard CPS 320 Actuarial and Related Matters",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding prudential standard.",
        "scope": "Insurers as defined in the standard.",
        "relevant": "Appointed Actuary role, actuarial advice and review of insurance liabilities "
                    "— a form of independent professional review of actuarial models.",
        "url": "https://www.apra.gov.au/prudential-standard-cps-320-actuarial-and-related-matters",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS530", "authority": "APRA",
        "title": "Prudential Standard SPS 530 Investment Governance",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Investment governance, valuation, liquidity management and stress testing "
                    "obligations that rely on models.",
        "url": "https://www.apra.gov.au/prudential-standard-sps-530-investment-governance",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS515", "authority": "APRA",
        "title": "Prudential Standard SPS 515 Strategic Planning and Member Outcomes",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding prudential standard.",
        "scope": "RSE licensees.",
        "relevant": "Business performance review and member outcomes assessment, which rely on "
                    "modelled projections.",
        "url": "https://www.apra.gov.au/prudential-standard-sps-515-strategic-planning-and-member-outcomes",
        "verification": V_SECONDARY, "checked": CHECKED,
    },
]

# Some requirement source IDs are aliases of registered sources.
SOURCE_ALIASES = {
    "APRA-GPS320": "APRA-CPS320",
    "APRA-LPS320": "APRA-CPS320",
    "BCBS-FW": "BCBS-239",
}


# --------------------------------------------------------------------------- #
# Annex content for the standard
# --------------------------------------------------------------------------- #

DEFINITIONS = [
    ["Model", "A quantitative method, system or approach that applies statistical, economic, "
              "financial, actuarial or mathematical theories, techniques or assumptions to process "
              "input data into quantitative estimates. A model comprises an information input "
              "component, a processing component and a reporting component."],
    ["Model risk", "The potential for adverse consequences from decisions based on incorrect or "
                   "misused model outputs. Model risk arises where a model has fundamental errors "
                   "and produces inaccurate outputs relative to its design objective and intended "
                   "use, or where a model is used incorrectly or inappropriately."],
    ["Material model", "A model whose failure or misuse could have a non-negligible effect on the "
                       "entity's financial position, regulatory obligations, customers, "
                       "beneficiaries or critical operations."],
    ["Model owner", "The person accountable for a model being fit for its approved purpose "
                    "throughout its lifecycle, including its documentation, performance monitoring, "
                    "communication of limitations and remediation of findings."],
    ["Model risk tier", "The classification assigned to a model under the entity's tiering "
                        "methodology, which determines the intensity of controls applied to it."],
    ["Independent validation", "An assessment of a model's fitness for its intended use performed "
                               "by persons who did not develop the model and who are not "
                               "accountable to those who developed it or who sponsor its use."],
    ["Effective challenge", "Critical analysis by parties with the competence to identify "
                            "deficiencies, the standing for their findings to carry weight, and "
                            "incentives that reward raising issues."],
    ["Conceptual soundness", "The quality of a model's design, theory, methodology and assumptions "
                             "as appropriate for the purpose for which the model will be used."],
    ["Outcomes analysis", "Comparison of model outputs with corresponding actual outcomes, used to "
                          "assess whether a model continues to perform as intended."],
    ["Overlay", "An adjustment applied to a model's output before it is used, including management "
                "overlays, post-model adjustments and model overrides."],
    ["Quantitative decision tool", "A quantitative method that materially informs a decision but "
                                   "does not meet the definition of a model."],
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
    "financial product, a claim, a benefit, a price or an employment outcome.",
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
     "240' is a drafting placeholder only."],
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
     "Confirm the model classes named for RSE licensees and the interaction with SPS 530 and "
     "SPS 515."],
    ["Accountability regime",
     "Settle the designation of the accountable senior executive and its interaction with the "
     "applicable accountability regime."],
    ["Notification",
     "Confirm that CPS 230 and CPS 234 remain the primary notification requirements, and settle "
     "whether any model-specific notification trigger is justified."],
    ["APRA powers",
     "Settle the powers to require information, restriction of model use, independent review or "
     "remediation, and ensure procedural fairness."],
    ["Commencement and transition",
     "Set commencement, transitional milestones for inventory, tiering and validation coverage, "
     "and the treatment of models already in use."],
    ["Records and privacy",
     "Balance the reconstructability requirement against data minimisation, security and technical "
     "feasibility."],
    ["Boundary with the AI instrument",
     "Settle the boundary rule between this standard and any AI risk management instrument so that "
     "no material system falls outside both."],
]
