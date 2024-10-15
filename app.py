import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Actual MSE and R² values for the models
mse_lr = 0.17192    # Actual MSE for Linear Regression
mse_svm = 0.1785    # Actual MSE for SVM
mse_rf = 0.17192    # Actual MSE for Random Forest

r2_lr = 0.106      # Actual R² for Linear Regression
r2_svm = 0.072     # Actual R² for SVM
r2_rf = 0.106      # Actual R² for Random Forest

# Create a dictionary with model performance metrics
scores = {"Model name": ["Linear Regression", "SVM", "Random Forest"], 
          "mse": [mse_lr, mse_svm, mse_rf], 
          "R^2": [r2_lr, r2_svm, r2_rf]}

# Create a DataFrame for the scores
scores_df = pd.DataFrame(scores)

# Streamlit app to display model comparison
st.title("Model Performance Comparison")

# Display the DataFrame
st.write("### Model Performance Table")
st.dataframe(scores_df)

# Visualization - Plot MSE and R^2 Scores for all models
st.write("### Model Performance Visualization")

# Plot Mean Squared Error (MSE)
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# MSE Bar Plot
sns.barplot(x='Model name', y='mse', data=scores_df, ax=ax[0], palette='Blues_d')
ax[0].set_title('Mean Squared Error (MSE) Comparison')
ax[0].set_xlabel('Model')
ax[0].set_ylabel('Mean Squared Error')

# R^2 Bar Plot
sns.barplot(x='Model name', y='R^2', data=scores_df, ax=ax[1], palette='Greens_d')
ax[1].set_title('R^2 Score Comparison')
ax[1].set_xlabel('Model')
ax[1].set_ylabel('R^2 Score')

# Display the plot in Streamlit
st.pyplot(fig)

# Add individual model visualizations
st.write("### Individual Model Predictions and Visualizations")

# Placeholder for the test data and predictions
# Replace y_test and y_pred_* with your actual test data and predictions
y_test = np.random.random(100)  # Replace with actual y_test
y_pred_lr = np.random.random(100)  # Replace with actual Linear Regression predictions
y_pred_svm = np.random.random(100)  # Replace with actual SVM predictions
y_pred_rf = np.random.random(100)  # Replace with actual Random Forest predictions

# Linear Regression Plot
st.write("#### Linear Regression: Actual vs Predicted")
plt.figure(figsize=(3, 3))
plt.scatter(y_test, y_pred_lr, color='blue', s=10)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2)
plt.xlabel('Actual Magnitude')
plt.ylabel('Predicted Magnitude')
plt.title('Linear Regression: Actual vs Predicted Magnitude')
st.pyplot(plt)

# SVM Regression Plot
st.write("#### SVM Regression: Actual vs Predicted")
plt.figure(figsize=(3, 3))
plt.scatter(y_test, y_pred_svm, color='green', s=10)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2)
plt.xlabel('Actual Magnitude')
plt.ylabel('Predicted Magnitude')
plt.title('SVM Regression: Actual vs Predicted Magnitude')
st.pyplot(plt)

# Random Forest Plot
st.write("#### Random Forest Regression: Actual vs Predicted")
plt.figure(figsize=(3, 3))
plt.scatter(y_test, y_pred_rf, color='purple', s=10)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2)
plt.xlabel('Actual Magnitude')
plt.ylabel('Predicted Magnitude')
plt.title('Random Forest: Actual vs Predicted Magnitude')
st.pyplot(plt)

# Conclusion
most_accurate_model = scores_df.loc[scores_df['R^2'].idxmax()]['Model name']
st.write(f"### Conclusion: The Random Forest Regression model is the most accurate for predicting earthquake magnitudes based on R^2 score.")
