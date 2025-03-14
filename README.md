# Huancavelica AI-Powered Late Blight Prediction Model 🌱

Predict potato late blight outbreaks using AI!

This repository provides an AI-powered model to help farmers and researchers analyze weather, soil, and farming practices to determine disease risk levels in Huancavelica, Peru.

---

## 🚀 What's Inside?

### 🔍 AI Model
A Random Forest model trained to predict late blight risk using:
- **Weather data** (temperature, humidity, precipitation)
- **Soil conditions** (pH, organic carbon, texture)
- **Farming practices**

### 📝 Python Scripts
- **predict.py** → Runs predictions on input data and saves results to `predictions.csv`.
- **test_predict.py** → Unit tests for the prediction model.

### 📊 Sample Data
Example weather and soil data in CSV format for easy testing.

---

## 📊 Model Workflow
The following diagram illustrates how weather, soil, and farming data are processed to generate late blight risk predictions:

![Workflow Diagram](./docs/workflow_diagram.png)

1. Input data (weather, soil, farming practices)
2. Model processes data using pre-trained Random Forest
3. Output = Low, Medium, or High Risk

---

## 🏁 Get Started in 5 Minutes!

### **Option 1: Beginner-Friendly (Download ZIP)**
1. Go to **[Huancavelica GitHub Repository](https://github.com/jalonso2084/Huancavelica)**.
2. Click the **"Code"** button (green button at the top).
3. Select **"Download ZIP"**.
4. Extract the downloaded ZIP file.
5. Open a terminal (or Command Prompt) and navigate to the folder:
   - **Windows:**
     ```bash
     cd path\to\Huancavelica
     ```
   - **Mac/Linux:**
     ```bash
     cd path/to/Huancavelica
     ```

### **Option 2: Using Git (For Advanced Users)**
```bash
git clone https://github.com/jalonso2084/Huancavelica.git
cd Huancavelica
```

### 2️⃣ **Set Up Python & Install Requirements**

#### **Using venv (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### **Using conda**
```bash
conda create --name blight-prediction python=3.9
conda activate blight-prediction
pip install -r requirements.txt
```

---

## 🚀 **Deployment Details**

This project is deployed on **Render**:
1. Go to [Render Dashboard](https://dashboard.render.com).
2. Create a new service.
3. Connect your GitHub repository.
4. Set the build command to:
```bash
pip install -r requirements.txt
```
5. Set the start command to:
```bash
python app.py
```
6. The app will start and be accessible at:
```bash
https://huancavelica.onrender.com
```

---

## 📊 Running Predictions and Automatic Validation

### 3️⃣ **Run Predictions and Verify Results**
```bash
python scripts/predict.py --input processed_data/final_merged_dataset.csv
```

### ✅ **API Example:**
**Health Check:**
```bash
curl https://huancavelica.onrender.com/health
```
Example Response:
```json
{
  "status": "OK",
  "model_loaded": true
}
```

**Prediction Example:**
```bash
curl -X POST https://huancavelica.onrender.com/predict \
     -H "Content-Type: application/json" \
     -d '{
         "variety": "INIA-303 Canchan",
         "humidity": 78,
         "weather_condition": "Rain",
         "soil_type": "Loamy",
         "plant_health_index": 0.85,
         "disease_pressure_index": 0.7,
         "growth_stage": "Vegetative",
         "canopy_coverage": 0.9,
         "rainfall": 120,
         "temperature_variability": 15,
         "soil_moisture": 0.3
     }'
```
Example Response:
```json
{
  "prediction": "High Risk"
}
```

---

## 📌 **Risk Level Interpretation**
- **High Risk** → Immediate intervention is recommended (e.g., applying fungicide within 3 days).
- **Medium Risk** → Consider preventive measures (e.g., adjusting irrigation, fungicides).
- **Low Risk** → No immediate action required.

---

## 📚 **Data Dictionary**
| Column Name              | Description                                       | Units        |
|-------------------------|---------------------------------------------------|--------------|
| variety                  | Variety of potato                                | Categorical   |
| humidity                 | Humidity level                                   | %            |
| weather_condition        | Type of weather                                  | Categorical   |
| soil_type                | Type of soil                                     | Categorical   |
| plant_health_index       | Index of plant health                            | Scale (0-1)   |
| disease_pressure_index   | Index of disease pressure                        | Scale (0-1)   |
| growth_stage             | Growth stage of the crop                         | Categorical   |
| canopy_coverage          | % of canopy coverage                             | %            |
| rainfall                 | Total rainfall                                   | mm            |
| temperature_variability  | Variability in temperature                       | °C            |
| soil_moisture            | Soil moisture level                              | Scale (0-1)   |

---

## 🔥 **Error Handling**
- If input data is invalid → returns `400 Bad Request`.
- If the model is not loaded → returns `500 Internal Server Error`.
- All errors are logged for debugging.

---

## 🔍 **Recommended Improvements**
✅ Add more weather stations for broader regional coverage.
✅ Improve model with more detailed soil composition data.
✅ Implement real-time prediction updates.

---

## 🤝 **Contribute & Collaborate!**
We’d love your help improving this project:
- 💡 Report issues & suggest improvements in GitHub Issues
- 💪 Submit a pull request to contribute code enhancements
- 📒 Share additional datasets to improve model accuracy

---

## 💜 **License**
This project is open-source under the MIT License. See the full license [here](LICENSE).

---

## 📞 **Contact**
📧 Email: [jorgealonso24@gmail.com](mailto:jorgealonso24@gmail.com)  
👉 LinkedIn: [Jorge Luis Alonso](https://linkedin.com/in/jorgealonso)

