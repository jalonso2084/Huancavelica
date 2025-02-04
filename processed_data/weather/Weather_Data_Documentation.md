# Weather Data Documentation for AI-Powered Late Blight Prediction System in Huancavelica, Peru

## 1. Background and Justification

This weather data supports the **AI-Powered Late Blight Prediction System for Huancavelica, Peru**. The system leverages **ERA5 reanalysis weather data** to provide accurate, explainable predictions of late blight outbreaks. The focus is on modeling environmental conditions, such as **temperature, humidity, and precipitation**, that influence the growth and spread of **Phytophthora infestans**, the pathogen responsible for late blight.

Traditional methods of managing late blight rely heavily on frequent fungicide applications, which are costly and environmentally damaging. By using ERA5 weather data in conjunction with advanced AI models, the system aims to provide **timely alerts** and **actionable insights** to farmers and researchers, reducing reliance on chemical interventions and promoting sustainable agricultural practices.

## 2. Data Sources
- **ERA5:** The exclusive data source for this project, providing high-resolution hourly weather data. ERA5 offers comprehensive coverage of variables such as **temperature**, **humidity**, **precipitation**, **wind speed**, and **solar radiation**, all of which are critical for predicting late blight outbreaks.

## 3. Key Variables and Units
| **Variable**       | **Unit**   | **Description**                                |
|--------------------|------------|------------------------------------------------|
| Temperature (t)    | °C       | Air temperature at 2m height                   |
| Humidity (cc)      | %          | Relative humidity                              |
| Precipitation (r)  | mm         | Total daily/hourly precipitation               |
| Wind Speed (u, v)  | m/s        | Wind speed components at 10m height            |
| Cloud Water (crwc) | kg/m^2     | Cloud liquid water content                     |
| Solar Radiation    | W/m²       | Solar energy received per unit area            |

## 4. Data Preprocessing Steps

### **4.1 Data Cleaning:**
- **Missing Values:** Identified using `df.isnull().sum()`. Handled using:
  - **Forward-fill (`ffill`):** For time-series continuity.
  - **Backward-fill (`bfill`):** As a fallback for initial missing entries.
  - **Mean Imputation:** Applied to random missing values in non-temporal data.
- **Outlier Detection:**
  - **Z-score Method:** Identified outliers with Z-scores > 3.
  - **Interquartile Range (IQR):** Values outside 1.5x IQR were reviewed.

### **4.2 Data Transformation:**
- **Temperature Conversion:** Transformed from Kelvin to Celsius using:
  ```
  Temp (°C) = Temp (K) - 273.15
  ```
- **Wind Speed Components:** Combined `u` and `v` components to calculate overall wind speed.

### **4.3 Data Aggregation:**
- Resampled hourly data to daily averages using:
  ```
  df.resample('D').mean()
  ```
- Summed daily precipitation from hourly data.

### **4.4 Data Formatting:**
- Organized into **CSV** and **NetCDF** formats for flexibility in analysis.
- Converted `valid_time` to datetime for time-based analysis:
  ```
  df['valid_time'] = pd.to_datetime(df['valid_time'])
  ```

## 5. Data Validation
- **Temporal Validation:** Verified the consistency of ERA5 weather data over time to identify any anomalies or missing periods.
- **Anomaly Detection:** Used statistical methods (e.g., Z-score, IQR) to detect unusual spikes or drops in temperature, humidity, and precipitation that could affect prediction accuracy.
- **Cross-Period Validation:** Compared weather trends across different seasons to ensure consistency and reliability in the data.

## 6. Data Availability and Sharing
- **Integration with AI System:** The ERA5 weather data is preprocessed and fed into the AI-powered model for predicting late blight outbreaks.
- **Explainability:** The AI system highlights the impact of specific weather variables on the likelihood of an outbreak, providing actionable insights for farmers and researchers.
- **Central Repository:** All datasets are stored in **Google Drive** under:
  - `G:/My Drive/Huancavelica/processed_data/weather`
- **Version Control:** Managed through **GitHub** repository:
  - [https://github.com/jalonso2084/weather-data](https://github.com/jalonso2084/weather-data)
- **Access Protocol:** Team members can request access via shared Google Drive link or GitHub repository.

## 7. Version Control and Updates
- All data updates are tracked using **GitHub**.
- **Commit Messages:** Clearly describe changes, e.g., "Fixed missing values and removed duplicates."
- **Version History:** Available in the GitHub repository for tracking all modifications.

## 8. Documentation Updates
- Updated on **2025-01-29** to align with the project **"[01/02; 9:00 AM] AI-Powered Late Blight Prediction System for Huancavelica, Peru"**, focusing on the exclusive use of ERA5 weather data and its integration into the AI system for real-time, explainable predictions.

---

By refining these details, the documentation now accurately reflects the data sources, processing steps, and integration with the AI-powered prediction system, ensuring consistency and reliability in managing potato late blight in Huancavelica, Peru.

