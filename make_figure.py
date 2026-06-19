# -*- coding: utf-8 -*-
"""Generate Figure 1 (framework, clean feedback arrow) and Figure 2 (DTI
illustration, non-overlapping labels)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np


def build_figure1():
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    ax.set_xlim(0, 12.4); ax.set_ylim(0, 6.2); ax.axis("off")

    w, h, y0 = 2.7, 2.5, 2.6
    xs = [0.2, 3.25, 6.3, 9.35]
    titles = ["Drivers", "Dynamic\ncapabilities", "Digital\ntransformation", "SME\nperformance"]
    bodies = [
        "\u2022 Market & competition\n\u2022 Technology (cloud,\n  AI, data, e-commerce)\n\u2022 Policy & funding",
        "\u2022 Sensing\n\u2022 Seizing\n\u2022 Reconfiguring",
        "\u2022 Digitisation\n\u2022 Digitalisation\n\u2022 Business-model\n  change",
        "\u2022 Productivity\n\u2022 Growth & exports\n\u2022 Resilience",
    ]
    colors = ["#e8eef7", "#dfe9df", "#f6efe0", "#f3e3e3"]
    centers = []
    for x, ttl, body, col in zip(xs, titles, bodies, colors):
        ax.add_patch(FancyBboxPatch((x, y0), w, h, boxstyle="round,pad=0.04,rounding_size=0.12",
                                    linewidth=1.3, edgecolor="#3a4a66", facecolor=col))
        ax.text(x + w / 2, y0 + h - 0.22, ttl, ha="center", va="top", fontsize=10, fontweight="bold")
        ax.text(x + w / 2, y0 + h - 0.95, body, ha="center", va="top", fontsize=8.3)
        centers.append(x + w / 2)

    midy = y0 + h / 2
    for i in range(3):
        ax.add_patch(FancyArrowPatch((xs[i] + w, midy), (xs[i + 1], midy),
                                     arrowstyle="-|>", mutation_scale=16, linewidth=1.6, color="#3a4a66"))

    # Clean feedback arc: from SME performance (bottom) back to Dynamic capabilities (bottom)
    start = (centers[3], y0)
    end = (centers[1], y0)
    ax.add_patch(FancyArrowPatch(start, end, connectionstyle="arc3,rad=0.32",
                                 arrowstyle="-|>", mutation_scale=15, linewidth=1.4,
                                 color="#9b1c1c", linestyle=(0, (6, 4))))
    ax.text((centers[1] + centers[3]) / 2, 0.55,
            "Performance feedback: reinvestment in capabilities and technology",
            ha="center", va="center", fontsize=8.6, style="italic", color="#9b1c1c")

    fig.tight_layout()
    fig.savefig("figure1_framework.png", dpi=200, bbox_inches="tight")
    print("saved figure1_framework.png")


def build_figure2():
    profiles = ["Micro service firm\n(DTI = 0.33)",
                "Small manufacturer\n(DTI = 0.54)",
                "Medium exporter\n(DTI = 0.80)"]
    dti = [0.33, 0.54, 0.80]
    C_high, C_low = 0.8, 0.3
    dp_high = [round(d * C_high, 2) for d in dti]
    dp_low = [round(d * C_low, 2) for d in dti]

    x = np.arange(len(profiles)); width = 0.36
    fig, ax = plt.subplots(figsize=(6.8, 4.3))
    b1 = ax.bar(x - width / 2, dp_high, width, label="High capability (C = 0.8)", color="#1f3b73")
    b2 = ax.bar(x + width / 2, dp_low, width, label="Low capability (C = 0.3)", color="#b8c4dc")
    for bars in (b1, b2):
        for r in bars:
            ax.annotate("%.2f" % r.get_height(),
                        (r.get_x() + r.get_width() / 2, r.get_height()),
                        ha="center", va="bottom", fontsize=8.5, xytext=(0, 2),
                        textcoords="offset points")
    ax.set_xticks(x)
    ax.set_xticklabels(profiles, fontsize=9)
    ax.tick_params(axis="x", pad=6)
    ax.set_ylabel("Illustrative performance gain  \u0394P = \u03b2\u2083\u00b7(DTI\u00d7C)", fontsize=10)
    ax.set_ylim(0, max(dp_high) * 1.28)
    ax.legend(fontsize=9, frameon=False, loc="upper left")
    ax.grid(axis="y", ls=":", alpha=0.5)
    ax.margins(x=0.05)
    fig.subplots_adjust(bottom=0.2)
    fig.tight_layout()
    fig.savefig("figure2_dti_application.png", dpi=200, bbox_inches="tight")
    print("saved figure2_dti_application.png")


build_figure1()
build_figure2()
