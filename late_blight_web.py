import streamlit as st
import requests
import os

# API URL (Use environment variable or config file for deployment)
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

def get_prediction(weather: str, humidity: int, soil_type: str, potato_variety: str) -> dict:
    """Send user input to API and get prediction."""
    payload = {
        "weather": weather,
        "humidity": humidity,
        "soil_type": soil_type,
        "potato_variety": potato_variety,
    }
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to get prediction: {e}"}

def main():
    st.title("Potato Late Blight Prediction System")
    st.write("Enter environmental conditions to predict late blight risk.")

    # User inputs
    weather = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Foggy"])
    humidity = st.slider("Humidity (%)", 10, 100, 50)
    soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay", "Silty"])
    potato_variety = st.selectbox("Potato Variety", ["Variety A", "Variety B", "Variety C"])

    if st.button("Predict Blight Risk"):
        with st.spinner("Predicting..."):
            prediction = get_prediction(weather, humidity, soil_type, potato_variety)

        if "error" in prediction:
            st.error(prediction["error"])
        elif "prediction" in prediction: #Example, adapt to your API response.
            risk_level = prediction["prediction"] #adapt to your API response.
            if risk_level > 0.7:
                st.warning(f"High Blight Risk: {risk_level:.2f}")
            elif risk_level > 0.3:
                st.info(f"Moderate Blight Risk: {risk_level:.2f}")
            else:
                st.success(f"Low Blight Risk: {risk_level:.2f}")
        elif "risk_level" in prediction: #Example, adapt to your API response.
            st.write(f"Risk level: {prediction['risk_level']}")
        else:
            st.write("Prediction result: ", prediction) #raw response if nothing else matches.

if __name__ == "__main__":
    main()