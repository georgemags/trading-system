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


## Documentation of Outputs
Stock: GOOGL
Bought 48 at 207.90, cost: 9979.05
Sold 48 at 340.67, proceeds: 16352.16
Total Return: 63.73%
Sharpe Ratio: 1.19
Max Drawdown: -21.02%
Num Trades: 2
Balance: 16373.108886718752
=== SMA Strategy ===

Stock: RKLB
Bought 1394 at 7.17, cost: 9994.98
Sold 1394 at 26.32, proceeds: 36690.08
Bought 1440 at 25.47, cost: 36676.80
Sold 1440 at 24.64, proceeds: 35481.60
Bought 1135 at 31.27, cost: 35491.45
Sold 1135 at 25.93, proceeds: 29430.55
Bought 1680 at 17.52, cost: 29433.60
Sold 1680 at 17.18, proceeds: 28862.40
Bought 1402 at 20.59, cost: 28867.18
Sold 1402 at 19.04, proceeds: 26694.08
Bought 1220 at 21.88, cost: 26693.60
Sold 1220 at 43.43, proceeds: 52984.60
Bought 1122 at 47.22, cost: 52980.84
Sold 1122 at 43.53, proceeds: 48840.66
Bought 1065 at 45.84, cost: 48819.60
Sold 1065 at 46.26, proceeds: 49266.90
Bought 1027 at 47.97, cost: 49265.19
Sold 1027 at 56.57, proceeds: 58097.39
Bought 1087 at 53.43, cost: 58078.41
Sold 1087 at 74.15, proceeds: 80601.05
Bought 992 at 81.27, cost: 80619.84
Sold 992 at 73.11, proceeds: 72525.12
Bought 1034 at 70.11, cost: 72493.74
Sold 1034 at 68.93, proceeds: 71273.62
Bought 1042 at 68.41, cost: 71283.22
Sold 1042 at 69.48, proceeds: 72398.16
Bought 994 at 72.88, cost: 72442.72
Sold 994 at 65.94, proceeds: 65544.36
Bought 928 at 70.62, cost: 65535.36
Sold 928 at 73.60, proceeds: 68300.80
Bought 823 at 82.93, cost: 68251.39
Sold 823 at 108.23, proceeds: 89073.29
Bought 1076 at 82.83, cost: 89125.08
Sold 1076 at 72.95, proceeds: 78494.20
Total Return: 685.06%
Sharpe Ratio: 1.76
Max Drawdown: -39.69%
Num Trades: 34
Balance: 78505.8584365845
=== Momentum Strategy ===


Stock: META
Bought 17 at 555.90, cost: 9450.33
Sold 17 at 564.33, proceeds: 9593.67
Bought 17 at 589.44, cost: 10020.46
Sold 17 at 596.29, proceeds: 10136.98
Bought 16 at 627.10, cost: 10033.61
Sold 16 at 605.34, proceeds: 9685.41
Bought 16 at 613.43, cost: 9814.85
Sold 16 at 655.00, proceeds: 10480.04
Bought 17 at 594.61, cost: 10108.41
Sold 17 at 715.29, proceeds: 12159.86
Bought 16 at 770.91, cost: 12334.61
Sold 16 at 748.66, proceeds: 11978.50
Bought 15 at 773.19, cost: 11597.79
Sold 15 at 715.48, proceeds: 10732.19
Bought 15 at 749.49, cost: 11242.36
Sold 15 at 664.74, proceeds: 9971.12
Bought 15 at 659.81, cost: 9897.21
Sold 15 at 647.53, proceeds: 9713.02
Bought 13 at 737.00, cost: 9580.94
Sold 13 at 636.12, proceeds: 8269.50
Bought 13 at 633.94, cost: 8241.25
Sold 13 at 609.07, proceeds: 7917.85
Bought 13 at 631.92, cost: 8215.02
Sold 13 at 597.08, proceeds: 7762.00
Bought 12 at 622.40, cost: 7468.84
Sold 12 at 592.45, proceeds: 7109.41
Bought 12 at 612.91, cost: 7354.92
Sold 12 at 582.90, proceeds: 6994.80
Bought 11 at 615.58, cost: 6771.38
Sold 11 at 539.03, proceeds: 5929.33
Total Return: -36.98%
Sharpe Ratio: -0.95
Max Drawdown: -51.43%
Num Trades: 30
Balance: 6301.695983886719
=== Momentum Strategy ===

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