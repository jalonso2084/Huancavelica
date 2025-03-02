from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# ✅ Define FastAPI app
app = FastAPI()

# ✅ Define request body format
class PredictionInput(BaseModel):
    humidity: int
    weather: str
    soil: str
    variety: str

# ✅ Health check endpoint
@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

# ✅ Prediction endpoint
@app.post("/predict")
def predict(data: PredictionInput):
    try:
        # Placeholder for actual model logic (replace this)
        risk_score = (data.humidity / 100) * 80  # Dummy formula
        return {
            "variety": data.variety,
            "predicted_risk": round(risk_score, 1)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ✅ Run the app locally (ignored by Render)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

