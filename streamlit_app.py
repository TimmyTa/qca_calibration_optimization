"""
Streamlit viewer for fsQCA calibration grid results.

Run:
    streamlit run streamlit_app.py

Or point at a specific result folder:
    streamlit run streamlit_app.py -- --root results/grid_demo_20261017_082529
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="fsQCA Grid Viewer", layout="wide",
                   initial_sidebar_state="expanded")


# =============================================================== constants ==
# Only QCA-quality metrics — no runtime / algorithm comparison.
METRIC_GROUPS = {
    "Core (Tier 1)": [
        "S", "feasible",
        "row_precision", "row_recall",
        "cs_correct", "ps_sub_correct", "ps_exact",
        "ps_term_precision_sub",
    ],
    "Calibration": [
        "membership_mae", "same_side_0.5",
        "crossover_err_pct", "crossover_err_scaled",
        "crisp",
    ],
    "Truth table": [
        "cons", "cov", "n_positive_rows",
        "row_precision", "row_recall", "false_positive_rows",
    ],
    "Conservative solution (cs)": [
        "n_cs", "cs_correct", "cs_sub_correct", "cs_exact",
        "cs_complete_sup", "cs_complete_sub",
        "cs_term_precision", "cs_term_precision_sub",
        "cs_paths_found_sup", "cs_paths_found_sub",
        "cs_irrelevant_in",
    ],
    "Parsimonious solution (ps)": [
        "n_ps", "ps_correct", "ps_sub_correct", "ps_exact",
        "ps_complete_sup", "ps_complete_sub",
        "ps_term_precision", "ps_term_precision_sub",
        "ps_paths_found_sup", "ps_paths_found_sub",
        "ps_irrelevant_in",
    ],
    "Stability (optimize only)": [
        "S", "feasible",
        "opt_feasible", "opt_n_feasible_seeds", "opt_crossover_pct_sd",
    ],
}

# Thứ tự hiển thị mong muốn cho các mode
MODE_ORDER = [
    "oracle", "quantile", "kde", "expert", 
    "opt", "opt_c6c7", "opt_expert"
]


# =============================================================== helpers ====
@st.cache_data(show_spinner=False)
def load_csv(path):
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_json(path):
    return json.load(open(path))


def find_grid_folders(root):
    root = Path(root)
    if not root.exists() or root.is_file():
        return []
    return sorted({p.parent for p in root.rglob("grid_all.csv")})


def numeric_cols(df):
    return [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]


def parse_args():
    import sys
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None, help="Root folder containing results/")
    args, _ = ap.parse_known_args(sys.argv[1:])
    return args


def load_fuzzvalues(folder):
    """Read fuzzvalues from config.json → {fuzz_id: label}."""
    cfg_path = Path(folder) / "config.json"
    if not cfg_path.exists():
        return {}
    try:
        cfg = load_json(cfg_path)
    except Exception:
        return {}
    grid = cfg.get("grid", {})
    fuzz = grid.get("fuzzvalues", [])
    sim = cfg.get("simulation", {})
    if not fuzz and "fuzzvalues" in sim:
        fuzz = [sim["fuzzvalues"]]
    return {i: str(v) for i, v in enumerate(fuzz)}


def fuzz_label(fuzz_id, fuzz_map):
    if fuzz_id is None or pd.isna(fuzz_id):
        return "-"
    try:
        fid = int(fuzz_id)
    except (ValueError, TypeError):
        return str(fuzz_id)
    return fuzz_map.get(fid, f"fuzz_id={fid}")


def render_metric_group(df, group_name, metrics, num_cols, expanded=False):
    """Render one summary table for one metric group."""
    available = [m for m in metrics if m in num_cols]
    if not available:
        return
    with st.expander(f"📊 {group_name} ({len(available)} metrics)", expanded=expanded):
        agg = df.groupby("mode")[available].mean(numeric_only=True).round(4)
        agg.insert(0, "datasets", df.groupby("mode").size())
        
        # Sắp xếp theo MODE_ORDER
        ordered_modes = [m for m in MODE_ORDER if m in agg.index]
        # Thêm bất kỳ mode nào không có trong MODE_ORDER vào cuối
        ordered_modes += [m for m in agg.index if m not in ordered_modes]
        agg = agg.reindex(ordered_modes).reset_index()

        st.dataframe(agg, use_container_width=True, hide_index=True)


# ================================================================ sidebar ===
st.sidebar.title("⚙️ Settings")

args = parse_args()
default_root = Path(args.root) if args.root else Path.cwd()

root_input = st.sidebar.text_input(
    "Root folder (contains results/)",
    value=str(default_root),
    help="Enter a folder containing results/, e.g. `results/` or a specific run folder",
    key="root_input",
)

grid_folders = find_grid_folders(root_input)
if not grid_folders:
    st.sidebar.error(f"No `grid_all.csv` found under `{root_input}`")
    st.info("💡 Enter a folder that contains results/, e.g. `results/` or a specific run folder.")
    st.stop()

folder_names = [str(p) for p in grid_folders]
selected_folder = st.sidebar.selectbox(
    "Result folder",
    folder_names,
    index=len(folder_names) - 1,
    key="result_folder",
)
folder = Path(selected_folder)
st.sidebar.caption(f"📁 `{folder}`")

# --- load grid_all
grid_all_path = folder / "grid_all.csv"
if not grid_all_path.exists():
    st.error(f"Missing `{grid_all_path}`")
    st.stop()

df = load_csv(grid_all_path)

# --- load config + fuzzvalues
cfg = {}
cfg_path = folder / "config.json"
if cfg_path.exists():
    try:
        cfg = load_json(cfg_path)
    except Exception:
        cfg = {}

fuzz_map = load_fuzzvalues(folder)

# --- filters
st.sidebar.markdown("---")
st.sidebar.subheader("Filters")

modes = sorted(df["mode"].unique())
# Sắp xếp danh sách filter theo MODE_ORDER để dễ nhìn
ordered_filter_modes = [m for m in MODE_ORDER if m in modes]
ordered_filter_modes += [m for m in modes if m not in ordered_filter_modes]

sel_modes = st.sidebar.multiselect("Mode", ordered_filter_modes, default=ordered_filter_modes, key="f_mode")

ns = sorted(df["n"].unique()) if "n" in df else []
sel_n = st.sidebar.multiselect("n", ns, default=ns, key="f_n") if ns else []

noises = sorted(df["noise"].unique()) if "noise" in df else []
sel_noise = st.sidebar.multiselect("noise", noises, default=noises, key="f_noise") if noises else []

frags = sorted(df["frag"].unique()) if "frag" in df else []
sel_frag = st.sidebar.multiselect("frag", frags, default=frags, key="f_frag") if frags else []

# --- fuzzy_id filter with meaningful label
fuzz_ids = sorted(df["fuzz_id"].unique()) if "fuzz_id" in df else []
fuzz_labels = {fid: fuzz_label(fid, fuzz_map) for fid in fuzz_ids}
sel_fuzz = []
if fuzz_ids:
    sel_fuzz_labels = st.sidebar.multiselect(
        "fuzz_id",
        options=[fuzz_labels[f] for f in fuzz_ids],
        default=[fuzz_labels[f] for f in fuzz_ids],
        key="f_fuzz",
    )
    label_to_id = {v: k for k, v in fuzz_labels.items()}
    sel_fuzz = [label_to_id[l] for l in sel_fuzz_labels if l in label_to_id]

mask = df["mode"].isin(sel_modes)
if sel_n: mask &= df["n"].isin(sel_n)
if sel_noise: mask &= df["noise"].isin(sel_noise)
if sel_frag: mask &= df["frag"].isin(sel_frag)
if sel_fuzz: mask &= df["fuzz_id"].isin(sel_fuzz)
df_f = df[mask].copy()

if df_f.empty:
    st.warning("No data after filtering.")
    st.stop()

# --- metrics
st.sidebar.markdown("---")
st.sidebar.subheader("Metrics")
num_cols = numeric_cols(df_f)
default_metrics = [m for m in ["S", "cons", "cov", "crisp", "row_recall",
                              "membership_mae", "ps_exact", "cs_correct"]
                   if m in num_cols]
sel_metrics = st.sidebar.multiselect(
    "Metrics to display", num_cols, default=default_metrics, key="f_metrics"
)

# --- config viewer
st.sidebar.markdown("---")
with st.sidebar.expander("📄 Config (config.json)", expanded=False):
    if cfg:
        st.markdown("**Simulation**")
        st.json(cfg.get("simulation", {}))
        st.markdown("**Grid**")
        st.json(cfg.get("grid", {}))
        st.markdown("**qca_rule**")
        st.code(str(cfg.get("qca_rule", "conventional")))
        st.markdown("**Modes**")
        st.json(cfg.get("modes", []))
        with st.popover("Full config"):
            st.json(cfg)
    else:
        st.caption("No config.json found.")

# ================================================================ header ====
st.title("📊 fsQCA Grid Viewer")
st.caption(f"Folder: `{folder}` — {len(df_f)} / {len(df)} rows")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Datasets", df_f["dataset"].nunique())
c2.metric("Modes", df_f["mode"].nunique())
c3.metric("n", ", ".join(map(str, sorted(df_f["n"].unique()))) if "n" in df_f else "-")
c4.metric("noise", ", ".join(map(str, sorted(df_f["noise"].unique()))) if "noise" in df_f else "-")
c5.metric("fuzz_id", ", ".join(str(f) for f in sorted(df_f["fuzz_id"].unique())) if "fuzz_id" in df_f else "-")

# ================================================================ tabs ======
tabs = st.tabs([
    "📋 Summary",
    "📊 Compare modes",
    "📈 Trend",
    "🔥 Heatmap",
    "🔵 Scatter",
    "📁 Dataset",
    "🧪 Fuzz values",
    "🗂️ Raw",
])

# ---------------------------------------------------------------- summary --
with tabs[0]:
    st.subheader("Summary by metric group")

    groups_to_show = st.multiselect(
        "Groups to display",
        list(METRIC_GROUPS.keys()),
        default=list(METRIC_GROUPS.keys()),
        key="summary_groups",
    )

    for group_name in groups_to_show:
        render_metric_group(
            df_f, group_name, METRIC_GROUPS[group_name], num_cols,
            expanded=(group_name == "Core (Tier 1)"),
        )

    st.markdown("---")
    st.subheader("Bar chart")
    if sel_metrics:
        bar_metric = st.selectbox("Metric", sel_metrics, key="summary_bar_metric")
        agg_long = df_f.groupby("mode")[bar_metric].mean().reset_index()
        
        # Sắp xếp theo MODE_ORDER
        agg_long["mode"] = pd.Categorical(agg_long["mode"], categories=MODE_ORDER, ordered=True)
        agg_long = agg_long.sort_values("mode")

        fig = px.bar(agg_long, x="mode", y=bar_metric, color="mode",
                     title=f"{bar_metric} — mean per mode")
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- compare --
with tabs[1]:
    st.subheader("Compare modes by metric")
    if sel_metrics:
        cmp_metric = st.selectbox("Metric", sel_metrics, key="compare_metric")
        group_cols = [c for c in ["n", "noise", "frag", "fuzz_id"] if c in df_f.columns]
        group = st.multiselect(
            "Group by", group_cols + ["mode"],
            default=group_cols + ["mode"], key="compare_group",
        )
        if group:
            piv = df_f.pivot_table(
                index="mode", columns=group_cols,
                values=cmp_metric, aggfunc="mean",
            ).round(3)
            
            # Sắp xếp theo MODE_ORDER
            ordered_idx = [m for m in MODE_ORDER if m in piv.index]
            ordered_idx += [m for m in piv.index if m not in ordered_idx]
            piv = piv.reindex(ordered_idx)

            if "fuzz_id" in group_cols:
                piv = piv.rename(columns={f: fuzz_label(f, fuzz_map) for f in piv.columns})
            st.dataframe(piv, use_container_width=True)

        # Boxplot - Plotly tự động sắp xếp theo category
        plot_df = df_f.copy()
        plot_df["mode"] = pd.Categorical(plot_df["mode"], categories=MODE_ORDER, ordered=True)
        plot_df = plot_df.sort_values("mode")

        fig = px.box(plot_df, x="mode", y=cmp_metric, color="mode",
                     title=f"{cmp_metric} distribution by mode")
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("📄 Full table"):
        show = df_f.copy()
        if "fuzz_id" in show.columns:
            show["fuzzvalues"] = show["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
        st.dataframe(show, use_container_width=True)

# ---------------------------------------------------------------- trend ---
with tabs[2]:
    st.subheader("Trend over noise / frag / n")
    if sel_metrics:
        trend_metric = st.selectbox("Metric", sel_metrics, key="trend_metric")
        trend_x = st.selectbox(
            "X axis",
            [c for c in ["noise", "frag", "n", "fuzz_id"] if c in df_f.columns],
            key="trend_x",
        )
        trend_color = st.selectbox(
            "Color", ["mode", "n", "noise", "frag", "fuzz_id"], key="trend_color"
        )
        trend_facet = st.selectbox(
            "Facet (optional)",
            ["(none)"] + [c for c in ["n", "noise", "frag"] if c in df_f.columns],
            key="trend_facet",
        )

        plot_df = df_f.copy()
        if "fuzz_id" in plot_df.columns:
            plot_df["fuzzvalues"] = plot_df["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
        if trend_x == "fuzz_id":
            trend_x = "fuzzvalues"
        if trend_color == "fuzz_id":
            trend_color = "fuzzvalues"

        # Nếu color là mode, sắp xếp lại để legend hiển thị đúng thứ tự
        if trend_color == "mode":
            plot_df["mode"] = pd.Categorical(plot_df["mode"], categories=MODE_ORDER, ordered=True)
            plot_df = plot_df.sort_values("mode")

        kwargs = dict(
            data_frame=plot_df, x=trend_x, y=trend_metric,
            color=trend_color, markers=True,
            title=f"{trend_metric} vs {trend_x}",
        )
        if trend_facet != "(none)":
            kwargs["facet_col"] = trend_facet
        fig = px.line(**kwargs)
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- heatmap --
with tabs[3]:
    st.subheader("Heatmap")
    if sel_metrics:
        heat_metric = st.selectbox("Metric", sel_metrics, key="heat_metric")
        heat_x = st.selectbox("X", ["noise", "frag", "n", "fuzz_id"], index=0, key="heat_x")
        heat_y = st.selectbox("Y", ["frag", "noise", "n", "fuzz_id"], index=0, key="heat_y")
        heat_mode = st.selectbox(
            "Mode", ["(all)"] + list(df_f["mode"].unique()), key="heat_mode"
        )
        sub = df_f if heat_mode == "(all)" else df_f[df_f["mode"] == heat_mode]

        if heat_x == "fuzz_id":
            sub = sub.copy()
            sub["fuzzvalues"] = sub["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
            heat_x = "fuzzvalues"
        if heat_y == "fuzz_id":
            sub = sub.copy()
            sub["fuzzvalues"] = sub["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
            heat_y = "fuzzvalues"

        piv = sub.pivot_table(
            index=heat_y, columns=heat_x, values=heat_metric, aggfunc="mean"
        )
        if not piv.empty:
            fig = px.imshow(
                piv, text_auto=".3f", color_continuous_scale="RdYlGn",
                title=f"{heat_metric} | mode={heat_mode} | x={heat_x}, y={heat_y}",
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Not enough data to build a heatmap.")

# ---------------------------------------------------------------- scatter --
with tabs[4]:
    st.subheader("Scatter")
    if len(num_cols) >= 2:
        c1, c2 = st.columns(2)
        scat_x = c1.selectbox("X", num_cols, index=0, key="scatter_x")
        scat_y = c2.selectbox("Y", num_cols, index=min(1, len(num_cols) - 1), key="scatter_y")
        scat_color = st.selectbox(
            "Color",
            ["mode"] + [c for c in ["n", "noise", "frag", "fuzz_id"] if c in df_f.columns],
            key="scatter_color",
        )
        plot_df = df_f.copy()
        if "fuzz_id" in plot_df.columns:
            plot_df["fuzzvalues"] = plot_df["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
        if scat_color == "fuzz_id":
            scat_color = "fuzzvalues"

        # Nếu color là mode, sắp xếp lại để legend hiển thị đúng thứ tự
        if scat_color == "mode":
            plot_df["mode"] = pd.Categorical(plot_df["mode"], categories=MODE_ORDER, ordered=True)
            plot_df = plot_df.sort_values("mode")

        fig = px.scatter(
            plot_df, x=scat_x, y=scat_y, color=scat_color,
            hover_data=[c for c in ["dataset", "n", "noise", "frag", "fuzz_id"] if c in plot_df.columns],
            title=f"{scat_y} vs {scat_x}",
        )
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------- dataset --
with tabs[5]:
    st.subheader("Dataset details")
    datasets = sorted(df_f["dataset"].unique())
    ds = st.selectbox("Dataset", datasets, key="ds_select")
    ds_dir = folder / "datasets" / ds

    if not ds_dir.exists():
        st.warning(f"Missing folder `{ds_dir}`")
    else:
        cmp_path = ds_dir / "compare.csv"
        if cmp_path.exists():
            st.markdown("### compare.csv")
            c_df = load_csv(cmp_path)
            if "mode" in c_df.columns:
                c_df["mode"] = pd.Categorical(c_df["mode"], categories=MODE_ORDER, ordered=True)
                c_df = c_df.sort_values("mode")
            st.dataframe(c_df, use_container_width=True)

        md_path = ds_dir / "compare.md"
        if md_path.exists():
            with st.expander("📄 compare.md"):
                st.markdown(md_path.read_text())

        anc_path = ds_dir / "anchors_compare.csv"
        if anc_path.exists():
            st.markdown("### anchors_compare.csv")
            st.dataframe(load_csv(anc_path), use_container_width=True)

        truth_path = ds_dir / "data" / "truth.json"
        if truth_path.exists():
            with st.expander("📄 truth.json"):
                st.json(load_json(truth_path))

        modes_dir = ds_dir / "modes"
        if modes_dir.exists():
            mode_names = sorted([p.name for p in modes_dir.iterdir() if p.is_dir()])
            if mode_names:
                ordered_mode_names = [m for m in MODE_ORDER if m in mode_names]
                ordered_mode_names += [m for m in mode_names if m not in ordered_mode_names]
                
                m = st.selectbox("Mode", ordered_mode_names, key="ds_mode")
                m_dir = modes_dir / m
                c1, c2 = st.columns(2)
                with c1:
                    anc = m_dir / "anchors.json"
                    if anc.exists():
                        st.markdown("**anchors.json**")
                        st.json(load_json(anc))
                with c2:
                    sol = m_dir / "solutions.json"
                    if sol.exists():
                        st.markdown("**solutions.json**")
                        st.json(load_json(sol))
                for f in ("truth_table.csv", "calibrated.csv", "seeds.csv"):
                    p = m_dir / f
                    if p.exists():
                        st.markdown(f"**{f}**")
                        st.dataframe(load_csv(p), use_container_width=True)

# ---------------------------------------------------------------- fuzz ----
with tabs[6]:
    st.subheader("Fuzz values")
    if fuzz_map:
        st.markdown("Map `fuzz_id` → `fuzzvalues` (from `config.json`):")
        fuzz_df = pd.DataFrame(
            [{"fuzz_id": k, "fuzzvalues": v} for k, v in sorted(fuzz_map.items())]
        )
        st.dataframe(fuzz_df, use_container_width=True, hide_index=True)

        st.markdown("### Distribution of fuzz_id in grid_all")
        if "fuzz_id" in df_f.columns:
            counts = df_f["fuzz_id"].value_counts().sort_index().reset_index()
            counts.columns = ["fuzz_id", "count"]
            counts["fuzzvalues"] = counts["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
            st.dataframe(counts, use_container_width=True, hide_index=True)
    else:
        st.info("No `fuzzvalues` found in `config.json`.")

    with st.expander("📄 config.json"):
        if cfg:
            st.json(cfg)
        else:
            st.caption("No config.json.")

# ---------------------------------------------------------------- raw -----
with tabs[7]:
    st.subheader("grid_all.csv (filtered)")
    show = df_f.copy()
    if "fuzz_id" in show.columns:
        show["fuzzvalues"] = show["fuzz_id"].map(lambda x: fuzz_label(x, fuzz_map))
    st.dataframe(show, use_container_width=True)

    st.download_button(
        "⬇️ Download filtered CSV",
        show.to_csv(index=False).encode("utf-8"),
        file_name="grid_filtered.csv",
        mime="text/csv",
        key="download_filtered",
    )

    if cfg:
        with st.expander("📄 config.json"):
            st.json(cfg)

    fail_path = folder / "failures.csv"
    if fail_path.exists():
        st.markdown("### failures.csv")
        st.dataframe(load_csv(fail_path), use_container_width=True)