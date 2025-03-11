from flask import Flask, request, jsonify
import joblib
import pandas as pd

# ✅ Load the model and metadata correctly
try:
    model, metadata = joblib.load('random_forest_model.pkl')
    print(f"✅ Model version 1.0.0 loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Prediction Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Read input data from request
        data = request.get_json()

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
        
        return jsonify({'prediction': prediction_label})
    
    except Exception as e:
        # ✅ Return clear error message if prediction fails
        return jsonify({'error': str(e)}), 400

# ✅ Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "model_loaded": model is not None})

# ✅ Expose Flask app to Waitress
if __name__ == "__main__":
    from waitress import serve
    import os
    
    # ✅ Bind to dynamic port for Render compatibility
    port = int(os.environ.get("PORT", 5000))
    print(f"✅ Starting server on port {port}...")
    
    # ✅ Start the app using Waitress
    serve(app, host="0.0.0.0", port=port)

# ✅ Make sure 'app' is exposed for Waitress
application = app
