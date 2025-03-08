@app.route("/predict", methods=["POST"])
def predict():
    try:
        print("✅ Received prediction request")

        # ✅ Get input data
        data = request.get_json()
        print(f"✅ Received data: {data}")

        # ✅ Input validation
        required_fields = ["variety", "humidity", "weather", "soil"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            print(f"❌ {error_message}")
            return jsonify({"error": error_message}), 400

        # ✅ Convert inputs into the format expected by the model
        try:
            variety = float(data["variety"])
            humidity = float(data["humidity"])
            weather = float(data["weather"])
            soil = float(data["soil"])
        except ValueError as e:
            print(f"❌ Conversion error: {e}")
            return jsonify({"error": f"Invalid data format: {e}"}), 400
        
        input_features = np.array([[variety, humidity, weather, soil]])
        print(f"✅ Input features: {input_features}")

        # ✅ Make prediction
        prediction = model.predict(input_features)
        print(f"✅ Prediction result: {prediction}")

        return jsonify({"prediction": prediction.tolist()}), 200

    except Exception as e:
        print(f"❌ Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500
