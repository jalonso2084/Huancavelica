from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
import os
from pydantic import BaseModel, ValidationError

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Test mode flag to disable OpenAI during testing
TEST_MODE = os.getenv("TESTING", "false").lower() in ["true", "1"]

# ✅ Load the Random Forest model using joblib (more secure than pickle)
MODEL_PATH = "random_forest_model.pkl"
try:
    model_version = "1.0.0"
    model = joblib.load(MODEL_PATH)
    logging.info(f"✅ Model version {model_version} loaded successfully.")
except Exception as e:
    logging.error(f"❌ Error loading model from {MODEL_PATH}: {e}")
    model = None

# ✅ Load OpenAI only if NOT in test mode
if not TEST_MODE:
    try:
        import openai
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OpenAI API key is missing. Set OPENAI_API_KEY in environment.")
    except Exception as e:
        logging.error(f"❌ OpenAI import error: {e}")
        openai = None

# ✅ Define structured input validation using Pydantic
class PredictionInput(BaseModel):
    variety: int = 0
    humidity: float = 0.0
    weather_condition: int = 0
    soil_type: int = 0
    plant_health_index: int = 0
    disease_pressure_index: int = 0
    growth_stage: int = 0
    canopy_coverage: int = 0
    rainfall: int = 0
    temperature_variability: int = 0
    soil_moisture: int = 0

# ✅ Root endpoint for health checks
@app.route("/")
def home():
    logging.info("✅ Health check requested.")
    return jsonify({"message": "API is running! Use /predict to make predictions."})

# ✅ Prediction endpoint with improved validation and input names
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        logging.info(f"✅ Received data: {data}")

        if not data:
            logging.warning("❌ No data received.")
            return jsonify({"error": "No input data provided"}), 400

        # ✅ Validate input using Pydantic
        try:
            input_data = PredictionInput(**data)
        except ValidationError as e:
            logging.error(f"❌ Input validation error: {e}")
            return jsonify({"error": str(e)}), 400

        # ✅ Convert input to numpy array
        input_array = np.array([list(input_data.dict().values())])
        logging.info(f"✅ Prepared input: {input_array}")

        # ✅ Check if model is loaded
        if model is None:
            logging.error("❌ Model not loaded.")
            return jsonify({"error": "Model not loaded"}), 500

        # ✅ Make prediction
        prediction = model.predict(input_array)[0]
        logging.info(f"✅ Prediction: {prediction}")

        # ✅ Return prediction as JSON
        response = {
            "prediction": float(prediction),  # Ensure float format
            "model_version": model_version
        }

        return jsonify(response), 200

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ OpenAI explanation endpoint with better key handling
@app.route("/explain", methods=["POST"])
def explain():
    if TEST_MODE:
        logging.warning("✅ Skipping OpenAI during testing.")
        return jsonify({"message": "Test mode is enabled — OpenAI disabled"}), 200

    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Missing 'query' field"}), 400

        query = data["query"]

        if openai is None:
            logging.error("❌ OpenAI is not available.")
            return jsonify({"error": "OpenAI is not available"}), 500

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}]
        )

        explanation = response["choices"][0]["message"]["content"]
        return jsonify({"explanation": explanation})

    except Exception as e:
        logging.error(f"❌ Error during OpenAI request: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ Run Flask app on the Render-assigned port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
