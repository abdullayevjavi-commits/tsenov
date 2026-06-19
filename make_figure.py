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



# ---------------------------------------------------------------------------
# Figure 2: Illustrative application of the DTI index - performance gain (DeltaP)
# for three SME archetypes under high vs low dynamic-capability levels.
# Purely illustrative (assumed adoption values); demonstrates the DTI x C interaction.
# ---------------------------------------------------------------------------
def build_figure2():
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Equal-weighted DTI from assumed adoption vectors over 7 digital elements
    archetypes = ["Micro service\nfirm", "Small\nmanufacturer", "Medium\nexporter"]
    adoption = {
        "Micro service\nfirm":  [1.0, 0.5, 0.5, 0.2, 0.1, 0.0, 0.0],
        "Small\nmanufacturer":  [1.0, 0.7, 0.6, 0.6, 0.5, 0.3, 0.1],
        "Medium\nexporter":     [1.0, 0.9, 0.9, 0.8, 0.8, 0.7, 0.5],
    }
    w = 1.0 / 7.0
    dti = {k: round(sum(v) * w, 2) for k, v in adoption.items()}
    C_high, C_low, beta = 0.8, 0.3, 1.0
    dp_high = [beta * dti[a] * C_high for a in archetypes]
    dp_low = [beta * dti[a] * C_low for a in archetypes]

    x = np.arange(len(archetypes)); width = 0.36
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    b1 = ax.bar(x - width/2, dp_high, width, label="High capability (C = 0.8)", color="#1f3b73")
    b2 = ax.bar(x + width/2, dp_low, width, label="Low capability (C = 0.3)", color="#b8c4dc")
    for bars in (b1, b2):
        for r in bars:
            ax.annotate("%.2f" % r.get_height(), (r.get_x() + r.get_width()/2, r.get_height()),
                        ha="center", va="bottom", fontsize=8)
    ax.set_xticks(x); ax.set_xticklabels(archetypes, fontsize=9)
    for i, a in enumerate(archetypes):
        ax.annotate("DTI = %.2f" % dti[a], (i, -0.06), ha="center", va="top",
                    fontsize=8, color="#555555", annotation_clip=False)
    ax.set_ylabel("Performance gain  \u0394P = \u03b2\u00b7DTI\u00b7C  (illustrative)", fontsize=10)
    ax.set_ylim(0, max(dp_high) * 1.25)
    ax.legend(fontsize=9, frameon=False, loc="upper left")
    ax.grid(axis="y", ls=":", alpha=0.5)
    fig.tight_layout()
    fig.savefig("figure2_dti_application.png", dpi=200, bbox_inches="tight")
    print("saved figure2_dti_application.png ; DTI =", dti)


build_figure2()
