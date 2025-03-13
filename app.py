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
    encoder = metadata['encoder']  # ✅ Load encoder!
    logging.info(f"✅ Model and metadata loaded successfully")
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

        # ✅ Create DataFrame with input
        input_df = pd.DataFrame([[
            data['variety'], data['humidity'], data['weather_condition'],
            data['soil_type'], data['plant_health_index'], data['disease_pressure_index'],
            data['growth_stage'], data['canopy_coverage'], data['rainfall'],
            data['temperature_variability'], data['soil_moisture']
        ]], columns=['variety', 'humidity', 'weather_condition', 'soil_type', 
                     'plant_health_index', 'disease_pressure_index', 'growth_stage',
                     'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture'])

        # ✅ Apply OneHotEncoder to match training format
        encoded = encoder.transform(input_df[['variety', 'weather_condition', 'soil_type', 'growth_stage']])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['variety', 'weather_condition', 'soil_type', 'growth_stage']))
        numeric_df = input_df.drop(columns=['variety', 'weather_condition', 'soil_type', 'growth_stage']).reset_index(drop=True)

        # ✅ Combine encoded + numeric data
        final_input = pd.concat([encoded_df, numeric_df], axis=1)

        # ✅ Match training features
        final_input = final_input.reindex(columns=metadata['features'], fill_value=0)

        prediction = model.predict(final_input)[0]
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
