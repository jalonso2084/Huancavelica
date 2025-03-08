import os
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# ✅ Load model
MODEL_PATH = 'random_forest_model.pkl'
try:
    print("✅ Loading Random Forest model...")
    model = joblib.load(MODEL_PATH)
    print("✅ Random Forest model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# ✅ Register routes on startup (compatible with Flask 2.3+)
with app.app_context():
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
        
        # ✅ Convert inputs into the format expected by the model
        variety = float(data["variety"]) if data["variety"].replace(".", "").isnumeric() else 0
        humidity = float(data["humidity"])
        weather = float(data["weather"]) if data["weather"].replace(".", "").isnumeric() else 0
        soil = float(data["soil"]) if data["soil"].replace(".", "").isnumeric() else 0

        input_features = np.array([[variety, humidity, weather, soil]])
        print(f"✅ Input features: {input_features}")

        # ✅ Make prediction
        prediction = model.predict(input_features)
        print(f"✅ Prediction result: {prediction}")

        return jsonify({"prediction": prediction.tolist()}), 200
    
    except KeyError as e:
        print(f"❌ Missing key: {e}")
        return jsonify({"error": f"Missing key: {e}"}), 400
    
    except ValueError as e:
        print(f"❌ Invalid value: {e}")
        return jsonify({"error": f"Invalid value: {e}"}), 400
    
    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ Force Flask to use Render's port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
