import sys
import os
import argparse
import pandas as pd
import pickle

# Force UTF-8 encoding to avoid UnicodeEncodeError in Windows CI/CD
sys.stdout.reconfigure(encoding='utf-8')

print("🚀 Running predict.py... This line should ALWAYS appear!")

# Function to load the trained model
def load_model():
    print("🔍 Entering load_model()...")

    model_path = os.path.join(
        "processed_data",
        "historical_disease_records",
        "data",
        "processed",
        "model",
        "trained_model.pkl"
    )

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
def predict(input_file, output_path="predictions.csv"):
    print(f"🔍 Loading input file: {input_file}")

    # Load the input dataset
    try:
        data = pd.read_csv(input_file, encoding="utf-8", encoding_errors="replace")
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

    # Fill missing features with default values
    normalized_features = {str(f): f for f in data.columns}

    for feature in missing_features:
        feature = normalized_features.get(str(feature), feature)
        default_value = 0  # Default numeric values to 0
        data[feature] = default_value

    # Ensure no missing values before prediction
    print("🔍 Filling any remaining missing values with default (0)...")
    data.fillna(0, inplace=True)
    print("✅ Missing values filled.")

    # Reorder columns to match model's expectations
    data = data[expected_features]

    print("🔍 Converting categorical columns to numeric format...")
    categorical_columns = data.select_dtypes(include=["object"]).columns

    if not categorical_columns.empty:
        print(f"⚠ Warning: Converting categorical columns: {list(categorical_columns)}")
        data[categorical_columns] = data[categorical_columns].astype("category").apply(lambda x: x.cat.codes)

    print("✅ Categorical conversion completed.")

    print("🔍 Making predictions...")

    try:
        predictions = model.predict(data)
        print(f"✅ Predictions: {predictions}")
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return

    print(f"🔍 Number of input rows: {len(data)}, Number of predictions: {len(predictions)}")

    if len(predictions) == len(data):
        data["Predicted_Disease_Risk"] = predictions
        print("✅ Predictions successfully added to dataset!")
    else:
        print(f"❌ Error: Number of predictions ({len(predictions)}) does not match number of rows ({len(data)})!")

    # Save results
    data.to_csv(output_path, index=False)
    print(f"📂 Results saved to: {output_path}")

# Command-line argument parsing
if __name__ == "__main__":
    print("🚀 Script started")
    
    parser = argparse.ArgumentParser(description="Run the late blight prediction model on input data.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input CSV file")
    parser.add_argument("--output", type=str, default="predictions.csv", help="Path to save the output predictions")  
    args = parser.parse_args()
    
    print(f"🔍 Input file received: {args.input}")
    print(f"📂 Output file will be saved as: {args.output}")  

    predict(args.input, args.output)
