import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

INPUT_FILE = os.path.join(DATA_DIR, "legacy_parts.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_parts.csv")

os.makedirs(DATA_DIR, exist_ok=True)

# Load legacy data
df = pd.read_csv(INPUT_FILE)

# Drop duplicates (keep latest modification)
df = df.sort_values("last_modified").drop_duplicates(
    subset=["part_id"], keep="last"
)

# Fill missing revisions
df["revision"] = df["revision"].fillna("A")

# Remove invalid weights
df = df[df["weight_kg"] > 0]

# Normalize dates
df["last_modified"] = pd.to_datetime(df["last_modified"])

# Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print("Validation & transformation complete.")
print(f"Input file: {INPUT_FILE}")
print(f"Output file: {OUTPUT_FILE}")
print(f"Record count: {len(df)}")

