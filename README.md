AI-Powered Late Blight Prediction API 🥔

🚀 Predict potato late blight outbreaks using AI!
This repository provides an AI-powered model to help farmers and researchers analyze weather, soil, and farming practices to determine disease risk levels in Huancavelica, Peru.



📂 What's Inside?

AI Model: A Random Forest model trained to predict late blight risk using weather, soil conditions, and farming practices.

Python Scripts:

predict.py: Runs predictions on input data and saves results to predictions.csv.

train.py: (Optional) Retrains the model with new data.

Flask API: A RESTful API to serve PPI correlation results in real time.

Sample Data: Example weather and soil data in CSV format for testing.

Jupyter Notebooks: Notebooks for data exploration, model training, and feature importance analysis.

References: A list of scientific papers used for model training and evaluation (see REFERENCES.md).

⚡ Get Started in 5 Steps!

1️⃣ Clone This Repository

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

🧪 Running Predictions

Run a Prediction on Sample Data

python scripts/predict.py --input sample_data/weather_sample.csv

✅ The results will be saved in predictions.csv.

Example Prediction Output

{
    "Latitude": -12.0433,
    "Longitude": -77.0283,
    "Predicted Risk": "High"
}

📡 Flask API for PPI Correlation

This repository includes a Flask API to serve real-time PPI correlation results.

1️⃣ Start the API

python ppi_api.py

2️⃣ Access the API

Open in a browser:

http://127.0.0.1:5000/ppi

Or use curl in the terminal:

curl http://127.0.0.1:5000/ppi

3️⃣ Example API Response

{
    "PPI_Correlation": 0.905,
    "CI_Lower": 0.3169,
    "CI_Upper": 1.4938,
    "Effective_Sample_Size": 6.78,
    "GPT_Explanation": "AI predictions are highly reliable."
}

⚙️ Technical Details

Model Type: Random Forest Classifier

Features Used: Temperature, humidity, soil pH, organic carbon, farming practices

Training Data Source: Historical late blight outbreak reports from Huancavelica, Peru

Hyperparameters:

n_estimators: 100

max_depth: 10

min_samples_split: 5

🚀 Deployment Instructions

To deploy this API on a cloud service (AWS, DigitalOcean, Render):

1️⃣ Install Gunicorn for production:

pip install gunicorn

2️⃣ Run Flask as a background process:

gunicorn -w 4 -b 0.0.0.0:5000 ppi_api:app

3️⃣ To expose it publicly, use Ngrok:

ngrok http 5000

Then, share the Ngrok link!

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

📧 Email: jorgealonso24@gmail.com💼 LinkedIn: https://www.linkedin.com/in/jorgeluisalonso/

🚀 Let's use AI to transform potato farming in Huancavelica! 🌱
