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
        "url": "https://www.apra.gov.au/standards/cps-220",
        "verification": V_PRIMARY, "checked": CHECKED,
    },
    {
        "id": "APRA-SPS220", "authority": "APRA",
        "title": "Prudential Standard SPS 220 Risk Management",
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
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
        "published": "Current at the as-of date", "effective": "1 July 2019",
        "date": "Eff. 1 Jul 2019",
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
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
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
        "published": "Current at the as-of date", "effective": "In force",
        "date": "In force",
        "status": "Binding prudential standard.",
        "scope": "Insurers as defined in the standard.",
        "relevant": "Appointed Actuary role, actuarial advice and review of insurance liabilities "
                    "— a form of independent professional review of actuarial models.",
        "url": "https://www.apra.gov.au/standards/cps-320",
        "verification": V_PRIMARY, "checked": CHECKED,
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
        "url": "https://www.apra.gov.au/standards/sps-530",
        "verification": V_PRIMARY, "checked": CHECKED,
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
        "url": "https://www.apra.gov.au/standards/sps-515",
        "verification": V_PRIMARY, "checked": CHECKED,
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


# --------------------------------------------------------------------------- #
# Principles register — labels and titles as printed by the issuing authority
# --------------------------------------------------------------------------- #

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
     "Firms set their own definition; Principle 1.1 requires one, and requires consideration of methods falling outside it.",
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
     "Section 6 model use; CRR Article 174 use of models is binding.",
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

    ["Aggregate model risk",
     "Not required.",
     "Sound practice to assess model risk individually and in aggregate, reflecting interactions, dependencies and reliance on common assumptions, data or methodologies.",
     "Principle 5 model risk mitigants, and aggregate model risk reporting.",
     "Outcome 1 requires model risk to be understood across the enterprise.",
     "Model risk considered in supervisory review.",
     "Not addressed.",
     "Not addressed.",
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
    ("M20", "OCC/Fed"): (MODERATE, "Retains validation but states its quality depends on the "
                                   "rigour of review rather than organisational structure, a "
                                   "softening from the rescinded 2011 text."),
    ("M19", "OCC/Fed"): (MODERATE, "Validation generally precedes first use, but use before "
                                   "validation is permitted for urgent business need with "
                                   "compensating controls."),
    ("M33", "OCC/Fed"): (DIVERGES, "Generative and agentic AI are expressly outside scope; "
                                   "non-generative AI models are in scope."),
    ("M34", "OCC/Fed"): (SILENT, "No parallel AI instrument, so no boundary rule arises."),
    ("M34", "OSFI"): (STRONG, "Single framework covering models including AI removes the boundary "
                              "problem entirely — the alternative architecture to the one proposed."),
    ("M38", "OSFI"): (SILENT, "Superannuation is outside OSFI's perimeter; federally regulated "
                              "pension plans are expressly excluded from E-23."),
    ("M13", "OCC/Fed"): (MODERATE, "Describes a comprehensive inventory as common industry "
                                   "practice rather than stating it as an expectation."),
    ("M18", "OCC/Fed"): (MODERATE, "Reduced in 2026 to a statement that adequate documentation "
                                   "helps support model risk management."),
    ("M30", "OSFI"): (STRONG, "Principle 3.6 expressly covers model decommission — the only "
                              "comparator that does."),
    ("M40", "OCC/Fed"): (STRONG, "Expressly requires assessment of model risk individually and in "
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
    ["ST-04", "CPS XXXX M22 / CPG XXXX", "Effective challenge",
     "Effective challenge survives in the 2026 US guidance, reformulated around expertise, "
     "sufficient independence, and organisational standing and influence to effect change.",
     "Extracted", V_PRIMARY,
     "SR 26-2 §III. The rescinded 2011 formulation was a combination of incentives, competence "
     "and influence.",
     "Corrected. The draft initially used the 2011 formulation. See RT-03."],
    ["ST-05", "CPS XXXX M21 / CPG XXXX", "Components of validation",
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
    ["ST-13", "CPS XXXX M38 / CPG XXXX", "Superannuation",
     "No comparator authority addresses model risk in superannuation.",
     "Inferred", V_PRIMARY,
     "Scope statements of each comparator instrument. OSFI expressly excludes federally regulated "
     "pension plans.",
     "None required. Recorded as a policy design choice with no benchmark."],
    ["ST-14", "CPS XXXX M43 / CPG XXXX", "Notification",
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
     "organisational standing and influence to effect change. M22 was redrafted to the current "
     "formulation; incentives are retained in the practice guide as a practical consideration "
     "rather than presented as part of the definition.",
     "M22 and the corresponding guidance paragraph rewritten.",
     "SR 26-2 §III; rescinded 2011 attachment §III for the superseded wording.",
     "Medium", "Closed — correction incorporated"],

    ["RT-04",
     "Validation scope was drafted as 'conceptual soundness, ongoing monitoring including process "
     "verification and benchmarking, and outcomes analysis'.",
     "Are those the current component names and does benchmarking sit where the draft places it?",
     "The 2026 guidance names the components conceptual soundness, outcomes analysis and ongoing "
     "model monitoring, in that order, and locates benchmarking under conceptual soundness rather "
     "than ongoing monitoring. M21 and the guidance were realigned.",
     "M21 and two guidance paragraphs rewritten.",
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
     "conflicting with the materiality criteria and timeframes in CPS 230 and CPS 234. M43 now "
     "cross-references the existing architecture and expects early engagement on material model "
     "weakness instead.",
     "M43 redrafted; the notification domain scored against the existing architecture rather than "
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
     "M20 and M24; the validation intensity table in the practice guide.",
     "OCC Bulletin 2025-26; PRA SS1/23 Principle 4.5; OSFI E-23 Principle 2.3.",
     "Medium", "Closed — correction incorporated"],

    ["RT-13",
     "An early draft required contractual access to vendor source code and training data for "
     "third-party models.",
     "Is that achievable, and is it required by any comparator?",
     "It is frequently impracticable and raises intellectual property and security issues. No "
     "comparator requires it; the 2026 US guidance expressly acknowledges that proprietary "
     "components may not be disclosed while maintaining that the principles still apply. M31 and "
     "M32 now require sufficient information or compensating controls, expressed as an outcome.",
     "M31 and M32; chapter 11 of the practice guide.",
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
     "M35, M37, Annex F; seven requirements carry a legal flag.",
     "APS 113; CPS 320; SPS 530; comparator review.",
     "High", "Open — referred for legal settlement"],

    ["RT-16",
     "The draft creates a boundary between this standard and a separate AI risk instrument.",
     "Does any comparator operate parallel model risk and AI instruments, and could a system fall "
     "between them?",
     "No comparator does. OSFI deliberately brought AI within a single model risk guideline, and "
     "the 2026 US guidance excludes generative and agentic AI from model risk scope without "
     "putting anything in its place. The boundary rule in M34 is therefore an Australian design "
     "choice, is labelled as one, and requires a single register recording which regime applies to "
     "each AI system so that the boundary is a documented determination.",
     "M34 marked as a policy choice and carrying a legal flag; chapter 12 of the practice guide.",
     "OSFI E-23 (2027) scope; SR 26-2 footnote 3.",
     "High", "Open — referred for consultation"],

    ["RT-17",
     "The claim that no comparator addresses superannuation model risk.",
     "Verify rather than assume — an unverified negative is as unsafe as an unverified positive.",
     "Confirmed. OSFI expressly excludes federally regulated pension plans from E-23; the PRA "
     "framework covers banks with internal model approval; the US guidance covers banking "
     "organisations. The superannuation domain is scored with no benchmark and the requirement is "
     "labelled a policy design choice.",
     "M38; the superannuation domain carries no benchmark authority in the gap assessment.",
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
