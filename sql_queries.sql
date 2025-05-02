-- 1) Total gap per category
SELECT categorie,
       SUM(ecart) AS total_ecart
FROM budget_ecarts
GROUP BY categorie
ORDER BY total_ecart DESC;

-- 2) Month with the largest absolute total gap
SELECT date,
       ABS(SUM(ecart)) AS ecart_mensuel
FROM budget_ecarts
GROUP BY date
ORDER BY ecart_mensuel DESC
LIMIT 1;

-- 3) Overall average gap
SELECT AVG(ecart) AS ecart_moyen
FROM budget_ecarts;

-- 4) Categories with positive average gap (overspending)
SELECT categorie,
       AVG(ecart) AS ecart_moyen
FROM budget_ecarts
GROUP BY categorie
HAVING ecart_moyen > 0;