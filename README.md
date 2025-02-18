📌 Huancavelica: AI-Powered Late Blight Prediction Model
🌱 An AI-driven system for forecasting late blight outbreaks in potato crops, optimizing disease management in Huancavelica, Peru.

📖 Overview
Late blight, caused by Phytophthora infestans, is one of the most devastating potato diseases, leading to significant yield losses. This project leverages machine learning, weather data, and historical disease records to predict outbreaks and support data-driven decision-making.

This repository contains:

A trained AI model for predicting late blight outbreaks.
Python scripts to preprocess data and run predictions.
Jupyter Notebooks for reproducibility.
Example datasets to help researchers test the model.
✅ Want a user-friendly interface?
🔗 Visit the Huancavelica AI Web App (Coming Soon!) to test predictions online! 🚀

📂 Repository Structure
bash
Copy
Edit
📂 Huancavelica/
│── 📂 data/                          # Raw & cleaned datasets
│── 📂 sample_data/                    # Small example datasets for testing
│── 📂 weather-data/                   # Climate and meteorological data
│── 📂 historical_disease_records/     # Past blight occurrences
│── 📂 soil_data/                      # Soil properties affecting disease spread
│── 📂 model/                          # Trained model & parameters
│── 📂 notebooks/                      # Jupyter notebooks for reproducibility
│── 📂 scripts/                        # Python scripts for preprocessing & training
│── 📂 website/                        # Web-based model deployment
│── 📄 README.md                        # Project documentation
│── 📄 INSTALL.md                        # Step-by-step setup instructions
│── 📄 API.md                           # API documentation for website integration
│── 📄 REFERENCES.md                     # Research citations & papers
│── 📄 .gitignore                        # Prevents unnecessary files from being tracked
│── 📄 requirements.txt                  # Python dependencies
⚡ Quick Start Guide
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/jalonso2084/Huancavelica.git
cd Huancavelica
2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Model
To test the model on sample weather data, use:

bash
Copy
Edit
python scripts/predict.py --input sample_data/weather_sample.csv
4️⃣ Use the Jupyter Notebook (Recommended)
For a step-by-step guide, open the interactive notebook:

bash
Copy
Edit
jupyter notebook notebooks/model_test.ipynb
🔬 Testing with Your Own Data
If you have your own dataset:

Ensure it follows this format:
bash
Copy
Edit
date,temperature,humidity,soil_moisture,precipitation
2024-02-01,18.5,85,30,2.1
Run:
bash
Copy
Edit
python scripts/predict.py --input your_data.csv
🌍 API & Web Interface
🚀 The model will soon be accessible via a REST API & Web Dashboard!

🔗 Visit: Huancavelica AI Web App (Coming Soon!)

For API access:

bash
Copy
Edit
curl -X POST "https://huancavelica-ai.com/api/predict" -H "Content-Type: application/json" -d '{"temperature": 20, "humidity": 85, "soil_moisture": 30}'
Expected response:

json
Copy
Edit
{
    "prediction": "High Risk",
    "confidence": 92.4
}
📖 More details in API.md.

🛠 Future Improvements
✅ Better Accuracy: Enhance model predictions with real-time weather API integration.
✅ Interactive Dashboard: Deploy a farmer-friendly web app for disease risk monitoring.
✅ More Data Sources: Expand training datasets for different potato-growing regions.

🤝 Contributing
We welcome contributions from researchers, data scientists, and agronomists.

Open an issue or feature request 📌
Submit a pull request 💡
Share additional datasets 📚
📜 License
This project is open-source under the MIT License. Feel free to use, modify, and share it!

📬 Contact
📩 Email: [jorgealonso24@gmail.com]
💼 LinkedIn: [https://www.linkedin.com/in/jorgeluisalonso/]

🚀 Let's use AI to revolutionize potato farming in Huancavelica!
