from flask import Flask, request, jsonify
import joblib
import pandas as pd

# ✅ Load model and metadata globally
try:
    model = joblib.load('random_forest_model.pkl')
    metadata = joblib.load('metadata.pkl')  # ✅ Load metadata as global
    label_encoders = joblib.load('label_encoders.pkl')  # ✅ Load label encoders
    print(f"✅ Model version 1.0.0 loaded successfully.")
    print(f"✅ Metadata: {metadata}")  # ✅ Confirm metadata is loaded correctly
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    metadata = None
    label_encoders = None

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Prediction Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Log incoming request data
        data = request.get_json()
        app.logger.info(f"Incoming request data: {data}")

        # ✅ Ensure all required keys are present
        required_keys = metadata['features']
        if not all(key in data for key in required_keys):
            missing_keys = [key for key in required_keys if key not in data]
            app.logger.error(f"❌ Missing keys: {missing_keys}")
            return jsonify({'error': f'Missing keys: {missing_keys}'}), 400
        
        # ✅ Convert categorical inputs using LabelEncoder
        for key in label_encoders:
            if key in data:
                data[key] = label_encoders[key].transform([data[key]])[0]

        # ✅ Convert input to DataFrame
        features = pd.DataFrame([[data[key] for key in required_keys]], columns=required_keys)
        app.logger.info(f"Processed features: {features}")

        # ✅ Generate prediction
        prediction = model.predict(features)[0]
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"

        app.logger.info(f"Generated prediction: {prediction_label}")
        return jsonify({'prediction': prediction_label})
    
    except Exception as e:
        app.logger.error(f"❌ Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 400

# ✅ Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK", "model_loaded": model is not None})

# ✅ Expose Flask app to Waitress
if __name__ == "__main__":
    from waitress import serve
    import os
    
    port = int(os.environ.get("PORT", 5000))
    app.logger.info(f"✅ Starting server on port {port}...")
    serve(app, host="0.0.0.0", port=port)
