import pandas as pd
import numpy as np
from scipy.stats import linregress
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

nav = pd.read_csv(BASE_DIR / "data/processed/02_nav_history_clean.csv")
benchmark = pd.read_csv(BASE_DIR / "data/processed/10_benchmark_indices_clean.csv")

# Date formatting
nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# -----------------------------
# Daily Returns
# -----------------------------
nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

# -----------------------------
# CAGR
# -----------------------------
cagr = []

for code, group in nav.groupby("amfi_code"):
    group = group.sort_values("date")

    start_nav = group["nav"].iloc[0]
    end_nav = group["nav"].iloc[-1]

    trading_days = len(group)

    years = trading_days / 252

    value = (end_nav / start_nav) ** (1 / years) - 1

    cagr.append([code, value])

cagr_df = pd.DataFrame(cagr, columns=["amfi_code", "CAGR"])

# -----------------------------
# Sharpe Ratio
# -----------------------------
risk_free = 0.065

sharpe = []

for code, group in nav.groupby("amfi_code"):

    ret = group["daily_return"].dropna()

    sr = ((ret.mean() * 252) - risk_free) / (ret.std() * np.sqrt(252))

    sharpe.append([code, sr])

sharpe_df = pd.DataFrame(sharpe, columns=["amfi_code", "Sharpe_Ratio"])

# -----------------------------
# Maximum Drawdown
# -----------------------------
drawdowns = []

for code, group in nav.groupby("amfi_code"):

    running_max = group["nav"].cummax()

    dd = (group["nav"] - running_max) / running_max

    drawdowns.append([code, dd.min()])

drawdown_df = pd.DataFrame(drawdowns, columns=["amfi_code", "Maximum_Drawdown"])

# -----------------------------
# Save Outputs
# -----------------------------
nav.to_csv(BASE_DIR/"data/processed/nav_with_daily_returns.csv", index=False)
cagr_df.to_csv(BASE_DIR/"data/processed/cagr_comparison.csv", index=False)
sharpe_df.to_csv(BASE_DIR/"data/processed/risk_metrics.csv", index=False)
drawdown_df.to_csv(BASE_DIR/"data/processed/max_drawdown.csv", index=False)

print("Performance metrics generated successfully.")