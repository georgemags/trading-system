# Trading System

## Overview
A Python script that fetches historical stock data from yfinance, calculates daily returns, and validates data quality.

## What It Does
- Downloads 1 year of daily OHLCV (Open, High, Low, Close, Volume) data for 10 stocks
- Calculates daily percentage returns
- Validates data for missing values (NaN) in Close prices
- Checks for missing trading dates (excluding weekends and US holidays)
- Saves clean data to CSV files

## Stocks Included
AAPL, MSFT, GOOGL, NVDA, RKLB, AMD, JPM, AVGO, META, TSM

## Requirements
pandas
yfinance
holidays
matplotlib

## Installation
```bash
pip install pandas yfinance 
```

## Usage
```bash
python fetch_data.py
```

The script will:
1. Download data for each stock
2. Print validation results (NaN count, missing dates)
3. Save each stock's data as `{SYMBOL}_data.csv`

## Output Files
- `AAPL_data.csv`, `MSFT_data.csv`, etc. - Stock data with Close, High, Low, Open, Volume, and daily_return columns

## Error Handling
If a stock fails to download, the script logs the error and continues with the next stock.


## Documentation of Outputs
=== SMA Strategy ===
Bought 43 at 229.38, cost: 9863.39
Sold 43 at 333.43, proceeds: 14337.49
Total Return: 44.74%
Sharpe Ratio: 0.06
Max Drawdown: -33.36%
Num Trades: 2
Balance: 14474.104202270508

=== Mean Reversion Strategy ===
Bought 46 at 215.84, cost: 9928.62
Sold 46 at 219.16, proceeds: 10081.38
Bought 38 at 261.87, cost: 9951.19
Sold 38 at 279.88, proceeds: 10635.52
Total Return: 8.37%
Sharpe Ratio: 0.06
Max Drawdown: -33.36%
Num Trades: 4
Balance: 10837.095764160156


=== Momentum Strategy ===
Sold 37 at 308.91, proceeds: 11429.67
Total Return: 16.01%
Sharpe Ratio: 0.05
Max Drawdown: -33.36%
Num Trades: 22
Balance: 11600.579803466802

## Results after testing each ticker and strategy
 | Symbol  Strategy  Return %  Sharpe  Trades    |
|-----------------------------------------------|
| 0    AAPL       sma     34.20    0.05       2 |
| 1    AAPL  mean_rev      8.37    0.05       4 |
| 2    AAPL  momentum     16.01    0.05      22 |
| 3    MSFT       sma    -21.24    0.02       2 |
| 4    MSFT  mean_rev     16.16    0.02       6 |
| 5    MSFT  momentum     10.00    0.02      24 |
| 6   GOOGL       sma     82.63    0.08       2 |
| 7   GOOGL  mean_rev     33.53    0.08       6 |
| 8   GOOGL  momentum     78.79    0.08      24 |
| 9    NVDA       sma     12.73    0.06       2 |
| 10   NVDA  mean_rev     15.07    0.06       4 |
| 11   NVDA  momentum    -15.49    0.06      42 |
| 12   RKLB       sma     45.05    0.12       2 |
| 13   RKLB  mean_rev     71.87    0.12       4 |
| 14   RKLB  momentum    926.37    0.12      32 |
| 15    AMD       sma    172.05    0.08       2 |
| 16    AMD  mean_rev     -3.40    0.08       4 |
| 17    AMD  momentum    172.40    0.08      30 |
| 18    JPM       sma     22.40    0.08       2 |
| 19    JPM  mean_rev     31.18    0.08       4 |
| 20    JPM  momentum     30.32    0.08      22 |
| 21   AVGO       sma     33.48    0.08       2 |
| 22   AVGO  mean_rev     83.48    0.08       6 |
| 23   AVGO  momentum     -5.16    0.08      38 |
| 24   META       sma    -12.47    0.02       2 |
| 25   META  mean_rev     69.19    0.02       6 |
| 26   META  momentum    -35.02    0.02      32 |
| 27    TSM       sma     74.96    0.09       2 |
| 28    TSM  mean_rev     15.79    0.09       4 |
| 29    TSM  momentum     88.11    0.09      20 |