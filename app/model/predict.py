import json

import pandas as pd
from huggingface_hub import hf_hub_download

from app.db.queries import insert_prediction
from app.model.load_model import model


HF_REPO_ID = "ClementMouton/employee-attrition-model"

METADATA_PATH = hf_hub_download(
    repo_id=HF_REPO_ID,
    filename="model_metadata.json"
)

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    model_metadata = json.load(f)

THRESHOLD = model_metadata["threshold"]


def predict(data: dict) -> dict:
    df = pd.DataFrame([data])

    proba = model.predict_proba(df)[0, 1]
    pred = int(proba >= THRESHOLD)

    try:
        insert_prediction(
            input_data=data,
            prediction=pred,
            probability=float(proba)
        )
    except Exception as e:
        print(f"Erreur lors de l'enregistrement en base : {e}")

    return {
        "prediction": pred,
        "probability": float(proba)
    }