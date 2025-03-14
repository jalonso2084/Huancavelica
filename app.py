from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

# ✅ Set up logging
logging.basicConfig(level=logging.INFO)

# ✅ Load model and metadata
try:
    model = joblib.load('random_forest_model.pkl')
    metadata = joblib.load('metadata.pkl')
    logging.info(f"✅ Model and metadata loaded successfully")
    logging.info(f"✅ Expected features: {metadata['features']}")
except Exception as e:
    logging.error(f"❌ Error loading model or metadata: {e}")
    model, metadata = None, None

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data is None:
            logging.error("❌ Error: request.get_json() returned None")
            return jsonify({'error': 'Invalid JSON data in request'}), 400

        logging.info(f"✅ Received data: {data}")

        # ✅ Convert to DataFrame
        input_data = pd.DataFrame([[
            data.get('variety', None), 
            data.get('humidity', None),
            data.get('weather_condition', None),
            data.get('soil_type', None),
            data.get('plant_health_index', None),
            data.get('disease_pressure_index', None),
            data.get('growth_stage', None),
            data.get('canopy_coverage', None),
            data.get('rainfall', None),
            data.get('temperature_variability', None),
            data.get('soil_moisture', None)
        ]], columns=[
            'variety', 'humidity', 'weather_condition', 'soil_type', 
            'plant_health_index', 'disease_pressure_index', 'growth_stage',
            'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture'
        ])

        # ✅ Apply One-Hot Encoding to match model input
        input_encoded = pd.get_dummies(input_data)
        logging.info(f"✅ Encoded input columns: {list(input_encoded.columns)}")

        # ✅ Add missing columns and fill with zeros
        for col in metadata['features']:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[metadata['features']]

        logging.info(f"✅ Final input data for model: \n{input_encoded}")

        # ✅ Generate prediction
        prediction = model.predict(input_encoded)[0]
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"

        logging.info(f"✅ Prediction result: {prediction_label}")
        return jsonify({'prediction': prediction_label})

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

# ✅ Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "model_loaded": model is not None})

# ✅ Start Flask app using Waitress
if __name__ == "__main__":
    from waitress import serve
    import os
    
    port = int(os.environ.get("PORT", 10000))
    logging.info(f"✅ Starting server on port {port}...")
    serve(app, host="0.0.0.0", port=port)
