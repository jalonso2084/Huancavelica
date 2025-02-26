from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    weather: str
    humidity: int
    soil_type: str
    potato_variety: str

@app.post("/predict")
def predict(data: InputData):
    # Dummy prediction logic (replace with your ML model)
    risk_level = (data.humidity / 100)  # Example calculation
    return {"risk_level": risk_level}
