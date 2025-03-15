import pandas as pd
import joblib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the model
MODEL_PATH = 'model.pkl'

def load_model():
    logging.info("Loading model...")
    model = joblib.load(MODEL_PATH)
    logging.info(f"Model loaded with expected features: {model.feature_names_in_}")
    return model

def predict(input_file, output_file):
    try:
        logging.info(f"Reading input file: {input_file}")
        df = pd.read_csv(input_file)
        logging.info(f"Input columns: {list(df.columns)}")
        
        model = load_model()

        # ✅ Ensure that input feature order matches the model's training order
        if not all(col in df.columns for col in model.feature_names_in_):
            missing_features = [col for col in model.feature_names_in_ if col not in df.columns]
            raise ValueError(f"❌ Missing features in input data: {missing_features}")

        # ✅ Reorder the columns to match the model’s training order
        df = df[model.feature_names_in_]

        logging.info("Running prediction...")
        predictions = model.predict(df)

        # ✅ Save the output
        output_df = pd.DataFrame(predictions, columns=["Predicted_Disease_Risk"])
        output_df.to_csv(output_file, index=False)
        logging.info(f"✅ Prediction successful! Results saved to: {output_file}")

    except Exception as e:
        logging.error(f"❌ Error during prediction: {e}")
        raise e

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        logging.error("❌ Usage: python predict.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    predict(input_file, output_file)
