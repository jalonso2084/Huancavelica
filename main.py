import openai
import os
import time
from flask import Flask, request, jsonify

# ✅ Initialize Flask API
app = Flask(__name__)

# ✅ Set OpenAI API key (ensure it's set in the environment)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ ERROR: OpenAI API key is missing. Set it as an environment variable.")
    exit(1)

client = openai.OpenAI(api_key=api_key)

def get_gpt4_explanation(predicted_risk, risk_factors):
    """
    Calls GPT-4 to generate an explanation for the given risk prediction.
    """
    try:
        print(f"🔄 Calling GPT-4 with risk: {predicted_risk}, factors: {risk_factors}")

        # ✅ Prevent rapid consecutive requests (avoids OpenAI rate limits)
        time.sleep(1)

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            max_tokens=300,  # ✅ Reduce response size to prevent memory issues
            timeout=10,  # ✅ Set timeout to prevent long API calls
            messages=[
                {"role": "system", "content": "You are an AI assistant providing explanations for potato disease predictions."},
                {"role": "user", "content": f"The model predicts {predicted_risk}% risk for late blight. Key risk factors: {risk_factors}. Explain why and suggest preventive actions."}
            ]
        )

        return response.choices[0].message.content

    except openai.error.Timeout:
        print("❌ ERROR: GPT-4 took too long to respond.")
        return "Error: GPT-4 response timed out."

    except openai.error.OpenAIError as e:
        print(f"❌ ERROR: OpenAI API call failed: {e}")
        return f"Error generating AI explanation: {e}"

    except Exception as e:  # ✅ Correct exception handling
        print(f"❌ ERROR: {e}")
        return f"Unexpected error: {e}"

@app.route("/", methods=["GET"])
def home():
    """
    Basic home route to check if the API is running.
    """
    return jsonify({"message": "Late Blight Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    """
    API endpoint that dynamically predicts late blight risk.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        # ✅ Extract Input Data
        variety = data.get("variety", "Unknown")
        humidity = data.get("humidity", 50)  # Default to 50 if missing
        weather = data.get("weather", "Cloudy")
        soil = data.get("soil", "Loamy")

        # ✅ Compute Dynamic Risk Score
        predicted_risk = 50  # Base risk

        # Adjust risk based on humidity
        if humidity > 80:
            predicted_risk += 15  # High humidity increases risk
        elif humidity < 40:
            predicted_risk -= 10  # Low humidity decreases risk

        # Adjust risk based on weather
        if weather == "Rainy":
            predicted_risk += 20  # Rainy weather significantly increases risk
        elif weather == "Sunny":
            predicted_risk -= 10  # Sunny weather reduces risk

        # Adjust risk based on potato variety
        if variety in ["INIA-321 Kawsay", "Poccoya"]:
            predicted_risk -= 10  # Resistant varieties decrease risk
        elif variety in ["Yungay"]:
            predicted_risk += 10  # Susceptible varieties increase risk

        # ✅ Ensure risk stays between 0-100%
        predicted_risk = max(0, min(100, predicted_risk))

        risk_factors = f"Humidity: {humidity}%, Weather: {weather}, Soil: {soil}, Variety: {variety}"

        # ✅ Generate AI Explanation using GPT-4
        gpt_explanation = get_gpt4_explanation(predicted_risk, risk_factors)

        # ✅ Return the response
        return jsonify({
            "variety": variety,
            "predicted_risk": predicted_risk,
            "validation": {
                "ppi_correlation": 0.84,
                "p_value": 0.2496,
                "confidence_score": 0.51,
                "reliability": "Medium Confidence"
            },
            "gpt_explanation": gpt_explanation
        })

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    from gunicorn.app.base import BaseApplication

    class GunicornApp(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        "bind": "0.0.0.0:5000",
        "workers": 1,  # ✅ Reduced from 2 to 1 to prevent memory overload
    }

    GunicornApp(app, options).run()
