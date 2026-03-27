from fastapi import FastAPI
from app.model.predict import predict
from app.db.database import engine
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API OK"}

from app.api.schema import EmployeeInput

@app.post("/predict")
def predict_endpoint(data: EmployeeInput):
    return predict(data.model_dump())

@app.get("/predictions")
def get_predictions():
    df = pd.read_sql("SELECT * FROM predictions ORDER BY created_at DESC", engine)
    return df.to_dict(orient="records")