import argparse
import pandas as pd
import pickle
import os

print("🚀 Running predict.py... This line should ALWAYS appear!")

# Function to load the trained model
def load_model():
    print("🔍 Entering load_model()...")

    model_path = os.path.join("processed_data", "historical_disease_records", "data", "processed", "model", "trained_model.pkl")

    try:
        print(f"🔍 Attempting to load model from: {model_path}")
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        print("✅ Model loaded successfully!")
        return model
    except FileNotFoundError:
        print(f"❌ Error: Model file not found at {model_path}")
        exit(1)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        exit(1)

# Function to make predictions
def predict(input_file):
    print(f"🔍 Loading input file: {input_file}")

    # Load the input dataset
    try:
        data = pd.read_csv(input_file)
        print(f"✅ Data loaded successfully! Columns: {list(data.columns)}")
    except Exception as e:
        print(f"❌ Error loading input file: {e}")
        return

    # Load the trained model
    print("🔍 Loading trained model...")
    model = load_model()

    # Ensure all model-required features are in the input data
    expected_features = model.feature_names_in_
    print(f"✅ Model expects features: {expected_features}")

    missing_features = [f for f in expected_features if f not in data.columns]

    if missing_features:
        print(f"⚠ Warning: Missing features in input file: {missing_features}")

    # **Fill missing features with default values (0)**
   for feature in missing_features:
    if feature in model.feature_names_in_:  # Check if feature exists in training data
        default_value = data.mean().get(feature, 0)  # Use mean value, default to 0 if not found
    else:
        default_value = 0  # If the feature is completely unknown, use 0
    data[feature] = default_value


    # Reorder columns to match model's expectations
    data = data[expected_features]

    print("🔍 Final input data being fed to the model:")
    print(data.head())  # Print the first few rows to check values

    print("🔍 Making predictions...")  # ✅ Indentation is now fixed

    # Make predictions
    try:
        predictions = model.predict(data)
        print(f"✅ Predictions: {predictions}")
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return

    # Save results
    data["Predicted_Disease_Risk"] = predictions
    print("✅ Predictions completed!")

    output_file = "predictions.csv"
    data.to_csv(output_file, index=False)
    print(f"📂 Results saved to: {output_file}")

# Command-line argument parsing
if __name__ == "__main__":
    print("🚀 Script started")
    
    parser = argparse.ArgumentParser(description="Run the late blight prediction model on input data.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input CSV file")
    args = parser.parse_args()
    
    print(f"🔍 Input file received: {args.input}")

    predict(args.input)
