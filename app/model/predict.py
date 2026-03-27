import json
from pathlib import Path

import pandas as pd

from app.db.queries import insert_prediction
from app.model.load_model import model

BASE_DIR = Path(__file__).resolve().parents[2]
METADATA_PATH = BASE_DIR / "artifacts" / "model_metadata.json"

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    model_metadata = json.load(f)

THRESHOLD = model_metadata["threshold"]


def predict(data: dict) -> dict:
    df = pd.DataFrame([data])

    proba = model.predict_proba(df)[0, 1]
    pred = int(proba >= THRESHOLD)

    insert_prediction(
        input_data=data,
        prediction=pred,
        probability=float(proba)
    )

    return {
        "prediction": pred,
        "probability": float(proba)
    }