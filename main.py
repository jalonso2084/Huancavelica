import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# Get the current directory where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "random_forest_model.pkl")

# Load the trained model
print("✅ Loading Random Forest model...")
try:
    model = joblib.load(MODEL_PATH)
    print("✅ Random Forest model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API is running! Use /predict to make predictions."})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model failed to load."}), 500
    
    try:
        print("Received prediction request.")  # Added log
        data = request.get_json()
        print(f"Received JSON data: {data}")  # Added log

        # Input validation
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON format"}), 400
        
        # Extract inputs from request, with default values to prevent errors
        variety = data.get("variety", 0.0)
        region = data.get("region", 0.0)
        criteria = data.get("criteria", 0.0)
        farming_practices = data.get("farming_practices", 0.0)
        
        soil = data.get("soil", {})
        pH = soil.get("pH", 0.0)
        bulk_density = soil.get("Bulk_Density", 0.0)
        organic_carbon = soil.get("Organic_Carbon", 0.0)
        cec = soil.get("CEC", 0.0)
        clay_content = soil.get("Clay_Content", 0.0)
        sand_content = soil.get("Sand_Content", 0.0)
        silt_content = soil.get("Silt_Content", 0.0)
        
        weather = data.get("weather", {})
        climate_variability = weather.get("climate_variability", 0.0)
        moderate_el_nino = weather.get("moderate_el_nino", 0.0)
        weak_el_nino = weather.get("weak_el_nino", 0.0)
        
        humidity = data.get("humidity", {})
        fungicide_applications = humidity.get("fungicide", 0.0)
        
        # Construct the input feature dictionary
        input_data = {
            "Latitude_left": 0.0,  # Default (can be updated if required)
            "Longitude_left": 0.0,
            "Types of Potatoes Grown": variety,
            "Region/Country": region,
            "Criteria for Selection": criteria,
            "Farming Practices": farming_practices,
            "pH_left": pH,
            "Bulk_Density_left": bulk_density,
            "Organic_Carbon_left": organic_carbon,
            "CEC_left": cec,
            "Clay_Content_left": clay_content,
            "Sand_Content_left": sand_content,
            "Silt_Content_left": silt_content,
            "Climatic_Climate Variability": climate_variability,
            "Climatic_Moderate El Niño, Increased Humidity": moderate_el_nino,
            "Climatic_Weak-Moderate El Niño, Excessive Rainfall": weak_el_nino,
            "Fungicide Applications (Proxy for Severity)": fungicide_applications
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make prediction
        prediction = model.predict(input_df)
        print(f"Prediction result: {prediction}")  # Added log
        
        # Return prediction as JSON
        return jsonify({"prediction": prediction.tolist()})
    
    except KeyError:
        return jsonify({"error": "Missing required field"}), 400
    except Exception as e:
        print(f"Error during prediction: {e}")  # Added log
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Registered Routes:")
    print(app.url_map)  # Print registered routes to verify /predict exists
    port = int(os.environ.get("PORT", 10000))  # Ensure the correct port for Render
    app.run(host='0.0.0.0', port=port, debug=True)
