"""
view_grid.py — đọc và visualize grid_all.csv / grid_summary_by_mode.csv

Usage:
    python view_grid.py grid_all.csv
    python view_grid.py grid_all.csv --mode opt --n 200
    python view_grid.py grid_all.csv --plot S,crisp,row_recall
    python view_grid.py grid_all.csv --heatmap S --x noise --y frag
    python view_grid.py grid_all.csv --trend S --x noise --n 200
    python view_grid.py grid_all.csv --scatter membership_mae crisp
    python view_grid.py grid_all.csv --plot S crisp --save out.png
"""

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="talk")


# ---------------------------------------------------------------- load ----
TEXT_COLS = {
    "dataset", "mode", "rule",
    "cs_solution", "ps_solution",
    "cs_irrelevant_in", "ps_irrelevant_in",
}


def to_numeric_safe(s):
    """Chuyển sang numeric nếu được, ngược lại giữ nguyên."""
    try:
        return pd.to_numeric(s, errors="raise")
    except (ValueError, TypeError):
        return s


def load(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]

    # cách 1: whitelist text cols (nhanh, rõ ràng)
    for c in df.columns:
        if c in TEXT_COLS:
            continue
        df[c] = to_numeric_safe(df[c])

    return df


def filter_df(df, mode=None, n=None, noise=None, frag=None, fuzz_id=None):
    if mode:
        df = df[df["mode"].isin(mode if isinstance(mode, list) else [mode])]
    if n is not None:
        df = df[df["n"].isin(n if isinstance(n, list) else [n])]
    if noise is not None:
        df = df[df["noise"].isin(noise if isinstance(noise, list) else [noise])]
    if frag is not None:
        df = df[df["frag"].isin(frag if isinstance(frag, list) else [frag])]
    if fuzz_id is not None:
        df = df[df["fuzz_id"].isin(fuzz_id if isinstance(fuzz_id, list) else [fuzz_id])]
    return df


# -------------------------------------------------------------- summary ----
def summarize(df, group="mode"):
    metrics = ["S", "feasible", "membership_mae", "same_side_0.5",
               "crossover_err_pct", "crisp", "row_precision", "row_recall",
               "cs_correct", "cs_term_precision", "ps_exact",
               "ps_term_precision_sub", "ps_irrelevant_in"]
    metrics = [m for m in metrics if m in df.columns]
    return df.groupby(group)[metrics].mean(numeric_only=True).round(4)


# ---------------------------------------------------------------- plots ----
def plot_metric(df, metric, group="mode", agg="mean", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))
    data = df.groupby(group)[metric].agg(agg).reset_index()
    sns.barplot(data=data, x=group, y=metric, ax=ax, palette="viridis")
    ax.set_title(f"{metric} by {group}")
    ax.tick_params(axis="x", rotation=45)
    return ax


def plot_box(df, metric, group="mode", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x=group, y=metric, ax=ax, palette="Set2")
    ax.set_title(f"{metric} distribution by {group}")
    ax.tick_params(axis="x", rotation=45)
    return ax


def plot_heatmap(df, metric, x="noise", y="frag", mode=None, ax=None):
    sub = df[df["mode"] == mode] if mode else df
    pivot = sub.pivot_table(index=y, columns=x, values=metric, aggfunc="mean")
    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(pivot, annot=True, fmt=".3f", cmap="RdYlGn", ax=ax)
    ax.set_title(f"{metric} | mode={mode or 'all'} | x={x}, y={y}")
    return ax


def plot_scatter(df, x, y, hue="mode", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax, s=60, alpha=0.7)
    ax.set_title(f"{y} vs {x}")
    return ax


def plot_trend(df, metric, x="noise", hue="mode", n=None, ax=None):
    sub = df if n is None else df[df["n"] == n]
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=sub, x=x, y=metric, hue=hue, marker="o", ax=ax, errorbar="sd")
    ax.set_title(f"{metric} vs {x}" + (f" (n={n})" if n else ""))
    return ax


# ------------------------------------------------------------------ CLI ----
def parse_list(value):
    """Chấp nhận cả 'a,b,c' và ['a','b','c']."""
    if value is None:
        return None
    out = []
    for v in value:
        out.extend(str(v).split(","))
    return [v.strip() for v in out if v.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="grid_all.csv hoặc grid_summary_by_mode.csv")
    ap.add_argument("--mode", nargs="*", default=None)
    ap.add_argument("--n", nargs="*", type=int, default=None)
    ap.add_argument("--noise", nargs="*", type=float, default=None)
    ap.add_argument("--frag", nargs="*", type=float, default=None)
    ap.add_argument("--fuzz_id", nargs="*", type=int, default=None)
    ap.add_argument("--plot", nargs="*", default=None,
                    help="các metric cần vẽ, ví dụ: --plot S,crisp hoặc --plot S crisp")
    ap.add_argument("--box", nargs="*", default=None,
                    help="các metric cần vẽ boxplot")
    ap.add_argument("--heatmap", default=None, help="metric cho heatmap")
    ap.add_argument("--heatmap-mode", default=None, help="mode cho heatmap (mặc định all)")
    ap.add_argument("--x", default="noise")
    ap.add_argument("--y", default="frag")
    ap.add_argument("--trend", default=None, help="metric cho line plot")
    ap.add_argument("--scatter", nargs=2, default=None, help="x y")
    ap.add_argument("--save", default=None, help="đường dẫn lưu hình (prefix)")
    args = ap.parse_args()

    df = load(args.path)
    df = filter_df(df, mode=args.mode, n=args.n, noise=args.noise,
                   frag=args.frag, fuzz_id=args.fuzz_id)

    print("=" * 60)
    print(f"Loaded {len(df)} rows from {args.path}")
    if "mode" in df: print("Modes:", sorted(df["mode"].unique()))
    if "n" in df: print("n:", sorted(df["n"].unique()))
    if "noise" in df: print("noise:", sorted(df["noise"].unique()))
    if "frag" in df: print("frag:", sorted(df["frag"].unique()))
    if "fuzz_id" in df: print("fuzz_id:", sorted(df["fuzz_id"].unique()))
    print("=" * 60)

    print("\n--- Summary by mode ---")
    print(summarize(df).to_string())

    plot_metrics = parse_list(args.plot)
    box_metrics = parse_list(args.box)

    # ---- bar plots
    if plot_metrics:
        ncols = min(len(plot_metrics), 3)
        nrows = int(np.ceil(len(plot_metrics) / ncols))
        fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 4 * nrows))
        axes = np.atleast_1d(axes).ravel()
        for ax, m in zip(axes, plot_metrics):
            if m not in df.columns:
                ax.axis("off")
                continue
            plot_metric(df, m, ax=ax)
        for ax in axes[len(plot_metrics):]:
            ax.axis("off")
        plt.tight_layout()
        if args.save:
            f = f"{args.save}_bar.png"
            plt.savefig(f, dpi=150, bbox_inches="tight")
            print(f"saved {f}")
        else:
            plt.show()

    # ---- box plots
    if box_metrics:
        ncols = min(len(box_metrics), 3)
        nrows = int(np.ceil(len(box_metrics) / ncols))
        fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 4 * nrows))
        axes = np.atleast_1d(axes).ravel()
        for ax, m in zip(axes, box_metrics):
            if m not in df.columns:
                ax.axis("off")
                continue
            plot_box(df, m, ax=ax)
        for ax in axes[len(box_metrics):]:
            ax.axis("off")
        plt.tight_layout()
        if args.save:
            f = f"{args.save}_box.png"
            plt.savefig(f, dpi=150, bbox_inches="tight")
            print(f"saved {f}")
        else:
            plt.show()

    # ---- heatmap
    if args.heatmap:
        plot_heatmap(df, args.heatmap, x=args.x, y=args.y, mode=args.heatmap_mode)
        plt.tight_layout()
        if args.save:
            f = f"{args.save}_heatmap_{args.heatmap}.png"
            plt.savefig(f, dpi=150, bbox_inches="tight")
            print(f"saved {f}")
        else:
            plt.show()

    # ---- trend
    if args.trend:
        for n in (args.n or sorted(df["n"].unique())):
            plot_trend(df, args.trend, x=args.x, n=n)
            plt.tight_layout()
            if args.save:
                f = f"{args.save}_trend_{args.trend}_n{n}.png"
                plt.savefig(f, dpi=150, bbox_inches="tight")
                print(f"saved {f}")
            else:
                plt.show()

    # ---- scatter
    if args.scatter:
        x, y = args.scatter
        plot_scatter(df, x, y)
        plt.tight_layout()
        if args.save:
            f = f"{args.save}_scatter_{x}_{y}.png"
            plt.savefig(f, dpi=150, bbox_inches="tight")
            print(f"saved {f}")
        else:
            plt.show()


if __name__ == "__main__":
    main()
