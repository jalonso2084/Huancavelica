from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

# Define potato variety resistance levels
variety_resistance = {
    "INIA-303 Canchan": 0,   # Highly susceptible
    "INIA-302 Amarilis": 1,  # Moderately resistant
    "Yungay": 0,             # Susceptible (Control)
    "INIA-321 Kawsay": 2,    # Highly resistant
    "CIP308488.92": 2,       
    "CIP308495.227": 2,      
    "CIP308478.59": 2,       
    "CIP308486.355": 2,      
    "CIP308487.157": 2,      
    "CIP308433.101": 2,      
    "CIP308436.84": 2,       
    "CIP308502.95": 2       
}

class PredictionInput(BaseModel):
    humidity: float
    weather: str
    soil: str
    variety: str

def adjust_prediction(base_risk, variety):
    """ Adjusts the blight risk based on variety resistance. """
    resistance_level = variety_resistance.get(variety, 1)  # Default to moderate
    adjusted_risk = base_risk * (1 - (resistance_level * 0.2))  # Reduce risk by 20% per resistance level
    return max(0, min(adjusted_risk, 1))  # Keep within [0,1] range

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.post("/predict")
async def predict_risk(input_data: PredictionInput):
    """ Predicts late blight risk based on input conditions. """
    base_risk = 0.8 if input_data.humidity > 70 else 0.5  # Simple rule-based model
    adjusted_risk = adjust_prediction(base_risk, input_data.variety)

    return {"variety": input_data.variety, "predicted_risk": round(adjusted_risk * 100, 2)}
