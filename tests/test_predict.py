import sys
import os

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

def test_predict_sample_data(tmp_path):
    """Test predict.py with a sample input CSV"""

    # Create a temporary input file
    sample_data = """Latitude_left,Longitude_left,Types of Potatoes Grown,Region/Country,Criteria for Selection,Farming Practices,pH_left,Bulk_Density_left,Organic_Carbon_left,CEC_left,Clay_Content_left,Sand_Content_left,Silt_Content_left,Climatic_Climate Variability,Climatic_Moderate El Niño, Increased Humidity,Climatic_Weak-Moderate El Niño, Excessive Rainfall,Fungicide Applications (Proxy for Severity)
    -13.8,-75.5,2,Peru,1,Traditional,5.6,1.2,2.1,15.3,20.5,50.2,29.3,0,0,1,4
    -13.8,-75.5,2,Peru,1,Traditional,5.6,1.2,2.1,15.3,20.5,50.2,29.3,0,0,1,1"""

    input_file = tmp_path / "sample_input.csv"
    input_file.write_text(sample_data)

    # Define output file path
    output_file = tmp_path / "predictions.csv"

    # Run prediction
    try:
        predict(str(input_file), str(output_file))
        assert output_file.exists(), "❌ Prediction output file was not created!"
        
        # Load predictions
        df = pd.read_csv(output_file)
        assert "Predicted_Disease_Risk" in df.columns, "❌ Predictions column missing!"
        assert len(df) == 2, "❌ Prediction output has incorrect number of rows!"
    except Exception as e:
        pytest.fail(f"❌ Prediction test failed: {e}")
