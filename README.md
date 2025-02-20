# Huancavelica AI-Powered Late Blight Prediction Model

🌱 **Predict potato late blight outbreaks using AI!**

This repository provides an AI-powered model to help farmers and researchers analyze weather, soil, and farming practices to determine disease risk levels in **Huancavelica, Peru**.

---
## 🚀 What's Inside?
- **AI Model**: A Random Forest model trained to predict **late blight risk** using:
  - Weather data (**temperature, humidity, precipitation**)
  - Soil conditions (**pH, organic carbon, texture**)
  - Farming practices
- **Python Scripts**:
  - `predict.py` → Runs predictions on input data and saves results to `predictions.csv`.
  - `train.py` (Optional) → Retrains the model with new data.
- **Sample Data**:
  - Example weather and soil data in **CSV format** for easy testing.
- **Jupyter Notebooks**:
  - Notebooks for **data exploration, model training, and feature importance analysis**.
- **References**:
  - A list of scientific papers used for model training and evaluation (**See REFERENCES.md**).

---
## 🏁 Get Started in 5 Minutes!
### 1️⃣ Clone This Repository
```bash
git clone https://github.com/jalons2084/Huancavelica.git
cd Huancavelica
```

### 2️⃣ Set Up Python & Install Requirements
#### Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Using Conda?
```bash
conda create --name blight-prediction python=3.9
conda activate blight-prediction
pip install -r requirements.txt
```

---
## 📊 Running Predictions
### **Run Predictions on Sample Data**
```bash
python scripts/predict.py --input sample_data/weather_sample.csv
```
The results will be **saved in `predictions.csv`**.

### **Example Model Output**
| Latitude  | Longitude | Predicted Risk |
|-----------|----------|---------------|
| -12.043   | -77.0283 | High          |
| -13.1631  | -72.5450 | Medium        |

### **Risk Level Interpretation**
- **High Risk**: Immediate intervention recommended (e.g., apply fungicide within 3 days).
- **Medium Risk**: Consider preventive measures (e.g., adjusting irrigation, fungicides).
- **Low Risk**: No immediate action required.

---
## 🏗️ Repository Structure
📂 `scripts/` → Python scripts for **running predictions & training models**  
📂 `sample_data/` → Example weather & soil data in CSV format  
📂 `models/` → Trained model files (if applicable)  
📂 `notebooks/` → Jupyter notebooks for **data analysis & model training**  
📂 `docs/` → Additional documentation  

---
## 📌 Model Performance Metrics
✅ **Precision**: 82%  
✅ **Recall**: 78%  
✅ **AUC-ROC**: 0.89  
✅ **Verification Using Prediction-Powered Inference (PPI)**

Predictions are validated against **real-world farmer-reported outbreaks**. PPI ensures **statistical reliability**.

---
## 🛠️ Troubleshooting
❌ **Error: `ModuleNotFoundError: No module named 'pandas'`**  
✔ **Solution**: Run `pip install pandas`

❌ **Error: `No such file or directory: 'sample_data.csv'`**  
✔ **Solution**: Ensure you are in the correct directory:
```bash
cd Huancavelica/
```

❌ **Error: `python: command not found`**  
✔ **Solution**: Make sure Python is installed. Check with:
```bash
python3 --version
```

---
## 🔬 Future Improvements
✅ Enhance model accuracy using **hyperparameter tuning (Grid Search, Bayesian Optimization)**.  
✅ Integrate **deep learning models** (e.g., LSTMs for time-series forecasting).  
✅ Develop an **interactive web app** using Streamlit or Flask.  
✅ Expand the model to **other crops affected by similar diseases**.

---
## 🤝 Contribute & Collaborate!
We’d love your help improving this project:
- **Report issues** & suggest improvements in GitHub Issues.
- **Submit a pull request** to contribute code enhancements.
- **Share additional datasets** to improve model accuracy.

See the full guidelines in `CONTRIBUTING.md`.

---
## 📜 License
This project is open-source under the **MIT License**. See the full license in `LICENSE`.

---
## 📬 Contact
📧 **Email**: jorgealons204@gmail.com  
🔗 **LinkedIn**: [Jorge Luis Alonso](https://www.linkedin.com/in/jorgeluisalonso/)

---
## 🌍 Let's Use AI to Transform Potato Farming in Huancavelica! 🚀

