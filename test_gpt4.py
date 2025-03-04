import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ ERROR: OpenAI API key is missing.")
    exit(1)

client = openai.OpenAI(api_key=api_key)
 

# Option 2: Use environment variable (recommended for security)
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

# ✅ Run test function
if __name__ == "__main__":
    test_risk = "High"
    test_factors = "High humidity and recent rainfall"
    
    explanation = get_gpt4_explanation(test_risk, test_factors)
    print("\n🔍 Final AI Explanation:\n", explanation)
