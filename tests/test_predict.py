import pytest
import pandas as pd
from scripts.predict import predict

def test_predict_sample_data(tmp_path):
    """Test predict.py with a sample input CSV"""

    # Create a temporary input file
    sample_data = """temperature,humidity,soil_moisture
    18,85,30
    22,70,40
    16,90,25
    20,65,35"""
    
    input_file = tmp_path / "sample_input.csv"
    input_file.write_text(sample_data)

    # Run prediction
    try:
        predict(str(input_file))
        output_file = tmp_path / "predictions.csv"
        assert output_file.exists(), "Prediction output file was not created!"
        
        # Load predictions
        df = pd.read_csv(output_file)
        assert "Predicted_Disease_Risk" in df.columns, "Predictions column missing!"
        assert len(df) == 4, "Prediction output has incorrect number of rows!"
    except Exception as e:
        pytest.fail(f"Prediction test failed: {e}")
