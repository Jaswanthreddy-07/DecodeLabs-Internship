import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "raw" / "Dataset for Data Analytics.xlsx"
output_dir = BASE_DIR / "data" / "cleaned"
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(input_file)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing numeric values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned data
df.to_csv(output_dir / "cleaned_data.csv", index=False)

print("✅ Cleaning completed successfully!")
