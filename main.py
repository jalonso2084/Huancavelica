import openai
import os
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
        print(f"🔄 Calling GPT-4 with risk: {predicted_risk}, factors: {risk_factors}")  # Debugging

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant providing explanations for potato disease predictions."},
                {"role": "user", "content": f"The model predicts {predicted_risk} risk for late blight. Key risk factors: {risk_factors}. Explain why and suggest preventive actions."}
            ]
        )

        explanation = response.choices[0].message.content
        print("✅ GPT-4 Response Received:\n", explanation)  # Debugging
        return explanation

    except openai.AuthenticationError:
        print("❌ ERROR: Invalid OpenAI API Key! Check your key at https://platform.openai.com/account/api-keys.")
        return "Error: Invalid API Key"

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
    API endpoint that predicts late blight risk and provides an AI-generated explanation.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        predicted_risk = 68  # Replace this with actual model output
        risk_factors = "High humidity (85%), Recent Rainfall"

        # ✅ Generate AI explanation using GPT-4
        gpt_explanation = get_gpt4_explanation(predicted_risk, risk_factors)

        # ✅ Return the response as JSON
        return jsonify({
            "variety": data.get("variety", "Unknown"),
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
    app.run(host="0.0.0.0", port=5000, debug=True)
