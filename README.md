🥔 Huancavelica AI-Powered Late Blight Prediction Model 🌍
🚀 Predict potato late blight outbreaks using AI!
This model helps farmers and researchers analyze weather, soil, and farming practices to determine disease risk levels in Huancavelica, Peru.

📂 What's Inside?
📌 AI Model – Trained to predict late blight risk
📌 Python Scripts – Easily run predictions on your data
📌 Sample Data – Test with example datasets
📌 Jupyter Notebooks – Explore model experiments

⚡ Get Started in 5 Steps!
1️⃣ Clone This Repository
git clone https://github.com/jalonso2084/Huancavelica.git
cd Huancavelica

2️⃣ Set Up Python & Install Requirements
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt

3️⃣ Run a Prediction on Sample Data
python scripts/predict.py --input sample_data/weather_sample.csv
✅ Results will be saved in predictions.csv

4️⃣ Check the Predictions
cat predictions.csv  # macOS/Linux
type predictions.csv # Windows

🧪 Want to Test Your Data?
Make sure your dataset has these columns:
Latitude, Longitude, Types of Potatoes Grown, Region/Country, Criteria for Selection,
Farming Practices, pH, Bulk_Density, Organic_Carbon, CEC, Clay_Content,
Sand_Content, Silt_Content, Climatic_Climate Variability, 
Climatic_Moderate El Niño, Climatic_Weak-Moderate El Niño, Fungicide Applications

Run Predictions on Your Data
python scripts/predict.py --input your_data.csv

🚀 Future Improvements
✅ Improve model accuracy with more training data 📊
✅ Develop an interactive web app for easy use 🌍
✅ Expand the model to detect diseases in other crops 🌾

🤝 Contribute & Collaborate!
We’d love your help! You can:

Open an issue to suggest improvements
Submit a pull request to contribute code
Share additional datasets to train a better model

📜 License
This project is open-source under the MIT License.

📬 Contact
📧 Email: jorgealonso24@gmail.com
💼 LinkedIn: Jorge Alonso

🚀 Let's use AI to transform potato farming in Huancavelica! 🌱

📚 References
This project is based on scientific research in late blight prediction and machine learning methodology.

🔬 Methodology Papers:
Luo et al., 2024 – Large language models surpass human experts in predicting neuroscience results. Nature Human Behaviour. DOI:10.1038/s41562-024-02046-9
Shimabucoro et al., 2024 – LLM See, LLM Do: Leveraging Active Inheritance to Target Non-Differentiable Objectives. Proceedings of the 2024 Conference on EMNLP. DOI:10.18653/v1/2024.emnlp-main.521

📊 Data Sources for Training & Evaluation:
Giraldo et al., 2010 – Severity of potato late blight in agricultural areas of Peru. Revista Peruana Geo-Atmosferica.
Gastelo et al., 2021 – Identification of Elite Potato Clones with Resistance to Late Blight Through Participatory Varietal Selection in Peru. Potato Research. DOI:10.1007/s11540-021-09495-z
Haan & Juarez, 2010 – Land use and potato genetic resources in Huancavelica, central Peru. Journal of Land Use Science. DOI:10.1080/1747423X.2010.500681
Zevallos et al., 2021 – First signs of late blight resistance in traditional native potatoes of Pasco—Peru. Agriculture & Food Security. DOI:10.1186/s40066-021-00330-9
Perez et al., 2022 – Farmer Perceptions Related to Potato Production and Late Blight Management in Two Communities in the Peruvian Andes. Frontiers in Sustainable Food Systems. DOI:10.3389/fsufs.2022.873490
Saffer et al., 2024 – Reconstructing historic and modern potato late blight outbreaks using text analytics. Scientific Reports. DOI:10.1038/s41598-024-52870-2
📖 For full reference details, see REFERENCES.md.


