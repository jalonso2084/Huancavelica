# Weather Data Documentation

## 1. Data Source
- **ERA5**: Reanalysis dataset providing hourly weather data.

## 2. Key Variables and Units
| Variable          | Unit         | Description |
|------------------|-------------|-------------|
| Temperature      | °C           | Air temperature at 2m height |
| Humidity        | %            | Relative humidity |
| Precipitation   | mm           | Total daily/hourly precipitation |
| Wind Speed      | m/s          | Wind speed at 10m height |
| Solar Radiation | W/m²         | Solar energy received per unit area |

## 3. Data Preprocessing Steps
- **Data Cleaning**:
  - Checked for missing values and outliers.
  - Interpolated missing data points where necessary.
- **Data Transformation**:
  - Converted temperature from Kelvin to Celsius: `Temp(°C) = Temp(K) - 273.15`.
- **Data Aggregation**:
  - Computed daily averages from hourly records.
  - Summed total daily precipitation.
- **Data Formatting**:
  - Exported in CSV and NetCDF formats.

## 4. Version Control and Updates
- All data updates are tracked via **GitHub**.
- Updates are committed with descriptive messages.
- Version history can be reviewed in the repository.

### References
- Giraldo, E., et al. (2010). *Severity of the Potato Late Blight (Phytophthora)*. [PDF](./docs/Giraldoetal-2010-SeverityofthePotatoLateBlight.pdf)



