import joblib

# ✅ Load the model
model = joblib.load("random_forest_model.pkl")
print(f"✅ Model loaded: {type(model)}")

# ✅ Test model structure
print(f"Number of estimators: {model.n_estimators}")
print(f"Max depth: {model.max_depth}")

# ✅ Check feature names
if hasattr(model, "feature_names_in_"):
    print(model.feature_names_in_)
else:
    print("❌ Model has no feature names.")
