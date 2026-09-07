# Backtest Trading System
A data pipeline that is an event-based backtester with three trading strategies(SMA, momentum and mean reversion) that prints results from these strategies and includes analysis of why these strategies succeed or fail.

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
python src/backtester.py
```

The script will:
1. Download data for each stock
2. Save each stock's data as `{SYMBOL}_data.csv`

## Output Files
- `AAPL_data.csv`, `MSFT_data.csv`, `etc. - Stock data with date and close price`

## Error Handling
If a stock fails to download, the script logs the error and continues with the next stock.


## Example Documentation of Outputs
Stock: GOOGL
Bought 48 at 207.90, cost: 9979.05
Sold 48 at 340.67, proceeds: 16352.16
Total Return: 63.73%
Sharpe Ratio: 1.19
Max Drawdown: -21.02%
Num Trades: 2
Balance: 16373.108886718752
=== SMA Strategy ===


## Results after testing each ticker and strategy 8/20/2026
|    | Symbol | Strategy | Return % | Sharpe | Trades |
|----|--------|----------|----------|--------|--------|
| 0  | AAPL   | sma      | 35.31    | 0.98   | 2      |
| 1  | AAPL   | mean_rev | 8.36     | 0.3    | 4      |
| 2  | AAPL   | momentum | 20.59    | 0.62   | 20     |
| 3  | MSFT   | sma      | -16.94   | -0.74  | 2      |
| 4  | MSFT   | mean_rev | 16.13    | 0.45   | 6      |
| 5  | MSFT   | momentum | 8.46     | 0.31   | 24     |
| 6  | GOOGL  | sma      | 63.73    | 1.19   | 2      |
| 7  | GOOGL  | mean_rev | 27.81    | 0.79   | 6      |
| 8  | GOOGL  | momentum | 62.88    | 1.18   | 28     |
| 9  | NVDA   | sma      | 20.5     | 0.49   | 2      |
| 10 | NVDA   | mean_rev | 15.07    | 0.38   | 4      |
| 11 | NVDA   | momentum | 4.09     | 0.22   | 40     |
| 12 | RKLB   | sma      | 54.29    | 0.65   | 2      |
| 13 | RKLB   | mean_rev | 71.87    | 0.98   | 4      |
| 14 | RKLB   | momentum | 685.06   | 1.76   | 34     |
| 15 | AMD    | sma      | 186.72   | 1.29   | 2      |
| 16 | AMD    | mean_rev | -4.73    | 0.08   | 4      |
| 17 | AMD    | momentum | 147.4    | 1.18   | 30     |
| 18 | JPM    | sma      | 21.14    | 0.7    | 2      |
| 19 | JPM    | mean_rev | 31.18    | 1.05   | 4      |
| 20 | JPM    | momentum | 41.29    | 1.05   | 20     |
| 21 | AVGO   | sma      | 24.46    | 0.49   | 2      |
| 22 | AVGO   | mean_rev | 83.48    | 1.16   | 6      |
| 23 | AVGO   | momentum | 3.01     | 0.23   | 34     |
| 24 | META   | sma      | -11.15   | -0.44  | 2      |
| 25 | META   | mean_rev | 69.19    | 1.05   | 6      |
| 26 | META   | momentum | -36.98   | -0.95  | 30     |
| 27 | TSM    | sma      | 76.85    | 1.16   | 2      |
| 28 | TSM    | mean_rev | 19.08    | 0.57   | 4      |
| 29 | TSM    | momentum | 96.05    | 1.2    | 20     |


## Analysis.md
Includes explanations of why/how these strategies work or fail. Along with explanations on max drawdown and why that loss would not be affected by the trading strategy as there exit parameters in each strategy.
[Analysis.md](Analysis.md)

## Interactive Dashboard

An interactive Tableau dashboard visualizing risk-adjusted strategy performance across all 10 equities:

**[View the dashboard on Tableau Public] (https://public.tableau.com/app/profile/george.maguire1017/viz/BacktestStrategyPerformanceDashboard/StrategyPerformanceDashboard)**

The dashboard includes:

- A risk vs. return scatter plot (Sharpe ratio vs. Return %) which is colored by symbol and shaped by strategy, highlighting outliers like RKLB's high-return/high-drawdown momentum result

- A bar chart comparing average Sharpe ratio across the three strategies (SMA, mean reversion, momentum)

## SQL Analysis
results.csv was loaded into was loaded into a local MySQL database and analyzed using SQL. In queries.sql the queries that were covered were

- Momentum strategy results, sorted by return (highest first) 
- Average return by strategy type, ranked highest to lowest
- Count of positive vs. negative Sharpe ratios across all rows
- Which strategies performed the best on avg based on sharpe ratio
- Which strategy performed the worst according to the symbol
- Difference between worst and best sharpe ratios on strategy by each symbol