import streamlit as st
import requests

# ✅ Set Page Title
st.set_page_config(page_title="AI-Powered Late Blight Prediction System")

# ✅ UI Header
st.markdown("<h1 style='text-align: center;'>🌱 AI-Powered Late Blight Prediction System</h1>", unsafe_allow_html=True)
st.write("### Enter Environmental Conditions")

# ✅ User Input Fields
weather = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy"])
humidity = st.slider("Humidity (%)", min_value=10, max_value=100, value=50)
soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay"])
potato_variety = st.selectbox(
    "Potato Variety",
    ["INIA-303 Canchan", "INIA-302 Amarilis", "Yungay", "INIA-321 Kawsay",
     "CIP308488.92", "CIP308495.227", "CIP308478.59", "CIP308486.355",
     "CIP308487.157", "CIP308433.101", "CIP308436.84", "CIP308502.95"]
)

# ✅ API Connection
api_url = "https://huancavelica.onrender.com/predict"

# ✅ Prediction Button
if st.button("Predict Blight Risk"):
    data = {
        "humidity": humidity,
        "weather": weather,
        "soil": soil_type,
        "variety": potato_variety
    }

    try:
        response = requests.post(api_url, json=data)
        result = response.json()

        if "predicted_risk" in result and "validation" in result:
            predicted_risk = result["predicted_risk"]
            validation = result["validation"]
            gpt_explanation = result.get("gpt_explanation", "No AI explanation available.")
            recommendation = result.get("recommendation", "No specific action needed.")

            # ✅ Display Results
            st.markdown(f"<h2 style='text-align: center; color: red;'>Predicted Risk: {predicted_risk}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>🔎 PPI Validation: {validation['reliability']}</h3>", unsafe_allow_html=True)

            # ✅ Show AI Explanation
            st.info(f"💡 **AI Explanation:** {gpt_explanation}")

            # ✅ Show Recommendation
            st.success(f"✅ **Recommended Action:** {recommendation}")

        else:
            st.error("⚠️ Unexpected response from the server.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")

# ✅ Updated Footer with Your Name
st.markdown("---")
st.markdown("🚀 Developed for **Jorge Luis Alonso** | **AI-Driven Agricultural Data Specialist**")
