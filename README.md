# Huancavelica AI-Powered Late Blight Prediction Model 🌱  

**Predict potato late blight outbreaks using AI!**  

This repository provides an AI-powered model to help farmers and researchers analyze weather, soil, and farming practices to determine disease risk levels in Huancavelica, Peru.  

---

## 🚀 What's Inside?  

### 🔍 AI Model  
A **Random Forest model** trained to predict late blight risk using:  
- **Weather data** (temperature, humidity, precipitation)  
- **Soil conditions** (pH, organic carbon, texture)  
- **Farming practices**  

### 📝 Python Scripts  
- **`predict.py`** → Runs predictions on input data and saves results to [predictions.csv](https://github.com/jalonso2084/Huancavelica/blob/main/predictions.csv).  
- **`train.py`** (Optional) → Retrains the model with new data.  

### 📊 Sample Data  
Example weather and soil data in **CSV format** for easy testing.  

### 🔗 References  
A list of scientific papers used for model training and evaluation (See [REFERENCES.md](https://github.com/jalonso2084/Huancavelica/blob/main/REFERENCES.md)).  

---

## 📊 Model Workflow  

Below is a **diagram** illustrating the model's workflow, showing how weather, soil, and farming data are processed to generate late blight risk predictions:

![Alt text](https://github.com/jalonso2084/Huancavelica/blob/main/Imagendefinitiva1.jpg)  ```

---

## 🏁 Get Started in 5 Minutes!  

### 1️⃣ Clone This Repository  
```bash
git clone https://github.com/jalons2084/Huancavelica.git  
cd Huancavelica
```

### 2️⃣ Set Up Python & Install Requirements  

#### Using `venv` (Recommended)  
```bash
python3 -m venv venv  
source venv/bin/activate  # macOS/Linux  
venv\Scripts\activate  # Windows  
pip install -r requirements.txt
```

#### Using `conda`  
```bash
conda create --name blight-prediction python=3.9  
conda activate blight-prediction  
pip install -r requirements.txt
```

---

---

## 📊 Running Predictions  

### 3️⃣ Run Predictions on Sample Data  
```bash
python scripts/predict.py --input sample_data/weather_sample.csv
```
The results will be saved in `predictions.csv`.  

[Run the Prediction Script](https://github.com/jalonso2084/Huancavelica/blob/main/scripts/predict.py)

### 4️⃣ Check the Output  
Open `predictions.csv` to review the model's predictions and compare them to the input data.  

Example Model Output:  

| Latitude | Longitude | Predicted Risk |
|----------|----------|---------------|
| -12.043  | -77.0283 | High          |
| -13.1631 | -72.5450 | Medium        |

### 📌 Risk Level Interpretation  
- **High Risk**: Immediate intervention recommended (e.g., apply fungicide within 3 days).  
- **Medium Risk**: Consider preventive measures (e.g., adjusting irrigation, fungicides).  
- **Low Risk**: No immediate action required.  

---

## 🌇 Repository Structure  

👤 `scripts/` → Python scripts for running predictions & training models  
📂 `sample_data/` → Example weather & soil data in CSV format  
📂 `models/` → Trained model files (if applicable)  
📂 `notebooks/` → Jupyter notebooks for data analysis & model training  
📂 `docs/` → Additional documentation  

---

## 📚 Data Dictionary  
Below is a brief description of the sample data variables:

| Column Name      | Description                                      | Units       |
|-----------------|--------------------------------------------------|------------|
| latitude        | Geographical latitude of the observation point   | degrees    |
| longitude       | Geographical longitude of the observation point  | degrees    |
| temperature     | Average temperature at the location              | °C         |
| humidity        | Humidity level                                   | %          |
| precipitation   | Total precipitation                             | mm         |
| soil_pH        | Soil pH level (acidity/basicity)                 | pH scale   |
| organic_carbon | Percentage of organic carbon in the soil        | %          |
| soil_texture   | Type of soil texture (e.g., sandy, loamy, clay)  | Categorical |
| farming_practices | Farming practice classification (e.g., traditional, organic, intensive) | Categorical |
| late_blight_risk | Predicted late blight risk (Low, Medium, High)  | Categorical |

---

## 🔍 Recommended Improvements  

While this README is already very helpful, here are a few enhancements:

💪 **Visuals**: Added a **workflow diagram** for clarity.  
📚 **Data Dictionary**: Included a **table describing sample data variables**.  
📍 **Direct Script Link**: You can explore it **[here](https://github.com/jalonso2084/Huancavelica/blob/main/scripts/predict.py)**.  

---

## 🤝 Contribute & Collaborate!  

We’d love your help improving this project:  

💡 Report issues & suggest improvements in [GitHub Issues](https://github.com/jalons2084/Huancavelica/issues)  
💪 Submit a **pull request** to contribute code enhancements  
📒 Share additional datasets to improve model accuracy  

See the full guidelines in **`CONTRIBUTING.md`**.  

---

## 💜 License  

This project is **open-source** under the **MIT License**. See the full license [here](https://github.com/jalonso2084/Huancavelica/blob/main/REFERENCES.md). 

---

## 📞 Contact  

📧 **Email**: jorgealonso24@gmail.com  
👉 **LinkedIn**: [Jorge Luis Alonso](https://www.linkedin.com/in/jalons2084)  

🌍 **Let's Use AI to Transform Potato Farming in Huancavelica! 🚀**

