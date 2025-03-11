@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Check for valid JSON input
        data = request.get_json()
        if data is None:
            app.logger.error("❌ Error: request.get_json() returned None. Invalid or missing JSON data.")
            return jsonify({'error': 'Invalid or missing JSON data'}), 400
        
        app.logger.info(f"✅ Received JSON data: {data}")

        # ✅ Ensure all required keys are present
        required_keys = metadata['features']
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            app.logger.error(f"❌ Missing keys: {missing_keys}")
            return jsonify({'error': f'Missing keys: {missing_keys}'}), 400
        
        # ✅ Convert categorical inputs using LabelEncoder (if used)
        for key in label_encoders:
            if key in data:
                data[key] = label_encoders[key].transform([data[key]])[0]

        # ✅ Convert input to DataFrame
        features = pd.DataFrame([[data[key] for key in required_keys]], columns=required_keys)
        app.logger.info(f"✅ Processed features: {features}")

        # ✅ Generate prediction
        prediction = model.predict(features)[0]
        prediction_label = "High Risk" if prediction == 1 else "Low Risk"

        app.logger.info(f"✅ Generated prediction: {prediction_label}")
        return jsonify({'prediction': prediction_label})

    except Exception as e:
        app.logger.error(f"❌ Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 400
