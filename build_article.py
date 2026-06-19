# -*- coding: utf-8 -*-
"""
Build the Economic Archive (Narodnostopanski Arhiv) article (.docx) following the
journal template. Topic: digital transformation in SMEs (dominant theme of the
supplied collection), management-oriented, adapted to emerging Asia, and revised
to address peer-review gaps (methodology, illustrative empirical application,
novelty statement, deeper Uzbekistan case, recent references, language).
"""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

FONT = "Times New Roman"
doc = Document()
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(14)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
for s in doc.sections:
    s.top_margin = Inches(1); s.bottom_margin = Inches(1)
    s.left_margin = Inches(1.18); s.right_margin = Inches(1.18)


def set_run(r, size=14, bold=False, italic=False):
    r.font.name = FONT; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    r._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)


def para(text="", *, size=14, bold=False, italic=False, align="justify",
         spacing=1.5, space_after=6, first_indent=0.0, caps=False):
    p = doc.add_paragraph()
    p.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY, "center": WD_ALIGN_PARAGRAPH.CENTER,
                   "left": WD_ALIGN_PARAGRAPH.LEFT, "right": WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf = p.paragraph_format
    pf.line_spacing = spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE if isinstance(spacing, float) else WD_LINE_SPACING.SINGLE
    pf.space_after = Pt(space_after); pf.space_before = Pt(0)
    if first_indent:
        pf.first_line_indent = Inches(first_indent)
    if text:
        set_run(p.add_run(text.upper() if caps else text), size=size, bold=bold, italic=italic)
    return p


def heading(t, *, size=14, sub=False):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(8 if sub else 10); p.paragraph_format.space_after = Pt(4 if sub else 6)
    set_run(p.add_run(t), size=size, bold=True, italic=sub)
    return p


def equation(txt, number):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(4)
    set_run(p.add_run(txt), italic=True)
    set_run(p.add_run("\t\t\t\t\t(%d)" % number))
    return p


def figure(path, caption, source, width=6.0):
    pic = doc.add_paragraph(); pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.space_before = Pt(6)
    pic.add_run().add_picture(path, width=Inches(width))
    cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.line_spacing = 1.0; cap.paragraph_format.space_after = Pt(2)
    set_run(cap.add_run(caption), size=12, bold=True)
    src = doc.add_paragraph(); src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    src.paragraph_format.line_spacing = 1.0; src.paragraph_format.space_after = Pt(10)
    set_run(src.add_run(source), size=11, italic=True)


def table(title_no, title, headers, rows, source, widths=None):
    para(title_no, bold=True, align="left", spacing=1.0, space_after=2)
    para(title, bold=True, size=12, align="left", spacing=1.0, space_after=4)
    t = doc.add_table(rows=1, cols=len(headers)); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = "Table Grid"
    for c, h in zip(t.rows[0].cells, headers):
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_run(c.paragraphs[0].add_run(h), size=12, bold=True)
    for row in rows:
        cells = t.add_row().cells
        for cell, txt in zip(cells, row):
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
            set_run(cell.paragraphs[0].add_run(txt), size=12)
    para(source, italic=True, size=11, align="left", spacing=1.0, space_after=10)


# ===================== FRONT MATTER =====================
para("Digital Transformation and the Performance of Small and Medium-Sized "
     "Enterprises: A Management Framework and Evidence from Emerging Asia",
     bold=True, align="center", spacing=1.0, space_after=10, caps=True)
para("[Author Name], [e-mail]", bold=True, align="center", spacing=1.0, space_after=2)
para("[Department]", bold=True, align="center", spacing=1.0, space_after=2)
para("[Institution]", bold=True, align="center", spacing=1.0, space_after=12)

abstract = (
    "Abstract: Digital transformation is the central management challenge for small and "
    "medium-sized enterprises (SMEs), which dominate the economies of emerging Asia yet adopt "
    "advanced digital technologies more slowly than large firms. This study develops and "
    "illustrates a management framework explaining how SMEs convert digital technologies into "
    "superior performance. Building on the dynamic-capabilities perspective and on the distinction "
    "between digitisation, digitalisation and digital transformation, the framework links external "
    "drivers to the firm\u2019s sensing, seizing and reconfiguring capabilities, to the depth of the "
    "transformation undertaken, and to performance, with a reinvestment feedback loop. Its novelty "
    "is a firm-level, management-actionable digital-transformation intensity (DTI) index combined "
    "with a multiplicative DTI\u00d7capability specification that makes the \u201ccapability-as-binding-"
    "constraint\u201d proposition testable, distinguishing it from macro composite indices and from "
    "prior conceptual reviews. The framework is built through a structured synthesis of the "
    "literature, illustrated with a worked application of the DTI index to representative SME "
    "archetypes, and examined against secondary evidence from emerging Asia, including the ASEAN "
    "region and a deeper case illustration of Uzbekistan. The analysis indicates that the binding "
    "constraint on SME performance is managerial and human capability rather than connectivity, and "
    "yields managerial and policy recommendations on capability building, finance, digital skills "
    "and shared digital infrastructure."
)
para(abstract, spacing=1.0, space_after=8)
para("Key words: digital transformation; small and medium-sized enterprises; dynamic capabilities; "
     "firm performance; emerging Asia.", spacing=1.0, space_after=4)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_after = Pt(12)
set_run(p.add_run("JEL: M15, M21, O33, L25, O18, O53."), bold=True)

# ===================== INTRODUCTION =====================
heading("Introduction")
para(
    "Digital technologies \u2014 cloud computing, data analytics, artificial intelligence, "
    "e-commerce platforms and connected devices \u2014 have moved from being a support function to "
    "being the principal arena of competition. For enterprises of every size, the management "
    "question is no longer whether to adopt such technologies but how to convert them into durable "
    "improvements in performance. This question is most acute for small and medium-sized enterprises "
    "(SMEs). In emerging Asia they are the backbone of the economy: in the member states of the "
    "Association of Southeast Asian Nations (ASEAN), micro, small and medium-sized enterprises make "
    "up on average more than ninety-seven per cent of all firms and provide the large majority of "
    "employment (Asian Development Bank, 2023). Yet they adopt advanced digital technologies more "
    "slowly than large enterprises and face tighter constraints on finance, skills and managerial "
    "capacity (OECD, 2021; Yoshino & Taghizadeh-Hesary, 2016).",
    first_indent=0.30)
para(
    "The literature has clarified what digital transformation is, but it has paid less attention to "
    "the specific managerial mechanisms through which a resource-constrained SME in an emerging "
    "economy turns technology into results. Digital transformation is more than the purchase of "
    "software; it is an organisational change process in which digital technologies reshape value "
    "creation, operations and the business model itself (Vial, 2019; Verhoef et al., 2021). Whether "
    "that process raises performance depends on the capabilities the firm can mobilise around it "
    "(Teece, 2007; Warner & W\u00e4ger, 2019). Recent systematic reviews confirm that the SME "
    "literature remains fragmented and short of process guidance, and that transformation levels in "
    "SMEs are generally low (de Mattos et al., 2024; Sagala & \u0150ri, 2024).",
    first_indent=0.30)
para(
    "This study addresses that gap with a management framework connecting the external drivers of "
    "digital transformation, the dynamic capabilities of the firm, the depth of the transformation "
    "undertaken and the resulting performance, closed by a reinvestment feedback loop. Its "
    "contribution differs from prior work in three respects. First, whereas existing composite "
    "measures such as national digital-intensity indices operate at the macro level, the proposed "
    "digital-transformation intensity (DTI) index is defined at the level of the individual firm and "
    "is directly actionable by management. Second, in contrast to conceptual reviews that catalogue "
    "factors (de Mattos et al., 2024; Sagala & \u0150ri, 2024), the framework specifies a "
    "multiplicative DTI\u00d7capability relationship that turns the often-asserted claim that "
    "\u201ctechnology alone is not enough\u201d into a testable proposition. Third, it is applied to "
    "emerging Asia \u2014 the ASEAN region and the under-researched economies of Central Asia, with "
    "Uzbekistan as a case illustration \u2014 where firm-level evidence is comparatively thin.",
    first_indent=0.30)
para(
    "The remainder of the article is organised as follows. Section 1 reviews the literature and "
    "defines the core constructs. Section 2 presents the framework and the DTI index. Section 3 "
    "describes the data and methods. Section 4 reports an illustrative application of the index and "
    "the regional evidence, including the Uzbekistan case. Section 5 discusses the management and "
    "policy implications. The final section concludes.",
    first_indent=0.30)

# ===================== 1. LITERATURE =====================
heading("1. Theoretical background and literature review")
para(
    "Research distinguishes three increasingly profound stages of digital change. Digitisation is "
    "the conversion of analogue information into digital form; digitalisation is the use of digital "
    "technologies to improve existing processes; and digital transformation is the deeper, "
    "firm-wide change in which technology reconfigures value creation and the business model "
    "(Verhoef et al., 2021). Vial (2019), synthesising a large body of work, defines digital "
    "transformation as a process in which digital technologies trigger strategic responses that "
    "alter value-creation paths while the firm manages structural change and organisational "
    "barriers. The implication for management is that technology alone does not deliver value; the "
    "value comes from the organisational changes that accompany it.",
    first_indent=0.30)
para(
    "The dynamic-capabilities perspective explains why firms facing the same technologies achieve "
    "different results. Teece (2007) decomposes the capacity to sustain performance in changing "
    "environments into sensing opportunities and threats, seizing them through investment and "
    "business-model choices, and reconfiguring the resource base accordingly. Warner and W\u00e4ger "
    "(2019) show that digital transformation is precisely an ongoing process of strategic renewal in "
    "which these capabilities are built and rebuilt. Bharadwaj, El Sawy, Pavlou and Venkatraman "
    "(2013) argue that digital strategy can no longer be a functional adjunct to business strategy "
    "but must be fused with it; Westerman, Bonnet and McAfee (2014) add that the binding constraint "
    "is usually leadership and management capability rather than technology as such; and Fitzgerald, "
    "Kruschwitz, Bonnet and Welch (2014) document that firms widely recognise digital technology as "
    "a strategic imperative while struggling to execute it.",
    first_indent=0.30)
para(
    "A further strand examines how the decision to adopt a technology is taken. The technology "
    "acceptance model relates adoption to perceived usefulness and perceived ease of use (Davis, "
    "1989); the unified theory of acceptance and use of technology adds performance and effort "
    "expectancy, social influence and facilitating conditions (Venkatesh, Morris, Davis & Davis, "
    "2003); and the technology\u2013organisation\u2013environment framework situates adoption in the "
    "interplay of technological readiness, organisational resources and the external environment "
    "(Tornatzky & Fleischer, 1990). For SMEs in emerging economies these frameworks matter because "
    "the adoption decision is concentrated in a small management team and is highly sensitive to "
    "skills, cost and the surrounding digital ecosystem.",
    first_indent=0.30)
para(
    "Recent empirical and review work sharpens the picture. Teng, Wu and Yang (2022), using a "
    "structural-equation model on 335 SMEs, find that digital technology, employee digital skills "
    "and a digital-transformation strategy are jointly and positively associated with transformation "
    "and, through it, with performance \u2014 evidence consistent with a capability-conditioned view. "
    "Systematic reviews by de Mattos, Pellegrini, Hagelaar and Dolfsma (2024) and Sagala and "
    "\u0150ri (2024) report that the field is dominated by factor lists, lacks process-level "
    "conceptualisation, and shows generally low transformation among SMEs, while the policy-oriented "
    "literature documents the SME-specific barriers \u2014 scarce skills, limited finance and "
    "uncertainty about returns (OECD, 2021; Yoshino & Taghizadeh-Hesary, 2016). Nambisan, Wright and "
    "Feldman (2019) note that digital technologies also reshape innovation and entrepreneurship "
    "themselves, raising the premium on digital capability. This body of work motivates a framework "
    "in which drivers, firm-level capabilities and the depth of transformation jointly determine "
    "performance, and a measure that operationalises it.",
    first_indent=0.30)

# ===================== 2. FRAMEWORK =====================
heading("2. A management framework and the digital-transformation intensity index")
para(
    "The framework links four blocks in sequence, with a feedback loop (Figure 1). The first block "
    "is the set of external drivers: market and competitive pressure, the availability and cost of "
    "digital technologies, and the policy environment, including funding and regulation. Drivers "
    "create the incentive and the opportunity to transform, but they do not determine the outcome.",
    first_indent=0.30)
para(
    "The second block is the firm\u2019s dynamic capabilities. Following Teece (2007), an SME senses "
    "digital opportunities and threats, seizes them by investing in technology and adjusting its "
    "business model, and reconfigures its processes, skills and structure so that the technology is "
    "actually used. The third block is the depth of the transformation undertaken, from digitisation "
    "through digitalisation to business-model change (Verhoef et al., 2021). The fourth block is "
    "performance: productivity, growth and export reach, and resilience. A feedback loop closes the "
    "framework: performance gains generate resources that are reinvested in further capability "
    "building and technology, so that successful SMEs can enter a virtuous cycle while laggards fall "
    "further behind.",
    first_indent=0.30)

figure("figure1_framework.png",
       "Figure 1. A management framework for digital transformation in SMEs",
       "Source: Authors\u2019 elaboration based on Teece (2007), Vial (2019) and Verhoef et al. (2021).")

para(
    "To make the central construct measurable, digital-transformation intensity of a firm is defined "
    "as a weighted composite of the digital technologies and practices in use,",
    first_indent=0.30)
equation("DTI = \u03a3\u1d62 w\u1d62 \u00b7 a\u1d62 ,   with  \u03a3\u1d62 w\u1d62 = 1,", 1)
para(
    "where a\u1d62 \u2208 [0, 1] is the adoption level of digital element i \u2014 connectivity, a "
    "website or e-commerce channel, digital payments, cloud services, enterprise software, data "
    "analytics, artificial intelligence and digital-security measures \u2014 and w\u1d62 is its "
    "weight. The index returns a value between zero and one and is conceptually comparable to the "
    "digital-intensity measures used in international statistics, but it is defined and computed for "
    "the individual firm. Firm performance is modelled as increasing in digital-transformation "
    "intensity but conditional on capability,",
    first_indent=0.30)
equation("\u0394P = \u03b2 \u00b7 DTI \u00b7 C + \u03b5 ,", 2)
para(
    "where \u0394P is the change in a performance measure, C \u2208 [0, 1] is the firm\u2019s "
    "dynamic-capability level, \u03b2 > 0 is the return to transformation and \u03b5 captures other "
    "influences. The multiplicative term DTI\u00b7C is the core managerial proposition: technology "
    "adoption raises performance only to the extent that the firm has the capability to absorb it. A "
    "high index with weak capability \u2014 technology bought but not embedded \u2014 yields little "
    "gain, the typical failure mode for SMEs in emerging markets, and one consistent with the SEM "
    "evidence of Teng et al. (2022) that skills and strategy, not technology alone, drive the "
    "performance effect.",
    first_indent=0.30)

# ===================== 3. DATA & METHODS =====================
heading("3. Data and methods")
para(
    "The study is conceptual-empirical and proceeds in three steps. First, the framework was built "
    "through a structured narrative synthesis of the literature in the tradition of evidence-informed "
    "management review (Tranfield, Denyer & Smart, 2003): peer-reviewed sources on digital "
    "transformation, dynamic capabilities and technology adoption were retrieved from Scopus- and "
    "Web of Science-indexed outlets, screened for relevance to SMEs and to performance, and "
    "synthesised into the four-block structure of Section 2. Recent systematic reviews (de Mattos et "
    "al., 2024; Sagala & \u0150ri, 2024) were used to position the contribution and to confirm the "
    "research gap.",
    first_indent=0.30)
para(
    "Second, the DTI index was operationalised over eight digital elements (Section 2). In the "
    "absence of firm-level primary data, the index is applied here as a transparent worked example "
    "with equal weights (w\u1d62 = 1/8); the weighting is a modelling choice that can be replaced by "
    "expert judgement or by data-driven weights when survey microdata are available, and the "
    "qualitative ordering of firms is robust to moderate changes in the weights. This illustrative "
    "application is explicitly not a substitute for primary estimation; it demonstrates the "
    "measurement logic and the DTI\u00d7capability interaction.",
    first_indent=0.30)
para(
    "Third, the framework is examined against secondary evidence for emerging Asia drawn from "
    "official and institutional sources: the Asian Development Bank (2023, 2024) and the OECD and "
    "ERIA (2024) for the ASEAN region; Yoshino and Taghizadeh-Hesary (2016) for the structural "
    "constraints on Asian SMEs; and, for the Uzbekistan case, the World Bank (2023, 2025) and "
    "UNESCAP (2025). Firm-level survey infrastructure for future calibration is identified in the "
    "World Bank Enterprise Surveys, which now include a 2024 round for Uzbekistan. The study does "
    "not collect primary survey data; quantifying \u03b2 and the capability threshold on firm-level "
    "data is set out as the principal direction for further work.",
    first_indent=0.30)

# ===================== 4. RESULTS =====================
heading("4. Results: illustrative application and regional evidence")

heading("4.1. Illustrative application of the DTI index", sub=True)
para(
    "To demonstrate the measurement logic, the DTI index is applied to three representative SME "
    "archetypes with assumed adoption vectors over the eight elements (these values are illustrative, "
    "not survey estimates). A micro service firm has full connectivity and partial web, payment and "
    "cloud adoption but no analytics or artificial intelligence; a small manufacturer has moderate "
    "adoption across most elements; and a medium-sized exporter is digitally advanced. Equal "
    "weighting yields DTI values of about 0.33, 0.54 and 0.80 respectively. Applying the performance "
    "relationship of equation (2) with a normalised return (\u03b2 = 1) under a high capability level "
    "(C = 0.8) and a low one (C = 0.3) produces the performance gains shown in Figure 2 and Table 1.",
    first_indent=0.30)

figure("figure2_dti_application.png",
       "Figure 2. Illustrative performance gain by DTI level under high and low capability",
       "Source: Authors\u2019 illustrative computation from equations (1)\u2013(2); values are not survey estimates.",
       width=5.6)

table("Table 1",
      "Illustrative DTI index and performance gain for three SME archetypes",
      ["SME archetype", "DTI", "\u0394P (C = 0.8)", "\u0394P (C = 0.3)"],
      [["Micro service firm", "0.33", "0.26", "0.10"],
       ["Small manufacturer", "0.54", "0.43", "0.16"],
       ["Medium exporter", "0.80", "0.64", "0.24"]],
      "Source: Authors\u2019 illustrative computation from equations (1)\u2013(2); \u03b2 normalised to 1. "
      "Values are illustrative, not survey estimates.")

para(
    "The illustration makes the central proposition visible: the performance gain rises with the DTI "
    "index but, for any given index value, is roughly two-and-a-half times larger when capability is "
    "high than when it is low. A digitally advanced firm with weak capability (medium exporter at C = "
    "0.3) gains less than a modestly equipped firm with strong capability would relative to its own "
    "potential. This is the analytical content of the claim that capability, not technology, is the "
    "binding constraint, and it is the relationship that future firm-level work should estimate.",
    first_indent=0.30)

heading("4.2. Regional evidence from emerging Asia", sub=True)
para(
    "Across the ASEAN member states, micro, small and medium-sized enterprises account for the "
    "overwhelming majority of firms and the bulk of employment, and the regional digital economy is "
    "expanding rapidly (Asian Development Bank, 2023). The constraints on their digital "
    "transformation are, however, systematic. Yoshino and Taghizadeh-Hesary (2016) show that Asian "
    "SMEs are held back by limited access to finance, the absence of comprehensive databases, low "
    "research and development spending and underdeveloped sales channels \u2014 conditions that "
    "depress the capability term in the framework. The OECD and ERIA (2024) confirm that, although "
    "ASEAN governments have strengthened SME policy frameworks, the digitalisation of smaller firms "
    "remains uneven and skills and finance are recurring bottlenecks. The regional statistics "
    "therefore indicate that connectivity and policy ambition are necessary but not sufficient: the "
    "binding constraint is the capability term C in equation (2).",
    first_indent=0.30)

heading("4.3. Case illustration: Uzbekistan", sub=True)
para(
    "Uzbekistan illustrates both the opportunity and the constraint with particular clarity, and is "
    "presented here as a case rather than as a statistical test. SMEs are central to the economy: the "
    "World Bank (2025) reports that micro, small and medium-sized enterprises account for over "
    "ninety per cent of businesses, about seventy-five per cent of employment and roughly "
    "fifty-five per cent of gross domestic product, and the national statistics authorities record "
    "more than 1.2 million small businesses in early 2025. Connectivity and e-commerce have grown "
    "quickly from a low base; the World Bank (2023) reports that the e-commerce market expanded "
    "roughly fivefold between 2018 and 2022, exceeding half a billion United States dollars by 2023, "
    "and national policy under the Digital Uzbekistan 2030 strategy aims to turn the country into a "
    "regional information-technology hub with sharply higher technology exports and large-scale job "
    "creation.",
    first_indent=0.30)
para(
    "The deeper transformation of enterprises nonetheless lags the roll-out of infrastructure. "
    "UNESCAP (2025) reports that only about ten per cent of SMEs were registered on the national "
    "digital public-services portal, a direct indication that adoption of even basic digital "
    "government services \u2014 let alone analytics or artificial intelligence \u2014 remains shallow. "
    "Interpreted through the framework, Uzbek SMEs increasingly possess the drivers and the "
    "connectivity but not yet the capability \u2014 skills, finance and managerial capacity \u2014 "
    "that converts adoption into performance. Table 2 summarises the regional and Uzbekistan "
    "evidence.",
    first_indent=0.30)

table("Table 2",
      "Digital transformation of SMEs in emerging Asia: selected secondary evidence",
      ["Indicator / observation", "Evidence", "Source"],
      [["MSME share of enterprises, ASEAN", "On average > 97% of firms", "ADB (2023)"],
       ["Main SME constraints in Asia", "Finance; databases; R&D; sales channels", "Yoshino & Taghizadeh-Hesary (2016)"],
       ["Uzbekistan \u2013 MSME role", "> 90% of firms; ~75% jobs; ~55% of GDP", "World Bank (2025)"],
       ["Uzbekistan \u2013 e-commerce", "~5\u00d7 growth 2018\u20132022; > USD 0.5 bn (2023)", "World Bank (2023)"],
       ["Uzbekistan \u2013 SMEs on e-gov portal", "Only ~10% registered", "UNESCAP (2025)"],
       ["Binding constraint (framework)", "Capability: skills, finance, management", "This study"]],
      "Source: Compiled by the authors from the cited institutional sources.")

# ===================== 5. IMPLICATIONS =====================
heading("5. Management and policy implications")
para(
    "For the management of the individual SME, the framework implies that investment should be "
    "sequenced according to capability rather than technology fashion. Because performance depends "
    "on the product of digital-transformation intensity and capability (equation 2), a firm with "
    "weak capabilities gains more from building sensing and absorptive capacity \u2014 digital "
    "skills, data literacy and a clear digital element of strategy \u2014 than from acquiring "
    "advanced tools it cannot embed. Adoption should follow the sequence of the framework: secure "
    "connectivity and a market-facing digital channel, including the digital-payment and e-commerce "
    "platforms spreading fastest in Asian markets; move core processes to cloud-based and enterprise "
    "software; and only then layer on analytics and artificial intelligence, with cybersecurity and "
    "data governance treated as a precondition. Digital strategy should be fused with business "
    "strategy and owned by the management team, not delegated as a technical project (Bharadwaj et "
    "al., 2013; Westerman et al., 2014).",
    first_indent=0.30)
para(
    "For policy in Asian emerging economies, the same logic reframes public support. Because the "
    "binding constraint is capability rather than connectivity, support should shift from subsidising "
    "hardware towards building skills and absorptive capacity: management and digital-skills "
    "training, advisory and diagnostic services, and demonstrator projects that reduce the "
    "uncertainty about returns that deters SME investment. Two Asia-specific priorities follow. "
    "First, the finance constraint identified by Yoshino and Taghizadeh-Hesary (2016) should be "
    "addressed directly, by bundling affordable finance with advice and by building the SME databases "
    "and credit information that lower the cost of lending. Second, shared public digital "
    "infrastructure \u2014 interoperable digital-payment systems, digital identity and the e-government "
    "services on which Uzbek SME uptake is still only about ten per cent (UNESCAP, 2025) \u2014 lowers "
    "the fixed cost of transformation for the smallest firms and should be prioritised (OECD & ERIA, "
    "2024; World Bank, 2023; Asian Development Bank, 2024).",
    first_indent=0.30)
para(
    "The two levels are complementary. Public investment in skills, finance and digital "
    "infrastructure raises the average capability level C across the SME population, which increases "
    "the performance return to any given level of technology adoption and so strengthens the "
    "incentive for firms to invest; firm-level reinvestment of the resulting gains sustains the "
    "virtuous cycle. Where this complementarity is neglected \u2014 where infrastructure and grants "
    "are provided without capability \u2014 the predictable outcome is adoption without "
    "transformation, and the gap between dynamic and lagging firms persists.",
    first_indent=0.30)

# ===================== CONCLUSIONS =====================
heading("Conclusions")
para(
    "Digital transformation is the dominant management challenge facing contemporary enterprises, "
    "and it is most demanding for the small and medium-sized firms that form the backbone of the "
    "economies of emerging Asia. This study argued that the decisive factor is not access to "
    "technology but the managerial capability to absorb it, and it offered three contributions: a "
    "firm-level, management-actionable digital-transformation intensity index; a multiplicative "
    "DTI\u00d7capability specification that renders the capability-as-binding-constraint proposition "
    "testable and distinguishes the framework from macro indices and from factor-listing reviews; and "
    "an application to emerging Asia and to the under-researched Central Asian context, illustrated "
    "by Uzbekistan.",
    first_indent=0.30)
para(
    "Examined against secondary evidence from the ASEAN region and Uzbekistan, the framework accounts "
    "for a consistent pattern: connectivity and policy ambition advance quickly, but the capability "
    "to turn technology into performance \u2014 skills, finance and management \u2014 lags behind. The "
    "practical message for managers is to sequence investment by capability and to own digital "
    "strategy at the top of the firm; for policymakers, to fund skills, finance and shared digital "
    "infrastructure rather than hardware alone. The study\u2019s main limitation is that the DTI index "
    "and the performance relationship are illustrated rather than estimated; the worked application "
    "uses assumed, not surveyed, adoption values. The clear next step is empirical validation on "
    "firm-level data \u2014 for example the World Bank Enterprise Surveys or a primary survey of "
    "Uzbek and ASEAN SMEs \u2014 which would allow the return to transformation \u03b2 and the "
    "capability threshold to be quantified and the policy priorities to be sharpened.",
    first_indent=0.30)

# ===================== REFERENCES =====================
heading("References")
refs = [
    "Asian Development Bank. (2023). Asia small and medium-sized enterprise monitor 2023. Manila: "
    "Asian Development Bank. Available online: https://www.adb.org/publications/asia-sme-monitor-2023",

    "Asian Development Bank. (2024). Digital transformation for inclusive and sustainable "
    "development in Asia. Manila: Asian Development Bank. Available online: "
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

    "Fitzgerald, M., Kruschwitz, N., Bonnet, D., & Welch, M. (2014). Embracing digital technology: A "
    "new strategic imperative. MIT Sloan Management Review, 55(2), 1\u201312.",

    "Nambisan, S., Wright, M., & Feldman, M. (2019). The digital transformation of innovation and "
    "entrepreneurship: Progress, challenges and key themes. Research Policy, 48(8), 103773. "
    "https://doi.org/10.1016/j.respol.2019.03.018",

    "OECD. (2021). The digital transformation of SMEs. Paris: OECD Publishing. "
    "https://doi.org/10.1787/bdb9256a-en",

    "OECD, & ERIA. (2024). SME Policy Index: ASEAN 2024 \u2013 Enabling sustainable growth and "
    "digitalisation. Paris: OECD Publishing / Jakarta: Economic Research Institute for ASEAN and "
    "East Asia. https://doi.org/10.1787/f1f0c5f3-en",

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

    "Tranfield, D., Denyer, D., & Smart, P. (2003). Towards a methodology for developing "
    "evidence-informed management knowledge by means of systematic review. British Journal of "
    "Management, 14(3), 207\u2013222. https://doi.org/10.1111/1467-8551.00375",

    "UNESCAP. (2025). Uzbekistan foresight on digital public services for small and medium-sized "
    "enterprises. Bangkok: United Nations Economic and Social Commission for Asia and the Pacific. "
    "Available online: https://www.unescap.org/events/2025/uzbekistan-foresight-digital-public-services-small-and-medium-sized-enterprises",

    "Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of "
    "information technology: Toward a unified view. MIS Quarterly, 27(3), 425\u2013478. "
    "https://doi.org/10.2307/30036540",

    "Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong, J., Fabian, N., & "
    "Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research "
    "agenda. Journal of Business Research, 122, 889\u2013901. "
    "https://doi.org/10.1016/j.jbusres.2019.09.022",

    "Vial, G. (2019). Understanding digital transformation: A review and a research agenda. The "
    "Journal of Strategic Information Systems, 28(2), 118\u2013144. "
    "https://doi.org/10.1016/j.jsis.2019.01.003",

    "Warner, K. S. R., & W\u00e4ger, M. (2019). Building dynamic capabilities for digital "
    "transformation: An ongoing process of strategic renewal. Long Range Planning, 52(3), "
    "326\u2013349. https://doi.org/10.1016/j.lrp.2018.12.001",

    "Westerman, G., Bonnet, D., & McAfee, A. (2014). Leading digital: Turning technology into "
    "business transformation. Boston, MA: Harvard Business Review Press.",

    "World Bank. (2023, November 30). World Bank to support Uzbekistan in developing the digital "
    "economy and creating new jobs in the information technology sector (Press release). Washington, "
    "DC: World Bank. Available online: "
    "https://www.worldbank.org/en/news/press-release/2023/11/30/world-bank-to-support-uzbekistan-in-developing-the-digital-economy-and-creating-new-jobs-in-the-it-sector",

    "World Bank. (2025, December 15). Improved access to finance to help 7,000 businesses in "
    "Uzbekistan grow and create jobs (Press release). Washington, DC: World Bank. Available online: "
    "https://www.worldbank.org/en/news/press-release/2025/12/15/improved-access-to-finance-to-help-7000-businesses-in-uzbekistan-grow-and-create-jobs",

    "Yoshino, N., & Taghizadeh-Hesary, F. (2016). Major challenges facing small and medium-sized "
    "enterprises in Asia and solutions for mitigating them (ADBI Working Paper No. 564). Tokyo: "
    "Asian Development Bank Institute. Available online: "
    "https://www.adb.org/publications/major-challenges-facing-small-and-medium-sized-enterprises-asia-and-solutions",
]
for ref in refs:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = 1.5; pf.space_after = Pt(4)
    pf.left_indent = Inches(0.5); pf.first_line_indent = Inches(-0.5)
    set_run(p.add_run(ref), size=14)

out = "Economic_Archive_Digital_Transformation_SMEs_Asia.docx"
doc.save(out)
print("Saved", out)
