import logging
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# ✅ Initialize logging for better debugging
logging.basicConfig(level=logging.INFO)

# ✅ Load model and metadata with error handling
try:
    model = joblib.load('random_forest_model.pkl')
    metadata = joblib.load('metadata.pkl')
    logging.info(f"✅ Model version 1.0.0 loaded successfully.")
    logging.info(f"✅ Metadata loaded: {metadata}")  # Confirm metadata is loaded
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
        # ✅ Read input data from request
        data = request.get_json()
        if data is None:
            logging.error("❌ Error: request.get_json() returned None")
            return jsonify({'error': 'Invalid JSON data in request'}), 400

        logging.info(f"✅ Received JSON data: {data}")

        # ✅ Confirm metadata is available
        if metadata is None:
            logging.error("❌ Metadata is not available.")
            return jsonify({'error': 'Metadata is not available'}), 500
        
        # ✅ Convert input to DataFrame using metadata feature names
        try:
            features = pd.DataFrame([[
                data['variety'], data['humidity'], data['weather_condition'],
                data['soil_type'], data['plant_health_index'], data['disease_pressure_index'],
                data['growth_stage'], data['canopy_coverage'], data['rainfall'],
                data['temperature_variability'], data['soil_moisture']
            ]], columns=metadata['features'])
        except KeyError as e:
            logging.error(f"❌ Missing key in request data: {e}")
            return jsonify({'error': f"Missing key in request data: {e}"}), 400

        # ✅ Generate prediction
        prediction = model.predict(features)[0]
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"

        logging.info(f"✅ Generated prediction: {prediction_label}")

        return jsonify({'prediction': prediction_label})

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

# ✅ Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    status = model is not None and metadata is not None
    return jsonify({"status": "OK" if status else "Error", "model_loaded": status})

# ✅ Expose Flask app to Waitress
if __name__ == "__main__":
    from waitress import serve
    import os
    
    # ✅ Bind to dynamic port for Render compatibility
    port = int(os.environ.get("PORT", 10000))
    logging.info(f"✅ Starting server on port {port}...")
    
    # ✅ Start the app using Waitress
    serve(app, host="0.0.0.0", port=port)

