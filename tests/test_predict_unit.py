import pytest

from app.model.predict import predict


# 🔹 Mock du modèle
class FakeModel:
    def predict_proba(self, X):
        return [[0.2, 0.8]]  # proba classe 1 = 0.8


# 🔹 Mock DB
def fake_insert_prediction(*args, **kwargs):
    return None


@pytest.fixture
def sample_data():
    return {
        "age": 30,
        "genre": "M",
        "revenu_mensuel": 2000,
        "statut_marital": "Célibataire",
        "departement": "IT",
        "poste": "Dev",
        "nombre_experiences_precedentes": 2,
        "nombre_heures_travailless": 40,
        "annee_experience_totale": 5,
        "annees_dans_l_entreprise": 2,
        "annees_dans_le_poste_actuel": 1,
        "satisfaction_employee_environnement": 3,
        "note_evaluation_precedente": 3,
        "niveau_hierarchique_poste": 2,
        "satisfaction_employee_nature_travail": 3,
        "satisfaction_employee_equipe": 3,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 3,
        "heure_supplementaires": "Non",
        "augementation_salaire_precedente": "10 %",
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 2,
        "nombre_employee_sous_responsabilite": 0,
        "distance_domicile_travail": 10,
        "niveau_education": 3,
        "domaine_etude": "IT",
        "ayant_enfants": "N",
        "frequence_deplacement": "Rare",
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 1
    }


def test_predict_returns_valid_output(monkeypatch, sample_data):
    # Mock du modèle
    monkeypatch.setattr("app.model.predict.model", FakeModel())

    # Mock DB
    monkeypatch.setattr(
        "app.model.predict.insert_prediction",
        fake_insert_prediction
    )

    result = predict(sample_data)

    assert "prediction" in result
    assert "probability" in result
    assert isinstance(result["prediction"], int)
    assert isinstance(result["probability"], float)


def test_predict_threshold_logic(monkeypatch, sample_data):
    class LowProbaModel:
        def predict_proba(self, X):
            return [[0.9, 0.1]]  # faible proba

    monkeypatch.setattr("app.model.predict.model", LowProbaModel())
    monkeypatch.setattr(
        "app.model.predict.insert_prediction",
        fake_insert_prediction
    )

    result = predict(sample_data)

    assert result["prediction"] in [0, 1]
    assert result["prediction"] == 0