# Stock Price Prediction Using Python

## Overview
This project uses Python to fetch and analyze historical stock price data downloaded from Kaggle. The data is processed using `pandas`, visualized with `matplotlib`, and lays the groundwork for future predictive modeling using machine learning techniques.

## Tech Stack
- **Python**
- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **scikit-learn**
- **tensorflow** (for future deep learning models)

## Data Source: Tesla Stock Price CSV from Kaggle

This project uses historical Tesla stock price data downloaded from Kaggle. The dataset includes the following columns:
- **Date**
- **Open**
- **High**
- **Low**
- **Close**
- **Volume**
- 
## Data Preprocessing

Clean and enhance the dataset by performing the following operations:
- **Data Cleaning:**  
  - Check for missing values and handle them using forward fill method.
- **Feature Engineering:**  
  - Compute the daily return as the percentage change of the closing price.
  - Calculate the 20-day and 50-day moving averages to capture short-term and long-term trends.

## Model Building

we build a simple Linear Regression model to predict the next day's closing price of Tesla stock. The steps involved are:

1. **Creating the Target Variable:**  
   The target is defined as the next day's 'Close' price.

2. **Preparing the Dataset:**  
   We use features such as 'Close', 'MA20', 'MA50', and 'Return'.

3. **Splitting the Data:**  
   The dataset is split into training (first 80%) and testing (remaining 20%) sets while preserving the time series order.

4. **Training the Model:**  
   A Linear Regression model is trained on the training data.

5. **Evaluation:**  
   Model performance is evaluated using RMSE and MAE. A plot comparing actual and predicted values is generated.
