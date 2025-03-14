import sys
import os
import joblib

# Ensure Python can find the scripts directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Attempt to import predict function, with an error message if it fails
try:
    from scripts.predict import predict
except ModuleNotFoundError as e:
    print(f"❌ ImportError: {e}")
    raise

import pytest
import pandas as pd

# ✅ Load expected feature order directly from metadata.pkl
metadata_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metadata.pkl'))
with open(metadata_path, 'rb') as f:
    metadata = joblib.load(f)
    EXPECTED_FEATURES = metadata['features']

def test_predict_sample_data(tmp_path):
    """Test predict.py with a sample input CSV"""

    # ✅ Updated sample input to match new format and order
    sample_data = [
        [78, 15, 120, 0.85, 0.7, 0.9, 0.3, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [70, 12, 110, 0.82, 0.65, 0.85, 0.4, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
    ]

    # ✅ Create DataFrame using the **exact feature order** from metadata
    df = pd.DataFrame(sample_data, columns=EXPECTED_FEATURES)

    # ✅ Create input file in temp directory
    input_file = tmp_path / "sample_input.csv"
    df.to_csv(input_file, index=False)

    # ✅ Define output file path
    output_file = tmp_path / "predictions.csv"

    # ✅ Run prediction
    try:
        predict(str(input_file), str(output_file))
        
        # ✅ Ensure output file was created
        assert output_file.exists(), "❌ Prediction output file was not created!"

        # ✅ Load predictions and check the structure
        df = pd.read_csv(output_file)
        assert "Predicted_Disease_Risk" in df.columns, "❌ Predictions column missing!"
        assert len(df) == 2, "❌ Prediction output has incorrect number of rows!"
    
    except Exception as e:
        pytest.fail(f"❌ Prediction test failed: {e}")
