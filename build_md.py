# -*- coding: utf-8 -*-
"""Render content.py to Markdown (readable copy that mirrors the DOCX/PDF)."""
import content as C

lines = []
lines.append("# " + C.TITLE.upper())
lines.append("")
for a in C.AUTHORS:
    lines.append("**" + a + "**")
lines.append("")
lines.append("> Prepared for *Economic Archive / Narodnostopanski Arhiv* (Tsenov Academy, "
             "Svishtov). Revision 4. Publication-ready file: "
             "`Economic_Archive_Digital_Transformation_SMEs_Asia.docx`; a PDF preview with the "
             "figures is also provided: `Economic_Archive_Digital_Transformation_SMEs_Asia.pdf`.")
lines.append("")
lines.append("**" + C.ABSTRACT + "**")
lines.append("")
lines.append("**" + C.KEYWORDS + "**")
lines.append("")
lines.append("**" + C.JEL + "**")
lines.append("")

for b in C.BLOCKS:
    kind = b[0]
    if kind == "h1":
        lines.append("## " + b[1]); lines.append("")
    elif kind == "h2":
        lines.append("### " + b[1]); lines.append("")
    elif kind == "p":
        lines.append(b[1]); lines.append("")
    elif kind == "eq":
        lines.append("> **(%d)**  *%s*" % (b[2], b[1])); lines.append("")
    elif kind == "fig":
        _, path, caption, source, width = b
        lines.append("![%s](%s)" % (caption, path)); lines.append("")
        lines.append("**" + caption + "**  "); lines.append("*" + source + "*"); lines.append("")
    elif kind == "table":
        _, no, title, headers, rows, source = b
        lines.append("**%s. %s**" % (no, title)); lines.append("")
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "|".join(["---"] * len(headers)) + "|")
        for r in rows:
            lines.append("| " + " | ".join(r) + " |")
        lines.append("")
        lines.append("*" + source + "*"); lines.append("")

lines.append("## References")
lines.append("")
for ref in C.REFERENCES:
    lines.append(ref); lines.append("")

with open("Economic_Archive_Digital_Transformation_SMEs_Asia.md", "w") as f:
    f.write("\n".join(lines))
print("Saved markdown")
