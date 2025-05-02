import pandas as pd
import matplotlib.pyplot as plt

# 1. Load both CSVs
df_prev = pd.read_csv('budget_previsionnel.csv', parse_dates=['date'])
df_real = pd.read_csv('depenses_reelles.csv',    parse_dates=['date'])

# 2. Merge on date + categorie
df = pd.merge(df_prev, df_real, on=['date', 'categorie'])
# 3. Compute the gap (écart)
df['ecart'] = df['montant_reel'] - df['montant_prevu']

# 4. Save merged data for later steps
df.to_csv('merged_budget.csv', index=False)
print("→ merged_budget.csv saved")

# 5. Quick stats by category
stats = df.groupby('categorie')['ecart'].agg(['mean', 'min', 'max', 'sum'])
print("\nÉcarts par catégorie :\n", stats)

# 6. Bar chart: total gap per category
total_gap = df.groupby('categorie')['ecart'].sum().sort_values()
total_gap.plot(kind='bar')
plt.title('Écart total par catégorie')
plt.xlabel('Catégorie')
plt.ylabel('Montant (€)')
plt.tight_layout()
plt.savefig('ecart_par_categorie.png')
plt.close()
print("→ ecart_par_categorie.png generated")

# 7. Line plot: prévues vs réelles pour “Alimentation” (exemple)
cat = 'Alimentation'
df_cat = df[df.categorie == cat].set_index('date')
df_cat[['montant_prevu', 'montant_reel']].plot()
plt.title(f'Prévu vs Réel – {cat}')
plt.xlabel('Date')
plt.ylabel('Montant (€)')
plt.tight_layout()
plt.savefig('prevision_reel_Alimentation.png')
plt.close()
print("→ prevision_reel_Alimentation.png generated")