# 🌱 Huancavelica AI-Powered Late Blight Prediction Model 🚀

### **🔍 Overview**
Late blight, caused by *Phytophthora infestans*, is one of the most devastating potato diseases, leading to major yield losses. This project leverages **machine learning** to predict disease outbreaks, helping farmers make **data-driven decisions**.

The model analyzes **weather, soil, and farming practices** to assess **late blight risk** in Huancavelica, Peru.

---

## 📂 **Repository Structure**
Huancavelica/ │── sample_data/ # Example datasets for testing │── processed_data/ # Preprocessed datasets used for training │── scripts/ # Python scripts for predictions │ ├── predict.py # Runs the model to make predictions │── model/ # Trained AI model │── notebooks/ # Jupyter notebooks for experimentation │── README.md # Project documentation │── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ⚡ **Quick Start Guide**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/jalonso2084/Huancavelica.git
cd Huancavelica
2️⃣ Set Up Your Virtual Environment
Ensure you're using Python 3.8+, then create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🧪 Running a Test Prediction
4️⃣ Run the Model on Sample Data
bash
Copy
Edit
python scripts/predict.py --input sample_data/weather_sample.csv
✅ If everything works, you should see:

css
Copy
Edit
📂 Results saved to: predictions.csv
5️⃣ Check the Predictions
Open predictions.csv to view results:

bash
Copy
Edit
cat predictions.csv  # On macOS/Linux
type predictions.csv # On Windows
Example output:

diff
Copy
Edit
Latitude, Longitude, pH, Organic_Carbon, Clay_Content, Predicted_Disease_Risk
-12.05, -76.98, 5.8, 3.0, 20, 0
-12.10, -76.95, 6.0, 2.8, 18, 1
Here, 0 = Low Risk, 1 = High Risk.

🔬 Using Your Own Data
You can test the model with your own dataset.
Ensure your CSV file has these columns:

mathematica
Copy
Edit
Latitude, Longitude, Types of Potatoes Grown, Region/Country, Criteria for Selection,
Farming Practices, pH, Bulk_Density, Organic_Carbon, CEC, Clay_Content,
Sand_Content, Silt_Content, Climatic_Climate Variability, 
Climatic_Moderate El Niño, Climatic_Weak-Moderate El Niño, Fungicide Applications
Run Predictions on Your Data
bash
Copy
Edit
python scripts/predict.py --input your_data.csv
🌍 Future Improvements
✅ Enhance Model Accuracy – Add more training data.
✅ Deploy as a Web App – Allow users to enter values via a website.
✅ Expand to Other Crops – Apply AI to predict diseases in different crops.

🤝 Contributing
We welcome contributions! 🚀

Ways to Contribute:
Open an issue 📌
Submit a pull request 🔄
Suggest new datasets 📊
📜 License
This project is open-source under the MIT License.
Feel free to use, modify, and share it! 🌱

📬 Contact
📧 Email: jorgealonso24@gmail.com
💼 LinkedIn: Jorge Alonso

🚀 Let's use AI to revolutionize potato farming in Huancavelica! 🌱

yaml
Copy
Edit

---

### **🚀 Next Steps**
1️⃣ **Copy & Paste the new `README.md` into your repository.**  
2️⃣ **Commit & Push to GitHub**:
   ```bash
   git add README.md
   git commit -m "Updated README with usage instructions"
   git push origin main
3️⃣ Share the repo with others! 🎉

🚀 Let me know if you need any modifications! 😊
