import pandas as pd
from sqlalchemy import create_engine

# Update these to match what you set during MySQL install
USER = "root"
PASSWORD = "Ghostblade21$"
HOST = "localhost"
DATABASE = "backtest"

# Connection string format: mysql+mysqlconnector://user:password@host/database
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}")

df = pd.read_csv("results.csv")
df.to_sql("results", engine, if_exists="replace", index=False)

print(f"Loaded {len(df)} rows into MySQL.")

# Quick sanity check query
with engine.connect() as conn:
    result = conn.exec_driver_sql("SELECT Symbol, Strategy, Sharpe FROM results ORDER BY Sharpe DESC LIMIT 5")
    for row in result:
        print(row)
