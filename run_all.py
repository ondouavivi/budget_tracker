import os

print("=== Budget Analyst: Analyse des Écarts Budgétaires ===\n")

# Step 1: Generate data
print("[1/3] Génération des données...")
os.system("python data_creation.py")

# Step 2: Analyse et visualisation
print("\n[2/3] Analyse des écarts...")
os.system("python analysis.py")

# Step 3: Insertion SQL
print("\n[3/3] Stockage SQL...")
os.system("python sql_storage.py")

print("\nTout est prêt !")
print("→ CSV générés")
print("→ Graphiques enregistrés (.png)")
print("→ Données insérées dans budget.db")
print("→ Lancer : sqlite3 budget.db < sql_queries.sql pour interroger les écarts.")