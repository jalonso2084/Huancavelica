# -*- coding: utf-8 -*-
import os
import pandas as pd
import pickle

# ✅ Load Model
def load_model():
    print("\U0001f50d Entering load_model()...")  # Unicode for magnifying glass
    model_path = os.path.join(
        "processed_data",
        "historical_disease_records",
        "data",
        "processed",
        "model",
        "trained_model.pkl"
    )

    try:
        print(f"\U0001f50d Attempting to load model from: {model_path}")
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        print("\u2705 Model loaded successfully!")  # ✅ Unicode checkmark
        return model
    except FileNotFoundError:
        print(f"\u274c Error: Model file not found at {model_path}")  # ❌ Unicode X mark
        exit(1)

# ✅ Prediction Function
def predict(input_file, output_file):
    print(f"\U0001f50d Loading input file: {input_file}")
    
    try:
        # ✅ Load input data
        data = pd.read_csv(input_file)
        print(f"\u2705 Data loaded successfully! Columns: {list(data.columns)}")
    except Exception as e:
        print(f"\u274c Error loading input file: {e}")
        exit(1)

    # ✅ Load the trained model
    model = load_model()

    try:
        # ✅ Ensure input columns match model expectations
        required_features = [
            'humidity', 'temperature_variability', 'rainfall', 
            'plant_health_index', 'disease_pressure_index', 
            'canopy_coverage', 'soil_moisture', 
            'variety_INIA-302 Amarilis', 'variety_INIA-303 Canchan', 
            'variety_INIA-321 Kawsay', 'variety_Poccoya', 'variety_Yungay', 
            'weather_condition_Rain', 'weather_condition_Sunny', 
            'soil_type_Loamy', 'soil_type_Sandy', 'soil_type_Silty',
            'growth_stage_Maturity', 'growth_stage_Vegetative'
        ]
        
        missing_features = [col for col in required_features if col not in data.columns]
        if missing_features:
            raise ValueError(f"Missing features: {missing_features}")
        
        # ✅ Ensure correct data types
        data = data[required_features]

        # ✅ Generate predictions
        predictions = model.predict(data)
        data['prediction'] = ["High Risk" if pred == 1 else "Low Risk" for pred in predictions]

        # ✅ Save to CSV
        data.to_csv(output_file, index=False)
        print(f"\u2705 Predictions saved to {output_file}")

    except Exception as e:
        print(f"\u274c Error during prediction: {e}")
        exit(1)

# ✅ Allow script to be executed directly
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run predictions on input data")
    parser.add_argument('--input', required=True, help="Path to input CSV file")
    parser.add_argument('--output', required=True, help="Path to output CSV file")

    args = parser.parse_args()

    predict(args.input, args.output)
