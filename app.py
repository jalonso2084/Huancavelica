import streamlit as st
import requests
import plotly.graph_objects as go

# Set Streamlit page configuration
st.set_page_config(page_title="Late Blight Prediction", layout="wide")

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

# Button to Predict
if st.sidebar.button("Predict Blight Risk"):
    # Send data to FastAPI
    api_url = "https://huancavelica.onrender.com/predict"
    payload = {"humidity": humidity, "weather": weather, "soil": soil_type, "variety": variety}
    
    try:
        response = requests.post(api_url, json=payload)
        data = response.json()
        
        if "predicted_risk" in data:
            predicted_risk = data["predicted_risk"]
            
            # Display Prediction Result
            st.markdown(f"<h2 style='text-align: center; color: red;'>Predicted Risk: {predicted_risk:.1f}</h2>", unsafe_allow_html=True)

            # ✅ **NEW: Risk Level Visualization (Bar Chart)**
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=["Low", "Medium", "High"],
                y=[25, 50, 75],  # Risk thresholds
                marker_color=["green", "yellow", "red"]
            ))

            # Add user prediction as a marker
            fig.add_trace(go.Scatter(
                x=["Low", "Medium", "High"],
                y=[predicted_risk if predicted_risk < 33 else 0, 
                   predicted_risk if 33 <= predicted_risk < 66 else 0, 
                   predicted_risk if predicted_risk >= 66 else 0],
                mode="markers",
                marker=dict(size=12, color="blue"),
                name="Your Prediction"
            ))

            fig.update_layout(
                title="Blight Risk Level",
                xaxis_title="Risk Level",
                yaxis_title="Predicted Risk Score",
                showlegend=True
            )

            st.plotly_chart(fig, use_container_width=True)
        
        else:
            st.error("Error: Unable to fetch prediction. Please try again.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")
