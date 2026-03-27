# Schéma de base de données

## Objectif

La base PostgreSQL permet d'assurer la traçabilité complète des échanges entre l'API et le modèle de machine learning.

## Tables

### employees

Contient les données d'entrée structurées pouvant être utilisées pour stocker un dataset de référence.

Champs principaux :
- id
- age
- genre
- revenu_mensuel
- departement
- poste
- variables de satisfaction
- variables d'ancienneté
- variables contextuelles

### predictions

Contient l'historique des prédictions effectuées par l'API.

Champs :
- id : identifiant unique
- created_at : date de création
- input_data : payload JSON envoyé à l'API
- prediction : classe prédite
- probability : probabilité associée

## Flux

1. L'utilisateur envoie un payload à `/predict`
2. L'API applique le modèle
3. La prédiction est générée
4. L'input et l'output sont enregistrés dans `predictions`

## Représentation logique

employees
- id
- données RH structurées

predictions
- id
- created_at
- input_data
- prediction
- probability