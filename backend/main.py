from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    model = joblib.load("model.joblib")
except:
    model = None

class PatientData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.get("/")
def home():
    return {"message": "Cardio-Guard API is running"}

@app.post("/predict")
def predict_risk(data: PatientData):
    if not model:
        return {"error": "Model not loaded"}
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)
    prob = model.predict_proba(df)
    return {"risk": int(pred[0]), "confidence": float(max(prob[0]) * 100)}
