import sqlite3
import pandas as pd
import os
from pathlib import Path


base_path = Path(__file__).resolve().parent.parent

# Defined paths relative to the Project Root
csv_path = base_path / "Data" / "cleaned_parts.csv"
db_path = base_path / "db" / "sandbox.db"

# Ensure the db directory exists
os.makedirs(base_path / "db", exist_ok=True)

# 3. Connect and Load
conn = sqlite3.connect(db_path)

if csv_path.exists():
    df = pd.read_csv(csv_path)
    df.to_sql("parts", conn, if_exists="replace", index=False)
    print(f"Successfully loaded {len(df)} rows into SQLite sandbox.")
else:
    print(f"Error: Could not find the file at {csv_path}")

conn.close()