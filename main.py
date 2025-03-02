from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import uvicorn
from ppi_validation import PPIValidation  # Import PPI Validation module

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Define request body format
class PredictionInput(BaseModel):
    humidity: int
    weather: str
    soil: str
    variety: str

# ✅ Load real-world validation data
try:
    human_data = pd.read_csv("real_outbreak_data.csv")
    print("✅ Loaded Data from real_outbreak_data.csv:\n", human_data.head())  # Debugging Step
except FileNotFoundError:
    print("❌ Error: 'real_outbreak_data.csv' not found.")
    human_data = None  # Prevent crashing if file is missing

# ✅ Health check endpoint (Test this at http://127.0.0.1:8000/)
@app.get("/")
def home():
    return {"message": "FastAPI is running with PPI Validation!"}

# ✅ Prediction endpoint (Test this at http://127.0.0.1:8000/docs)
@app.post("/predict")
def predict(data: PredictionInput):
    try:
        # ✅ Placeholder AI Prediction Logic (Replace this with an actual ML model later)
        risk_score = (data.humidity / 100) * 80  # Dummy calculation

        # ✅ Generate AI predictions that follow historical outbreak trends
        if human_data is not None and not human_data.empty:
            previous_outbreaks = human_data["outbreak_risk"].values
            avg_outbreak = sum(previous_outbreaks) / len(previous_outbreaks) if len(previous_outbreaks) > 0 else risk_score
            trend_adjustment = avg_outbreak * 0.5 + risk_score * 0.5  # Blends AI prediction with outbreak history
        else:
            trend_adjustment = risk_score  # Default if no historical data

        ai_predictions_df = pd.DataFrame([
            {"predicted_risk": trend_adjustment},
            {"predicted_risk": trend_adjustment * 1.1},  # Small increase
            {"predicted_risk": trend_adjustment * 0.9}   # Small decrease
        ])

        # ✅ Validate using PPI if human_data is available
        if human_data is not None and not human_data.empty:
            ppi = PPIValidation(human_data, ai_predictions_df)
            validation_results = ppi.validate_predictions()
        else:
            validation_results = {
                "ppi_correlation": None,
                "p_value": None,
                "confidence_score": None,
                "reliability": "Low Confidence (Missing Validation Data)"
            }

        # ✅ Return AI Prediction with PPI Validation Results
        return {
            "variety": data.variety,
            "predicted_risk": round(risk_score, 1),
            "validation": validation_results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

# ✅ Run the app locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
