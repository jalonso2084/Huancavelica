import argparse
import pandas as pd
import pickle
import os

# Define the model path
MODEL_PATH = os.path.join("processed_data", "historical_disease_records", "data", "processed", "model", "trained_model.pkl")

# Function to load the trained model
def load_model():
    try:
        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        print("❌ Error: Model file not found at", MODEL_PATH)
        exit(1)

# Function to make predictions
def predict(input_file):
    # Load the input dataset
    data = pd.read_csv(input_file)
    
    # Drop the target column if it exists
    if "disease_risk" in data.columns:
        data = data.drop(columns=["disease_risk"])

    # Load the trained model
    model = load_model()
    
    # Make predictions
    predictions = model.predict(data)
    
    # Display results
    data["Predicted_Disease_Risk"] = predictions
    print("✅ Predictions completed!")
    print(data)

    # Save the output
    output_file = "predictions.csv"
    data.to_csv(output_file, index=False)
    print(f"📂 Results saved to: {output_file}")

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the late blight prediction model on input data.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input CSV file")
    args = parser.parse_args()

    # Run the prediction function
    predict(args.input)
