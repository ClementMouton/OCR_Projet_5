-- Vérifier les prédictions enregistrées
SELECT * 
FROM predictions
ORDER BY created_at DESC;

-- Compter le nombre total de prédictions
SELECT COUNT(*) AS total_predictions
FROM predictions;

-- Voir les probabilités moyennes
SELECT AVG(probability) AS avg_probability
FROM predictions;

-- Voir les prédictions positives
SELECT *
FROM predictions
WHERE prediction = 1
ORDER BY created_at DESC;