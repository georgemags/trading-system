import pandas as pd
import yfinance as yf

symbols = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'RKLB', 'AMD', 'JPM',
'AVGO', 'META', 'TSM']

results = []

strategies = [
    ('sma', {'sma1': 42, 'sma2': 252}),
    ('mean_rev', {'lookback': 50, 'threshold': 2.0}),
    ('momentum', {'lookback': 20, 'threshold': 0.02})
]

for symbol in symbols:
    try:
        stock_data = yf.download(symbol, period='2y')

        close_data = stock_data[['Close']].copy()
        close_data.columns = ['Close']

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
        self.symbol = filename.split("/")[1].split("_")[0]

    def get_data(self):
        self.data = pd.read_csv(self.filename, index_col=0, parse_dates=True)

    def place_buy_order(self, bar, units = None, amount = None):
        """ Places a buy order of specified ticket at given day(bar) and the amount

        Args:
            bar (int): given day of stock market
            units (int, optional): How many shares of stock. Defaults to None.
            amount (int, optional): Amount of money. Defaults to None.
        """        
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
        """ Places a sell order of specified ticket at given day(bar) and the units

        Args:
            bar (int): given day of stock market
            units (int, optional): How many shares of stock. Defaults to None.
            amount (int, optional): Amount of money. Defaults to None.
        """        
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
        """ Close out of current positions
        """        
        if self.position == 1:
            last_bar = len(self.data) - 1
            self.place_sell_order(last_bar, units = self.units)


    def run_sma_strat(self, SMA1, SMA2):
        """Runs SMA(Simple Moving Average) strategy which starts looking back
        at 42 days for SMA1 and comparing price for those days to lookback days 
        of 252.
        Will trigger a buy order if the SMA1 price is greater than SMA2 and sell
        order if SMA1 price is less than SMA2

        Args:
            SMA1 (int): Simple moving average across how many input days
            SMA2 (int): Simple moving average across how many input days
        """        
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

        print("=== SMA Strategy ===")
        print(f"Stock: {self.symbol }\n")


    def calculate_metrics(self):
        """Calculates metrics of stock with total return, sharpe ratio and max drawdown

        Prints:
            int: Total Return as a percentage, Sharpe Ratio and Max Drawdown
        """        
        self.total_return = ((self.balance - self.initial_amount) /
self.initial_amount) * 100
        self.data['daily_returns'] = self.data['Close'].pct_change()

        avg_daily_returns = self.data['daily_returns'].mean()
        std_daily_returns = self.data['daily_returns'].std()
        self.sharpe_ratio = avg_daily_returns/std_daily_returns

        running_max = self.data['Close'].expanding().max()
        drawdown = (self.data['Close'] - running_max) / running_max
        self.max_drawdown = drawdown.min() * 100

        print(f"Total Return: {self.total_return:.2f}%")
        print(f"Sharpe Ratio: {self.sharpe_ratio:.2f}")
        print(f"Max Drawdown: {self.max_drawdown:.2f}%")


    def run_mean_reversion(self, lookback = 50, threshold = 2.0):
        """Runs mean reversion strategy which triggers a buy order if the price 
        during the lookback days(50) is less than the lower band and a sell order
        if the price is higher than the upper band

        Args:
            lookback (int, optional): How many days to go back to. Defaults to 50.
            threshold (float, optional): Chosen percentage. Defaults to 2.0.
        """        
        rolling_mean = self.data['Close'].rolling(lookback).mean()
        rolling_std_dev = self.data['Close'].rolling(lookback).std()
        lower_band = rolling_mean - (threshold * rolling_std_dev)
        upper_band = rolling_mean + (threshold * rolling_std_dev)
        self.position = 0
        self.num_trades = 0

        for bar in range(lookback, len(self.data)):
            price = self.data["Close"].iloc[bar]
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

        print("=== Mean Reversion Strategy ===")
        print(f"Stock: {self.symbol }\n")

    def run_momentum(self, lookback=20, threshold = 0.02):
        """Runs a momentum strategy which triggers a buy order if the pct change of 
        a stock price is greater than the threshold and sell order if the pct change of a 
        stock price is less than the threshold

        Args:
            lookback (int, optional): How many days to go back to. Defaults to 20.
            threshold (float, optional): Chosen percentage. Defaults to 0.02.
        """        
        self.position = 0
        self.num_trades = 0

        self.data["momentum"] = self.data["Close"].pct_change(lookback)

        for bar in range(lookback, len(self.data)):
            momentum = self.data["momentum"].iloc[bar]
            if self.position == 0:
                if momentum > threshold:
                    self.place_buy_order(bar, amount = self.balance)
                    self.position = 1
            elif self.position == 1:
                if momentum < -threshold:
                    self.place_sell_order(bar, units = self.units)
                    self.position = 0

        self.close_out()
        self.calculate_metrics()
        
        print(f"Num Trades: {self.num_trades}")
        print(f"Balance: {self.balance}")

        print("=== Momentum Strategy ===")
        print(f"Stock: {self.symbol }\n")

for symbol in symbols:
    for strat_name, params in strategies:
        bb = BacktestBase(f'data/{symbol}_data.csv', 10000)
        
        if strat_name == 'sma':
            bb.run_sma_strat(params['sma1'], params['sma2'])
        elif strat_name == 'mean_rev':
            bb.run_mean_reversion(params['lookback'], params['threshold'])
        elif strat_name == 'momentum':
            bb.run_momentum(params['lookback'], params['threshold'])
        
        results.append({
            'Symbol': symbol,
            'Strategy': strat_name,
            'Return %': round(bb.total_return,2),
            'Sharpe': round(bb.sharpe_ratio,2),
            'Trades': round(bb.num_trades,2)
        })

df = pd.DataFrame(results)
print(df.to_string())
df.to_csv('results.csv')