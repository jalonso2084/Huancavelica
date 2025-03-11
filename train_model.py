import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

# ✅ Load training data with error handling
try:
    data = pd.read_csv('training_data.csv')
except FileNotFoundError:
    raise FileNotFoundError("❌ training_data.csv not found. Make sure the file exists in the working directory.")
except pd.errors.EmptyDataError:
    raise ValueError("❌ training_data.csv is empty. Please check the file.")
except pd.errors.ParserError as e:
    raise ValueError(f"❌ Error parsing training_data.csv: {e}")
except Exception as e:
    raise Exception(f"❌ Error loading training data: {e}")

# ✅ Define feature columns (match the API input)
FEATURE_COLUMNS = [
    'variety', 'humidity', 'weather_condition', 'soil_type', 
    'plant_health_index', 'disease_pressure_index', 'growth_stage',
    'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture'
]

# ✅ Define target column (update this based on your dataset)
TARGET_COLUMN = 'blight_risk'

# ✅ Ensure that all feature columns are present
missing_columns = [col for col in FEATURE_COLUMNS if col not in data.columns]
if missing_columns:
    raise ValueError(f"❌ Missing columns in data: {missing_columns}")

# ✅ Prepare input and target data
X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]

# ✅ Initialize and train the model
model = RandomForestClassifier(
    n_estimators=100,  # Number of trees
    max_depth=None,     # No limit on depth
    random_state=42     # Seed for reproducibility
)

print("✅ Training model...")
model.fit(X, y)
print("✅ Model training complete!")

# ✅ Sample prediction to verify model output type
try:
    # Convert to DataFrame to include feature names (removes warning)
    sample_data = pd.DataFrame([X.iloc[0].values], columns=FEATURE_COLUMNS)
    prediction = model.predict(sample_data)[0]
    prediction_label = "High Risk" if prediction == 1 else "Low Risk"
    print(f"✅ Sample Prediction: {prediction_label}")
except Exception as e:
    print(f"❌ Error during sample prediction: {e}")

# ✅ Save the trained model and metadata using Pathlib
model_path = Path.cwd() / 'random_forest_model.pkl'
metadata = {
    'features': FEATURE_COLUMNS,
    'target': TARGET_COLUMN,
    'n_estimators': 100,
    'random_state': 42
}
joblib.dump((model, metadata), model_path)
print(f"✅ Model and metadata saved to {model_path}")
