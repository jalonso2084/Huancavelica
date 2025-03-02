import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error

class PPIValidation:
    def __init__(self, human_data: pd.DataFrame, ai_predictions: pd.DataFrame):
        """
        Initialize the PPI Validation class.
        
        :param human_data: Pandas DataFrame with real-world blight observations.
        :param ai_predictions: Pandas DataFrame with AI model-generated predictions.
        """
        self.human_data = human_data
        self.ai_predictions = ai_predictions

    def compute_ppi_correlation(self):
        """
        Calculate the PPI correlation (ρ̃) between AI predictions and real observations.
        """
        actual = self.human_data["outbreak_risk"].dropna().values  # Remove NaN values
        predicted = self.ai_predictions["predicted_risk"].dropna().values

        print(f"📊 Debug - Actual Data (real outbreaks) Count: {len(actual)} → {actual}")  # Debugging Step
        print(f"📊 Debug - Predicted Data (AI output) Count: {len(predicted)} → {predicted}")  # Debugging Step

        # Ensure at least two values exist
        if len(actual) < 2 or len(predicted) < 2:
            print("❌ Error: Not enough data for correlation calculation!")
            return None, None

        # Ensure actual and predicted have the same length
        min_length = min(len(actual), len(predicted))
        actual = actual[:min_length]
        predicted = predicted[:min_length]

        try:
            correlation, p_value = pearsonr(actual, predicted)
            print(f"✅ Pearson Correlation: {correlation}, P-Value: {p_value}")  # Debugging Step
        except Exception as e:
            print(f"❌ Error computing correlation: {str(e)}")
            return None, None

        return correlation, p_value

    def compute_ppi_confidence(self):
        """
        Compute prediction confidence score based on Mean Squared Error (MSE).
        """
        actual = self.human_data["outbreak_risk"].dropna().values
        predicted = self.ai_predictions["predicted_risk"].dropna().values

        if len(actual) < 2 or len(predicted) < 2:
            print("⚠️ Warning: Not enough data for meaningful confidence calculation.")
            return 0.0  # Return low confidence if data is insufficient

        # Ensure actual and predicted have the same length
        min_length = min(len(actual), len(predicted))
        actual = actual[:min_length]
        predicted = predicted[:min_length]

        mse = mean_squared_error(actual, predicted)
        
        # Prevent confidence from going to exactly 0
        confidence_score = max(0.2, np.exp(-mse))  # Ensure minimum confidence of 0.2
  # Ensures at least 0.01 confidence
        
        return round(confidence_score, 3)

    def validate_predictions(self):
        """
        Validate AI predictions and return an adjusted output with confidence scores.
        """
        try:
            correlation, p_value = self.compute_ppi_correlation()
            confidence_score = self.compute_ppi_confidence()
        except ValueError as e:
            print(f"❌ Validation Error: {str(e)}")
            return {
                "ppi_correlation": None,
                "p_value": None,
                "confidence_score": None,
                "reliability": "Low Confidence (Insufficient Data)"
            }

        return {
            "ppi_correlation": round(correlation, 3) if correlation is not None else None,
            "p_value": round(p_value, 4) if p_value is not None else None,
            "confidence_score": confidence_score,
            "reliability": self.get_reliability_level(confidence_score)
        }

    def get_reliability_level(self, confidence_score):
        """
        Categorize predictions based on confidence score.
        """
        if confidence_score >= 0.8:
            return "High Confidence"
        elif confidence_score >= 0.5:
            return "Medium Confidence"
        else:
            return "Low Confidence"
