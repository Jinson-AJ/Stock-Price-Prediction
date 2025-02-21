#---importing the libraries---

import pandas as pd # to handle the data
import matplotlib.pyplot as plt # to plot the data

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
stock_data.fillna(stock_data.mean(), inplace=True)  # Fill missing values with the mean of the column

#---feature engineering---

# 1. adding a column for the daily return (pecentage change in the closing price)
stock_data['Return'] = stock_data['Close'].pct_change()  # Calculate the daily return
# 2. adding a column for the moving average of the closing price
stock_data['MA20']=stock_data['Close'].rolling(window=20).mean() # Calculate the 20-day moving average
stock_data['MA50']=stock_data['Close'].rolling(window=50).mean() # Calculate the 50-day moving average

#display the data after feature engineering
print(stock_data.head(30))

#---data visualization---

# Plot the closing price over time
plt.figure(figsize=(10, 5))  # Set the size of the plot (width=10 inches, height=5 inches)
plt.plot(stock_data['Close'], label='Tesla Closing Price',color='Blue') # Plot the closing price on the y-axis
plt.plot(stock_data['MA20'], label='20-Day Moving Average',color='Red') # Plot the 20-day moving average on the y-axis
plt.plot(stock_data['MA50'], label='50-Day Moving Average',color='Green') # plot the 50-day moving average on the y-axis
plt.xlabel('Date')  # Label the x-axis as Date
plt.ylabel('Price (USD)')  # Label the y-axis as Price in USD
plt.title('Tesla Stock Price Over Time')  # Set the title of the plot
plt.legend()  # Display the legend on the plot
plt.show()  # Render the plot in a window