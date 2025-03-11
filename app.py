from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Configure Logging
logging.basicConfig(level=logging.INFO)

# ✅ Load the model
MODEL_PATH = "random_forest_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
    logging.info(f"✅ Model loaded: {type(model)}")
    logging.info(f"Number of estimators: {model.n_estimators}")
    logging.info(f"Max depth: {model.max_depth}")
except Exception as e:
    logging.error(f"❌ Error loading model: {e}")
    model = None

# ✅ Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model is not loaded."}), 500

    data = request.get_json()
    logging.info(f"✅ Received data: {data}")

    try:
        input_data = [
            data.get("variety", 0),
            data.get("humidity", 0.0),
            data.get("weather_condition", 0),
            data.get("soil_type", 0),
            data.get("plant_health_index", 0),
            data.get("disease_pressure_index", 0),
            data.get("growth_stage", 0),
            data.get("canopy_coverage", 0),
            data.get("rainfall", 0),
            data.get("temperature_variability", 0),
            data.get("soil_moisture", 0)
        ]

        input_array = np.array([input_data])
        prediction = model.predict(input_array)[0]

        response = {
            "model_version": "1.0.0",
            "prediction": float(prediction)
        }

        return jsonify(response)

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ Health Check Route
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "API is running! Use /predict to make predictions."})

    if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

