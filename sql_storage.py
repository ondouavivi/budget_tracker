import sqlite3
import pandas as pd

# 1. Connect (or create) local SQLite database
conn = sqlite3.connect('budget.db')
cur = conn.cursor()

# 2. Create table if it doesn’t exist
cur.execute('''
CREATE TABLE IF NOT EXISTS budget_ecarts (
    date TEXT,
    categorie TEXT,
    montant_prevu REAL,
    montant_reel REAL,
    ecart REAL
)
''')

# 3. Load merged data
df = pd.read_csv('merged_budget.csv', parse_dates=['date'])

# 4. Insert each row into the table
for _, row in df.iterrows():
    cur.execute('''
        INSERT INTO budget_ecarts (date, categorie, montant_prevu, montant_reel, ecart)
        VALUES (?, ?, ?, ?, ?)
    ''', (str(row['date']), row['categorie'],
          row['montant_prevu'], row['montant_reel'],
          row['ecart'])
    )

conn.commit()
conn.close()
print("→ Data stored into budget.db")