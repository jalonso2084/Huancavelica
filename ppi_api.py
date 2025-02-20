from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load latest PPI results
def load_ppi_results():
    try:
        df = pd.read_csv("ppi_results.csv")
        latest_entry = df.iloc[-1]
        return {
            "PPI_Correlation": latest_entry["PPI_Correlation"],
            "CI_Lower": latest_entry["CI_Lower"],
            "CI_Upper": latest_entry["CI_Upper"],
            "Effective_Sample_Size": latest_entry["Effective_Sample_Size"],
            "GPT_Explanation": generate_explanation(latest_entry["PPI_Correlation"])
        }
    except Exception as e:
        return {"error": f"Failed to load PPI results: {str(e)}"}

# Generate explanation based on PPI Correlation
def generate_explanation(rho):
    if rho > 0.7:
        return "AI predictions are highly reliable."
    elif 0.4 <= rho <= 0.7:
        return "AI predictions are moderately reliable. Additional validation advised."
    else:
        return "AI model shows low reliability. Manual review is recommended."

@app.route('/ppi', methods=['GET'])
def get_ppi_results():
    """API endpoint to retrieve the latest PPI correlation results."""
    return jsonify(load_ppi_results())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
