# -*- coding: utf-8 -*-
"""Render content.py to a journal-formatted .docx (Times New Roman 14 pt)."""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
import content as C

FONT = "Times New Roman"
doc = Document()
normal = doc.styles["Normal"]
normal.font.name = FONT; normal.font.size = Pt(14)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
for s in doc.sections:
    s.top_margin = Inches(1); s.bottom_margin = Inches(1)
    s.left_margin = Inches(1.18); s.right_margin = Inches(1.18)


def run(p, text, size=14, bold=False, italic=False):
    r = p.add_run(text); r.font.name = FONT; r.font.size = Pt(size)
    r.bold = bold; r.italic = italic
    r._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    return r


def para(text="", *, size=14, bold=False, italic=False, align="justify",
         spacing=1.5, space_after=6, first_indent=0.0, hang=0.0):
    p = doc.add_paragraph()
    p.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY, "center": WD_ALIGN_PARAGRAPH.CENTER,
                   "left": WD_ALIGN_PARAGRAPH.LEFT}[align]
    pf = p.paragraph_format
    pf.line_spacing = spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE if isinstance(spacing, float) else WD_LINE_SPACING.SINGLE
    pf.space_after = Pt(space_after); pf.space_before = Pt(0)
    if first_indent:
        pf.first_line_indent = Inches(first_indent)
    if hang:
        pf.left_indent = Inches(hang); pf.first_line_indent = Inches(-hang)
    if text:
        run(p, text, size=size, bold=bold, italic=italic)
    return p


# front matter
para(C.TITLE.upper(), bold=True, align="center", spacing=1.0, space_after=10)
for a in C.AUTHORS:
    para(a, bold=True, align="center", spacing=1.0, space_after=2)
doc.paragraphs[-1].paragraph_format.space_after = Pt(12)
para(C.ABSTRACT, spacing=1.0, space_after=8)
para(C.KEYWORDS, spacing=1.0, space_after=4)
para(C.JEL, bold=True, spacing=1.0, space_after=12)

for b in C.BLOCKS:
    kind = b[0]
    if kind == "h1":
        p = para(spacing=1.5, space_after=6); p.paragraph_format.space_before = Pt(10)
        run(p, b[1], bold=True)
    elif kind == "h2":
        p = para(spacing=1.5, space_after=4); p.paragraph_format.space_before = Pt(8)
        run(p, b[1], bold=True, italic=True)
    elif kind == "p":
        para(b[1], first_indent=0.30)
    elif kind == "eq":
        p = para(align="center", spacing=1.5, space_after=4); p.paragraph_format.space_before = Pt(4)
        run(p, b[1], italic=True); run(p, "\t\t\t\t\t(%d)" % b[2])
    elif kind == "fig":
        _, path, caption, source, width = b
        pic = para(align="center", space_after=2); pic.paragraph_format.space_before = Pt(6)
        pic.add_run().add_picture(path, width=Inches(width))
        para(caption, size=12, bold=True, align="center", spacing=1.0, space_after=2)
        para(source, size=11, italic=True, align="center", spacing=1.0, space_after=10)
    elif kind == "table":
        _, no, title, headers, rows, source = b
        para(no, bold=True, align="left", spacing=1.0, space_after=2)
        para(title, bold=True, size=12, align="left", spacing=1.0, space_after=4)
        t = doc.add_table(rows=1, cols=len(headers)); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.style = "Table Grid"
        for c, htxt in zip(t.rows[0].cells, headers):
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            run(c.paragraphs[0], htxt, size=12, bold=True)
        for rrow in rows:
            cells = t.add_row().cells
            for cell, txt in zip(cells, rrow):
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
                run(cell.paragraphs[0], txt, size=12)
        para(source, italic=True, size=11, align="left", spacing=1.0, space_after=10)

# references
p = para(spacing=1.5, space_after=6); p.paragraph_format.space_before = Pt(10)
run(p, "References", bold=True)
for ref in C.REFERENCES:
    para(ref, spacing=1.5, space_after=4, hang=0.5)

out = "Economic_Archive_Digital_Transformation_SMEs_Asia.docx"
doc.save(out)
print("Saved", out)
