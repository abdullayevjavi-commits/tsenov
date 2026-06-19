# -*- coding: utf-8 -*-
"""
Build the Economic Archive (Narodnostopanski Arhiv) article as a .docx that
follows the journal template (m9_Template_BM_eng.doc).

Topic: the dominant theme in the supplied 600+ page collection of recently
accepted articles - DIGITAL TRANSFORMATION / technology adoption in enterprises,
with a strong SME focus - reframed toward management.
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
     "Enterprises: A Management Framework and Evidence from the European Union",
     bold=True, align="center", spacing=1.0, space_after=10, caps=True)

para("[Author Name], [e-mail]", bold=True, align="center", spacing=1.0, space_after=2)
para("[Department]", bold=True, align="center", spacing=1.0, space_after=2)
para("[Institution]", bold=True, align="center", spacing=1.0, space_after=12)

abstract = (
    "Abstract: Digital transformation has become the central management challenge for small and "
    "medium-sized enterprises (SMEs), which account for the bulk of employment and value added in "
    "the European economy yet adopt digital technologies more slowly than large firms. This article "
    "develops a management framework that explains how SMEs convert digital technologies into "
    "superior performance. Building on the dynamic-capabilities perspective and on the distinction "
    "between digitisation, digitalisation and digital transformation, the framework links external "
    "drivers to the firm\u2019s sensing, seizing and reconfiguring capabilities, to the depth of the "
    "transformation undertaken, and ultimately to productivity, growth and resilience, with a "
    "reinvestment feedback loop. A composite digital-transformation intensity index is proposed to "
    "make the construct measurable for management purposes. The framework is confronted with "
    "official European evidence, which shows a persistent gap between the European Union\u2019s "
    "Digital Decade ambition and the actual digital intensity of SMEs, and a particularly wide gap "
    "for lagging member states such as Bulgaria. The analysis yields concrete managerial and policy "
    "recommendations on capability building, technology adoption, digital skills, cybersecurity and "
    "targeted public support."
)
para(abstract, spacing=1.0, space_after=8)

para("Key words: digital transformation; small and medium-sized enterprises; dynamic capabilities; "
     "firm performance; technology adoption.", spacing=1.0, space_after=4)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_after = Pt(12)
r = p.add_run("JEL: M15, M21, O33, L25, D22."); set_run(r, bold=True)

# ===================== INTRODUCTION =====================
heading("Introduction")

para(
    "Digital technologies \u2014 cloud computing, data analytics, artificial intelligence, "
    "e-commerce platforms and connected devices \u2014 have moved from being a support function to "
    "being the principal arena of competition. For enterprises of every size, the management "
    "question is no longer whether to adopt such technologies but how to convert them into durable "
    "improvements in performance. This question is most acute for small and medium-sized enterprises "
    "(SMEs). They constitute the overwhelming majority of firms in the European Union and generate a "
    "large share of employment and value added, yet they adopt advanced digital technologies more "
    "slowly than large firms and face tighter constraints on finance, skills and managerial "
    "capacity (OECD, 2021).",
    first_indent=0.30)

para(
    "The literature has clarified what digital transformation is but has paid less attention to the "
    "specific managerial mechanisms through which a resource-constrained SME turns technology into "
    "results. Digital transformation is more than the purchase of software; it is an organisational "
    "change process in which digital technologies reshape value creation, operations and the "
    "business model itself (Vial, 2019; Verhoef et al., 2021). Whether that process raises "
    "performance depends on the capabilities the firm can mobilise around it (Teece, 2007; Warner & "
    "W\u00e4ger, 2019). For SMEs, where these capabilities are scarce, the gap between adopting a "
    "technology and benefiting from it is correspondingly wide.",
    first_indent=0.30)

para(
    "This article addresses that gap with a management framework that connects the external drivers "
    "of digital transformation, the dynamic capabilities of the firm, the depth of the "
    "transformation undertaken and the resulting performance, closed by a reinvestment feedback "
    "loop. The framework is deliberately managerial and is made operational through a composite "
    "index of digital-transformation intensity. It is then confronted with official European "
    "evidence on the digital uptake of SMEs, including the position of a lagging member state, "
    "Bulgaria, to ground the discussion in the European policy context of the Digital Decade.",
    first_indent=0.30)

para(
    "The contribution is threefold. The study (i) integrates the process view of digital "
    "transformation with the dynamic-capabilities perspective into a single, SME-oriented "
    "management framework; (ii) proposes a measurable digital-transformation intensity index that "
    "managers and analysts can apply; and (iii) derives evidence-based managerial and policy "
    "recommendations. The remainder of the article is organised as follows. Section 1 reviews the "
    "literature and defines the core constructs. Section 2 presents the framework and the index. "
    "Section 3 examines the European and Bulgarian evidence. Section 4 discusses the management and "
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
    "resources and the external environment (Tornatzky & Fleischer, 1990). For SMEs these "
    "frameworks are particularly relevant because the adoption decision is concentrated in a small "
    "management team and is highly sensitive to skills, cost and the surrounding ecosystem.",
    first_indent=0.30)

para(
    "Finally, a policy-oriented strand documents the SME-specific character of digital "
    "transformation. The OECD (2021) shows that SMEs lag larger firms across most digital "
    "indicators and that the barriers are systematic \u2014 scarce internal skills, limited finance, "
    "uncertainty about returns and exposure to digital-security risk. Nambisan, Wright and Feldman "
    "(2019) emphasise that digital technologies also reshape the innovation and entrepreneurship "
    "process itself, lowering some entry barriers while raising the premium on digital capability. "
    "Taken together, the literature motivates a framework in which external drivers, firm-level "
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
    "a website or e-commerce channel, cloud services, enterprise software, data analytics, "
    "artificial intelligence and digital-security measures) and w\u1d62 is its weight. The index "
    "yields a value between zero and one and corresponds, in spirit, to the \u201cdigital "
    "intensity\u201d measures used in official European statistics. Firm performance is then modelled "
    "as increasing in digital-transformation intensity but conditional on capability,",
    first_indent=0.30)

equation("\u0394P = \u03b2 \u00b7 DTI \u00b7 C + \u03b5 ,", 2)

para(
    "where \u0394P is the change in a performance measure, C \u2208 [0, 1] is the firm\u2019s "
    "dynamic-capability level, \u03b2 > 0 is the return to transformation and \u03b5 captures other "
    "influences. The multiplicative term DTI \u00b7 C expresses the core managerial proposition: "
    "technology adoption raises performance only to the extent that the firm has the capability to "
    "absorb it. A high index combined with weak capability \u2014 technology bought but not "
    "embedded \u2014 yields little gain, which is the typical failure mode for SMEs. Table 1 sets out "
    "the components of the index and the managerial levers associated with each block of the "
    "framework.",
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
    ("Seizing", "Cloud services; enterprise software; e-commerce", "Investment decisions; business-model redesign"),
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
heading("3. Evidence from the European Union and Bulgaria")

para(
    "The framework can be illustrated with official European statistics, which measure the digital "
    "intensity of enterprises directly. Under the European Union\u2019s Digital Decade policy "
    "programme, the agreed ambition is that more than ninety per cent of SMEs should reach at least "
    "a basic level of digital intensity by 2030. According to Eurostat (2024), in 2023 the SMEs of "
    "the European Union were some thirty-two percentage points below that ambition \u2014 that is, "
    "only around fifty-eight per cent reached at least a basic level of digital intensity. The gap "
    "is not in basic connectivity, which is almost universal, but in the more advanced technologies "
    "\u2014 cloud computing, data analytics and artificial intelligence \u2014 that correspond to "
    "the seizing and reconfiguring blocks of the framework and that are most strongly associated "
    "with performance gains (OECD, 2021).",
    first_indent=0.30)

para(
    "The aggregate gap conceals wide differences across member states, and these differences map "
    "onto the framework. For a lagging country such as Bulgaria, the European Commission (2025) "
    "reports that, despite well-developed connectivity infrastructure, the country is held back by "
    "low digital skills, SME digital uptake among the lowest in the Union, and limited adoption of "
    "cloud computing, artificial intelligence and data analytics. In the language of the framework, "
    "Bulgarian SMEs are not short of drivers or of basic connectivity; they are short of the "
    "capabilities \u2014 skills, finance and managerial capacity \u2014 that translate adoption into "
    "the deeper transformation that raises performance. Table 2 summarises the European picture.",
    first_indent=0.30)

# ----- Table 2 -----
para("Table 2", bold=True, align="left", spacing=1.0, space_after=2)
para("Digital intensity of SMEs in the European Union: ambition and reality",
     bold=True, size=12, align="left", spacing=1.0, space_after=4)
t2 = doc.add_table(rows=1, cols=2); t2.alignment = WD_TABLE_ALIGNMENT.CENTER; t2.style = "Table Grid"
for c, txt in zip(t2.rows[0].cells, ["Indicator", "Value / observation"]):
    c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(c.paragraphs[0].add_run(txt), size=12, bold=True)
data2 = [
    ("Digital Decade 2030 target (SMEs, basic digital intensity)", "at least 90%"),
    ("EU SMEs reaching basic digital intensity, 2023", "approx. 58% (32 pp below target)"),
    ("Main shortfall", "Cloud, data analytics and AI (advanced technologies)"),
    ("Bulgaria \u2013 connectivity", "Well-developed infrastructure"),
    ("Bulgaria \u2013 SME digital uptake", "Among the lowest in the EU"),
    ("Bulgaria \u2013 binding constraints", "Digital skills; cloud/AI/analytics adoption; cybersecurity"),
]
for a, b in data2:
    cells = t2.add_row().cells
    for cell, txt in zip(cells, (a, b)):
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        set_run(cell.paragraphs[0].add_run(txt), size=12)
para("Source: Compiled by the authors from Eurostat (2024), European Commission (2025) and "
     "OECD (2021).", italic=True, size=11, align="left", spacing=1.0, space_after=10)

para(
    "The evidence is consistent with the framework in two respects. First, the binding constraint "
    "on performance is the capability term C in equation (2) rather than the mere availability of "
    "technology: connectivity is near-universal, but advanced adoption and the skills to use it are "
    "not. Second, the feedback loop helps explain the persistence of the gap between leading and "
    "lagging member states: firms and countries that transform early reinvest the resulting gains "
    "in further capability, while those that do not risk being locked into a low-intensity "
    "equilibrium. This is the central management and policy challenge that the next section "
    "addresses.",
    first_indent=0.30)

# ===================== 4. IMPLICATIONS =====================
heading("4. Management and policy implications")

para(
    "For the management of the individual SME, the framework implies that investment should be "
    "sequenced according to capability rather than technology fashion. Because performance depends "
    "on the product of digital-transformation intensity and capability (equation 2), an SME with "
    "weak capabilities gains more from building sensing and absorptive capacity \u2014 digital "
    "skills, data literacy and a clear digital element of strategy \u2014 than from acquiring "
    "advanced tools it cannot embed. Adoption should follow the sequence of the framework: secure "
    "connectivity and a market-facing digital channel, move core processes to cloud-based and "
    "enterprise software, and only then layer on analytics and artificial intelligence, with "
    "cybersecurity and data governance treated as a precondition rather than an afterthought "
    "(OECD, 2021; Westerman et al., 2014). Crucially, digital strategy should be fused with business "
    "strategy and owned by the management team, not delegated as a technical project (Bharadwaj "
    "et al., 2013).",
    first_indent=0.30)

para(
    "For policy, the same logic reframes public support. Because the binding constraint is "
    "capability rather than connectivity, support should shift from subsidising hardware towards "
    "building skills and absorptive capacity: management and digital-skills training, advisory and "
    "diagnostic services, and demonstrator projects that reduce the uncertainty about returns that "
    "deters SME investment. Instruments should be designed for the smallest firms, whose fixed costs "
    "of adoption are proportionally highest, and should bundle finance with advice rather than offer "
    "them separately (OECD, 2021). For lagging member states such as Bulgaria, the European "
    "Commission\u2019s (2025) diagnosis points to a clear set of priorities \u2014 digital skills, "
    "the uptake of cloud, analytics and artificial intelligence by SMEs, and cybersecurity \u2014 on "
    "which the substantial European recovery and cohesion funding earmarked for the digital "
    "transition can be concentrated.",
    first_indent=0.30)

para(
    "The two levels are complementary. Public investment in skills and advice raises the average "
    "capability level C across the SME population, which increases the performance return to any "
    "given level of technology adoption and so strengthens the incentive for firms to invest. "
    "Firm-level reinvestment of the resulting gains then sustains the virtuous cycle. Where this "
    "complementarity is neglected \u2014 where grants fund technology without capability \u2014 the "
    "predictable outcome is adoption without transformation, and the gap with digital leaders "
    "persists.",
    first_indent=0.30)

# ===================== CONCLUSIONS =====================
heading("Conclusions")

para(
    "Digital transformation is the dominant management challenge facing contemporary enterprises, "
    "and it is most demanding for the small and medium-sized firms that form the backbone of the "
    "European economy. This article has argued that the decisive factor is not access to technology "
    "but the managerial capability to absorb it. Integrating the process view of digital "
    "transformation with the dynamic-capabilities perspective, it proposed a management framework "
    "that links external drivers, the firm\u2019s sensing, seizing and reconfiguring capabilities, "
    "the depth of the transformation undertaken and the resulting performance, closed by a "
    "reinvestment feedback loop, and it made the central construct measurable through a "
    "digital-transformation intensity index.",
    first_indent=0.30)

para(
    "Confronted with official European evidence, the framework accounts for the persistent gap "
    "between the Digital Decade ambition and the actual digital intensity of SMEs, and for the "
    "especially wide gap in lagging member states such as Bulgaria, where connectivity is adequate "
    "but capability is not. The practical message for managers is to sequence investment by "
    "capability and to own digital strategy at the top of the firm; the message for policymakers is "
    "to fund skills and absorptive capacity, not hardware alone. The framework is conceptual and its "
    "index and performance relationship are proposed rather than estimated; the natural next step is "
    "empirical validation on firm-level data, including Bulgarian SME samples, which would allow the "
    "return to transformation and the capability threshold to be quantified and the policy "
    "priorities to be sharpened.",
    first_indent=0.30)

# ===================== REFERENCES =====================
heading("References")
refs = [
    "Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business "
    "strategy: Toward a next generation of insights. MIS Quarterly, 37(2), 471\u2013482. "
    "https://doi.org/10.25300/MISQ/2013/37:2.3",

    "Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of "
    "information technology. MIS Quarterly, 13(3), 319\u2013340. https://doi.org/10.2307/249008",

    "European Commission. (2025). Bulgaria 2025 Digital Decade country report. Brussels: European "
    "Commission. Available online: "
    "https://digital-strategy.ec.europa.eu/en/factpages/bulgaria-2025-digital-decade-country-report",

    "Eurostat. (2024). How digitalised have the EU\u2019s enterprises become? (Eurostat news article, "
    "29 August 2024). Luxembourg: Eurostat. Available online: "
    "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20240829-1",

    "Fitzgerald, M., Kruschwitz, N., Bonnet, D., & Welch, M. (2014). Embracing digital technology: A "
    "new strategic imperative. MIT Sloan Management Review, 55(2), 1\u201312.",

    "Nambisan, S., Wright, M., & Feldman, M. (2019). The digital transformation of innovation and "
    "entrepreneurship: Progress, challenges and key themes. Research Policy, 48(8), 103773. "
    "https://doi.org/10.1016/j.respol.2019.03.018",

    "OECD. (2021). The digital transformation of SMEs. Paris: OECD Publishing. "
    "https://doi.org/10.1787/bdb9256a-en",

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
]
for ref in refs:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = 1.5; pf.space_after = Pt(4)
    pf.left_indent = Inches(0.5); pf.first_line_indent = Inches(-0.5)
    set_run(p.add_run(ref), size=14)

out = "Economic_Archive_Digital_Transformation_SMEs.docx"
doc.save(out)
print("Saved", out)
