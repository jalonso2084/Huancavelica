import numpy as np
import pandas as pd
import scipy.stats as stats

# Load your dataset (Modify paths as needed)
try:
    ai_predictions = pd.read_csv("ai_predictions.csv")
    human_reports = pd.read_csv("human_reports.csv")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# Merge datasets on the 'date' column
data = pd.merge(ai_predictions, human_reports, on="date", how="inner")

# Rename columns for clarity
data = data.rename(columns={"ai_risk": "Y_AI", "human_outbreak": "Y_Human"})

# Compute PPI Correlation (ρ̃)
rho = np.corrcoef(data["Y_AI"], data["Y_Human"])[0, 1]

# Compute Effective Sample Size (ESS)
n_human = len(data["Y_Human"])
n_ai = len(data["Y_AI"])
ess = n_human * (n_human + n_ai) / (n_human + n_ai * (1 - rho**2))

# Compute 95% Confidence Interval
ci_lower, ci_upper = stats.norm.interval(0.95, loc=rho, scale=np.sqrt((1 - rho**2) / (len(data) - 2)))

# Save results to CSV
results_df = pd.DataFrame({
    "PPI_Correlation": [rho],
    "CI_Lower": [ci_lower],
    "CI_Upper": [ci_upper],
    "Effective_Sample_Size": [ess]
})
results_df.to_csv("ppi_results.csv", index=False)

print("✅ PPI results saved to 'ppi_results.csv'")
