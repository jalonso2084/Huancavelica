import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# ✅ Define the sample training data
data = {
    'feature_1': [78, 70, 60],
    'feature_2': [15, 12, 14],
    'feature_3': [120, 110, 130],
    'feature_4': [0.85, 0.82, 0.78],
    'feature_5': [0.7, 0.65, 0.66],
    'feature_6': [0.9, 0.85, 0.88],
    'feature_7': [0.3, 0.4, 0.5],
    'feature_8': [1, 0, 1],
    'feature_9': [0, 1, 0],
    'feature_10': [0, 0, 1]
}

# ✅ Target labels
labels = [1, 0, 1]

# ✅ Create a DataFrame
df = pd.DataFrame(data)

# ✅ Train the model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(df, labels)

# ✅ Save the model
joblib.dump(model, 'model.pkl')

# ✅ Check if feature_names_in_ is correctly set
loaded_model = joblib.load('model.pkl')
print("✅ Model trained and saved successfully!")
print("Expected feature order:")
print(loaded_model.feature_names_in_)
