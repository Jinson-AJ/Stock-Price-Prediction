# importing the libraries
import pandas as pd # to handle the data
import matplotlib.pyplot as plt # to plot the data

# Load the data
file_path = 'TSLA.csv'  # Path to the data file
#read the data using pandas

stock_data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

# displaying the first 5 rows of the data
print(stock_data.head())

# Plot the closing price over time
plt.figure(figsize=(10, 5))  # Set the size of the plot (width=10 inches, height=5 inches)
plt.plot(stock_data['Close'], label='Tesla Closing Price',color='blue') # Plot the closing price on the y-axis
plt.xlabel('Date')  # Label the x-axis as Date
plt.ylabel('Price (USD)')  # Label the y-axis as Price in USD
plt.title('Tesla Stock Price Over Time')  # Set the title of the plot
plt.legend()  # Display the legend on the plot
plt.show()  # Render the plot in a window