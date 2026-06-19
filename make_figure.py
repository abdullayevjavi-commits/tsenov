# -*- coding: utf-8 -*-
"""Figure 1: A conceptual framework linking digital transformation drivers,
dynamic capabilities, the transformation process and SME performance.
Drawn as labelled boxes with arrows (no fabricated data)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(7.2, 3.7))
ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")

boxes = [
    (0.3, 2.1, "Drivers\n\n\u2022 Market & competition\n\u2022 Technology (cloud, AI,\n  data, e-commerce)\n\u2022 Policy & funding", "#e8eef7"),
    (3.3, 2.1, "Dynamic\ncapabilities\n\n\u2022 Sensing\n\u2022 Seizing\n\u2022 Reconfiguring", "#dfe9df"),
    (6.3, 2.1, "Digital\ntransformation\n\n\u2022 Digitisation\n\u2022 Digitalisation\n\u2022 Business-model\n  change", "#f6efe0"),
    (9.3, 2.1, "SME\nperformance\n\n\u2022 Productivity\n\u2022 Growth & exports\n\u2022 Resilience", "#f3e3e3"),
]
w, h = 2.6, 2.6
centers = []
for x, y, label, color in boxes:
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.12",
                         linewidth=1.3, edgecolor="#3a4a66", facecolor=color)
    ax.add_patch(box)
    ax.text(x + w/2, y + h - 0.18, label.split("\n")[0] + ("\n" + label.split("\n",1)[1] if "\n" in label else ""),
            ha="center", va="top", fontsize=8.6)
    centers.append((x + w/2, y + h/2))

for i in range(len(centers) - 1):
    x0 = boxes[i][0] + w; x1 = boxes[i+1][0]
    arr = FancyArrowPatch((x0, 3.4), (x1, 3.4), arrowstyle="-|>",
                          mutation_scale=16, linewidth=1.6, color="#3a4a66")
    ax.add_patch(arr)

# feedback loop
fb = FancyArrowPatch((10.6, 2.1), (1.6, 1.0), connectionstyle="arc3,rad=0.25",
                     arrowstyle="-|>", mutation_scale=14, linewidth=1.2,
                     color="#9b1c1c", linestyle="--")
ax.add_patch(fb)
ax.text(6.0, 0.55, "Performance feedback: reinvestment in capabilities and technology",
        ha="center", va="center", fontsize=8.2, color="#9b1c1c", style="italic")

fig.tight_layout()
fig.savefig("figure1_framework.png", dpi=200, bbox_inches="tight")
print("saved figure1_framework.png")
