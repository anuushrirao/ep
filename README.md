# Earthquake Magnitude Prediction

This project aims to predict the magnitude of earthquakes based on various factors such as geographical location, depth, and other related features using machine learning models. The dataset used for this project contains historical earthquake data with relevant attributes.

## Project Overview

The objective of this project is to compare the performance of different machine learning models in predicting earthquake magnitudes. We have implemented and compared the following models:
- **Linear Regression**
- **Support Vector Machine (SVM)**
- **Random Forest**

The models are evaluated using two key metrics:
- **Mean Squared Error (MSE)**
- **R² Score**

Based on the analysis, the **Random Forest** model is the most accurate in predicting earthquake magnitudes, as it captures more complex relationships within the data compared to other models.

## Features

The main features used in the prediction models include:
- Latitude (deg)
- Longitude (deg)
- Depth (km)
- Number of Stations

## Results

- **Linear Regression**: 
  - MSE: 0.17192
  - R² Score: 0.106
  
- **SVM**: 
  - MSE: 0.1785
  - R² Score: 0.072
  
- **Random Forest**:
  - MSE: 0.17192
  - R² Score: 0.106

The Random Forest model outperforms others in terms of capturing the non-linear relationships present in the data.

## Visualizations

The project includes several visualizations to show the performance of the models:
- Scatter plots for actual vs predicted values for each model.
- Bar charts comparing model performance (MSE and R² Scores).

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/earthquake-prediction.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

4. Explore the visualizations and predictions made by different models.

## Dataset

The dataset used in this project contains earthquake data with features like date, time, location, depth, magnitude, and other associated details.

## Conclusion

After evaluating the three models, **Random Forest** provides the best performance in predicting earthquake magnitudes. This model is more capable of capturing the non-linear relationships present in the data compared to Linear Regression and SVM.
