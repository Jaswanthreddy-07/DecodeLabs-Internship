SELECT AVG(TotalPrice) AS average_order_value
FROM dataset;

SELECT MAX(TotalPrice) AS highest_order
FROM dataset;

SELECT MIN(TotalPrice) AS lowest_order
FROM dataset;

SELECT Product, COUNT(*) AS total_orders
FROM dataset
GROUP BY Product
ORDER BY total_orders DESC;

SELECT PaymentMethod, COUNT(*) AS usage_count
FROM dataset
GROUP BY PaymentMethod;

SELECT OrderStatus, COUNT(*) AS total_orders
FROM dataset
GROUP BY OrderStatus;

SELECT ReferralSource, SUM(TotalPrice) AS revenue
FROM dataset
GROUP BY ReferralSource
ORDER BY revenue DESC;

SELECT Product, AVG(Quantity) AS avg_quantity
FROM dataset
GROUP BY Product;
