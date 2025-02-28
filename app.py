import streamlit as st
import requests

# Define API endpoint (update if needed)
API_URL = "https://huancavelica.onrender.com/predict"  # Use your deployed API URL

# Potato variety options
varieties = [
    "INIA-303 Canchan", "INIA-302 Amarilis", "Yungay", "INIA-321 Kawsay",
    "CIP308488.92", "CIP308495.227", "CIP308478.59", "CIP308486.355",
    "CIP308487.157", "CIP308433.101", "CIP308436.84", "CIP308502.95"
]

st.title("🌱 AI-Powered Late Blight Prediction System")

# Input fields
st.subheader("Enter Environmental Conditions")
weather = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy"])
humidity = st.slider("Humidity (%)", 10, 100, 50)
soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay"])
variety = st.selectbox("Potato Variety", varieties)

# Submit button
if st.button("Predict Blight Risk"):
    payload = {"humidity": humidity, "weather": weather, "soil": soil_type, "variety": variety}
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"🌿 The predicted blight risk for {variety} is **{result['predicted_risk']}%**.")
    else:
        st.error("⚠️ Error: Could not get prediction. Please try again.")
