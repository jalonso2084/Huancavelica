import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# ✅ Load training data
data = pd.read_csv('training_data.csv')

# ✅ Define feature columns (directly from CSV since it's one-hot encoded)
FEATURE_COLUMNS = [
    'humidity', 'temperature_variability', 'rainfall', 'plant_health_index',
    'disease_pressure_index', 'canopy_coverage', 'soil_moisture',
    'variety_INIA-302 Amarilis', 'variety_INIA-303 Canchan', 'variety_INIA-321 Kawsay', 
    'variety_Poccoya', 'variety_Yungay', 
    'weather_condition_Rain', 'weather_condition_Sunny',
    'soil_type_Loamy', 'soil_type_Sandy', 'soil_type_Silty',
    'growth_stage_Maturity', 'growth_stage_Vegetative'
]

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

# ✅ Generate a sample prediction to test it locally
sample_input = X.iloc[[0]]
sample_prediction = model.predict(sample_input)[0]
prediction_label = "High Risk" if sample_prediction == 1 else "Low Risk"
print(f"✅ Sample Prediction: {prediction_label}")

# ✅ Save the trained model and metadata
model_path = os.path.join(os.getcwd(), 'random_forest_model.pkl')
metadata_path = os.path.join(os.getcwd(), 'metadata.pkl')

# ✅ Save model and metadata
joblib.dump(model, model_path)
joblib.dump({
    'features': list(X.columns)
}, metadata_path)

print(f"✅ Model saved to {model_path}")
print(f"✅ Metadata saved to {metadata_path}")
