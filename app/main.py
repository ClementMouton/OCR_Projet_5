from fastapi import FastAPI
from app.model.predict import predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API OK"}

from app.api.schema import EmployeeInput

@app.post("/predict")
def predict_endpoint(data: EmployeeInput):
    return predict(data.model_dump())