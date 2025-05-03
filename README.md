# Budget Analyst : Analyse des Écarts Budgétaires

## Contexte

Ce projet a été réalisé dans le cadre d'un portfolio d'étudiante en Master 1 Data Analyst. Il vise à illustrer de manière concrète les compétences essentielles d'une analyste de données, notamment :

* La création et la manipulation de jeux de données
* L'analyse d'écarts budgétaires
* L'utilisation de Python, SQL et Power BI
* La structuration d'un projet réaliste, clair et facilement compréhensible

## Objectif du projet

Créer un outil automatisé permettant d’analyser les dépenses mensuelles, d’identifier les postes de dépense majeurs, et de proposer des pistes concrètes pour réaliser des économies.

## Structure du projet

Le projet suit une démarche progressive et pédagogique :

1. Génération d’un jeu de données fictif avec catégories de dépenses
2. Nettoyage et transformation des données avec Python (Pandas)
3. Stockage dans une base SQL et requêtes analytiques
4. Visualisation interactive via Power BI (bientôt)

## Prérequis

Avant de commencer, assurez-vous d'avoir :

* Python 3.8 ou plus
* pip installé
* sqlite3 installé (généralement présent par défaut)

## Installation et exécution rapide

Cloner le projet, installer les dépendances et tout exécuter d'un coup :

```bash
git clone https://github.com/ondouavivi/budget_tracker.git
cd budget_tracker
pip install -r requirements.txt
python run_all.py
```

Ce script va :

1. Générer deux jeux de données (budget et réel)
2. Calculer les écarts et générer des graphiques
3. Stocker les données dans une base SQLite locale

Vous obtiendrez :

* `budget_previsionnel.csv`
* `depenses_reelles.csv`
* `merged_budget.csv`
* `budget.db avec toutes les données insérées`
* Deux graphiques au format `.png`

## Requêtes SQL

Pour analyser les écarts avec SQL :

```bash
sqlite3 budget.db < sql_queries.sql
```
## Graphique image png

Cela affichera :

* Les écarts totaux par catégorie
* Le mois avec l'écart le plus important
* Les catégories les plus régulièrement dépassées