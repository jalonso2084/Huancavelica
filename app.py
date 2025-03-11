from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import logging

# ✅ Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Load the model and metadata correctly
try:
    model, metadata = joblib.load('random_forest_model.pkl')

    # ✅ Type checking — ensure model is a RandomForestClassifier
    if not isinstance(model, RandomForestClassifier):
        raise TypeError(f"❌ Loaded object is type '{type(model)}' instead of RandomForestClassifier")

    logger.info(f"✅ Model version 1.0.0 loaded successfully.")

except Exception as e:
    logger.error(f"❌ Error loading model: {e}")
    model = None

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Required keys for input validation
REQUIRED_KEYS = [
    'variety', 'humidity', 'weather_condition', 'soil_type', 
    'plant_health_index', 'disease_pressure_index', 'growth_stage',
    'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # ✅ Validate input data
        if not all(key in data for key in REQUIRED_KEYS):
            logger.warning("❌ Missing required input data")
            return jsonify({'error': 'Missing required input data'}), 400
        
        # ✅ Validate feature order consistency with metadata
        if list(metadata['features']) != REQUIRED_KEYS:
            logger.error("❌ Feature order mismatch in metadata")
            return jsonify({'error': 'Feature order mismatch in metadata'}), 500

        # ✅ Convert input to DataFrame using metadata feature names
        features = pd.DataFrame([[
            data['variety'], data['humidity'], data['weather_condition'],
            data['soil_type'], data['plant_health_index'], data['disease_pressure_index'],
            data['growth_stage'], data['canopy_coverage'], data['rainfall'],
            data['temperature_variability'], data['soil_moisture']
        ]], columns=metadata['features'])

        # ✅ Generate prediction
        prediction = model.predict(features)[0]
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"
        logger.info(f"✅ Prediction: {prediction_label}")

        return jsonify({'prediction': prediction_label})
    
    except Exception as e:
        logger.error(f"❌ Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

# ✅ Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    status = {"status": "OK", "model_loaded": model is not None}
    logger.info(f"✅ Health Check: {status}")
    return jsonify(status)

# ✅ Expose Flask app to Waitress
if __name__ == "__main__":
    from waitress import serve
    import os
    
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"✅ Starting server on port {port}...")
    serve(app, host="0.0.0.0", port=port)

# ✅ Ensure app is exposed for Waitress
application = app
