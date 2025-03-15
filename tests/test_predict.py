import pytest
import pandas as pd
import os
from scripts.predict import predict

# Mock the model's expected features
EXPECTED_FEATURES = [
    'feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5',
    'feature_6', 'feature_7', 'feature_8', 'feature_9', 'feature_10'
]

@pytest.fixture
def sample_data(tmp_path):
    # ✅ Create sample input data in correct order
    data = {
        'feature_1': [78, 70],
        'feature_2': [15, 12],
        'feature_3': [120, 110],
        'feature_4': [0.85, 0.82],
        'feature_5': [0.7, 0.65],
        'feature_6': [0.9, 0.85],
        'feature_7': [0.3, 0.4],
        'feature_8': [1, 0],
        'feature_9': [0, 1],
        'feature_10': [0, 0]
    }
    df = pd.DataFrame(data)

    input_file = tmp_path / "sample_input.csv"
    df.to_csv(input_file, index=False)

    output_file = tmp_path / "predictions.csv"

    return input_file, output_file

def test_predict_sample_data(sample_data):
    input_file, output_file = sample_data
    
    try:
        # ✅ Run the prediction
        predict(str(input_file), str(output_file))
        
        # ✅ Confirm that output file was created
        assert output_file.exists(), "❌ Prediction output file was not created!"

        # ✅ Load and check structure of output file
        df = pd.read_csv(output_file)
        assert "Predicted_Disease_Risk" in df.columns, "❌ Predictions column missing!"
        assert len(df) == 2, "❌ Prediction output has incorrect number of rows!"

    except Exception as e:
        pytest.fail(f"❌ Prediction test failed: {e}")
