import streamlit as st
import requests

# ✅ Load potato variety descriptions from file
with open("potato_varieties.txt", "r", encoding="utf-8") as file:
    variety_info = file.read()

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
    ["INIA-303 Canchan", "INIA-302 Amarilis", "INIA-321 Kawsay", "Yungay", "Poccoya", "CIP-Matilde"]
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

            # ✅ Fetch variety-specific details from reference text
            variety_details = "No specific information available."
            for line in variety_info.split("\n"):
                if potato_variety in line:
                    variety_details = line.strip()
                    break

            # ✅ Display Results
            st.markdown(f"<h2 style='text-align: center; color: red;'>Predicted Risk: {predicted_risk}</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>🔎 PPI Validation: {validation['reliability']}</h3>", unsafe_allow_html=True)

            # ✅ Show AI Explanation
            if gpt_explanation and gpt_explanation != "GPT-4 explanation is currently unavailable.":
                st.info(f"💡 **AI Explanation:**\n\n{gpt_explanation}")
                st.success(f"📝 **Potato Variety Information:**\n\n{variety_details}")
            else:
                st.warning("⚠️ AI-generated explanation is not available.")

        else:
            st.error("⚠️ Unexpected response from the server.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")

# ✅ Updated Footer with Clickable LinkedIn Link
st.markdown("---")
st.markdown("🚀 Developed for **[Jorge Luis Alonso](https://www.linkedin.com/in/jorgeluisalonso/)** | **AI-Driven Agricultural Data Specialist**")
