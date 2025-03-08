import joblib

# Path to important_features.pkl
feature_path = r"G:\My Drive\Huancavelica\processed_data\historical_disease_records\data\processed\model\important_features.pkl"

# Load feature names
try:
    feature_names = joblib.load(feature_path)  # Load the feature names from the pickle file
    print("✅ Expected model features:", feature_names)
except Exception as e:
    print("❌ Error loading feature file:", e)
