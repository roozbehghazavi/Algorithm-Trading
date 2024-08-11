import pandas as pd
import yfinance as yf

# Set the start and end dates
start_date = '2022-06-01'
end_date = '2023-06-01'

# Retrieve the historical data from Yahoo! Finance
data = yf.download('BTC-USD', start=start_date, end=end_date)

# Extract the 'Close' prices
close_prices = data['Close']

# Calculate the Simple Moving Average (SMA)
sma = close_prices.rolling(window=30).mean()

# Calculate the Standard Deviation (SD)
sd = close_prices.rolling(window=30).std()

# Initialize variables
position = 0
units = 0
capital = 100000  # Starting capital in USD

# Iterate over the prices and apply the strategy
for i in range(len(close_prices)):
    if close_prices[i] > sma[i] + sd[i] and position == 0:
        # Open a sell position
        units = capital / close_prices[i]
        position = -1  # Negative value indicates a sell position
    elif close_prices[i] < sma[i] - sd[i] and position == 0:
        # Open a buy position
        units = capital / close_prices[i]
        position = 1  # Positive value indicates a buy position
    elif (close_prices[i] <= sma[i] or close_prices[i] >= sma[i]) and position != 0:
        # Close the position when the price reaches the SMA
        capital = units * close_prices[i]
        units = 0
        position = 0

# Calculate the percent return and compound return
percent_return = ((capital - 100000) / 100000) * 100
compound_return = (capital / 100000) ** (365 / len(close_prices)) - 1

# Calculate the Sharpe ratio (assuming risk-free rate of 0%)
sharpe_ratio = (compound_return - 0) / (sd.mean() * (252 ** 0.5))

# Print the results
print(f"Percent Return: {percent_return:.2f}%")
print(f"Compound Return: {compound_return:.2f}%")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
