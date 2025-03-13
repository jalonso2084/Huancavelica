from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging
import os

# ✅ Set up logging to capture detailed info
logging.basicConfig(level=logging.INFO)

# ✅ Load model and metadata correctly
try:
    model = joblib.load('random_forest_model.pkl')
    metadata = joblib.load('metadata.pkl')
    logging.info("✅ Model and metadata loaded successfully.")
    logging.info(f"✅ Metadata: {metadata}")
except Exception as e:
    logging.error(f"❌ Error loading model or metadata: {e}")
    model = None
    metadata = None

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Prediction Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Log the incoming request data
        data = request.get_json()
        logging.info(f"📥 Incoming data: {data}")

        # ✅ Validate JSON data
        if data is None:
            logging.error("❌ Error: request.get_json() returned None")
            return jsonify({'error': 'Invalid JSON data in request'}), 400
        
        # ✅ Ensure all expected fields are present
        missing_fields = [field for field in metadata['features'] if field not in data]
        if missing_fields:
            logging.error(f"❌ Error: Missing fields: {missing_fields}")
            return jsonify({'error': f"Missing fields: {missing_fields}"}), 400

        # ✅ Convert input to DataFrame using metadata feature names
        features = pd.DataFrame([[data[field] for field in metadata['features']]],
                                columns=metadata['features'])

        logging.info(f"✅ DataFrame created: {features}")

        # ✅ Generate prediction
        prediction = model.predict(features)[0]
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"
        logging.info(f"✅ Prediction: {prediction_label}")

        return jsonify({'prediction': prediction_label})

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

# ✅ Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "model_loaded": model is not None})

# ✅ Start the Flask app using Waitress
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    logging.info(f"✅ Starting server on port {port}...")
    from waitress import serve
    serve(app, host="0.0.0.0", port=port)
