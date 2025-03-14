import pandas as pd
import numpy as np
import joblib
import os
import logging

# ✅ Set up logging
logging.basicConfig(level=logging.INFO)

# ✅ Define the correct expected features (match the training data)
EXPECTED_FEATURES = [
    'humidity', 'temperature_variability', 'rainfall', 'plant_health_index',
    'disease_pressure_index', 'canopy_coverage', 'soil_moisture',
    'variety_INIA-302 Amarilis', 'variety_INIA-303 Canchan', 'variety_INIA-321 Kawsay',
    'variety_Poccoya', 'variety_Yungay', 'weather_condition_Rain', 'weather_condition_Sunny',
    'soil_type_Loamy', 'soil_type_Sandy', 'soil_type_Silty',
    'growth_stage_Maturity', 'growth_stage_Vegetative'
]

# ✅ Load Model
def load_model():
    logging.info("🔍 Entering load_model()...")
    
    model_path = os.path.join(
        os.getcwd(),
        'random_forest_model.pkl'
    )
    
    try:
        logging.info(f"🔍 Attempting to load model from: {model_path}")
        model = joblib.load(model_path)
        logging.info("✅ Model loaded successfully!")
        return model
    except Exception as e:
        logging.error(f"❌ Error loading model: {e}")
        exit(1)

# ✅ Prediction Function
def predict(input_file, output_file):
    logging.info(f"🔍 Loading input file: {input_file}")

    try:
        # ✅ Load the data
        data = pd.read_csv(input_file)
        logging.info(f"✅ Data loaded successfully! Columns: {list(data.columns)}")

        # ✅ Verify expected features
        missing_features = [feature for feature in EXPECTED_FEATURES if feature not in data.columns]
        if missing_features:
            raise ValueError(f"❌ Missing features: {missing_features}")

        # ✅ Make predictions
        model = load_model()
        predictions = model.predict(data[EXPECTED_FEATURES])

        # ✅ Add predictions to DataFrame
        data['prediction'] = ["High Risk" if p == 1 else "Low Risk" for p in predictions]

        # ✅ Save to output file
        data.to_csv(output_file, index=False)
        logging.info(f"✅ Predictions saved to {output_file}")

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run predictions using the trained model")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to save output CSV file")
    
    args = parser.parse_args()
    
    predict(args.input, args.output)
