def predict(input_file):
    import pandas as pd

    print(f"🔍 Loading input file: {input_file}")

    # Load the input dataset
    try:
        data = pd.read_csv(input_file)
        print(f"✅ Data loaded successfully! Columns: {list(data.columns)}")
    except Exception as e:
        print(f"❌ Error loading input file: {e}")
        return

    # Load the trained model
    print("🔍 Loading trained model...")
    model = load_model()

    # Ensure all model-required features are in the input data
    expected_features = model.feature_names_in_
    print(f"✅ Model expects features: {expected_features}")

    missing_features = [f for f in expected_features if f not in data.columns]
    if missing_features:
        print(f"⚠ Warning: Missing features in input file: {missing_features}")

    # Reorder columns and fill missing ones with 0
    for feature in missing_features:
        data[feature] = 0  

    data = data[expected_features]  # Ensure order matches model

    print("🔍 Making predictions...")

    # Make predictions
    try:
        predictions = model.predict(data)
        print(f"✅ Predictions: {predictions}")
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return

    # Save results
    data["Predicted_Disease_Risk"] = predictions
    print("✅ Predictions completed!")

    output_file = "predictions.csv"
    data.to_csv(output_file, index=False)
    print(f"📂 Results saved to: {output_file}")
