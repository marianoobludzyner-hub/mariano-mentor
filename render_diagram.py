#!/usr/bin/env python3
"""
Flow diagram for the mariano-mentor repo.
Obludzyner & Co. | https://obludzyner.com

OPTIONAL, one-off. Requires matplotlib:
    pip install matplotlib
    python3 render_diagram.py examples/flow-diagram.png
"""

import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
SURFACE = "#fcfcfb"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
GREEN = "#0ca30c"

plt.rcParams["font.family"] = "DejaVu Sans"


def box(ax, x, y, w, h, title, subtitle, color, title_size=10.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.06",
                                  linewidth=1.4, edgecolor=color, facecolor="#ffffff"))
    ax.text(x + w / 2, y + h * 0.66, title, fontsize=title_size, fontweight="bold", color=INK,
             ha="center", va="center")
    ax.text(x + w / 2, y + h * 0.30, subtitle, fontsize=8.3, color=INK_SECONDARY,
             ha="center", va="center", linespacing=1.4)


def arrow(ax, x0, y, x1, color=INK_MUTED):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=13,
                                   linewidth=1.6, color=color))


def render(out_path):
    steps = [
        ("1. Discovery\nskill", "One question at a\ntime, 5 categories", BLUE),
        ("2. Five .md\nfiles", "company, motion,\nnumbers, team, goals", BLUE),
        ("3. Claude\nProject", "uploaded as\nproject knowledge", ORANGE),
        ("4. Mariano\nMentor", "reads the project,\ndiagnoses with SHIFT", GREEN),
        ("5. Grounded\nadvice", "specific to your\nnumbers, not generic", GREEN),
    ]

    n = len(steps)
    w, h, gap, y = 1.9, 1.65, 0.32, 1.0
    total_w = n * w + (n - 1) * gap
    fig_w = total_w + 0.6

    fig, ax = plt.subplots(figsize=(fig_w, 3.6), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, 3.6)
    ax.axis("off")

    fig.text(0.02, 0.95, "OBLUDZYNER & CO.  -  MARIANO MENTOR: HOW IT FITS TOGETHER",
              fontsize=9.5, color=INK_MUTED, fontweight="bold", ha="left")

    x = 0.3
    for i, (title, subtitle, color) in enumerate(steps):
        box(ax, x, y, w, h, title, subtitle, color)
        if i < n - 1:
            arrow(ax, x + w + 0.04, y + h / 2, x + w + gap - 0.04)
        x += w + gap

    fig.text(0.02, 0.06, "obludzyner.com | open-source SHIFT Method tools", fontsize=9, color=INK_MUTED)

    fig.savefig(out_path, facecolor=SURFACE, bbox_inches="tight")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "examples/flow-diagram.png"
    render(out)
