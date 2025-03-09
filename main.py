from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
import os
import traceback

# ✅ Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# ✅ Load the model
MODEL_PATH = "random_forest_model.pkl"
MODEL_VERSION = "1.0.0"

try:
    model = joblib.load(MODEL_PATH)
    logging.info(f"✅ Model version {MODEL_VERSION} loaded successfully.")
except Exception as e:
    logging.error(f"❌ Error loading model: {e}")
    model = None

# ✅ Check model structure
if model:
    logging.info(f"Number of estimators: {model.n_estimators}")
    logging.info(f"Max depth: {model.max_depth}")
    if hasattr(model, "feature_names_in_"):
        logging.info(f"Feature names: {model.feature_names_in_}")
    else:
        logging.warning("❌ Model has no feature names.")

# ✅ Health check endpoint
@app.route("/", methods=["GET"])
def health_check():
    logging.info("✅ Health check requested.")
    return jsonify({"message": "API is running! Use /predict to make predictions."})

# ✅ Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        logging.error("❌ Model is not loaded.")
        return jsonify({"error": "Model is not loaded"}), 500
    
    try:
        # ✅ Read JSON data
        data = request.get_json()
        logging.info(f"✅ Received data: {data}")

        # ✅ Define expected features
        expected_features = [
            "variety", "humidity", "weather_condition", "soil_type", 
            "plant_health_index", "disease_pressure_index", "growth_stage", 
            "canopy_coverage", "rainfall", "temperature_variability", "soil_moisture"
        ]

        # ✅ Validate input format
        if not all(feature in data for feature in expected_features):
            missing_features = [feature for feature in expected_features if feature not in data]
            logging.error(f"❌ Missing features: {missing_features}")
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # ✅ Create input array (ensure correct order)
        input_array = np.array([[
            data["variety"], data["humidity"], data["weather_condition"], data["soil_type"],
            data["plant_health_index"], data["disease_pressure_index"], data["growth_stage"],
            data["canopy_coverage"], data["rainfall"], data["temperature_variability"],
            data["soil_moisture"]
        ]])

        logging.info(f"🔎 Input array before prediction: {input_array}")

        # ✅ Make prediction
        prediction = model.predict(input_array)[0]
        logging.info(f"✅ Prediction result: {prediction}")

        # ✅ Return prediction
        return jsonify({
            "model_version": MODEL_VERSION,
            "prediction": float(prediction)
        })

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ✅ OpenAI Integration (Optional)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

@app.route("/explain", methods=["POST"])
def explain():
    if not OPENAI_API_KEY:
        logging.error("❌ OpenAI API key is missing.")
        return jsonify({"error": "OpenAI API key is missing"}), 500

    try:
        data = request.get_json()
        logging.info(f"✅ OpenAI request data: {data}")

        input_text = data.get("input_text", "")
        if not input_text:
            logging.error("❌ Missing 'input_text' in request.")
            return jsonify({"error": "Missing 'input_text'"}), 400

        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        # ✅ Make OpenAI request
        response = client.Completion.create(
            model="gpt-4-turbo",
            prompt=input_text,
            max_tokens=100
        )

        # ✅ Return explanation
        explanation = response.choices[0].text.strip()
        logging.info(f"✅ Explanation: {explanation}")

        return jsonify({"explanation": explanation})

    except Exception as e:
        logging.error(f"❌ Error during OpenAI request: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ✅ Start the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logging.info(f"✅ Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)
