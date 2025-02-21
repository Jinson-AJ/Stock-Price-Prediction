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
  - Check for missing values and handle them using replace with mean.
- **Feature Engineering:**  
  - Compute the daily return as the percentage change of the closing price.
  - Calculate the 20-day and 50-day moving averages to capture short-term and long-term trends.
