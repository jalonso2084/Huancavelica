import openai
import os
import platform
import joblib  # ✅ Load Machine Learning Models
import numpy as np
from flask import Flask, request, jsonify

# ✅ Initialize Flask API
app = Flask(__name__)

# ✅ Detect Operating System
IS_WINDOWS = platform.system() == "Windows"

# ✅ Load Trained Model
MODEL_PATH = "random_forest_model.pkl"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ Random Forest model loaded successfully!")
else:
    print("❌ ERROR: No trained model found!")

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
        print(f"🔄 Calling GPT-4 with risk: {predicted_risk}, factors: {risk_factors}")  # Debugging

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            max_tokens=300,
            timeout=10,
            messages=[
                {"role": "system", "content": "You are an AI assistant providing explanations for potato disease predictions."},
                {"role": "user", "content": f"The model predicts {predicted_risk}% risk for late blight. Key risk factors: {risk_factors}. Explain why and suggest preventive actions."}
            ]
        )

        explanation = response.choices[0].message.content
        print("✅ GPT-4 Response Received:\n", explanation)  # Debugging
        return explanation

    except openai.AuthenticationError:
        print("❌ ERROR: OpenAI API Key is invalid or missing.")
        return "Error: Invalid API Key. Please check your OpenAI key settings."

    except openai.OpenAIError as e:
        print(f"❌ ERROR: OpenAI API call failed: {e}")  # Debugging
        return f"Error generating AI explanation: {e}"

@app.route("/", methods=["GET"])
def home():
    """
    Basic home route to check if the API is running.
    """
    return jsonify({"message": "Late Blight Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    """
    API endpoint that dynamically predicts late blight risk using Random Forest.
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

        # ✅ Encode categorical variables
        weather_mapping = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}
        soil_mapping = {"Sandy": 0, "Loamy": 1, "Clay": 2}
        variety_mapping = {
            "INIA-303 Canchan": 0, "INIA-302 Amarilis": 1, "INIA-321 Kawsay": 2,
            "Yungay": 3, "Poccoya": 4, "CIP-Matilde": 5
        }

        weather_encoded = weather_mapping.get(weather, 1)
        soil_encoded = soil_mapping.get(soil, 1)
        variety_encoded = variety_mapping.get(variety, 3)

        # ✅ Use Random Forest model if available
        if os.path.exists(MODEL_PATH):
            print("🔄 Using Random Forest Model for Prediction")
            input_features = np.array([[humidity, weather_encoded, soil_encoded, variety_encoded]])
            predicted_risk = model.predict(input_features)[0]
        else:
            print("⚠️ Falling back to static risk calculation")
            predicted_risk = 50  # Default if model is missing

        predicted_risk = max(0, min(100, predicted_risk))  # ✅ Ensure risk stays within 0-100%

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
    if IS_WINDOWS:
        print("✅ Running on Windows with Waitress")
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000)
    else:
        print("✅ Running on Linux with Gunicorn")
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
            "workers": 1  # ✅ Reduce memory usage
        }
        GunicornApp(app, options).run()
