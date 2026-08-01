# Trading System Stage 1: Data Pipeline

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
pip install pandas yfinance holidays matplotlib
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
