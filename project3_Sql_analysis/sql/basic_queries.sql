SELECT * FROM dataset LIMIT 10;

SELECT COUNT(*) AS total_orders
FROM dataset;

SELECT DISTINCT Product
FROM dataset;

SELECT OrderID, Product, TotalPrice
FROM dataset
ORDER BY TotalPrice DESC
LIMIT 10;
