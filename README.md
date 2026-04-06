# Employee Attrition Prediction API

## 📌 Description

Ce projet expose un modèle de machine learning permettant de prédire la probabilité de départ d’un employé (attrition) via une API FastAPI.

L’application permet :

* d’envoyer des données employé
* d’obtenir une prédiction
* d’enregistrer les inputs et outputs dans une base PostgreSQL
* d’assurer une traçabilité complète des prédictions

---

## 🧠 Modèle de Machine Learning

* **Modèle** : Logistic Regression
* **Librairies** : scikit-learn

### Pipeline :

* StandardScaler (features numériques)
* OneHotEncoder (features catégorielles)

👉 Le modèle est versionné et stocké sur Hugging Face.

---

## 🏗️ Architecture

```
Client → FastAPI → Modèle ML → PostgreSQL
                     ↓
               Hugging Face (artefacts)
```

---

## 📂 Structure du projet

```
app/
├── main.py
├── model/
│   ├── load_model.py
│   └── predict.py
├── db/
│   ├── database.py
│   └── queries.py

tests/
sql/
docs/
artifacts/
requirements.txt
README.md
```

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone <repo_url>
cd OCR_Projet_5
```

### 2. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

---

## 🗄️ Mise en place PostgreSQL

### 1. Lancer PostgreSQL (pgAdmin ou service local)

### 2. Créer la base

Nom recommandé :

```
attrition_db
```

### 3. Exécuter les scripts SQL

Dans pgAdmin ou via SQL :

```sql
-- create_tables.sql
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    input_data JSONB,
    prediction INTEGER,
    probability FLOAT
);
```

---

## 🚀 Lancer l’API

```bash
python -m uvicorn app.main:app --reload
```

👉 Swagger :

```
http://127.0.0.1:8000/docs
```

---

## 🔗 Endpoints

### GET /

Health check

---

### POST /predict

Prédit le risque de départ d’un employé

#### Exemple de payload

```json
{
  "age": 30,
  "genre": "M",
  "revenu_mensuel": 1700,
  "departement": "Data",
  "poste": "Data Scientist"
}
```

#### Output

```json
{
  "prediction": 0,
  "probability": 0.26
}
```

---

### GET /predictions

Retourne l’historique des prédictions stockées en base

---

## 🧪 Tests

### Lancer les tests

```bash
python -m pytest
```

### Couverture des tests

```bash
python -m pytest --cov=app --cov-report=term
```

---

## 🔁 CI/CD

* GitHub Actions
* Tests automatiques à chaque push
* Validation du code avant merge

---

## 📦 Hugging Face

Le modèle et ses métadonnées sont stockés sur Hugging Face :

* `attrition_pipeline.joblib`
* `model_metadata.json`

---

## 🌐 Démo en ligne

👉 https://huggingface.co/spaces/ClementMouton/attrition-predictor

Cette interface permet de tester le modèle sans installation locale.

---

## 🗄️ Base de données PostgreSQL

Le projet utilise PostgreSQL pour garantir la traçabilité des prédictions.

* inputs utilisateur enregistrés
* outputs du modèle enregistrés
* timestamp automatique

### Fichiers associés

* `sql/create_tables.sql`
* `sql/sample_queries.sql`
* `docs/database_schema.md`

---

## 🧠 Documentation Base de Données

### 🎯 Objectif

Assurer la traçabilité complète des prédictions.

### 🧱 Table : predictions

| Colonne     | Type      | Description          |
| ----------- | --------- | -------------------- |
| id          | SERIAL    | Identifiant unique   |
| created_at  | TIMESTAMP | Date de création     |
| input_data  | JSONB     | Données du modèle    |
| prediction  | INTEGER   | Résultat             |
| probability | FLOAT     | Probabilité associée |

---

## 🔄 Flux de données

1. L’utilisateur envoie un payload à `/predict`
2. L’API appelle le modèle
3. Le résultat est généré
4. Input + output sont stockés en base

---

## 🧠 Choix techniques

* JSONB → flexibilité des inputs
* PostgreSQL → robustesse
* FastAPI → performance
* Hugging Face → versionning du modèle

---

## ⚠️ Limitations

* dépendance à la qualité des données
* modèle basé sur données historiques
* biais possibles

---

## 🧪 Étapes pour faire tourner le projet (end-to-end)

### 1. Lancer PostgreSQL

* via pgAdmin ou service local

---

### 2. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

---

### 3. Lancer l’API

```bash
python -m uvicorn app.main:app --reload
```

---

### 4. Tester l’API

👉 ouvrir :

```
http://127.0.0.1:8000/docs
```

---

### 5. Lancer les tests

```bash
python -m pytest
```

---

### 6. Vérifier la couverture

```bash
python -m pytest --cov=app --cov-report=term
```

---

### 7. Vérifier la base de données

Dans pgAdmin :

```sql
SELECT * FROM predictions;
```

---

### 8. Tester la démo en ligne

👉 Hugging Face Space :
https://huggingface.co/spaces/ClementMouton/attrition-predictor

---

## 👨‍💻 Auteur

Clément Mouton
