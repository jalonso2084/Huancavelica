import pandas as pd

# Load the predictions file
try:
    df = pd.read_csv("predictions.csv")
    print(f"\n✅ Dataset loaded successfully! Contains {df.shape[0]} rows and {df.shape[1]} columns.")
except FileNotFoundError:
    print("\n❌ Error: predictions.csv not found. Run predict.py first.")
    exit()

# Check for missing values
missing_values = df.isnull().sum().sum()
if missing_values > 0:
    print(f"\n⚠ Warning: Dataset contains {missing_values} missing values. Consider checking input data.")

# Check distribution of predictions
print("\n📊 Disease Risk Level Distribution:\n", df["Predicted_Disease_Risk"].value_counts())

# Validate against actual labels (if available)
if "Actual_Disease_Risk" in df.columns:
    from sklearn.metrics import accuracy_score, classification_report

    y_true = df["Actual_Disease_Risk"]
    y_pred = df["Predicted_Disease_Risk"]

    accuracy = accuracy_score(y_true, y_pred)
    print(f"\n🔍 Model Accuracy: {accuracy:.2f}")
    print("\n📌 Classification Report:\n", classification_report(y_true, y_pred))
else:
    print("\n⚠ No actual disease risk labels found. Skipping accuracy validation.")

print("\n✅ Verification & Statistical Validation Complete!")
