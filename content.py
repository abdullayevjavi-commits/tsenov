# -*- coding: utf-8 -*-
"""Single source of truth for the article. Rendered to DOCX and PDF by the
render_*.py scripts so the two outputs never drift. Revision 5 (addresses the
fourth review round: proposed-framework reframing, narrowed scope, structured
search, expanded Uzbekistan vignette, weighting and endogeneity discussion,
sustainability references and practical checklists)."""

TITLE = ("Digital Transformation and SME Performance in ASEAN and Central Asia: "
         "A Proposed Management Framework")

AUTHORS = ["[Author Name], [e-mail]", "[Department]", "[Institution]"]

ABSTRACT = (
    "Abstract: Digital transformation is the central management challenge for small and "
    "medium-sized enterprises (SMEs), which dominate the economies of ASEAN and Central Asia yet "
    "adopt advanced digital technologies more slowly than large firms. This study proposes a "
    "management framework explaining how SMEs convert digital technologies into superior "
    "performance. Building on the dynamic-capabilities perspective and on the distinction between "
    "digitisation, digitalisation and digital transformation, the framework links external drivers "
    "to the firm\u2019s sensing, seizing and reconfiguring capabilities, to the depth of the "
    "transformation undertaken, and to performance, with a reinvestment feedback loop. The "
    "contribution is integrative rather than metric: unlike prior reviews that establish the "
    "relevance of capabilities, and unlike existing composite indices such as the European DESI "
    "that score adoption alone, the framework embeds firm-level digital-adoption measures in an "
    "explicit capability-conditioned causal structure and states the often-asserted claim that "
    "\u201ctechnology alone is not enough\u201d as a single, estimable moderation hypothesis \u2014 "
    "a digital-transformation intensity (DTI) measure interacting with dynamic capability \u2014 "
    "together with a capability-threshold diagnostic for public support. Both constructs are "
    "operationalised with established adoption items and a validated dynamic-capabilities scale, and "
    "the data, weighting options, endogeneity concerns and estimation strategy for testing the "
    "specification are set out. The framework is built through a structured narrative review of "
    "Scopus and Web of Science sources, illustrated with a numerical example of the moderation "
    "logic, and assessed in light of secondary indicators for the ASEAN region and an expanded "
    "country vignette of Uzbekistan with a Kazakhstan comparison. The empirical estimation of the "
    "specification is identified as the principal direction for further work. The analysis points "
    "to managerial skills and finance, rather than connectivity, as the binding constraints for "
    "ASEAN and Central Asian SMEs, and derives step-by-step managerial and policy checklists "
    "accordingly."
)

KEYWORDS = ("Key words: digital transformation; small and medium-sized enterprises; dynamic "
            "capabilities; firm performance; ASEAN; Central Asia.")
JEL = "JEL: M15, M21, O33, L25, O10, O18, O53."

BLOCKS = [
    ("h1", "Introduction"),
    ("p",
     "Digital technologies \u2014 cloud computing, data analytics, artificial intelligence, "
     "e-commerce platforms and connected devices \u2014 have moved from being a support function to "
     "being the principal arena of competition. For enterprises of every size, the management "
     "question is no longer whether to adopt such technologies but how to convert them into durable "
     "improvements in performance. This question is most acute for small and medium-sized enterprises "
     "(SMEs). In the member states of the Association of Southeast Asian Nations (ASEAN), micro, "
     "small and medium-sized enterprises make up on average more than ninety-seven per cent of all "
     "firms and provide the large majority of employment (Asian Development Bank, 2023); in the "
     "economies of Central Asia they play a comparably central role (OECD, 2021b). Yet across both "
     "regions these firms adopt advanced digital technologies more slowly than large enterprises and "
     "face tighter constraints on finance, skills and managerial capacity (OECD, 2021a; Yoshino & "
     "Taghizadeh-Hesary, 2016)."),
    ("p",
     "The literature has clarified what digital transformation is, but it has paid less attention to "
     "the managerial mechanisms through which a resource-constrained SME in an emerging economy turns "
     "technology into results. Digital transformation is an organisational change process in which "
     "digital technologies reshape value creation, operations and the business model itself (Vial, "
     "2019; Verhoef et al., 2021), and recent comprehensive reviews stress that its outcomes hinge on "
     "managerial and organisational factors rather than on technology adoption alone (Hanelt et al., "
     "2021; Kraus et al., 2022). Whether the process raises performance depends on the capabilities "
     "the firm can mobilise around it (Teece, 2007; Warner & W\u00e4ger, 2019), and SME-focused "
     "reviews report that transformation levels in smaller firms remain low and that the field still "
     "lacks process-level guidance (de Mattos et al., 2024; Sagala & \u0150ri, 2024). A parallel "
     "strand now links SME digital transformation to sustainability and the Sustainable Development "
     "Goals, but likewise concludes that managerial capability and a clear strategy, not technology "
     "access, determine whether transformation translates into competitive and sustainable advantage "
     "(Mick et al., 2024; Lu & Shaharudin, 2024)."),
    ("p",
     "This study addresses that gap with a management framework connecting the external drivers of "
     "digital transformation, the dynamic capabilities of the firm, the depth of the transformation "
     "undertaken and the resulting performance, closed by a reinvestment feedback loop. The framework "
     "is proposed and specified for testing rather than estimated here. Its contribution differs from "
     "prior work in three specific ways. First, whereas existing reviews establish that capabilities "
     "matter (Hanelt et al., 2021; Kraus et al., 2022; de Mattos et al., 2024), this study embeds "
     "firm-level digital-adoption measures in an explicit, capability-conditioned causal structure. "
     "Second, whereas composite digital-intensity indices such as the European Digital Economy and "
     "Society Index score adoption on its own, the framework states the claim that \u201ctechnology "
     "alone is not enough\u201d as a single, estimable moderation hypothesis \u2014 the interaction "
     "between digital-transformation intensity and dynamic capability \u2014 and derives from it a "
     "capability-threshold diagnostic that is new to the SME-policy debate. Third, it applies the "
     "framework to a deliberately bounded set of economies, the ASEAN region and Central Asia, with "
     "an expanded Uzbekistan vignette and a Kazakhstan comparison, where firm-level evidence is "
     "comparatively thin, rather than to \u201cemerging Asia\u201d as a whole."),
    ("p",
     "The remainder of the article is organised as follows. Section 1 reviews the literature and "
     "defines the core constructs. Section 2 presents the framework, the measures and the estimable "
     "specification. Section 3 describes the methodology \u2014 the structured review, the data, the "
     "operationalisation of the constructs, the treatment of endogeneity and the estimation strategy. "
     "Section 4 reports a numerical illustration of the moderation logic and the regional indicators, "
     "including the expanded Uzbekistan vignette and the Kazakhstan comparison. Section 5 sets out "
     "the management and policy implications as concrete checklists. The final section concludes."),

    ("h1", "1. Theoretical background and literature review"),
    ("p",
     "Research distinguishes three increasingly profound stages of digital change. Digitisation is "
     "the conversion of analogue information into digital form; digitalisation is the use of digital "
     "technologies to improve existing processes; and digital transformation is the deeper, "
     "firm-wide change in which technology reconfigures value creation and the business model "
     "(Verhoef et al., 2021). Vial (2019) defines digital transformation as a process in which "
     "digital technologies trigger strategic responses that alter value-creation paths while the firm "
     "manages structural change and organisational barriers; large-scale reviews confirm this "
     "organisational-change reading and the centrality of strategy and leadership, noting that firms "
     "widely recognise digital technology as a strategic imperative yet struggle to execute it "
     "(Hanelt et al., 2021; Kraus et al., 2022). The implication for management is that technology "
     "alone does not deliver value; the value comes from the organisational changes that accompany "
     "it."),
    ("p",
     "The dynamic-capabilities perspective explains why firms facing the same technologies achieve "
     "different results. Teece (2007) decomposes the capacity to sustain performance into sensing "
     "opportunities and threats, seizing them through investment and business-model choices, and "
     "reconfiguring (transforming) the resource base accordingly. Warner and W\u00e4ger (2019) show "
     "that digital transformation is precisely an ongoing process of strategic renewal in which these "
     "capabilities are built and rebuilt, and Kump, Engelmann, Kessler and Schweiger (2019) provide a "
     "validated survey scale that measures sensing, seizing and transforming capacities separately. "
     "Bharadwaj, El Sawy, Pavlou and Venkatraman (2013) argue that digital strategy must be fused "
     "with business strategy, and Westerman, Bonnet and McAfee (2014) add that the binding constraint "
     "is usually leadership and management capability rather than technology as such."),
    ("p",
     "A further strand explains how the adoption of a specific technology is decided, and it feeds "
     "directly into the framework\u2019s measures. The technology acceptance model relates adoption "
     "to perceived usefulness and perceived ease of use (Davis, 1989), and the unified theory of "
     "acceptance and use of technology adds performance and effort expectancy, social influence and "
     "facilitating conditions (Venkatesh, Morris, Davis & Davis, 2003); both inform the items that "
     "make up the adoption levels aggregated in the digital-transformation intensity measure below, "
     "and managerial acceptance is itself part of the sensing and seizing capability. At the "
     "organisational level, the technology\u2013organisation\u2013environment framework situates "
     "adoption in the interplay of technological readiness, organisational resources and the external "
     "environment (Tornatzky & Fleischer, 1990), which maps onto the framework\u2019s capability and "
     "driver blocks respectively. For SMEs in emerging economies these models matter because the "
     "adoption decision is concentrated in a small management team and is highly sensitive to skills, "
     "cost and the surrounding digital ecosystem."),
    ("p",
     "Recent empirical and policy work sharpens the picture. Teng et al. (2022), using a "
     "structural-equation model on 335 SMEs, find that digital technology, employee digital skills "
     "and a digital-transformation strategy are jointly and positively associated with transformation "
     "and, through it, with performance \u2014 evidence consistent with a capability-conditioned view "
     "and with an interaction between technology and capability. The policy-oriented literature "
     "documents the SME-specific barriers \u2014 scarce skills, limited finance and uncertainty about "
     "returns (OECD, 2021; Yoshino & Taghizadeh-Hesary, 2016) \u2014 and Nambisan, Wright and Feldman "
     "(2019) note that digital technologies also reshape innovation and entrepreneurship themselves, "
     "raising the premium on digital capability. This body of work motivates a framework in which "
     "drivers, firm-level capabilities and the depth of transformation jointly determine performance, "
     "and a specification that can be tested."),

    ("h1", "2. Framework, measures and estimable specification"),
    ("p",
     "The framework links four blocks in sequence, with a feedback loop (Figure 1). The first block "
     "is the set of external drivers: market and competitive pressure, the availability and cost of "
     "digital technologies, and the policy environment, including funding and regulation. Drivers "
     "create the incentive and the opportunity to transform, but they do not determine the outcome."),
    ("p",
     "The second block is the firm\u2019s dynamic capabilities. Following Teece (2007), an SME senses "
     "digital opportunities and threats, seizes them by investing in technology and adjusting its "
     "business model, and reconfigures its processes, skills and structure so that the technology is "
     "actually used. The third block is the depth of the transformation undertaken, from digitisation "
     "through digitalisation to business-model change (Verhoef et al., 2021). The fourth block is "
     "performance: productivity, growth and export reach, and resilience. A feedback loop closes the "
     "framework: performance gains generate resources that are reinvested in further capability "
     "building and technology, as shown by the return arrow from performance to capabilities in "
     "Figure 1."),
    ("fig", "figure1_framework.png",
     "Figure 1. A management framework for digital transformation in SMEs",
     "Source: Authors\u2019 elaboration based on Teece (2007), Vial (2019) and Verhoef et al. (2021). "
     "The dashed arrow denotes the performance feedback loop (reinvestment in capabilities and "
     "technology).", 6.0),
    ("h2", "2.1. Measuring digital-transformation intensity and capability"),
    ("p",
     "Two constructs must be measured. Digital-transformation intensity (DTI) summarises the digital "
     "technologies and practices a firm actually uses, as a weighted composite"),
    ("eq", "DTI = \u03a3\u1d62 w\u1d62 \u00b7 a\u1d62 ,   \u03a3\u1d62 w\u1d62 = 1 ,   a\u1d62 \u2208 [0, 1] ,", 1),
    ("p",
     "where a\u1d62 is the adoption level of digital element i \u2014 connectivity, a website or "
     "e-commerce channel, digital payments, cloud services, enterprise software, data analytics, "
     "artificial intelligence and digital-security measures \u2014 and w\u1d62 is its weight. The "
     "elements and items follow established firm-level instruments (the World Bank Enterprise Surveys "
     "and the European digital-intensity indicators) and the acceptance literature (Davis, 1989; "
     "Venkatesh et al., 2003); the measure is therefore not a new statistic but a transparent "
     "aggregation of existing ones for use inside the framework."),
    ("p",
     "The weights w\u1d62 are not arbitrary and can be fixed by one of three transparent procedures, "
     "reported side by side as a robustness check. (i) Equal weighting sets w\u1d62 = 1/n for all n "
     "elements; it imposes no prior and serves only as a baseline. (ii) Expert weighting elicits the "
     "relative importance of each element from a panel of five to seven domain experts, who rate each "
     "element on a one-to-five scale, after which the normalised mean ratings become the weights; "
     "this is the recommended approach where a credible panel is available. (iii) Data-driven "
     "weighting derives the weights from the data themselves \u2014 from the factor loadings of an "
     "exploratory or confirmatory factor analysis, or from the variance shares of a principal-"
     "component analysis \u2014 so that elements carrying more common information receive more "
     "weight. Because the three procedures can diverge, the empirical strategy is to compute DTI "
     "under all three and report whether the substantive results are stable, rather than to defend a "
     "single weighting on a priori grounds."),
    ("p",
     "Capability (C) is operationalised, rather than left undefined, as the firm\u2019s dynamic "
     "capability measured on the validated scale of Kump et al. (2019), which captures sensing "
     "(S\u2081), seizing (S\u2082) and transforming (S\u2083) capacities through multi-item "
     "managerial-survey constructs. A composite capability index can be formed as"),
    ("eq", "C = (S\u2081 + S\u2082 + S\u2083) / 3 ,   C \u2208 [0, 1] ,", 2),
    ("p",
     "where equal weights are a simplifying assumption adopted for exposition; empirical application "
     "should verify the factorial structure of the scale (Kump et al., 2019) rather than impose equal "
     "weights, and observable complements \u2014 managerial digital skills, the presence of an "
     "explicit digital strategy, prior technology projects and staff training \u2014 are available as "
     "proxies where survey access is limited. Because the Kump et al. (2019) scale was validated on "
     "Austrian firms, applying it to Uzbek or other Central Asian SMEs requires prior local "
     "validation \u2014 translation and back-translation, a pilot, and a confirmatory factor analysis "
     "to check that the sensing, seizing and transforming items load as intended in the new context "
     "\u2014 before the composite C is treated as comparable across settings. Subject to that "
     "validation, both DTI and C are measurable with existing, peer-validated instruments."),
    ("h2", "2.2. The estimable specification"),
    ("p",
     "Let \u0394P denote the change in a performance measure (for example labour productivity, sales "
     "growth or export intensity). The framework\u2019s central claim \u2014 that adoption pays off "
     "only when matched by capability \u2014 is a moderation hypothesis, estimated in the standard "
     "interaction form rather than asserted as a pure product:"),
    ("eq", "\u0394P = \u03b2\u2080 + \u03b2\u2081\u00b7DTI + \u03b2\u2082\u00b7C + \u03b2\u2083\u00b7(DTI\u00d7C) + \u03b3\u00b7X + \u03b5 ,", 3),
    ("p",
     "where X is a vector of controls (firm size, age, sector, region) and \u03b5 is the error term. "
     "The interaction term DTI\u00d7C is the object of interest: a positive \u03b2\u2083 means the "
     "marginal performance return to digital adoption, \u2202\u0394P/\u2202DTI = \u03b2\u2081 + "
     "\u03b2\u2083\u00b7C, rises with capability \u2014 the complementarity between technology and "
     "capability familiar from absorptive-capacity and complementarity theory and consistent with the "
     "structural-equation evidence of Teng et al. (2022). The additive terms \u03b2\u2081 and "
     "\u03b2\u2082 are retained precisely because theory does not require a pure product; the sign and "
     "size of all four coefficients are empirical questions to be settled by estimation, not "
     "assumptions of the model."),
    ("p",
     "For the sole purpose of the numerical illustration in Section 4.1, and making no empirical "
     "claim about the additive terms, equation (3) is simplified by setting \u03b2\u2080 = "
     "\u03b2\u2081 = \u03b2\u2082 = 0 and \u03b2\u2083 = 1, which isolates and traces only the "
     "interaction effect:"),
    ("eq", "\u0394P = \u03b2\u2083\u00b7(DTI\u00d7C)   [illustration only] .", 4),

    ("h1", "3. Methodology: review protocol, data and estimation strategy"),
    ("p",
     "This article is conceptual with an empirical research design specified for testing; it does not "
     "itself collect primary data. The framework was developed through a structured narrative review "
     "of the literature. Searches were run in Scopus and Web of Science using the Boolean string "
     "(\u201cdigital transformation\u201d OR \u201cdigitalisation\u201d OR \u201cdigitization\u201d) "
     "AND (\u201cSME\u201d OR \u201csmall and medium-sized enterprises\u201d) AND (\u201cdynamic "
     "capabilities\u201d OR \u201cfirm performance\u201d), restricted to peer-reviewed journal "
     "articles in English published between 2010 and 2025, and supplemented by backward and forward "
     "citation tracking of the principal reviews. Records were screened on title and abstract and "
     "retained when they addressed SMEs and linked digital transformation to capabilities or "
     "performance; foundational works on dynamic capabilities and technology acceptance were retained "
     "regardless of date because they define the constructs. The synthesis is reported as a "
     "structured narrative review: it makes the databases, search terms, time window and "
     "inclusion criteria explicit, but it does not claim the exhaustive coverage, full screening "
     "counts or PRISMA flow diagram of a systematic review, and the reading of the evidence is "
     "interpretive rather than meta-analytic."),
    ("p",
     "For testing the specification in equation (3), the constructs are operationalised as follows. "
     "DTI is computed from firm-level adoption items of the kind collected in the World Bank "
     "Enterprise Surveys \u2014 whose 2024 round for Uzbekistan provides a suitable primary, "
     "firm-level data source \u2014 such as use of a website or e-commerce, e-mail with clients and "
     "suppliers, and, in recent rounds, cloud services and digital payments, complemented by the "
     "European digital-intensity indicators; the equal, expert and data-driven weighting schemes of "
     "Section 2.1 are all applied and compared. Capability C is measured with the locally validated "
     "Kump et al. (2019) sensing\u2013seizing\u2013transforming scale administered to owner-managers, "
     "with the observable proxies noted in Section 2.1 used where a full survey is infeasible. "
     "Performance \u0394P is taken from accounts or survey self-reports (productivity, sales growth, "
     "export intensity). The baseline estimator is ordinary least squares with robust standard "
     "errors, or structural-equation modelling when the latent constructs are modelled directly; the "
     "moderation is read from the sign, size and significance of \u03b2\u2083 and from marginal-effect "
     "plots of \u2202\u0394P/\u2202DTI across the range of C, with the identification strategy of "
     "Section 3.1 used to support a causal interpretation."),
    ("h2", "3.1. Endogeneity and identification"),
    ("p",
     "Estimating equation (3) by ordinary least squares would not, on its own, support a causal "
     "reading, because capability and performance are plausibly jointly determined: better-performing "
     "firms generate the resources to invest in capability and technology, exactly the reinvestment "
     "loop the framework builds in, so DTI, C and the interaction term are likely correlated with the "
     "error. The design therefore treats identification explicitly. First, an instrumental-variables "
     "strategy uses instruments that shift adoption and capability but do not directly affect a given "
     "firm\u2019s performance \u2014 the quality of local internet infrastructure (broadband speed "
     "and coverage in the firm\u2019s district), peer adoption among neighbouring or same-sector "
     "firms, and eligibility for or distance to public digital-support programmes \u2014 estimated by "
     "two-stage least squares with the usual relevance and exclusion checks. Second, where panel data "
     "are available, firm fixed effects absorb time-invariant heterogeneity and lagged regressors "
     "reduce simultaneity. Third, the staggered roll-out of broadband and of government subsidy "
     "schemes offers quasi-experimental variation that a difference-in-differences design can "
     "exploit. These strategies are part of the proposed design; the present article specifies them "
     "rather than implementing them."),
    ("p",
     "Pending such firm-level estimation, the framework is assessed in light of secondary indicators "
     "for the ASEAN region and Central Asia drawn from official and institutional sources: the Asian "
     "Development Bank (2023, 2024) and the OECD and ERIA (2024) for the ASEAN region; Yoshino and "
     "Taghizadeh-Hesary (2016) for the structural constraints on Asian SMEs; and, for the Central "
     "Asian vignettes, the OECD\u2019s work on digital skills in Uzbekistan (OECD, 2023a) and on "
     "framework conditions for the digital transformation of businesses in Kazakhstan (OECD, 2023b), "
     "the regional outlook of OECD (2021b), World Bank country updates (2023, 2025), the World Bank "
     "Enterprise Surveys (2024) and a UNESCAP (2025) foresight initiative. Estimating "
     "\u03b2\u2080\u2013\u03b2\u2083 on firm-level data, including a primary survey of Uzbek and ASEAN "
     "SMEs, is the principal direction for further work."),

    ("h1", "4. Illustration and regional indicators"),
    ("h2", "4.1. Numerical illustration of the moderation logic"),
    ("p",
     "Before turning to the indicators, a numerical example clarifies what the moderation in equation "
     "(3) implies; it is a didactic device, not new empirical information, and traces only the "
     "isolated interaction of equation (4) for transparent inputs. Three representative SME profiles "
     "are used: a micro service firm with full connectivity but no analytics or artificial "
     "intelligence (DTI \u2248 0.33), a small manufacturer with moderate adoption (DTI \u2248 0.54) "
     "and a digitally advanced medium-sized exporter (DTI \u2248 0.80). Holding the slope at the "
     "illustrative value \u03b2\u2083 = 1, the implied performance gain is plotted for a high "
     "capability level (C = 0.8) and a low one (C = 0.3) in Figure 2, with the underlying figures in "
     "Table 1."),
    ("fig", "figure2_dti_application.png",
     "Figure 2. Numerical illustration: performance gain by DTI level under high and low capability",
     "Source: Authors\u2019 illustration of equation (4) with \u03b2\u2083 = 1 for didactic purposes; "
     "the values are inputs, not estimates or survey data.", 5.7),
    ("table", "Table 1",
     "Numerical illustration of the DTI\u00d7capability moderation (didactic, not empirical)",
     ["SME profile", "DTI", "Gain at C = 0.8", "Gain at C = 0.3"],
     [["Micro service firm", "0.33", "0.26", "0.10"],
      ["Small manufacturer", "0.54", "0.43", "0.16"],
      ["Medium exporter", "0.80", "0.64", "0.24"]],
     "Source: Authors\u2019 illustration of equation (4) with \u03b2\u2083 set to one. The values are "
     "didactic inputs, not estimates or survey data."),
    ("p",
     "The example conveys one point only: under the moderated specification, the performance return "
     "to a given level of digital adoption is far larger when capability is high than when it is low "
     "\u2014 about two-and-a-half times larger at C = 0.8 than at C = 0.3 \u2014 so a digitally "
     "advanced firm with weak capability gains little relative to its potential. This is the "
     "qualitative content of the proposition that capability, not technology, is the binding "
     "constraint; establishing its magnitude requires estimating equation (3) on firm-level data, as "
     "set out in Section 3."),
    ("h2", "4.2. Regional indicators for ASEAN and Central Asia"),
    ("p",
     "Across the ASEAN member states, micro, small and medium-sized enterprises account for the "
     "overwhelming majority of firms and the bulk of employment, and the regional digital economy is "
     "expanding rapidly (Asian Development Bank, 2023). The constraints on their digital "
     "transformation are, however, systematic. Yoshino and Taghizadeh-Hesary (2016) show that Asian "
     "SMEs are held back by limited access to finance, the absence of comprehensive databases, low "
     "research and development spending and underdeveloped sales channels \u2014 conditions that "
     "depress the capability term in the framework. The OECD and ERIA (2024) confirm that, although "
     "ASEAN governments have strengthened SME policy frameworks, the digitalisation of smaller firms "
     "remains uneven and skills and finance are recurring bottlenecks. These secondary indicators are "
     "consistent with the framework\u2019s prediction that capability, not connectivity, is the "
     "binding constraint."),
    ("h2", "4.3. Country vignette: Uzbekistan"),
    ("p",
     "Uzbekistan illustrates both the opportunity and the constraint. SMEs are central to the "
     "economy: World Bank country updates (2025) report that micro, small and medium-sized "
     "enterprises account for over ninety per cent of businesses, about seventy-five per cent of "
     "employment and roughly fifty-five per cent of gross domestic product, and the national "
     "statistics authorities record more than 1.2 million small businesses in early 2025. "
     "Connectivity and e-commerce have grown quickly from a low base; the World Bank (2023) reports "
     "that the e-commerce market expanded roughly fivefold between 2018 and 2022, exceeding half a "
     "billion United States dollars by 2023."),
    ("p",
     "National policy is organised around the Digital Uzbekistan 2030 strategy. Its principal lines "
     "of action are the build-out of digital infrastructure, the expansion of the information-"
     "technology sector and the digitalisation of public services. On the supply side, IT Park "
     "Uzbekistan, established in 2019, hosts a large and growing community of resident technology "
     "companies and anchors the strategy\u2019s targets of substantially higher technology exports "
     "and large-scale job creation, supported by sizeable public investment in infrastructure (World "
     "Bank, 2023). On the public-services side, a unified digital-government portal and the "
     "my.gov.uz interactive services consolidate tax, statistical and licensing procedures in a "
     "single-window form intended to lower the transaction costs SMEs face. The OECD (2023a) "
     "assessment of digital skills for private-sector competitiveness in Uzbekistan documents the "
     "complementary skills agenda this requires."),
    ("p",
     "The deeper transformation of enterprises nonetheless lags the roll-out of infrastructure, and "
     "the binding constraints are those the framework predicts. Coverage and quality of connectivity "
     "remain uneven between urban and rural areas; managerial and technical skills are scarce; "
     "access to finance for technology investment is limited; and the regulatory environment for the "
     "digital economy is still maturing (OECD, 2023a; World Bank, 2023). Preliminary figures "
     "presented at a UNESCAP (2025) foresight workshop suggest that only about ten per cent of SMEs "
     "were registered on the national digital public-services portal, an indication that the uptake "
     "of even basic digital government services \u2014 let alone analytics or artificial intelligence "
     "\u2014 remains shallow; this single figure is treated as indicative and would benefit from "
     "confirmation in firm-level survey data. Viewed through the lens of the framework, Uzbek SMEs "
     "increasingly possess the drivers and the connectivity but not yet the capability \u2014 skills, "
     "finance and managerial capacity \u2014 that converts adoption into performance."),
    ("p",
     "A brief comparison with Kazakhstan sharpens the point. Kazakhstan launched its Digital "
     "Kazakhstan programme earlier, in 2017, and the OECD (2023b) review of framework conditions for "
     "the digital transformation of businesses there finds that, even with more mature digital "
     "infrastructure and e-government, the digitalisation of smaller firms still turns on managerial "
     "capability, skills and the regulatory and financing environment rather than on connectivity "
     "alone. The two Central Asian cases thus point in the same direction as the ASEAN evidence: "
     "infrastructure and policy ambition advance first, and the capability to convert them into "
     "firm-level performance follows more slowly. Table 2 summarises the regional, Uzbekistan and "
     "Kazakhstan indicators."),
    ("table", "Table 2",
     "Digital transformation of SMEs in ASEAN and Central Asia: selected secondary indicators",
     ["Indicator / observation", "Value", "Source"],
     [["MSME share of enterprises, ASEAN", "On average > 97% of firms", "ADB (2023)"],
      ["Main SME constraints in Asia", "Finance; databases; R&D; sales channels", "Yoshino & Taghizadeh-Hesary (2016)"],
      ["Uzbekistan \u2013 MSME role", "> 90% of firms; ~75% jobs; ~55% of GDP", "World Bank (2025)"],
      ["Uzbekistan \u2013 e-commerce", "~5\u00d7 growth 2018\u20132022; > USD 0.5 bn (2023)", "World Bank (2023)"],
      ["Uzbekistan \u2013 digital strategy", "Digital Uzbekistan 2030; IT Park (est. 2019)", "World Bank (2023); OECD (2023a)"],
      ["Uzbekistan \u2013 SMEs on e-gov portal", "~10% registered (indicative)", "UNESCAP (2025)"],
      ["Kazakhstan \u2013 digital strategy", "Digital Kazakhstan (since 2017); capability the constraint", "OECD (2023b)"],
      ["Binding constraint (framework)", "Capability: skills, finance, management", "This study"]],
     "Source: Compiled by the authors from the cited institutional sources; the e-government-portal "
     "figure is indicative."),

    ("h1", "5. Management and policy implications"),
    ("p",
     "For the management of the individual SME, the framework implies that investment should be "
     "sequenced according to capability rather than technology fashion. Because the performance "
     "return to adoption rises with capability (equation 3), a firm with weak capabilities gains more "
     "from building sensing and absorptive capacity than from acquiring advanced tools it cannot "
     "embed. The actionable corollary, which goes beyond the general advice to \u201cinvest in "
     "skills\u201d, is a capability-matched adoption rule: a firm should advance to the next, more "
     "demanding digital element only once its capability level has risen to support it, so that DTI "
     "and C grow together along the diagonal of highest return rather than letting adoption outrun "
     "capability."),
    ("p",
     "For policy in Asian emerging economies, the moderation logic yields a concrete diagnostic that "
     "is new to this debate. Because the marginal return to adoption is \u03b2\u2081 + "
     "\u03b2\u2083\u00b7C, a government can estimate the average capability level C\u0304 across its "
     "SME population from existing enterprise-survey data and identify the threshold beyond which "
     "subsidising further technology adoption yields less than investing the same funds in raising "
     "capability \u2014 a calculation national statistical offices could perform with the World Bank "
     "Enterprise Survey instruments already in use. Where C\u0304 is low, as the ASEAN and Central "
     "Asian indicators suggest, the implication is to reallocate support from hardware subsidies "
     "towards skills, advisory and diagnostic services and the SME databases and credit information "
     "that relax the finance constraint identified by Yoshino and Taghizadeh-Hesary (2016)."),
    ("p",
     "Shared public digital infrastructure complements both levers. Interoperable digital-payment "
     "systems, digital identity and the e-government services on which Uzbek SME uptake is only about "
     "ten per cent (UNESCAP, 2025) lower the fixed cost of transformation for the smallest firms and "
     "raise the baseline of the digital-transformation intensity index across the population (OECD & "
     "ERIA, 2024; World Bank, 2023; Asian Development Bank, 2024). Where capability building and "
     "shared infrastructure are neglected and support is confined to hardware, the predictable "
     "outcome is adoption without transformation, and the gap between dynamic and lagging firms "
     "persists."),
    ("h2", "5.1. How to compute the capability-threshold diagnostic"),
    ("p",
     "The capability-threshold diagnostic is computed in four steps. (i) Estimate equation (3) on the "
     "available SME sample to obtain \u03b2\u2081 and \u03b2\u2083. (ii) Recall that the marginal "
     "return to adoption is \u2202\u0394P/\u2202DTI = \u03b2\u2081 + \u03b2\u2083\u00b7C, so the "
     "threshold capability at which an extra unit of adoption begins to pay off (the marginal return "
     "turns positive) is C\u0304 = \u2212\u03b2\u2081 / \u03b2\u2083 when \u03b2\u2081 < 0 and "
     "\u03b2\u2083 > 0. (iii) Compute the average capability of the SME population from the Kump et "
     "al. (2019) scale or its proxies and compare it with C\u0304. (iv) Read off the policy "
     "implication: if the population average lies below C\u0304, the marginal currency unit is better "
     "spent raising capability (skills, advisory services) than subsidising further hardware, and "
     "vice versa. Because C\u0304 depends on estimated coefficients, it should be reported with a "
     "confidence interval and re-estimated as data accumulate."),
    ("h2", "5.2. Checklist for SME managers"),
    ("p", "\u25a1 Compute the firm\u2019s current digital-transformation intensity (DTI) on a 0\u20131 "
          "scale from the adoption items in Section 2.1."),
    ("p", "\u25a1 Assess current capability (C) across sensing, seizing and transforming using the "
          "Kump et al. (2019) items or the observable proxies (digital skills, a written digital "
          "strategy, prior technology projects, staff training)."),
    ("p", "\u25a1 If C is low (below about 0.5): invest first in skills and training, appoint a "
          "decision-owner for digitalisation, and start with foundational tools \u2014 a business "
          "website, professional e-mail, digital payments and cloud-based accounting \u2014 before "
          "moving further."),
    ("p", "\u25a1 If C is high (above about 0.5): advance to data analytics, integrated enterprise "
          "software and, where justified, artificial-intelligence tools, and use them to support "
          "business-model change rather than only to automate existing tasks."),
    ("p", "\u25a1 Advance one digital element at a time, raising DTI only as C rises, so that adoption "
          "and capability grow together (the capability-matched adoption rule)."),
    ("h2", "5.3. Checklist for policymakers"),
    ("p", "\u25a1 Estimate the average SME capability (C\u0304) for the country or sector from "
          "enterprise-survey data and compute the capability threshold as in Section 5.1."),
    ("p", "\u25a1 If average capability is low (below about 0.4): channel public support towards "
          "skills, advisory and diagnostic services, SME databases and credit-information systems "
          "that relax the finance constraint (Yoshino & Taghizadeh-Hesary, 2016), rather than towards "
          "hardware subsidies."),
    ("p", "\u25a1 If average capability is higher (above about 0.6): shift support towards "
          "infrastructure, innovation and advanced-technology adoption, where the marginal return is "
          "now greater."),
    ("p", "\u25a1 In all cases, invest in shared digital public infrastructure \u2014 interoperable "
          "payments, digital identity and single-window e-government such as Uzbekistan\u2019s "
          "my.gov.uz \u2014 which lowers the fixed cost of transformation for the smallest firms; and "
          "monitor SME digital uptake with firm-level surveys rather than infrastructure indicators "
          "alone."),

    ("h1", "Conclusions"),
    ("p",
     "Across ASEAN and Central Asia, the firms that most need the productivity gains of digital "
     "technology \u2014 the small and medium-sized enterprises that dominate employment and output "
     "\u2014 are also those least equipped to realise them. This study argued that the decisive "
     "factor is not access to technology but the managerial capability to absorb it. Integrating the "
     "process view of digital transformation with the dynamic-capabilities perspective, it proposed a "
     "framework linking external drivers, the firm\u2019s sensing, seizing and reconfiguring "
     "capabilities, the depth of the transformation undertaken and the resulting performance, with a "
     "reinvestment feedback loop; it operationalised both digital-transformation intensity and "
     "dynamic capability using existing, validated instruments; and it expressed the core claim as a "
     "single moderation hypothesis that can be estimated on firm-level data. Its distinct "
     "contribution is to combine an explicit capability-conditioned causal structure, an estimable "
     "interaction and a capability-threshold diagnostic, rather than to add another adoption index or "
     "another review."),
    ("p",
     "Assessed in light of secondary indicators from the ASEAN region, Uzbekistan and Kazakhstan, the "
     "framework is consistent with a clear pattern: connectivity and policy ambition advance quickly, "
     "but the capability to turn technology into performance \u2014 skills, finance and management "
     "\u2014 lags behind, a pattern that also conditions whether digital transformation supports the "
     "sustainability goals now linked to it (Mick et al., 2024; Lu & Shaharudin, 2024). The practical "
     "message for managers is to grow adoption and capability together; for policymakers, to use the "
     "capability-threshold diagnostic and to fund skills, finance and shared digital infrastructure "
     "rather than hardware alone. The study\u2019s main limitation is that the moderation is proposed "
     "and illustrated rather than estimated; the numerical example uses didactic inputs, not data. "
     "The clear next step is to estimate equation (3) on firm-level evidence \u2014 the World Bank "
     "Enterprise Surveys, including the 2024 Uzbekistan round, or a dedicated primary survey of Uzbek "
     "and ASEAN SMEs \u2014 which would quantify the interaction \u03b2\u2083 and the capability "
     "threshold and sharpen the policy priorities."),
]

REFERENCES = [
    "Asian Development Bank. (2023). Asia small and medium-sized enterprise monitor 2023. Manila: "
    "Asian Development Bank. https://www.adb.org/publications/asia-sme-monitor-2023",
    "Asian Development Bank. (2024). Digital transformation for inclusive and sustainable "
    "development in Asia. Manila: Asian Development Bank. "
    "https://www.adb.org/publications/digital-transformation-for-inclusive-and-sustainable-development-in-asia",
    "Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business "
    "strategy: Toward a next generation of insights. MIS Quarterly, 37(2), 471\u2013482. "
    "https://doi.org/10.25300/MISQ/2013/37:2.3",
    "Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of "
    "information technology. MIS Quarterly, 13(3), 319\u2013340. https://doi.org/10.2307/249008",
    "de Mattos, C. S., Pellegrini, G., Hagelaar, G., & Dolfsma, W. (2024). Systematic literature "
    "review on technological transformation in SMEs: A transformation encompassing technology "
    "assimilation and business model innovation. Management Review Quarterly, 74(2), 1057\u20131095. "
    "https://doi.org/10.1007/s11301-023-00327-7",
    "Hanelt, A., Bohnsack, R., Marz, D., & Antunes Marante, C. (2021). A systematic review of the "
    "literature on digital transformation: Insights and implications for strategy and organizational "
    "change. Journal of Management Studies, 58(5), 1159\u20131197. https://doi.org/10.1111/joms.12639",
    "Kraus, S., Durst, S., Ferreira, J. J., Veiga, P., Kailer, N., & Weinmann, A. (2022). Digital "
    "transformation in business and management research: An overview of the current status quo. "
    "International Journal of Information Management, 63, 102466. "
    "https://doi.org/10.1016/j.ijinfomgt.2021.102466",
    "Kump, B., Engelmann, A., Kessler, A., & Schweiger, C. (2019). Toward a dynamic capabilities "
    "scale: Measuring organizational sensing, seizing, and transforming capacities. Industrial and "
    "Corporate Change, 28(5), 1149\u20131172. https://doi.org/10.1093/icc/dty054",
    "Lu, Z., & Shaharudin, M. S. (2024). Role of digital transformation for sustainable competitive "
    "advantage of SMEs: A systematic literature review. Cogent Business & Management, 11(1), "
    "2419489. https://doi.org/10.1080/23311975.2024.2419489",
    "Mick, A. C., Kovaleski, J. L., & Chiroli, D. M. de G. (2024). Sustainable digital transformation "
    "roadmaps for SMEs: A systematic literature review. Sustainability, 16(19), 8551. "
    "https://doi.org/10.3390/su16198551",
    "Nambisan, S., Wright, M., & Feldman, M. (2019). The digital transformation of innovation and "
    "entrepreneurship: Progress, challenges and key themes. Research Policy, 48(8), 103773. "
    "https://doi.org/10.1016/j.respol.2019.03.018",
    "OECD. (2021a). The digital transformation of SMEs. Paris: OECD Publishing. "
    "https://doi.org/10.1787/bdb9256a-en",
    "OECD. (2021b). Beyond COVID-19: Prospects for economic recovery in Central Asia. Paris: OECD "
    "Publishing. https://doi.org/10.1787/03882e7b-en",
    "OECD. (2023a). Digital skills for private sector competitiveness in Uzbekistan. Paris: OECD "
    "Publishing. https://doi.org/10.1787/6c54f447-en",
    "OECD. (2023b). Improving framework conditions for the digital transformation of businesses in "
    "Kazakhstan. Paris: OECD Publishing. https://doi.org/10.1787/368d4d01-en",
    "OECD, & ERIA. (2024). SME Policy Index: ASEAN 2024 \u2013 Enabling sustainable growth and "
    "digitalisation. Paris: OECD Publishing / Jakarta: Economic Research Institute for ASEAN and East "
    "Asia. https://doi.org/10.1787/f1f0c5f3-en",
    "Sagala, G. H., & \u0150ri, D. (2024). Toward SMEs digital transformation success: A systematic "
    "literature review. Information Systems and e-Business Management, 22(4), 667\u2013719. "
    "https://doi.org/10.1007/s10257-024-00682-2",
    "Teece, D. J. (2007). Explicating dynamic capabilities: The nature and microfoundations of "
    "(sustainable) enterprise performance. Strategic Management Journal, 28(13), 1319\u20131350. "
    "https://doi.org/10.1002/smj.640",
    "Teng, X., Wu, Z., & Yang, F. (2022). Research on the relationship between digital transformation "
    "and performance of SMEs. Sustainability, 14(10), 6012. https://doi.org/10.3390/su14106012",
    "Tornatzky, L. G., & Fleischer, M. (1990). The processes of technological innovation. Lexington, "
    "MA: Lexington Books.",
    "UNESCAP. (2025). Uzbekistan foresight on digital public services for small and medium-sized "
    "enterprises [Foresight workshop]. Bangkok: United Nations Economic and Social Commission for "
    "Asia and the Pacific. "
    "https://www.unescap.org/events/2025/uzbekistan-foresight-digital-public-services-small-and-medium-sized-enterprises",
    "Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of "
    "information technology: Toward a unified view. MIS Quarterly, 27(3), 425\u2013478. "
    "https://doi.org/10.2307/30036540",
    "Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong, J., Fabian, N., & "
    "Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. "
    "Journal of Business Research, 122, 889\u2013901. https://doi.org/10.1016/j.jbusres.2019.09.022",
    "Vial, G. (2019). Understanding digital transformation: A review and a research agenda. The "
    "Journal of Strategic Information Systems, 28(2), 118\u2013144. "
    "https://doi.org/10.1016/j.jsis.2019.01.003",
    "Warner, K. S. R., & W\u00e4ger, M. (2019). Building dynamic capabilities for digital "
    "transformation: An ongoing process of strategic renewal. Long Range Planning, 52(3), "
    "326\u2013349. https://doi.org/10.1016/j.lrp.2018.12.001",
    "Westerman, G., Bonnet, D., & McAfee, A. (2014). Leading digital: Turning technology into "
    "business transformation. Boston, MA: Harvard Business Review Press.",
    "World Bank. (2023). Supporting Uzbekistan in developing the digital economy and creating new "
    "jobs in the information technology sector [Country update]. Washington, DC: World Bank. "
    "https://www.worldbank.org/en/news/press-release/2023/11/30/world-bank-to-support-uzbekistan-in-developing-the-digital-economy-and-creating-new-jobs-in-the-it-sector",
    "World Bank. (2024). World Bank Enterprise Survey 2024: Uzbekistan (UZB_2024_WBES) [Data set]. "
    "Washington, DC: World Bank Group. https://microdata.worldbank.org/index.php/catalog/6711",
    "World Bank. (2025). Improved access to finance to help businesses in Uzbekistan grow and create "
    "jobs [Country update]. Washington, DC: World Bank. "
    "https://www.worldbank.org/en/news/press-release/2025/12/15/improved-access-to-finance-to-help-7000-businesses-in-uzbekistan-grow-and-create-jobs",
    "Yoshino, N., & Taghizadeh-Hesary, F. (2016). Major challenges facing small and medium-sized "
    "enterprises in Asia and solutions for mitigating them (ADBI Working Paper No. 564). Tokyo: Asian "
    "Development Bank Institute. "
    "https://www.adb.org/publications/major-challenges-facing-small-and-medium-sized-enterprises-asia-and-solutions",
]
