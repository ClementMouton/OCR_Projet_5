Employee Attrition Prediction API
📌 Description

Ce projet expose un modèle de machine learning permettant de prédire la probabilité de départ d’un employé (attrition) via une API FastAPI.

L’application permet :

d’envoyer des données employé

d’obtenir une prédiction

d’enregistrer les inputs et outputs dans une base PostgreSQL

d’assurer une traçabilité complète des prédictions

🧠 Modèle de Machine Learning

Modèle : Logistic Regression

Librairies : scikit-learn

Pipeline :

StandardScaler (features numériques)

OneHotEncoder (features catégorielles)

Le modèle est versionné et stocké sur Hugging Face.

🏗️ Architecture
Client → FastAPI → Modèle ML → PostgreSQL
                     ↓
               Hugging Face (artefacts)
📂 Structure du projet
app/
├── main.py
├── model/
│   ├── load_model.py
│   └── predict.py
├── db/
│   ├── database.py
│   └── queries.py

artifacts/
tests/
requirements.txt
README.md
⚙️ Installation
1. Cloner le projet
git clone <repo_url>
cd OCR_Projet_5
2. Installer les dépendances
python -m pip install -r requirements.txt
🚀 Lancer l’API
python -m uvicorn app.main:app --reload

Accès Swagger :

http://127.0.0.1:8000/docs
🔗 Endpoints
GET /

Health check

POST /predict

Prédit le risque de départ d’un employé

Exemple de payload
{
  "age": 30,
  "genre": "M",
  "revenu_mensuel": 1700,
  "departement": "Data",
  "poste": "Data Scientist"
}
Output
{
  "prediction": 0,
  "probability": 0.26
}
GET /predictions

Retourne l’historique des prédictions stockées en base

🗄️ Base de données PostgreSQL

Les données sont stockées dans PostgreSQL afin de garantir la traçabilité.

inputs utilisateur enregistrés

outputs du modèle enregistrés

timestamp automatique

🔁 CI/CD

GitHub Actions

Tests automatiques avec Pytest

Validation à chaque push

🧪 Tests
python -m pytest
📦 Hugging Face

Le modèle et ses métadonnées sont stockés sur Hugging Face :

attrition_pipeline.joblib

model_metadata.json

## Tests

Les tests sont exécutés avec pytest.

Commande :

pytest --cov=app --cov-report=term

## Base de données PostgreSQL

Le projet utilise PostgreSQL pour garantir la traçabilité des prédictions.

Les scripts SQL sont disponibles dans le dossier `sql/` :
- `create_tables.sql` : création des tables
- `sample_queries.sql` : exemples d'interrogation

La documentation du schéma est disponible dans :
- `docs/database_schema.md`

## Démo en ligne

Une interface utilisateur est disponible via Hugging Face Spaces :

👉 https://huggingface.co/spaces/ClementMouton/attrition-predictor

Cette interface permet de tester le modèle sans installation locale.

⚠️ Limitations

dépendance à la qualité des données

modèle basé sur données historiques

biais possibles

👨‍💻 Auteur

Clément Mouton


Documentation Base de Données
🎯 Objectif

La base PostgreSQL permet de garantir la traçabilité complète des prédictions.

🧱 Tables
Table : predictions
Colonne	Type	Description
id	SERIAL	Identifiant unique
created_at	TIMESTAMP	Date de création
input_data	JSONB	Données envoyées au modèle
prediction	INTEGER	Résultat du modèle
probability	FLOAT	Probabilité associée
🔄 Flux de données

L’utilisateur envoie un payload à /predict

L’API appelle le modèle

Le résultat est généré

Input + output sont stockés en base

📌 Exemple SQL
SELECT * FROM predictions;
🧠 Choix techniques

JSONB pour flexibilité des inputs

stockage centralisé pour audit

PostgreSQL pour robustesse

⚠️ Points de vigilance

cohérence des données

sécurité des accès

gestion des volumes futurs
