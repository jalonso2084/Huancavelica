from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import uvicorn

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Define request model
class PredictionInput(BaseModel):
    humidity: int
    weather: str
    soil: str
    variety: str

# ✅ Function to calculate PPI validation metrics
def compute_ppi_validation(predicted_risk):
    """
    Simulates PPI framework validation using statistical parameters.
    """
    # ✅ Ensure correlation is always between 0 and 1
    ppi_correlation = round(random.uniform(0.3, 0.9), 2)

    # ✅ Simulated p-value
    p_value = round(random.uniform(0.05, 0.9), 4)

    # ✅ Ensure confidence score is within a reasonable range
    confidence_score = round(random.uniform(0.5, 0.95), 2)

    # ✅ Determine reliability level
    if confidence_score >= 0.8:
        reliability = "High Confidence"
    elif confidence_score >= 0.6:
        reliability = "Medium Confidence"
    else:
        reliability = "Low Confidence"

    return {
        "ppi_correlation": ppi_correlation,
        "p_value": p_value,
        "confidence_score": confidence_score,
        "reliability": reliability
    }

# ✅ Root endpoint (Health Check)
@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

# ✅ Prediction endpoint
@app.post("/predict")
def predict(data: PredictionInput):
    try:
        # ✅ Replace with your actual ML model
        predicted_risk = int((data.humidity / 100) * 80)  # Example risk calculation

        # ✅ Compute PPI validation
        validation = compute_ppi_validation(predicted_risk)

        return {
            "variety": data.variety,
            "predicted_risk": predicted_risk,
            "validation": validation
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ✅ Run the API locally (Ignored by Render)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
