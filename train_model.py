import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib
import os

# ✅ Load training data
data = pd.read_csv('training_data.csv')

# ✅ Define feature columns
FEATURE_COLUMNS = [
    'variety', 'humidity', 'weather_condition', 'soil_type', 
    'plant_health_index', 'disease_pressure_index', 'growth_stage',
    'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture'
]

# ✅ Define target column
TARGET_COLUMN = 'blight_risk'

# ✅ Prepare input and target data
X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]

# ✅ One-hot encode categorical columns
encoder = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')
X_encoded = encoder.fit_transform(X[['variety', 'weather_condition', 'soil_type', 'growth_stage']])
X_encoded = np.concatenate([X_encoded, X[['humidity', 'plant_health_index', 'disease_pressure_index', 'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture']].values], axis=1)

# ✅ Initialize and train the model
model = RandomForestClassifier(
    n_estimators=100, 
    max_depth=None, 
    random_state=42
)

print("✅ Training model...")
model.fit(X_encoded, y)
print("✅ Model training complete!")

# ✅ Save the trained model and metadata in the same folder
model_path = os.path.join(os.getcwd(), 'random_forest_model.pkl')
metadata_path = os.path.join(os.getcwd(), 'metadata.pkl')

# ✅ Create metadata (feature names)
metadata = {
    'features': encoder.get_feature_names_out(['variety', 'weather_condition', 'soil_type', 'growth_stage']).tolist() +
                ['humidity', 'plant_health_index', 'disease_pressure_index', 'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture']
}

joblib.dump(model, model_path)
joblib.dump(metadata, metadata_path)

print(f"✅ Model saved to {model_path}")
print(f"✅ Metadata saved to {metadata_path}")
