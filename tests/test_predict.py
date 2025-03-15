import sys
import os
import pytest
import pandas as pd

# Ensure Python can find the scripts directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Attempt to import predict function
try:
    from scripts.predict import predict
except ModuleNotFoundError as e:
    print(f"❌ ImportError: {e}")
    raise

# ✅ Define expected features to match model input order
EXPECTED_FEATURES = [
    'humidity', 'temperature_variability', 'rainfall', 'plant_health_index', 'disease_pressure_index',
    'canopy_coverage', 'soil_moisture', 'variety_INIA-302 Amarilis', 'variety_INIA-303 Canchan',
    'variety_INIA-321 Kawsay', 'variety_Poccoya', 'variety_Yungay', 'weather_condition_Rain',
    'weather_condition_Sunny', 'soil_type_Loamy', 'soil_type_Sandy', 'soil_type_Silty',
    'growth_stage_Maturity', 'growth_stage_Vegetative'
]

@pytest.fixture
def sample_data(tmp_path):
    # ✅ Updated sample input to match new format and order
    sample_data = [
        [78, 15, 120, 0.85, 0.7, 0.9, 0.3, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],  # Row 1
        [70, 12, 110, 0.82, 0.65, 0.85, 0.4, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]  # Row 2
    ]
    
    # ✅ Create DataFrame using exact feature order from metadata
    df = pd.DataFrame(sample_data, columns=EXPECTED_FEATURES)
    
    # ✅ Create input file in temp directory
    input_file = tmp_path / "sample_input.csv"
    df.to_csv(input_file, index=False)
    
    # ✅ Define output file path
    output_file = tmp_path / "predictions.csv"
    
    return input_file, output_file

def test_predict_sample_data(sample_data):
    input_file, output_file = sample_data
    
    try:
        # ✅ Run the prediction
        predict(str(input_file), str(output_file))

        # ✅ Ensure output file was created
        assert output_file.exists(), "❌ Prediction output file was not created!"
        
        # ✅ Load and check structure of output file
        df = pd.read_csv(output_file)
        assert "Predicted_Disease_Risk" in df.columns, "❌ Predictions column missing!"
        assert len(df) == 2, "❌ Prediction output has incorrect number of rows!"

    except Exception as e:
        pytest.fail(f"❌ Prediction test failed: {e}")
