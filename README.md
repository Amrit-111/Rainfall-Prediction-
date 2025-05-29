# Rainfall-Prediction-
Analyze precipitation trends in Austin, TX using linear regression and data visualization with Python.


📁 **Dataset**:
Source: Historical weather data for Austin
Filename: austin_weather.csv

Columns Used:
TempAvgF
DewPointAvgF
HumidityAvgPercent
SeaLevelPressureAvgInches
VisibilityAvgMiles
WindAvgMPH
PrecipitationSumInches

⚙️ **Libraries Used**:
pandas
numpy
matplotlib
seaborn
scikit-learn

🔄 **Workflow**:
> Load the dataset
> Clean and preprocess the data
> Remove irrelevant columns
> Replace special characters (T, _, -) with 0.0
> Save the cleaned dataset
> Build a Linear Regression model

**Visualize**:
Precipitation trend over days
Precipitation vs Atmospheric attributes

📊 **Key Visualizations**:
Precipitation over Time: Highlights general trends and specific anomalies
Scatter plots of precipitation against various attributes like temperature, humidity, etc.



**Project Structure:**
Austin-Weather-Analysis/
│
├── austin_weather.csv                  # Original dataset
├── austin_weather_final.csv           # Cleaned dataset
├── precipitation_analysis.py          # Python script
├── README.md                          # Project documentation
