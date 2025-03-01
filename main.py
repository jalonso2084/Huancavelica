import streamlit as st
import requests

# Set the title
st.set_page_config(page_title="AI-Powered Late Blight Prediction System")

st.markdown(
    "<h1 style='text-align: center;'>🌱 AI-Powered Late Blight Prediction System</h1>", 
    unsafe_allow_html=True
)

st.write("### Enter Environmental Conditions")

# Dropdown for weather condition
weather = st.selectbox(
    "Weather Condition", 
    ["Sunny", "Cloudy", "Rainy"]
)

# Slider for humidity percentage
humidity = st.slider("Humidity (%)", min_value=10, max_value=100, value=50)

# Dropdown for soil type
soil_type = st.selectbox(
    "Soil Type", 
    ["Sandy", "Loamy", "Clay"]
)

# Dropdown for potato variety
potato_variety = st.selectbox(
    "Potato Variety",
    [
        "INIA-303 Canchan",
        "INIA-302 Amarilis",
        "Yungay",
        "INIA-321 Kawsay",
        "CIP308488.92",
        "CIP308495.227",
        "CIP308478.59",
        "CIP308486.355",
        "CIP308487.157",
        "CIP308433.101",
        "CIP308436.84",
        "CIP308502.95"
    ]
)

# Button to submit input and get prediction
if st.button("Predict Blight Risk"):
    # Prepare input data
    data = {
        "humidity": str(humidity),
        "weather": weather,
        "soil": soil_type,
        "variety": potato_variety
    }

    # API URL - Update this with your Render backend URL
    api_url = "https://huancavelica.onrender.com/predict"

    try:
        response = requests.post(api_url, json=data)
        result = response.json()
        
        if "predicted_risk" in result:
            st.success(f"🌿 Predicted Late Blight Risk: {result['predicted_risk']}")
        else:
            st.error("⚠️ Unexpected response from the server.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")

# Footer
st.markdown("---")
st.markdown("🌍 Developed for **Huancavelica Potato Farmers** | 🔬 AI-Powered Agricultural Research")
