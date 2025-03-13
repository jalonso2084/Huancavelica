import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib
import os

# ✅ Load training data (replace 'training_data.csv' with your actual data file)
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

# ✅ Encode categorical data
encoder = OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore')
X_encoded = encoder.fit_transform(X[['variety', 'weather_condition', 'soil_type', 'growth_stage']])
X_encoded = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(['variety', 'weather_condition', 'soil_type', 'growth_stage']))
X_numeric = X.drop(columns=['variety', 'weather_condition', 'soil_type', 'growth_stage']).reset_index(drop=True)

# ✅ Combine encoded + numeric data
X_final = pd.concat([X_encoded, X_numeric], axis=1)

# ✅ Initialize and train the model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)

print("✅ Training model...")
model.fit(X_final, y)
print("✅ Model training complete!")

# ✅ Generate sample prediction to test locally
sample_input = X_final.iloc[[0]]
sample_prediction = model.predict(sample_input)[0]
prediction_label = "High Risk" if sample_prediction == 1 else "Low Risk"
print(f"✅ Sample Prediction: {prediction_label}")

# ✅ Save the trained model and metadata
model_path = os.path.join(os.getcwd(), 'random_forest_model.pkl')
metadata_path = os.path.join(os.getcwd(), 'metadata.pkl')

joblib.dump(model, model_path)
joblib.dump({
    'features': X_final.columns.tolist(),
    'encoder': encoder  # Save the encoder!
}, metadata_path)

print(f"✅ Model saved to {model_path}")
print(f"✅ Metadata saved to {metadata_path}")
