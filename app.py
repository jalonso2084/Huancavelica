import streamlit as st
import requests
import plotly.graph_objects as go

# Set Streamlit page configuration
st.set_page_config(page_title="Late Blight Prediction", layout="wide")

# ✅ Mobile-Friendly UI
st.markdown("""
    <style>
        .block-container {
            max-width: 95% !important;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center;'>🌱 AI-Powered Late Blight Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict the risk of late blight based on environmental factors.</p>", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header("Enter Environmental Conditions")

# Dropdowns & Inputs
weather = st.sidebar.selectbox("Weather Condition", ["Sunny", "Rainy", "Cloudy"])
humidity = st.sidebar.slider("Humidity (%)", min_value=10, max_value=100, value=50)
soil_type = st.sidebar.selectbox("Soil Type", ["Sandy", "Loamy", "Clay"])
variety = st.sidebar.selectbox(
    "Potato Variety",
    ["INIA-303 Canchan", "INIA-302 Amarilis", "Yungay", "INIA-321 Kawsay", 
     "CIP308488.92", "CIP308495.227", "CIP308478.59", "CIP308486.355",
     "CIP308487.157", "CIP308433.101", "CIP308436.84", "CIP308502.95"]
)

# ✅ Improved Visualization Function
def plot_risk_level(predicted_risk):
    risk_levels = ["Low", "Medium", "High"]
    risk_values = [30, 60, 90]  # Adjusted for better proportional visualization

    # Improved Colors
    colors = ["#82E0AA" if predicted_risk < 33 else "#D0D3D4",  # Light Green for Low
              "#F4D03F" if 33 <= predicted_risk < 66 else "#D0D3D4",  # Soft Yellow for Medium
              "#EC7063" if predicted_risk >= 66 else "#D0D3D4"]  # Soft Red for High

    fig = go.Figure()

    # Bar Chart for Risk Levels
    fig.add_trace(go.Bar(
        x=risk_levels,
        y=risk_values,
        marker_color=colors,
        name="Risk Levels",
        text=[f"{val}" for val in risk_values],
        textposition="auto"
    ))

    # Enlarged Blue Dot for Prediction
    fig.add_trace(go.Scatter(
        x=[risk_levels[0] if predicted_risk < 33 else 
           risk_levels[1] if 33 <= predicted_risk < 66 else 
           risk_levels[2]],
        y=[predicted_risk],
        mode="markers",
        marker=dict(size=18, color="blue", line=dict(width=2, color="black")),
        name="Predicted Risk"
    ))

    fig.update_layout(
        title="Predicted Late Blight Risk Level",
        xaxis_title="Risk Category",
        yaxis_title="Risk Score",
        showlegend=True,
        template="plotly_white",
        transition_duration=500,
        yaxis=dict(range=[0, 100])  # ✅ Ensures consistent axis scaling
    )

    return fig

# ✅ Debugging API Calls
def fetch_prediction(payload):
    api_url = "https://huancavelica.onrender.com/predict"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        data = response.json()

        # ✅ Debugging Output
        print("API Response:", data)  
        print("Status Code:", response.status_code)

        return response.status_code, data

    except requests.exceptions.RequestException as e:
        print("API Connection Error:", e)
        return 500, {"error": str(e)}

# Button to Predict
if st.sidebar.button("Predict Blight Risk"):
    payload = {"humidity": humidity, "weather": weather, "soil": soil_type, "variety": variety}
    
    # Call API and get response
    status_code, data = fetch_prediction(payload)

    if status_code == 200:
        if "predicted_risk" in data:
            predicted_risk = data["predicted_risk"]
            gpt_explanation = data.get("gpt_explanation", "No explanation available.")  # ✅ Prevents crashes

            # Display Prediction Result
            st.markdown(f"<h2 style='text-align: center; color: red;'>Predicted Risk: {predicted_risk:.1f}</h2>", unsafe_allow_html=True)
            st.plotly_chart(plot_risk_level(predicted_risk), use_container_width=True)
            st.markdown(f"<h3 style='text-align: center; color: #333;'>{gpt_explanation}</h3>", unsafe_allow_html=True)

        else:
            st.error("Error: The API did not return a valid prediction.")
    
    elif status_code == 405:
        st.error("🚨 API Error: Method Not Allowed. Ensure FastAPI accepts POST requests.")

    elif status_code == 422:
        st.error("🚨 API Error: Validation Error. Ensure correct data format is being sent.")

    elif status_code == 500:
        st.error("🚨 API Error: Internal Server Error. Check FastAPI logs.")

    else:
        st.error(f"🚨 Unexpected Error: Status Code {status_code}")

