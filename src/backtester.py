import pandas as pd
import yfinance as yf

symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'RKLB', 'AMD', 'JPM',
'AVGO', 'META', 'TSM']

for symbol in symbols:
    try:
        stock_data = yf.download(symbol, period='2y')

        # Extract just the Close column and reset it
        close_data = stock_data[['Close']].copy()
        close_data.columns = ['Close']

        # Save it
        close_data.to_csv(f'data/{symbol}_data.csv')
        print(f"Saved {symbol} data")

    except Exception as e:
        print(f"Failed to download {symbol}: {e}")


class BacktestBase:

    def __init__(self, filename, initial_amount, ftc=0.0, ptc=0.0):
        self.filename = filename
        self.initial_amount = initial_amount
        self.balance = initial_amount
        self.units = 0
        self.position = 0
        self.num_trades = 0
        self.ftc = ftc
        self.ptc = ptc
        self.get_data()

    def get_data(self):
        self.data = pd.read_csv(self.filename, index_col=0, parse_dates=True)

    def place_buy_order(self, bar, units = None, amount = None):
        price = self.data.iloc[bar]['Close']

        if units is None:
            units = int(amount / price)

        cost = (units * price) * (1 + self.ptc) + self.ftc

        self.balance -= cost
        self.units += units
        self.position = 1
        self.num_trades += 1

        print(f"Bought {units} at {price:.2f}, cost: {cost:.2f}")

    def place_sell_order(self, bar, units = None, amount = None):
        price = self.data.iloc[bar]['Close']

        if units is None:
            units = int(amount / price)

        proceeds = (units * price) * (1 - self.ptc) - self.ftc

        self.balance += proceeds
        self.units -= units
        self.position = 0
        self.num_trades += 1

        print(f"Sold {units} at {price:.2f}, proceeds: {proceeds:.2f}")

    def close_out(self):
        if self.position == 1:
            last_bar = len(self.data) - 1
            self.place_sell_order(last_bar, units = self.units)


    def run_sma_strat(self, SMA1, SMA2):
        self.position = 0
        self.num_trades = 0
        self.data["SMA1"] = self.data["Close"].rolling(SMA1).mean()
        self.data["SMA2"] = self.data["Close"].rolling(SMA2).mean()

        for bar in range(SMA2, len(self.data)):
            if self.position == 0:
                if self.data["SMA1"].iloc[bar] > self.data["SMA2"].iloc[bar]:
                    self.place_buy_order(bar, amount = self.balance)
                    self.position = 1
            elif self.position == 1:
                if self.data["SMA1"].iloc[bar] < self.data["SMA2"].iloc[bar]:
                    self.place_sell_order(bar, units = self.units)
                    self.position = 0

        self.close_out()
        self.calculate_metrics()

        print(f"Num Trades: {self.num_trades}")
        print(f"Balance: {self.balance}")


    def calculate_metrics(self):
        self.total_return = ((self.balance - self.initial_amount) /
self.initial_amount) * 100
        self.data['daily_returns'] = self.data['Close'].pct_change()

        avg_daily_returns = self.data['daily_returns'].mean()
        std_daily_returns = self.data['daily_returns'].std()
        sharpe_ratio = avg_daily_returns/std_daily_returns

        running_max = self.data['Close'].expanding().max()
        drawdown = (self.data['Close'] - running_max) / running_max
        max_drawdown = drawdown.min() * 100

        print(f"Total Return: {self.total_return:.2f}%")
        print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
        print(f"Max Drawdown: {max_drawdown:.2f}%")


    def run_mean_reversion(self, lookback = 50, threshold = 2.0):
        rolling_mean = self.data['Close'].rolling(lookback).mean()
        rolling_std_dev = self.data['Close'].rolling(lookback).std()
        lower_band = rolling_mean - (threshold * rolling_std_dev)
        upper_band = rolling_mean + (threshold * rolling_std_dev)
        self.position = 0
        self.num_trades = 0

        for bar in range(lookback, len(self.data)):
            price = self.data["Close"].iloc[bar]
            mean = rolling_mean.iloc[bar]
            std = rolling_std_dev.iloc[bar]
            if self.position == 0:
                if price < lower_band.iloc[bar]:
                    self.place_buy_order(bar, amount = self.balance)
                    self.position = 1

            elif self.position == 1:
                if price > upper_band.iloc[bar]:
                    self.place_sell_order(bar, units = self.units)
                    self.position = 0

        self.close_out()
        self.calculate_metrics()

        print(f"Num Trades: {self.num_trades}")
        print(f"Balance: {self.balance}")

bb1 = BacktestBase('data/AAPL_data.csv', 10000)
print("=== SMA Strategy ===")
bb1.run_sma_strat(42, 252)

print("\n=== Mean Reversion Strategy ===")
bb2 = BacktestBase('data/AAPL_data.csv', 10000)
bb2.run_mean_reversion(lookback=50, threshold=2.0)