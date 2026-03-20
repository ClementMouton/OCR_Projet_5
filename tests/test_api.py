from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API OK"}


def test_predict_success():
    payload = {
        "age": 31,
        "genre": "M",
        "revenu_mensuel": 11557,
        "statut_marital": "Divorcé(e)",
        "departement": "Commercial",
        "poste": "Senior Manager",
        "nombre_experiences_precedentes": 9,
        "nombre_heures_travailless": 80,
        "annee_experience_totale": 10,
        "annees_dans_l_entreprise": 5,
        "annees_dans_le_poste_actuel": 4,
        "satisfaction_employee_environnement": 3,
        "note_evaluation_precedente": 2,
        "niveau_hierarchique_poste": 3,
        "satisfaction_employee_nature_travail": 4,
        "satisfaction_employee_equipe": 3,
        "satisfaction_employee_equilibre_pro_perso": 2,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": "Non",
        "augementation_salaire_precedente": "21 %",
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 3,
        "nombre_employee_sous_responsabilite": 1,
        "distance_domicile_travail": 7,
        "niveau_education": 3,
        "domaine_etude": "Infra & Cloud",
        "ayant_enfants": "Y",
        "frequence_deplacement": "Occasionnel",
        "annees_depuis_la_derniere_promotion": 0,
        "annes_sous_responsable_actuel": 1
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "probability" in data
    assert isinstance(data["prediction"], int)
    assert isinstance(data["probability"], float)


def test_predict_missing_field():
    payload = {
        "age": 31  # volontairement incomplet
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422