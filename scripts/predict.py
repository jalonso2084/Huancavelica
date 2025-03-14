
# -*- coding: utf-8 -*-

import os
import pandas as pd
import joblib
import logging

# ✅ Set up logging
logging.basicConfig(level=logging.INFO)

def load_model():
    logging.info("🔍 Entering load_model()...")

    # ✅ Updated path to match the actual model location
    model_path = os.path.join(
        os.getcwd(),  # Current working directory
        "random_forest_model.pkl"  # Model file in root directory
    )

    try:
        logging.info(f"🔍 Attempting to load model from: {model_path}")
        with open(model_path, "rb") as file:
            model = joblib.load(file)
        logging.info("✅ Model loaded successfully!")
        return model
    except FileNotFoundError:
        logging.error(f"❌ Error: Model file not found at {model_path}")
        exit(1)

def predict(input_file, output_file):
    logging.info(f"🔍 Loading input file: {input_file}")

    try:
        data = pd.read_csv(input_file)
        logging.info(f"✅ Data loaded successfully! Columns: {list(data.columns)}")
    except Exception as e:
        logging.error(f"❌ Error loading input file: {e}")
        exit(1)

    # ✅ Load the model
    model = load_model()

    try:
        logging.info("🔍 Making predictions...")
        predictions = model.predict(data)
        logging.info(f"✅ Predictions generated: {predictions}")

        # ✅ Save predictions to CSV
        output_df = data.copy()
        output_df["Predicted Risk"] = predictions
        output_df.to_csv(output_file, index=False)
        logging.info(f"✅ Predictions saved to {output_file}")

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        exit(1)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Predict Late Blight Risk")
    parser.add_argument("--input", type=str, required=True, help="Path to input CSV file")
    parser.add_argument("--output", type=str, required=True, help="Path to output CSV file")

    args = parser.parse_args()

    predict(args.input, args.output)
