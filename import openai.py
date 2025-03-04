import openai
import os

# ✅ Initialize OpenAI client correctly
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt4_explanation(predicted_risk, risk_factors):
    """
    Calls GPT-4 to generate an explanation for the given risk prediction.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant providing explanations for potato disease predictions."},
                {"role": "user", "content": f"The model predicts {predicted_risk} risk for late blight. Key risk factors: {risk_factors}. Explain why and suggest preventive actions."}
            ]
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"Error generating AI explanation: {e}"

def predict(data):
    """
    Main API function that predicts late blight risk and provides an explanation.
    """
    predicted_risk = 68  # Replace with actual model output
    risk_factors = "High humidity (85%), Rainy weather"

    # ✅ Generate AI explanation
    gpt_explanation = get_gpt4_explanation(predicted_risk, risk_factors)

    # ✅ Return structured API response
    return {
        "variety": data["variety"],
        "predicted_risk": predicted_risk,
        "validation": {
            "ppi_correlation": 0.84,
            "p_value": 0.2496,
            "confidence_score": 0.51,
            "reliability": "Low Confidence"
        },
        "gpt_explanation": gpt_explanation
    }
