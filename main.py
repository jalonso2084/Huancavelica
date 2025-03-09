from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
import os

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# ✅ Test mode flag to disable OpenAI during testing
TEST_MODE = os.environ.get("TESTING", "False").lower() == "true"

# ✅ Load the Random Forest model using joblib (more secure than pickle)
try:
    model_version = "1.0.0"
    model = joblib.load("random_forest_model.pkl")
    logging.info(f"✅ Model version {model_version} loaded successfully.")
except Exception as e:
    logging.error(f"❌ Error loading model: {e}")
    model = None

# ✅ Load OpenAI only if NOT in test mode
if not TEST_MODE:
    import openai

# ✅ Root endpoint for health checks
@app.route("/")
def home():
    logging.info("✅ Health check requested.")
    return jsonify({"message": "API is running! Use /predict to make predictions."})

# ✅ Prediction endpoint (fixing feature size mismatch)
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ✅ Get input data
        data = request.get_json()
        logging.info(f"✅ Received data: {data}")

        if not data:
            logging.warning("❌ No data received.")
            return jsonify({"error": "No input data provided"}), 400

        # ✅ Expected 11 input fields (provide default values)
        input_data = [
            data.get("variety", 0),         # Default = 0
            data.get("humidity", 0.0),       # Default = 0.0
            data.get("weather", 0),          # Default = 0
            data.get("soil", 0),             # Default = 0
            data.get("feature_5", 0),        # Default = 0
            data.get("feature_6", 0),        # Default = 0
            data.get("feature_7", 0),        # Default = 0
            data.get("feature_8", 0),        # Default = 0
            data.get("feature_9", 0),        # Default = 0
            data.get("feature_10", 0),       # Default = 0
            data.get("feature_11", 0)        # Default = 0
        ]

        # ✅ Type conversion (int/float)
        try:
            input_data = [
                int(input_data[0]),  # variety
                float(input_data[1]),  # humidity
                int(input_data[2]),  # weather
                int(input_data[3]),  # soil
                int(input_data[4]), int(input_data[5]), int(input_data[6]),
                int(input_data[7]), int(input_data[8]), int(input_data[9]),
                int(input_data[10])
            ]
        except ValueError as e:
            logging.error(f"❌ Type conversion error: {e}")
            return jsonify({"error": f"Invalid input format: {e}"}), 400

        # ✅ Check if model is loaded
        if model is None:
            logging.error("❌ Model not loaded.")
            return jsonify({"error": "Model not loaded"}), 500

        # ✅ Convert input to numpy array
        input_array = np.array([input_data])
        logging.info(f"✅ Prepared input: {input_array}")

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

# ✅ OpenAI example endpoint (optional)
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
