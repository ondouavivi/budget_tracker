import pandas as pd
import numpy as np

# 1. Fix seed for reproducible “random” numbers
np.random.seed(42)

# 2. Define categories and a 6-month period
categories = ['Loyer', 'Alimentation', 'Transport', 'Loisirs', 'Santé']
dates = pd.date_range(start='2025-01-01', periods=6, freq='M')

# 3. Build budget prévisionnel
rows_prev = []
for date in dates:
    for cat in categories:
        # simulate a base amount (e.g. higher for Rent)
        base = 1000 if cat == 'Loyer' else 300
        montant = np.random.normal(loc=base, scale=base*0.05)
        rows_prev.append({
            'date': date.strftime('%Y-%m-%d'),
            'categorie': cat,
            'montant_prevu': round(max(montant, 0), 2)
        })
df_prev = pd.DataFrame(rows_prev)
df_prev.to_csv('budget_previsionnel.csv', index=False)
print("→ budget_previsionnel.csv generated")

# 4. Build dépenses réelles by adding noise around the prévisionnel
rows_real = []
for date in dates:
    for cat in categories:
        prev_val = float(
            df_prev.loc[
                (df_prev.date == date.strftime('%Y-%m-%d')) &
                (df_prev.categorie == cat),
                'montant_prevu'
            ]
        )
        real = prev_val * np.random.normal(loc=1.0, scale=0.1)
        rows_real.append({
            'date': date.strftime('%Y-%m-%d'),
            'categorie': cat,
            'montant_reel': round(max(real, 0), 2)
        })
df_real = pd.DataFrame(rows_real)
df_real.to_csv('depenses_reelles.csv', index=False)
print("→ depenses_reelles.csv generated")