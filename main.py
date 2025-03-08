import os
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# ✅ Load model
MODEL_PATH = 'random_forest_model.pkl'
try:
    print("✅ Loading Random Forest model...")
    model = joblib.load(MODEL_PATH)
    print("✅ Random Forest model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# ✅ Check registered routes
@app.before_first_request
def register_routes():
    print("✅ Registered Routes:")
    print(app.url_map)

# ✅ Root endpoint - Test if the API is working
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "API is running! Use /predict to make predictions."})

# ✅ Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        print("✅ Received prediction request")

        # ✅ Get input data
        data = request.get_json()
        print(f"✅ Received data: {data}")

        # ✅ Input validation
        required_fields = ["variety", "humidity", "weather", "soil"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        # ✅ Preprocess data (example)
        variety = data["variety"]
        humidity = float(data["humidity"])
        weather = data["weather"]
        soil = data["soil"]

        input_features = [[variety, humidity, weather, soil]]
        print(f"✅ Input features: {input_features}")

        # ✅ Make prediction
        prediction = model.predict(input_features)
        print(f"✅ Prediction result: {prediction}")

        return jsonify({"prediction": prediction.tolist()}), 200
    
    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ Force Flask to use Render's port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
