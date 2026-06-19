# -*- coding: utf-8 -*-
"""
Build the Economic Archive (Narodnostopanski Arhiv) article as a .docx that
follows the journal template (m9_Template_BM_eng.doc).

Topic: the dominant theme in the supplied 600+ page collection of recently
accepted articles - DIGITAL TRANSFORMATION / technology adoption in enterprises,
with a strong SME focus - reframed toward management and adapted to the ASIAN
context (emerging Asia: ASEAN and Central Asia / Uzbekistan).
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
    r.font.name = FONT; r.font.size = Pt(size)
    r.bold = bold; r.italic = italic
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
        r = p.add_run(text.upper() if caps else text)
        set_run(r, size=size, bold=bold, italic=italic)
    return p


def heading(t, *, size=14):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(t); set_run(r, size=size, bold=True)
    return p


def equation(txt, number):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(4)
    r = p.add_run(txt); set_run(r, italic=True)
    r2 = p.add_run("\t\t\t\t\t(%d)" % number); set_run(r2)
    return p


# ===================== FRONT MATTER =====================
para("Digital Transformation and the Performance of Small and Medium-Sized "
     "Enterprises: A Management Framework and Evidence from Emerging Asia",
     bold=True, align="center", spacing=1.0, space_after=10, caps=True)

para("[Author Name], [e-mail]", bold=True, align="center", spacing=1.0, space_after=2)
para("[Department]", bold=True, align="center", spacing=1.0, space_after=2)
para("[Institution]", bold=True, align="center", spacing=1.0, space_after=12)

abstract = (
    "Abstract: Digital transformation has become the central management challenge for small and "
    "medium-sized enterprises (SMEs), which dominate the economies of emerging Asia yet adopt "
    "advanced digital technologies more slowly than large firms. This article develops a management "
    "framework that explains how SMEs convert digital technologies into superior performance. "
    "Building on the dynamic-capabilities perspective and on the distinction between digitisation, "
    "digitalisation and digital transformation, the framework links external drivers to the "
    "firm\u2019s sensing, seizing and reconfiguring capabilities, to the depth of the transformation "
    "undertaken, and ultimately to productivity, growth and resilience, with a reinvestment feedback "
    "loop. A composite digital-transformation intensity index is proposed to make the construct "
    "measurable for management purposes. The framework is confronted with evidence from emerging "
    "Asia, drawing on regional sources for the Association of Southeast Asian Nations and on the "
    "rapidly digitalising economies of Central Asia, with Uzbekistan as an illustrative case. The "
    "evidence shows that the binding constraint on SME performance is managerial and human "
    "capability rather than connectivity, and the analysis yields concrete managerial and policy "
    "recommendations on capability building, technology adoption, digital skills, finance and "
    "targeted public support for Asian emerging economies."
)
para(abstract, spacing=1.0, space_after=8)

para("Key words: digital transformation; small and medium-sized enterprises; dynamic capabilities; "
     "firm performance; emerging Asia.", spacing=1.0, space_after=4)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_after = Pt(12)
r = p.add_run("JEL: M15, M21, O33, L25, O53."); set_run(r, bold=True)

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
    "employment (Asian Development Bank, 2023). Yet these firms adopt advanced digital technologies "
    "more slowly than large enterprises and face tighter constraints on finance, skills and "
    "managerial capacity (OECD, 2021; OECD & ERIA, 2024).",
    first_indent=0.30)

para(
    "The literature has clarified what digital transformation is but has paid less attention to the "
    "specific managerial mechanisms through which a resource-constrained SME in an emerging economy "
    "turns technology into results. Digital transformation is more than the purchase of software; it "
    "is an organisational change process in which digital technologies reshape value creation, "
    "operations and the business model itself (Vial, 2019; Verhoef et al., 2021). Whether that "
    "process raises performance depends on the capabilities the firm can mobilise around it (Teece, "
    "2007; Warner & W\u00e4ger, 2019). For Asian SMEs, where these capabilities are scarce, the gap "
    "between adopting a technology and benefiting from it is correspondingly wide.",
    first_indent=0.30)

para(
    "This article addresses that gap with a management framework that connects the external drivers "
    "of digital transformation, the dynamic capabilities of the firm, the depth of the "
    "transformation undertaken and the resulting performance, closed by a reinvestment feedback "
    "loop. The framework is deliberately managerial and is made operational through a composite "
    "index of digital-transformation intensity. It is then confronted with evidence from emerging "
    "Asia \u2014 the ASEAN region and the fast-digitalising economies of Central Asia, with "
    "Uzbekistan as an illustrative case \u2014 to ground the discussion in the realities of "
    "developing-Asian markets.",
    first_indent=0.30)

para(
    "The contribution is threefold. The study (i) integrates the process view of digital "
    "transformation with the dynamic-capabilities perspective into a single, SME-oriented "
    "management framework; (ii) proposes a measurable digital-transformation intensity index that "
    "managers and analysts can apply; and (iii) derives evidence-based managerial and policy "
    "recommendations for Asian emerging economies. The remainder of the article is organised as "
    "follows. Section 1 reviews the literature and defines the core constructs. Section 2 presents "
    "the framework and the index. Section 3 examines the Asian evidence. Section 4 discusses the "
    "management and policy implications. The final section concludes.",
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
    "environments into three classes of capability: sensing opportunities and threats, seizing them "
    "through investment and business-model choices, and reconfiguring the resource base "
    "accordingly. Warner and W\u00e4ger (2019) show that digital transformation is precisely an "
    "ongoing process of strategic renewal in which these capabilities are built and rebuilt. "
    "Bharadwaj, El Sawy, Pavlou and Venkatraman (2013) argue that, in this environment, digital "
    "strategy can no longer be a functional adjunct to business strategy but must be fused with it. "
    "Westerman, Bonnet and McAfee (2014) add that the binding constraint is usually leadership and "
    "management capability rather than technology as such, and Fitzgerald, Kruschwitz, Bonnet and "
    "Welch (2014) document that firms widely recognise digital technology as a strategic imperative "
    "while struggling to execute it.",
    first_indent=0.30)

para(
    "A further strand examines how the decision to adopt a technology is actually taken. The "
    "technology acceptance model relates adoption to perceived usefulness and perceived ease of use "
    "(Davis, 1989), and the unified theory of acceptance and use of technology adds performance and "
    "effort expectancy, social influence and facilitating conditions (Venkatesh, Morris, Davis & "
    "Davis, 2003). At the organisational level, the technology\u2013organisation\u2013environment "
    "framework situates adoption in the interplay of technological readiness, organisational "
    "resources and the external environment (Tornatzky & Fleischer, 1990). For SMEs in emerging "
    "economies these frameworks are particularly relevant because the adoption decision is "
    "concentrated in a small management team and is highly sensitive to skills, cost and the "
    "surrounding digital ecosystem.",
    first_indent=0.30)

para(
    "Finally, a policy-oriented strand documents the SME-specific character of digital "
    "transformation in Asia. The OECD (2021) shows that SMEs lag larger firms across most digital "
    "indicators, while Yoshino and Taghizadeh-Hesary (2016) identify the structural constraints that "
    "slow SME growth in Asia: limited access to finance, the absence of comprehensive databases, "
    "low research and development spending and underdeveloped sales channels. Nambisan, Wright and "
    "Feldman (2019) emphasise that digital technologies also reshape the innovation and "
    "entrepreneurship process itself, lowering some entry barriers while raising the premium on "
    "digital capability, and the Asian Development Bank (2024) argues that digitalisation can raise "
    "the productive capacity of Asian economies provided the enabling conditions are in place. Taken "
    "together, the literature motivates a framework in which external drivers, firm-level "
    "capabilities and the depth of transformation jointly determine SME performance.",
    first_indent=0.30)

# ===================== 2. FRAMEWORK =====================
heading("2. A management framework and a measure of digital-transformation intensity")

para(
    "The framework proposed here links four blocks in sequence, with a feedback loop, and is "
    "summarised in Figure 1. The first block is the set of external drivers: market and competitive "
    "pressure, the availability and cost of digital technologies, and the policy environment, "
    "including funding and regulation. Drivers create the incentive and the opportunity to "
    "transform, but they do not determine the outcome.",
    first_indent=0.30)

para(
    "The second block is the firm\u2019s dynamic capabilities. Following Teece (2007), an SME senses "
    "digital opportunities and threats, seizes them by investing in technology and adjusting its "
    "business model, and reconfigures its processes, skills and structure so that the technology is "
    "actually used. These capabilities are the scarce managerial resource that converts drivers into "
    "transformation. The third block is the depth of the digital transformation undertaken, ranging "
    "from simple digitisation, through the digitalisation of processes, to genuine business-model "
    "change (Verhoef et al., 2021). The fourth block is performance: productivity, growth and export "
    "reach, and resilience to shocks. A feedback loop closes the framework: performance gains "
    "generate the resources that are reinvested in further capability building and technology, so "
    "that successful SMEs can enter a virtuous cycle while laggards fall further behind.",
    first_indent=0.30)

para(
    "To make the central construct measurable for management, let digital-transformation intensity "
    "of a firm be a weighted composite of the technologies and practices actually in use,",
    first_indent=0.30)

equation("DTI = \u03a3\u1d62 w\u1d62 \u00b7 a\u1d62 ,   with  \u03a3\u1d62 w\u1d62 = 1,", 1)

para(
    "where a\u1d62 \u2208 [0, 1] is the adoption level of digital element i (for example connectivity, "
    "a website or e-commerce channel, digital payments, cloud services, enterprise software, data "
    "analytics, artificial intelligence and digital-security measures) and w\u1d62 is its weight. The "
    "index yields a value between zero and one and corresponds, in spirit, to the digital-intensity "
    "measures used in international statistics. Firm performance is then modelled as increasing in "
    "digital-transformation intensity but conditional on capability,",
    first_indent=0.30)

equation("\u0394P = \u03b2 \u00b7 DTI \u00b7 C + \u03b5 ,", 2)

para(
    "where \u0394P is the change in a performance measure, C \u2208 [0, 1] is the firm\u2019s "
    "dynamic-capability level, \u03b2 > 0 is the return to transformation and \u03b5 captures other "
    "influences. The multiplicative term DTI \u00b7 C expresses the core managerial proposition: "
    "technology adoption raises performance only to the extent that the firm has the capability to "
    "absorb it. A high index combined with weak capability \u2014 technology bought but not "
    "embedded \u2014 yields little gain, which is the typical failure mode for SMEs in emerging "
    "markets. Table 1 sets out the components of the index and the managerial levers associated with "
    "each block of the framework.",
    first_indent=0.30)

# ----- Figure 1 -----
pic = doc.add_paragraph(); pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
pic.paragraph_format.space_before = Pt(6)
pic.add_run().add_picture("figure1_framework.png", width=Inches(6.0))
cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
cap.paragraph_format.line_spacing = 1.0; cap.paragraph_format.space_after = Pt(2)
set_run(cap.add_run("Figure 1. A management framework for digital transformation in SMEs"),
        size=12, bold=True)
src = doc.add_paragraph(); src.alignment = WD_ALIGN_PARAGRAPH.CENTER
src.paragraph_format.line_spacing = 1.0; src.paragraph_format.space_after = Pt(10)
set_run(src.add_run("Source: Authors\u2019 elaboration based on Teece (2007), Vial (2019) and "
                    "Verhoef et al. (2021)."), size=11, italic=True)

# ----- Table 1 -----
para("Table 1", bold=True, align="left", spacing=1.0, space_after=2)
para("Components of digital-transformation intensity and associated managerial levers",
     bold=True, size=12, align="left", spacing=1.0, space_after=4)
t1 = doc.add_table(rows=1, cols=3); t1.alignment = WD_TABLE_ALIGNMENT.CENTER; t1.style = "Table Grid"
for c, txt in zip(t1.rows[0].cells, ["Framework block", "Digital element / capability", "Managerial lever"]):
    c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(c.paragraphs[0].add_run(txt), size=12, bold=True)
rows = [
    ("Drivers", "Market pressure; technology cost; policy and funding", "Environmental scanning; use of public support"),
    ("Sensing", "Connectivity; web presence; market intelligence", "Digital awareness; customer-data analysis"),
    ("Seizing", "Digital payments; cloud services; e-commerce", "Investment decisions; business-model redesign"),
    ("Reconfiguring", "Data analytics; AI; process integration", "Skills development; change management"),
    ("Protection", "Cybersecurity and data governance", "Risk management; compliance"),
    ("Performance", "Productivity; growth and exports; resilience", "Monitoring and reinvestment of gains"),
]
for a, b, c in rows:
    cells = t1.add_row().cells
    for cell, txt in zip(cells, (a, b, c)):
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        set_run(cell.paragraphs[0].add_run(txt), size=12)
para("Source: Authors\u2019 elaboration based on Teece (2007), Tornatzky and Fleischer (1990) and "
     "OECD (2021).", italic=True, size=11, align="left", spacing=1.0, space_after=10)

# ===================== 3. EVIDENCE =====================
heading("3. Evidence from emerging Asia")

para(
    "The framework can be illustrated with the experience of emerging Asia, where SMEs are at once "
    "economically dominant and digitally constrained. Across the ASEAN member states, micro, small "
    "and medium-sized enterprises account for the overwhelming majority of firms and the bulk of "
    "employment, and the regional digital economy is expanding rapidly (Asian Development Bank, "
    "2023). The constraints on their digital transformation are, however, systematic. Yoshino and "
    "Taghizadeh-Hesary (2016) show that Asian SMEs are held back by limited access to finance, the "
    "absence of comprehensive databases, low research and development spending and underdeveloped "
    "sales channels \u2014 precisely the conditions that depress the capability term in the "
    "framework. The OECD and ERIA (2024) confirm that, while ASEAN governments have strengthened "
    "SME policy frameworks, the digitalisation of smaller firms remains uneven and skills and "
    "finance are recurring bottlenecks.",
    first_indent=0.30)

para(
    "The Central Asian economies illustrate both the opportunity and the constraint with particular "
    "clarity. Connectivity and digital infrastructure have improved quickly, and e-commerce has "
    "grown from a low base: in Uzbekistan, the World Bank reports that the e-commerce market "
    "expanded roughly fivefold between 2018 and 2022, exceeding half a billion United States dollars "
    "by 2023. National policy is ambitious; under the Digital Uzbekistan 2030 strategy and the "
    "country\u2019s development agenda, the authorities aim to turn Uzbekistan into a regional "
    "information-technology hub, with sharply higher technology exports and large-scale job creation "
    "in the sector (World Bank, 2023). Yet the same sources note that implementation is uneven and "
    "that the deeper transformation of enterprises \u2014 as opposed to the roll-out of "
    "infrastructure \u2014 depends on skills, finance and managerial capacity that remain scarce. In "
    "the language of the framework, Central Asian SMEs increasingly have the drivers and the "
    "connectivity, but not yet the capabilities that convert adoption into performance.",
    first_indent=0.30)

para(
    "Table 2 summarises the Asian picture. Read through the framework, the regional evidence "
    "delivers a consistent message: connectivity and policy ambition are necessary but not "
    "sufficient. The binding constraint on SME performance is the capability term C in equation "
    "(2) \u2014 digital skills, finance and managerial capacity \u2014 rather than the availability "
    "of technology, and the reinvestment feedback loop helps explain why early movers and dynamic "
    "urban firms pull ahead while the mass of smaller enterprises risk being locked into a "
    "low-intensity equilibrium.",
    first_indent=0.30)

# ----- Table 2 -----
para("Table 2", bold=True, align="left", spacing=1.0, space_after=2)
para("Digital transformation of SMEs in emerging Asia: selected observations",
     bold=True, size=12, align="left", spacing=1.0, space_after=4)
t2 = doc.add_table(rows=1, cols=2); t2.alignment = WD_TABLE_ALIGNMENT.CENTER; t2.style = "Table Grid"
for c, txt in zip(t2.rows[0].cells, ["Indicator / observation", "Evidence"]):
    c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(c.paragraphs[0].add_run(txt), size=12, bold=True)
data2 = [
    ("MSME share of enterprises in ASEAN", "On average more than 97% of all firms"),
    ("Role in the economy", "Majority of employment; large share of GDP"),
    ("Main SME constraints in Asia", "Finance; databases; R&D; sales channels"),
    ("Uzbekistan \u2013 e-commerce growth", "About fivefold, 2018\u20132022; > USD 0.5 bn by 2023"),
    ("Uzbekistan \u2013 policy ambition", "Digital 2030: regional IT hub; higher IT exports"),
    ("Binding constraint (framework)", "Capability: digital skills, finance, management"),
]
for a, b in data2:
    cells = t2.add_row().cells
    for cell, txt in zip(cells, (a, b)):
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        set_run(cell.paragraphs[0].add_run(txt), size=12)
para("Source: Compiled by the authors from Asian Development Bank (2023, 2024), Yoshino and "
     "Taghizadeh-Hesary (2016), OECD and ERIA (2024) and World Bank (2023).",
     italic=True, size=11, align="left", spacing=1.0, space_after=10)

# ===================== 4. IMPLICATIONS =====================
heading("4. Management and policy implications")

para(
    "For the management of the individual SME, the framework implies that investment should be "
    "sequenced according to capability rather than technology fashion. Because performance depends "
    "on the product of digital-transformation intensity and capability (equation 2), an SME with "
    "weak capabilities gains more from building sensing and absorptive capacity \u2014 digital "
    "skills, data literacy and a clear digital element of strategy \u2014 than from acquiring "
    "advanced tools it cannot embed. Adoption should follow the sequence of the framework: secure "
    "connectivity and a market-facing digital channel, including the digital-payment and e-commerce "
    "platforms that are spreading fastest in Asian markets; move core processes to cloud-based and "
    "enterprise software; and only then layer on analytics and artificial intelligence, with "
    "cybersecurity and data governance treated as a precondition rather than an afterthought (OECD, "
    "2021; Westerman et al., 2014). Crucially, digital strategy should be fused with business "
    "strategy and owned by the management team, not delegated as a technical project (Bharadwaj "
    "et al., 2013).",
    first_indent=0.30)

para(
    "For policy in Asian emerging economies, the same logic reframes public support. Because the "
    "binding constraint is capability rather than connectivity, support should shift from "
    "subsidising hardware towards building skills and absorptive capacity: management and "
    "digital-skills training, advisory and diagnostic services, and demonstrator projects that "
    "reduce the uncertainty about returns that deters SME investment. Two Asia-specific priorities "
    "follow from the regional evidence. First, the finance constraint identified by Yoshino and "
    "Taghizadeh-Hesary (2016) should be addressed directly, by bundling affordable finance with "
    "advice and by developing the SME databases and credit information that lower the cost of "
    "lending. Second, public digital infrastructure \u2014 interoperable digital-payment systems, "
    "digital identity and trade-facilitating platforms \u2014 lowers the fixed cost of "
    "transformation for the smallest firms and should be prioritised, as the ASEAN and Central "
    "Asian experiences suggest (OECD & ERIA, 2024; World Bank, 2023; Asian Development Bank, 2024).",
    first_indent=0.30)

para(
    "The two levels are complementary. Public investment in skills, finance and digital "
    "infrastructure raises the average capability level C across the SME population, which "
    "increases the performance return to any given level of technology adoption and so strengthens "
    "the incentive for firms to invest. Firm-level reinvestment of the resulting gains then sustains "
    "the virtuous cycle. Where this complementarity is neglected \u2014 where infrastructure and "
    "grants are provided without capability \u2014 the predictable outcome is adoption without "
    "transformation, and the gap between dynamic and lagging firms persists.",
    first_indent=0.30)

# ===================== CONCLUSIONS =====================
heading("Conclusions")

para(
    "Digital transformation is the dominant management challenge facing contemporary enterprises, "
    "and it is most demanding for the small and medium-sized firms that form the backbone of the "
    "economies of emerging Asia. This article has argued that the decisive factor is not access to "
    "technology but the managerial capability to absorb it. Integrating the process view of digital "
    "transformation with the dynamic-capabilities perspective, it proposed a management framework "
    "that links external drivers, the firm\u2019s sensing, seizing and reconfiguring capabilities, "
    "the depth of the transformation undertaken and the resulting performance, closed by a "
    "reinvestment feedback loop, and it made the central construct measurable through a "
    "digital-transformation intensity index.",
    first_indent=0.30)

para(
    "Confronted with evidence from the ASEAN region and from the fast-digitalising economies of "
    "Central Asia, with Uzbekistan as an illustrative case, the framework accounts for a persistent "
    "pattern: connectivity and policy ambition are advancing quickly, but the capability to turn "
    "technology into performance \u2014 skills, finance and management \u2014 lags behind. The "
    "practical message for managers is to sequence investment by capability and to own digital "
    "strategy at the top of the firm; the message for policymakers is to fund skills, finance and "
    "shared digital infrastructure, not hardware alone. The framework is conceptual and its index "
    "and performance relationship are proposed rather than estimated; the natural next step is "
    "empirical validation on firm-level data from Asian emerging economies, which would allow the "
    "return to transformation and the capability threshold to be quantified and the policy "
    "priorities to be sharpened.",
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

    "Fitzgerald, M., Kruschwitz, N., Bonnet, D., & Welch, M. (2014). Embracing digital technology: A "
    "new strategic imperative. MIT Sloan Management Review, 55(2), 1\u201312.",

    "Nambisan, S., Wright, M., & Feldman, M. (2019). The digital transformation of innovation and "
    "entrepreneurship: Progress, challenges and key themes. Research Policy, 48(8), 103773. "
    "https://doi.org/10.1016/j.respol.2019.03.018",

    "OECD. (2021). The digital transformation of SMEs. Paris: OECD Publishing. "
    "https://doi.org/10.1787/bdb9256a-en",

    "OECD, & ERIA. (2024). SME Policy Index: ASEAN 2024 \u2013 Enabling sustainable growth and "
    "digitalisation. Paris: OECD Publishing / Jakarta: Economic Research Institute for ASEAN and "
    "East Asia. Available online: https://www.oecd.org/en/publications.html",

    "Teece, D. J. (2007). Explicating dynamic capabilities: The nature and microfoundations of "
    "(sustainable) enterprise performance. Strategic Management Journal, 28(13), 1319\u20131350. "
    "https://doi.org/10.1002/smj.640",

    "Tornatzky, L. G., & Fleischer, M. (1990). The processes of technological innovation. Lexington, "
    "MA: Lexington Books.",

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
