# -*- coding: utf-8 -*-
"""Render content.py to a PDF (preview that unmistakably embeds the figures),
using a Unicode serif font so Greek/maths characters display correctly."""
import os
import matplotlib
from fpdf import FPDF
import content as C

TTF = os.path.join(matplotlib.get_data_path(), "fonts", "ttf")
SERIF = os.path.join(TTF, "DejaVuSerif.ttf")
SERIF_B = os.path.join(TTF, "DejaVuSerif-Bold.ttf")
SERIF_I = os.path.join(TTF, "DejaVuSerif-Italic.ttf")


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-12)
        self.set_font("serif", "I", 8)
        self.cell(0, 8, "Page %d" % self.page_no(), align="C")


pdf = PDF(format="A4")
pdf.set_auto_page_break(True, margin=18)
pdf.add_font("serif", "", SERIF)
pdf.add_font("serif", "B", SERIF_B)
pdf.add_font("serif", "I", SERIF_I)
pdf.set_margins(25, 18, 25)
pdf.add_page()
EPW = pdf.epw


def text(s, style="", size=11, align="J", lh=5.6, space=2.0):
    pdf.set_font("serif", style, size)
    pdf.multi_cell(0, lh, s, align=align)
    pdf.ln(space)


# front matter
text(C.TITLE.upper(), "B", 13, "C", 6.2, 3)
for a in C.AUTHORS:
    text(a, "B", 11, "C", 5.2, 0.5)
pdf.ln(2)
text(C.ABSTRACT, "", 10.5, "J", 5.0, 2)
text(C.KEYWORDS, "", 10.5, "J", 5.0, 1.5)
text(C.JEL, "B", 10.5, "J", 5.0, 3)

for b in C.BLOCKS:
    kind = b[0]
    if kind == "h1":
        pdf.ln(1); text(b[1], "B", 12.5, "L", 6, 2)
    elif kind == "h2":
        text(b[1], "BI", 11.5, "L", 5.6, 1.5) if False else text(b[1], "I", 11.5, "L", 5.6, 1.5)
    elif kind == "p":
        text(b[1], "", 11, "J", 5.6, 2.2)
    elif kind == "eq":
        text("%s          (%d)" % (b[1], b[2]), "I", 11, "C", 5.6, 2.2)
    elif kind == "fig":
        _, path, caption, source, width = b
        wmm = width * 25.4 / 6.0 * 6.0  # interpret width in inches
        wmm = min(width * 25.4, EPW)
        x = (210 - wmm) / 2
        if pdf.get_y() + 70 > 279:
            pdf.add_page()
        pdf.image(path, x=x, w=wmm)
        pdf.ln(1.5)
        text(caption, "B", 10, "C", 5, 1)
        text(source, "I", 9, "C", 4.6, 2.5)
    elif kind == "table":
        _, no, title, headers, rows, source = b
        text(no, "B", 10.5, "L", 5, 0.6)
        text(title, "B", 10, "L", 5, 1.5)
        ncol = len(headers)
        widths = [EPW * w for w in ([0.42, 0.18, 0.20, 0.20] if ncol == 4 else [0.40, 0.34, 0.26])]
        pdf.set_font("serif", "B", 9)
        line_h = 5
        for h, w in zip(headers, widths):
            pdf.cell(w, line_h, h, border=1, align="C")
        pdf.ln(line_h)
        pdf.set_font("serif", "", 9)
        for rrow in rows:
            # compute row height from wrapped lines
            heights = []
            for txt, w in zip(rrow, widths):
                nlines = max(1, len(pdf.multi_cell(w, line_h, txt, split_only=True)))
                heights.append(nlines)
            rh = max(heights) * line_h
            x0, y0 = pdf.get_x(), pdf.get_y()
            if y0 + rh > 279:
                pdf.add_page(); x0, y0 = pdf.get_x(), pdf.get_y()
            for txt, w in zip(rrow, widths):
                x, y = pdf.get_x(), pdf.get_y()
                pdf.multi_cell(w, line_h, txt, border=1, align="L", max_line_height=line_h)
                pdf.set_xy(x + w, y)
            pdf.ln(rh)
        pdf.ln(1.5)
        text(source, "I", 8.5, "L", 4.4, 2.5)

pdf.ln(1)
text("References", "B", 12.5, "L", 6, 2)
pdf.set_font("serif", "", 9.5)
for ref in C.REFERENCES:
    # hanging indent
    y = pdf.get_y()
    pdf.multi_cell(0, 5, ref, align="J")
    pdf.ln(1.2)

out = "Economic_Archive_Digital_Transformation_SMEs_Asia.pdf"
pdf.output(out)
print("Saved", out)
