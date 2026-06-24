import pandas as pd

file_path = "data/raw/hdfc_top100_nav.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("SHAPE")
print(df.shape)

print("\n" + "=" * 50)
print("DATA TYPES")
print(df.dtypes)

print("\n" + "=" * 50)
print("FIRST 5 ROWS")
print(df.head())

print("\n" + "=" * 50)
print("MISSING VALUES")
print(df.isnull().sum())