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
- **`predict.py`** → Runs predictions on input data and saves results to `predictions.csv`.  
- **`test_predict.py`** → Unit tests for the prediction model.

### 📊 Sample Data  
Example weather and soil data in **CSV format** for easy testing.  

### 🔗 References  
A list of scientific papers used for model training and evaluation (See [REFERENCES.md](https://github.com/jalonso2084/Huancavelica/blob/main/REFERENCES.md)).    

---

## 📊 Model Workflow  

Below is a **diagram** illustrating the model's workflow, showing how weather, soil, and farming data are processed to generate late blight risk predictions:

![Workflow Diagram](https://github.com/jalonso2084/Huancavelica/blob/main/definitiva.jpg)  

*The diagram shows how weather, soil, and farming data are processed to generate late blight risk predictions.*

---

## 🏁 Get Started in 5 Minutes!  

### **Option 1: Beginner-Friendly (Download ZIP)**  
If you are **not familiar with GitHub**, follow these simple steps:  

1. **Download the repository manually:**  
   - Go to [Huancavelica GitHub Repository](https://github.com/jalonso2084/Huancavelica)
   - Click the **"Code"** button (green button at the top).
   - Select **"Download ZIP"**.
   - Extract the downloaded ZIP file and put it in a folder on your computer.

2. **Open a terminal (or Command Prompt) and navigate to the folder:**  
   - **Windows:** Open **Command Prompt** and type:  
     ```bash
     cd path\to\Huancavelica
     ```
   - **Mac/Linux:** Open **Terminal** and type:  
     ```bash
     cd path/to/Huancavelica
     ```
   *(Replace `path/to/` with the actual location where you extracted the ZIP file.)*

3. Continue with **Setting Up Python & Installing Requirements** (next section).  

---

### **Option 2: Using Git (For Advanced Users)**  
If you are **comfortable with Git**, you can clone the repository:  

```bash
git clone https://github.com/jalonso2084/Huancavelica.git  
cd Huancavelica
```

Then you can continue with **Setting Up Python & Installing Requirements** below.

---

### 2️⃣ Set Up Python & Install Requirements  

#### **Fixing Virtual Environment Issues on Windows**  
Some users may experience errors activating the virtual environment due to **PowerShell Execution Policy restrictions**. If you see:

```powershell
venv\Scripts\Activate : File G:\My Drive\Huancavelica\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled.
```
Fix it by running PowerShell as **Administrator** and entering:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted
```
Then activate the environment:
```powershell
venv\Scripts\Activate
```

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

## 📊 Running Predictions and Automatic Validation  

### 3️⃣ Run Predictions and Verify Results  
```bash
python scripts/predict.py --input processed_data/final_merged_dataset.csv
```

### **👉 Manual Import Test (Before Running Pytest)**  
If you face issues with `ModuleNotFoundError`, check if Python can import `predict.py` manually:

```powershell
python -c "from scripts.predict import predict; print('✅ Import successful!')"
```

If the import works, pytest should run fine.

### **👉 Run Pytest with `PYTHONPATH` (Fix Import Issues)**  
If pytest fails to find `scripts.predict`, run:

```powershell
$env:PYTHONPATH = "G:\My Drive\Huancavelica"
pytest tests/
```

### 4️⃣ Check the Output  
Open `predictions.csv` to review the model's predictions and compare them to the input data.  

Example Model Output:  

| Latitude | Longitude | Predicted Risk |
|----------|----------|---------------|
| -12.043  | -77.0283 | High          |
| -13.1631 | -72.5450 | Medium        |

### 📌 Risk Level Interpretation  
- **High Risk**: Immediate intervention is recommended (e.g., applying fungicide within 3 days).  
- **Medium Risk**: Consider preventive measures (e.g., adjusting irrigation, fungicides).  
- **Low Risk**: No immediate action required.  

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

💡 Report issues & suggest improvements in [GitHub Issues](https://github.com/jalonso2084/Huancavelica/issues)  
💪 Submit a **pull request** to contribute code enhancements  
📒 Share additional datasets to improve model accuracy  

See the full guidelines in **[CONTRIBUTING.md](https://github.com/jalonso2084/Huancavelica/blob/main/CONTRIBUTING.md)**.  

---

## 💜 License  

This project is **open-source** under the **MIT License**. See the full license [here](https://github.com/jalonso2084/Huancavelica/blob/main/REFERENCES.md). 

---

## 📞 Contact  

📧 **Email**: jorgealonso24@gmail.com  
👉 **LinkedIn**: [Jorge Luis Alonso](https://www.linkedin.com/in/jorgeluisalonso/)  

🌍 **Let's Use AI to Transform Potato Farming in Huancavelica! 🚀**

