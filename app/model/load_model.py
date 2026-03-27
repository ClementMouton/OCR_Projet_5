import os
from pathlib import Path

import joblib
from huggingface_hub import hf_hub_download

HF_REPO_ID = "ClementMouton/employee-attrition-model"

MODEL_PATH = hf_hub_download(
    repo_id=HF_REPO_ID,
    filename="attrition_pipeline.joblib",
    repo_type="model"
)

model = joblib.load(MODEL_PATH)