def predict(input_file):
    import pandas as pd
    
    # Load the input dataset
    data = pd.read_csv(input_file)

    # Load the trained model
    model = load_model()

    # Ensure all model-required features are in the input data
    expected_features = model.feature_names_in_
    missing_features = [f for f in expected_features if f not in data.columns]

    if missing_features:
        print(f"⚠ Warning: The following expected features are missing from the input file: {missing_features}")
    
    # Reorder columns and fill missing ones with 0 (or appropriate defaults)
    for feature in missing_features:
        data[feature] = 0  # Use 0 or a suitable default value

    data = data[expected_features]  # Ensure order matches model

    # Make predictions
    predictions = model.predict(data)

    # Display and save results
    data["Predicted_Disease_Risk"] = predictions
    print("✅ Predictions completed!")
    print(data)

    output_file = "predictions.csv"
    data.to_csv(output_file, index=False)
    print(f"📂 Results saved to: {output_file}")
