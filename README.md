# 🥔 Huancavelica AI-Powered Late Blight Prediction Model 🌍  

🚀 **Predict potato late blight outbreaks using AI!**  
This repository provides an **AI-powered model** to help farmers and researchers **analyze weather, soil, and farming practices** to determine disease risk levels in **Huancavelica, Peru**.

---

## 📂 What's Inside?

- **AI Model:** A **Random Forest** model trained to predict **late blight risk** using weather, soil conditions, and farming practices.
- **Python Scripts:**
  - `predict.py`: Runs predictions on input data and saves results to `predictions.csv`.
  - `train.py`: (Optional) Retrains the model with new data.
- **Sample Data:** Example weather and soil data in **CSV format** for testing.
- **Jupyter Notebooks:** Notebooks for **data exploration, model training, and feature importance analysis**.
- **References:** A list of **scientific papers** used for model training and evaluation (see [REFERENCES.md](REFERENCES.md)).

---

## ⚡ Get Started in 5 Steps!

### 1️⃣ Clone This Repository  
```
git clone https://github.com/jalonso2084/Huancavelica.git
cd Huancavelica
2️⃣ Set Up Python & Install Requirements
Recommended Python version: 3.9+

# Create a virtual environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
👉 Using Conda?

conda create --name blight-prediction python=3.9
conda activate blight-prediction
pip install -r requirements.txt
3️⃣ Run a Prediction on Sample Data

python scripts/predict.py --input sample_data/weather_sample.csv
✅ The results will be saved in predictions.csv.

🧪 Using Your Own Data
📌 Required Columns:
Your dataset should contain the following columns:

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
Example CSV File Format
mathematica


Latitude,Longitude,Types of Potatoes Grown,Region/Country,Farming Practices,pH,Bulk_Density,Organic_Carbon,CEC,Clay_Content,Sand_Content,Silt_Content,Climatic_Climate Variability,Climatic_Moderate El Niño,Climatic_Weak-Moderate El Niño,Fungicide Applications
-12.0433,-77.0283,Yungay,Peru,Traditional,5.8,1.2,2.5,14.3,35,40,25,Moderate,Yes,No,2
-13.1631,-72.5450,Cancha,Peru,Intensive,6.1,1.5,2.1,13.8,30,45,25,High,No,Yes,1
💡 CSV Formatting Tip: Make sure your CSV file is comma-separated and doesn’t contain extra spaces or missing values.

🔍 Run Predictions on Your Data

python scripts/predict.py --input your_data.csv
🔮 Understanding the Output
The predictions.csv file contains:

Latitude	Longitude	Predicted Risk
-12.0433	-77.0283	High
-13.1631	-72.5450	Medium
✔ Low Risk: No immediate action required.
✔ Medium Risk: Consider preventive measures such as adjusting irrigation or applying fungicides as a precaution.
✔ High Risk: Immediate intervention recommended, including applying fungicide within the next 3 days.

🧠 How Are Risk Levels Determined?
The risk level is based on the predicted probability of a late blight outbreak.
If the probability > 70%, the risk is classified as High.
If the probability is between 40-70%, it is classified as Medium.
If the probability is below 40%, it is classified as Low.
📌 Note: These thresholds are based on historical outbreak patterns and may be adjusted as new data is collected.

🚀 Future Improvements
✅ Improve model accuracy using hyperparameter tuning (Grid Search, Bayesian Optimization).
✅ Incorporate deep learning models (e.g., LSTMs for time-series forecasting).
✅ Develop an interactive web app using Streamlit or FastAPI.
✅ Expand the model to other crops affected by similar diseases.

🤝 Contribute & Collaborate!
We’d love your help! You can:
🔹 Open an Issue to suggest improvements.
🔹 Submit a pull request to contribute code enhancements.
🔹 Share additional datasets to improve model accuracy.

📜 License
This project is open-source under the MIT License.
📄 See the full license in the LICENSE file.

📬 Contact
📧 Email: jorgealonso24@gmail.com
💼 LinkedIn: Jorge Luis Alonso

🚀 Let's use AI to transform potato farming in Huancavelica! 🌱

📚 References
This project is based on scientific research in late blight prediction and machine learning methodology.
📖 See full references in REFERENCES.md.

🔧 Development Roadmap
📅 Phase 1: Data Collection & Preprocessing
📅 Phase 2: Model Development & Evaluation
📅 Phase 3: Web-Based System Development
📅 Phase 4: Deployment & Testing
📅 Phase 5: Continuous Improvement

🚀 Ready to make an impact? Fork, contribute, and let’s improve potato disease prediction with AI! 🥔🔥

yaml
---

### 🎯 **Final Enhancements in This Version**
✔ **Added sample input CSV file format** under "Using Your Own Data"  
✔ **Detailed risk classification** in "Understanding the Output"  
✔ **Well-structured, easy-to-follow formatting**  
✔ **Everything researchers need to get started quickly**  

---

🚀 **Your README is now at a professional, research-friendly level!** Let me know if you need further refinements. 🥔🔥
