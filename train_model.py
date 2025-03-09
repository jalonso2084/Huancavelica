# train_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# ✅ Load training data (replace 'data.csv' with your actual data file)
data = pd.read_csv('training_data.csv')

# ✅ Define feature columns (match the API input)
FEATURE_COLUMNS = [
    'variety', 'humidity', 'weather_condition', 'soil_type', 
    'plant_health_index', 'disease_pressure_index', 'growth_stage',
    'canopy_coverage', 'rainfall', 'temperature_variability', 'soil_moisture'
]

# ✅ Define target column (update this based on your dataset)
TARGET_COLUMN = 'blight_risk'

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

# ✅ Save the trained model
model_path = os.path.join(os.getcwd(), 'random_forest_model.pkl')
joblib.dump(model, model_path)
print(f"✅ Model saved to {model_path}")
