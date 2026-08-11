# Trading System

## Overview
A Python script that fetches historical stock data from yfinance, calculates  returns from three different trading strategies(SMA, momentum, mean reversion) over two years, and validates data quality.

## What It Does
- Downloads 2 year of daily close price of each stock ticker
- Calculates return percentage from each trading strategy(SMA, momentum and mean reversion), total units bought with cost and sold at total proceeds. 
- Saves clean data to CSV files

## Stocks Included
AAPL, MSFT, GOOGL, NVDA, RKLB, AMD, JPM, AVGO, META, TSM

## Requirements
pandas
yfinance


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
2. Save each stock's data as `{SYMBOL}_data.csv`

## Output Files
- `AAPL_data.csv`, `MSFT_data.csv`, etc. - Stock data with strategy associated with each symbol, return %, sharpe ratio and number of trades

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

## Results after testing each ticker and strategy 8/3/2026
|    | Symbol | Strategy | Return % | Sharpe | Trades |
| -- | ------ | -------- | -------- | ------ | ------ |
| 0  | AAPL   | sma      | 36.1     | 0.05   | 2      |
| 1  | AAPL   | mean_rev | 8.37     | 0.05   | 4      |
| 2  | AAPL   | momentum | 18.13    | 0.05   | 22     |
| 3  | MSFT   | sma      | \-21.52  | 0.03   | 2      |
| 4  | MSFT   | mean_rev | 16.16    | 0.03   | 6      |
| 5  | MSFT   | momentum | 18.61    | 0.03   | 24     |
| 6  | GOOGL  | sma      | 74.25    | 0.09   | 2      |
| 7  | GOOGL  | mean_rev | 32.85    | 0.09   | 6      |
| 8  | GOOGL  | momentum | 67.82    | 0.09   | 26     |
| 9  | NVDA   | sma      | 22.16    | 0.07   | 2      |
| 10 | NVDA   | mean_rev | 15.07    | 0.07   | 4      |
| 11 | NVDA   | momentum | 7.51     | 0.07   | 40     |
| 12 | RKLB   | sma      | 90.62    | 0.12   | 2      |
| 13 | RKLB   | mean_rev | 71.87    | 0.12   | 4      |
| 14 | RKLB   | momentum | 1000.37  | 0.12   | 34     |
| 15 | AMD    | sma      | 175.79   | 0.08   | 2      |
| 16 | AMD    | mean_rev | \-1.95   | 0.08   | 4      |
| 17 | AMD    | momentum | 186.09   | 0.08   | 30     |
| 18 | JPM    | sma      | 23.86    | 0.08   | 2      |
| 19 | JPM    | mean_rev | 31.18    | 0.08   | 4      |
| 20 | JPM    | momentum | 38.18    | 0.08   | 22     |
| 21 | AVGO   | sma      | 37.51    | 0.08   | 2      |
| 22 | AVGO   | mean_rev | 83.48    | 0.08   | 6      |
| 23 | AVGO   | momentum | 19.14    | 0.08   | 36     |
| 24 | META   | sma      | \-14.68  | 0.02   | 2      |
| 25 | META   | mean_rev | 69.19    | 0.02   | 6      |
| 26 | META   | momentum | \-35.15  | 0.02   | 30     |
| 27 | TSM    | sma      | 73.15    | 0.09   | 2      |
| 28 | TSM    | mean_rev | 20.21    | 0.09   | 4      |
| 29 | TSM    | momentum | 103.45   | 0.09   | 18     |