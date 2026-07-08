import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

risk = pd.read_csv(BASE_DIR/"data/processed/risk_metrics.csv")
cagr = pd.read_csv(BASE_DIR/"data/processed/cagr_comparison.csv")

data = risk.merge(cagr, on="amfi_code")

# Recommendation Logic
def recommend(row):

    if row["Sharpe_Ratio"] > 1.2 and row["CAGR"] > 0.12:
        return "Highly Recommended"

    elif row["Sharpe_Ratio"] > 0.8:
        return "Recommended"

    else:
        return "High Risk"

data["Recommendation"] = data.apply(recommend, axis=1)

data.to_csv(BASE_DIR/"data/processed/fund_recommendations.csv", index=False)

print(data[["amfi_code","Recommendation"]].head())

print("\nRecommendations generated successfully.")