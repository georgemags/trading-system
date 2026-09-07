-- SQL Analysis of Backtest Results
-- Database: backtest, Table: results
-- Loaded via load_to_mysql.py from results.csv
 
-- 1. Momentum strategy results, sorted by return (highest first)
SELECT * 
FROM backtest.results
WHERE Strategy = 'momentum'
ORDER BY `Return %` DESC;
 
-- 2. Average return by strategy type, ranked highest to lowest
SELECT strategy, AVG(`return %`) AS avg_return
FROM backtest.results
GROUP BY strategy
ORDER BY avg_return DESC;
 
-- 3. Count of positive vs. negative Sharpe ratios across all rows
SELECT 
    SUM(CASE WHEN sharpe > 0 THEN 1 ELSE 0 END) AS positive_count,
    SUM(CASE WHEN sharpe < 0 THEN 1 ELSE 0 END) AS negative_count
FROM backtest.results;

-- 4. Which strategies performed the best on avg based on sharpe ratio
SELECT strategy, AVG(sharpe) AS avg_sharpe
FROM backtest.results
GROUP BY strategy
HAVING AVG(sharpe) > 0.5
ORDER BY avg_sharpe DESC;

-- 5. Which strategy performed the worst according to the symbol
SELECT symbol, MIN(sharpe) as worst_sharpe
FROM backtest.results
GROUP BY symbol

-- 6. Difference between worst and best sharpe ratios on strategy by each symbol
SELECT symbol, round(MAX(sharpe) - MIN(sharpe), 2) as sharpe_diff
FROM backtest.results
GROUP BY symbol
ORDER BY sharpe_diff desc