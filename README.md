# Algorithm Trading Project

## Overview
This project is part of my algorithm trading course and includes both theoretical research and practical coding exercises. The project is divided into three main parts: a simple trading strategy on historical Bitcoin prices, a modified trading strategy with partial investments, and an analysis of coin combinations with the lowest p-values.

## Part 1: Simple Trading Strategy
This code implements a simple trading strategy on historical Bitcoin (BTC) prices using the Yahoo! Finance API and calculates some performance metrics.

### Steps:
1. **Import Libraries**: Uses `yfinance` and `pandas` for data manipulation and analysis.
2. **Set Date Range**: Defines the start and end dates for retrieving historical data.
3. **Retrieve Data**: Uses `yf.download` from the `yfinance` library to get the price data for "BTC-USD" within the specified date range.
4. **Extract Close Prices**: Stores the close prices from the retrieved data.
5. **Calculate SMA and SD**: Computes the Simple Moving Average (SMA) and Standard Deviation (SD) using a 30-day rolling window on the close prices.
6. **Initialize Variables**: Sets up variables for position, units, and capital.
7. **Apply Trading Strategy**: Iterates over the close prices to apply the trading strategy:
   - Opens a short position if the current price is greater than the sum of SMA and SD and no position exists.
   - Opens a long position if the current price is less than the difference between SMA and SD and no position exists.
   - Closes the position if the current price reaches the SMA.
8. **Calculate Performance Metrics**: Computes the percentage return, compounded return, and Sharpe ratio based on the final capital relative to the initial capital.

## Part 2: Modified Trading Strategy
This part is similar to the first part but with a modification: instead of investing all the capital at once, one-third of the capital is invested each time, and the position is closed when the price returns to the SMA.

## Part 3: Coin Combinations Analysis
In this part, three combinations of coins with the lowest p-values are selected using the code from Exercise 5. These combinations are then used in the functions from Parts 1 and 2 to calculate the performance metrics.

---

