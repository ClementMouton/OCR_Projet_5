import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = Path("artifacts/attrition_pipeline.joblib")

model = joblib.load(MODEL_PATH)