"""Generate Figure 1: illustrative social welfare as a function of the number of
universities, showing the interior optimum n* that balances quality (scale
economies) against competition, variety and access.

The curve is purely illustrative of the model in Section 3; it is not an
empirical estimate.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

n = np.linspace(1, 60, 600)

# Quality benefit: rises then is diluted as resources are spread over more HEIs
# N*v(Q(n)) with Q(n) decreasing in n -> concave, decreasing component for large n
quality_benefit = 120 * np.log(n + 1) - 1.4 * n          # scale / quality term
# Competition, variety and access benefit: increasing, concave
variety_competition = 70 * (1 - np.exp(-0.12 * n))        # g(n)
# Fixed-cost duplication: linear in n
fixed_cost = 2.3 * n

welfare = quality_benefit + variety_competition - fixed_cost

n_star = n[np.argmax(welfare)]
w_star = welfare.max()

fig, ax = plt.subplots(figsize=(6.3, 4.0))
ax.plot(n, welfare, color="#1f3b73", lw=2.2, label="Social welfare  W(n)")
ax.axvline(n_star, color="#9b1c1c", ls="--", lw=1.3)
ax.scatter([n_star], [w_star], color="#9b1c1c", zorder=5)
ax.annotate(r"$n^{*}$",
            xy=(n_star, w_star),
            xytext=(n_star + 3, w_star - 18),
            fontsize=13, color="#9b1c1c")

ax.set_xlabel("Number of universities (n)", fontsize=11)
ax.set_ylabel("Social welfare (illustrative units)", fontsize=11)
ax.set_title("")
ax.grid(True, ls=":", alpha=0.5)
ax.legend(loc="lower center", fontsize=10, frameon=False)
ax.margins(x=0)
fig.tight_layout()
fig.savefig("figure1_welfare.png", dpi=200)
print("saved figure1_welfare.png ; n_star =", round(n_star, 1))
