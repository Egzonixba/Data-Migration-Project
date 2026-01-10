import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "db", "sandbox.db")

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Row count
cursor.execute("SELECT COUNT(*) FROM parts;")
count = cursor.fetchone()[0]

# Data quality checks
cursor.execute("SELECT COUNT(*) FROM parts WHERE revision IS NULL;")
null_revisions = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM parts WHERE weight_kg <= 0;")
invalid_weights = cursor.fetchone()[0]

conn.close()

print(f"Records in sandbox DB: {count}")
print(f"NULL revisions: {null_revisions}")
print(f"Invalid weights: {invalid_weights}")
