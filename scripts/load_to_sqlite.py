from sqlalchemy import create_engine
import pandas as pd
import os

# Get the project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create SQLite database
db_path = os.path.join(BASE_DIR, "bluestock_mf.db")
engine = create_engine(f"sqlite:///{db_path}")

# Mapping of table names to cleaned CSV files
files = {
    "fund_master": "01_fund_master_clean.csv",
    "nav_history": "02_nav_history_clean.csv",
    "aum_by_fund_house": "03_aum_by_fund_house_clean.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows_clean.csv",
    "category_inflows": "05_category_inflows_clean.csv",
    "industry_folio_count": "06_industry_folio_count_clean.csv",
    "scheme_performance": "07_scheme_performance_clean.csv",
    "investor_transactions": "08_investor_transactions_clean.csv",
    "portfolio_holdings": "09_portfolio_holdings_clean.csv",
    "benchmark_indices": "10_benchmark_indices_clean.csv"
}

print("Loading cleaned datasets into SQLite...\n")

for table_name, filename in files.items():
    file_path = os.path.join(BASE_DIR, "data", "processed", filename)

    if not os.path.exists(file_path):
        print(f"File not found: {filename}")
        continue

    df = pd.read_csv(file_path)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully ({len(df)} rows)")

print("\nAll datasets loaded successfully!")
print(f"Database created at:\n{db_path}")