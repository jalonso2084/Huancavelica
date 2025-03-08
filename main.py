from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Load the Random Forest model using joblib (more secure than pickle)
try:
    model_version = "1.0.0"
    model = joblib.load("random_forest_model.pkl")
    logging.info(f"✅ Model version {model_version} loaded successfully.")
except Exception as e:
    logging.error(f"❌ Error loading model: {e}")
    model = None

# ✅ Root endpoint for health checks
@app.route("/")
def home():
    logging.info("✅ Health check requested.")
    return jsonify({"message": "API is running! Use /predict to make predictions."})

# ✅ Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ✅ Get input data
        data = request.get_json()
        logging.info(f"✅ Received data: {data}")

        if not data:
            logging.warning("❌ No data received.")
            return jsonify({"error": "No input data provided"}), 400

        # ✅ Validate input fields
        required_fields = ["variety", "humidity", "weather", "soil"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            logging.warning(f"❌ {error_message}")
            return jsonify({"error": error_message}), 400
        
        # ✅ Type and range validation
        try:
            variety = int(data["variety"])
            humidity = float(data["humidity"])
            weather = int(data["weather"])
            soil = int(data["soil"])

            # ✅ Range checks
            if not (0 <= humidity <= 100):
                raise ValueError("Humidity must be between 0 and 100.")
            if not (0 <= weather <= 10):  # Assuming 10 is the highest expected weather code
                raise ValueError("Invalid weather code.")
            if not (0 <= soil <= 10):  # Assuming 10 is the highest soil type code
                raise ValueError("Invalid soil type.")
        except ValueError as e:
            logging.error(f"❌ Invalid input: {e}")
            return jsonify({"error": f"Invalid input: {e}"}), 400

        # ✅ Check if model is loaded
        if model is None:
            logging.error("❌ Model not loaded.")
            return jsonify({"error": "Model not loaded"}), 500

        # ✅ Prepare input for model
        input_data = np.array([[variety, humidity, weather, soil]])

        # ✅ Make prediction
        prediction = model.predict(input_data)[0]
        logging.info(f"✅ Prediction: {prediction}")

        # ✅ Return result (convert to int if needed)
        response = {
            "prediction": int(prediction) if prediction.is_integer() else float(prediction),
            "model_version": model_version
        }
        return jsonify(response)

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ Run Flask app locally for testing
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
