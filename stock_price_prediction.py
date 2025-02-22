#---importing the libraries---

import pandas as pd # to handle the data
import matplotlib.pyplot as plt # to plot the data
import numpy as np # for mathematical operations
from sklearn.model_selection import train_test_split # to split the data into training and testing sets
from sklearn.linear_model import LinearRegression # for linear regression
from sklearn.metrics import mean_squared_error , mean_absolute_error # for evaluation

#---Load the data---

file_path = 'TSLA.csv'  # Path to the data file
#read the data using pandas
stock_data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
# displaying the first 5 rows of the data
print(stock_data.head())

#---data cleaning---

# Check for missing values
print('\nMissing Values:\n', stock_data.isnull().sum())  # Check for missing values in the data
# handling the missing values (if any)
stock_data.fillna(method='ffill', inplace=True)  # Fill missing values using forward fill method

#---feature engineering---

# 1. adding a column for the daily return (pecentage change in the closing price)
stock_data['Return'] = stock_data['Close'].pct_change()  # Calculate the daily return
# 2. adding a column for the moving average of the closing price
stock_data['MA20']=stock_data['Close'].rolling(window=20).mean() # Calculate the 20-day moving average
stock_data['MA50']=stock_data['Close'].rolling(window=50).mean() # Calculate the 50-day moving average

#display the data after feature engineering
print(stock_data.head(30))

#---data modeling---

# creating a target variable
stock_data['Target'] = stock_data['Close'].shift(-1) # Shift the Close price by 1 day to create the target variable
# Drop the rows with missing values
stock_data.dropna(inplace=True)
# define the features and target variable
x = stock_data[['Close','MA20','MA50','Return']] # the features
y = stock_data['Target'] # the target variable

# Split the data into training and testing sets
split_index = int(0.8 * len(stock_data)) 
x_train, x_test = x.iloc[:split_index], x.iloc[split_index:]
y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]

# Create a linear regression model
model = LinearRegression() # Create a linear regression model
model.fit(x_train,y_train) # Train the model using the training data

# Make predictions using the testing data
y_pred = model.predict(x_test) # Make predictions using the testing data

# Evaluate the model
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # Calculate the root mean squared error
mae = mean_absolute_error(y_test, y_pred) # Calculate the mean absolute error
print('Linear Regression Model Performance:')
print('root mean squared error:',rmse)
print('mean absolute error:',mae)
# if the error is high, we can try to improve the model by adding more features, using a different model, or tuning the hyperparameters


#---data visualization---

# Plot the closing price over time
plt.figure(figsize=(12, 6))  # Set the size of the plot (width=10 inches, height=5 inches)
plt.plot(y_test.index, y_test, label='Actual Price', color='blue')  # Plot the actual price in blue
plt.plot(y_test.index, y_pred, label='Predicted Price', color='red')  # Plot the predicted price in red
plt.xlabel('Date')  # Label the x-axis as Date
plt.ylabel('Price (USD)')  # Label the y-axis as Price in USD
plt.title('Actual vs Predicted Price')  # Set the title of the plot
plt.legend()  # Display the legend on the plot
plt.show()  # Render the plot in a window