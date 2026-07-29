import pandas as pd
import yfinance as yf

symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'RKLB', 'AMD', 'JPM', 'AVGO', 'META', 'TSM']

for symbol in symbols:
    try:
        stock_data = yf.download(symbol, period='1y')
        
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
        self.ftc = ftc  # Store fixed transaction cost
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



bb = BacktestBase('data/AAPL_data.csv', 10000)
print(bb.data.head())
print(f"Initial Balance: {bb.balance}")
bb.place_buy_order(bar = 42, units = 10)
print(f"After buy:  {bb.balance}")
bb.place_sell_order(bar = 56, units= bb.units)
print(f"After sell: {bb.balance}")