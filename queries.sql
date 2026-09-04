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