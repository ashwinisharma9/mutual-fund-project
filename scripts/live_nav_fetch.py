import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("Fund Name:", data["meta"]["scheme_name"])
print("Fund House:", data["meta"]["fund_house"])

nav_df = pd.DataFrame(data["data"])

print("\nFirst 5 Records:")
print(nav_df.head())

nav_df.to_csv(
    "data/raw/hdfc_top100_nav.csv",
    index=False
)

print("\nCSV saved successfully!")