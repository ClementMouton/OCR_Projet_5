import pandas as pd
from app.model.load_model import model
import json

with open("artifacts/model_metadata.json", "r") as f:
    model_metadata = json.load(f)

THRESHOLD = model_metadata["threshold"]

def predict(data: dict):
    df=pd.DataFrame([data])

    proba = model.predict_proba(df)[0, 1]

    pred = int(proba >= THRESHOLD)

    return {"prediction": pred, "probability": float(proba)}