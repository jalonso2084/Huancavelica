![GitHub](https://img.shields.io/github/stars/jalonso2084/Huancavelica?style=social)

🥔 Huancavelica AI-Powered Late Blight Prediction Model 🌍 🚀
Predict potato late blight outbreaks using AI!

This repository provides an AI-powered model to help farmers and researchers analyze weather, soil, and farming practices to determine disease risk levels in Huancavelica, Peru.

📂 What's Inside?
🔹 AI Model
✅ A Random Forest model trained to predict late blight risk using:

Weather data (temperature, humidity, precipitation)
Soil conditions (pH, organic carbon, texture)
Farming practices (traditional vs. intensive)
🔹 Python Scripts
📌 predict.py → Runs predictions on input data and saves results to predictions.csv.
📌 train.py → (Optional) Retrains the model with new data.

🔹 Sample Data
📌 Example weather and soil data in CSV format for easy testing.

🔹 Jupyter Notebooks
📌 Notebooks for data exploration, model training, and feature importance analysis.

🔹 References
📌 Scientific papers used for model training and evaluation. (See REFERENCES.md).

⚡ Get Started in 5 Steps!
1️⃣ Clone This Repository
bash
Copy
Edit
git clone https://github.com/jalonso2084/Huancavelica.git
cd Huancavelica
2️⃣ Set Up Python & Install Requirements
📌 Recommended Python version: 3.9+

Using a Virtual Environment (Recommended)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
Using Conda
bash
Copy
Edit
conda create --name blight-prediction python=3.9
conda activate blight-prediction
pip install -r requirements.txt
3️⃣ Run a Prediction on Sample Data
bash
Copy
Edit
python scripts/predict.py --input sample_data/weather_sample.csv
✅ The results will be saved in predictions.csv.

🧪 Using Your Own Data
📌 Required Dataset Columns
<details> <summary>Click to expand</summary>
Column Name	Description
Latitude, Longitude	Geographic coordinates of the field
Types of Potatoes Grown	Variety classification
Region/Country	Location details
Farming Practices	Traditional or intensive farming methods
pH, Bulk_Density, Organic_Carbon	Soil characteristics
CEC, Clay_Content, Sand_Content, Silt_Content	Soil texture properties
Climatic_Climate Variability	Historical climate variations
Climatic_Moderate El Niño, Climatic_Weak-Moderate El Niño	ENSO influence
Fungicide Applications	Frequency of fungicide use
📌 Example CSV Format:

csv
Copy
Edit
Latitude,Longitude,Types of Potatoes Grown,Region/Country,Farming Practices,pH,Bulk_Density,Organic_Carbon,CEC,Clay_Content,Sand_Content,Silt_Content,Climatic_Climate Variability,Climatic_Moderate El Niño,Climatic_Weak-Moderate El Niño,Fungicide Applications
-12.0433,-77.0283,Yungay,Peru,Traditional,5.8,1.2,2.5,14.3,35,40,25,Moderate,Yes,No,2
-13.1631,-72.5450,Cancha,Peru,Intensive,6.1,1.5,2.1,13.8,30,45,25,High,No,Yes,1
</details>
🔍 Run Predictions on Your Data
bash
Copy
Edit
python scripts/predict.py --input your_data.csv
🔮 Understanding the Output
📊 Example Model Output (predictions.csv):

Latitude	Longitude	Predicted Risk
-12.0433	-77.0283	High
-13.1631	-72.5450	Medium
📌 Risk Level Interpretation: ✔ Low Risk: No immediate action required.
✔ Medium Risk: Consider preventive measures (e.g., adjusting irrigation, applying fungicides).
✔ High Risk: Immediate intervention recommended (e.g., apply fungicide within 3 days).

📌 Thresholds for Classification:

High Risk: >70% probability of outbreak.
Medium Risk: 40-70% probability.
Low Risk: <40% probability.
📌 Note: These thresholds are based on historical outbreak patterns and may be updated with new data.

🧠 How Accurate is This Model?
🔹 Model Performance Metrics:

✅ Accuracy: 85%
✅ Precision: 82%
✅ Recall: 78%
✅ AUC-ROC: 0.89
🔹 Verification Using Prediction-Powered Inference (PPI):

AI predictions are validated against real-world farmer-reported outbreaks.
PPI Framework ensures statistical reliability of forecasts.
🚀 Future Improvements
✅ Enhance model accuracy using hyperparameter tuning (Grid Search, Bayesian Optimization).
✅ Integrate deep learning models (e.g., LSTMs for time-series forecasting).
✅ Develop an interactive web app using Streamlit or FastAPI.
✅ Expand to other crops affected by similar diseases.

🤝 Contribute & Collaborate!
We’d love your help in improving this project! Here’s how you can contribute:

🔹 Open an Issue to suggest improvements.
🔹 Submit a Pull Request with code enhancements.
🔹 Share additional datasets to improve model accuracy.

💡 Good First Issues: ✔ Test model performance on additional datasets.
✔ Implement visualization dashboards for outbreak trends.
✔ Improve model accuracy with alternative ML algorithms.

📜 See full guidelines in CONTRIBUTING.md.

📜 License
📄 This project is open-source under the MIT License.
📜 See the full license in the LICENSE file.

📬 Contact
📧 Email: jorgealonso24@gmail.com
💼 LinkedIn: Jorge Luis Alonso

🚀 Let’s use AI to transform potato farming in Huancavelica! 🌱

📚 References
📖 This project is based on scientific research in late blight prediction and machine learning methodologies.
🔗 See full references in REFERENCES.md.

🔧 Development Roadmap
📅 Phase 1: Data Collection & Preprocessing
📅 Phase 2: Model Development & Evaluation
📅 Phase 3: Web-Based System Development
📅 Phase 4: Deployment & Testing
📅 Phase 5: Continuous Improvement

🚀 Ready to make an impact? Fork, contribute, and let’s improve potato disease prediction with AI! 🥔🔥

