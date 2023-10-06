-- 2.1) show total revenue in year 2020 in Chennai
SELECT SUM(cost_price) as revenue
FROM transactions
JOIN markets
ON transactions.market_code = markets.markets_code
WHERE markets_name = "Chennai" AND YEAR(order_date) = "2020";

-- 2.2) show total revenue in year 2020, January Month
SELECT SUM(cost_price) as revenue
FROM transactions
WHERE MONTH(order_date)= "1" AND YEAR(order_date) = "2020";

-- 2.3) show the most profitable markets_name and total sales_amount for them.
SELECT SUM(cost_price) as revenue, SUM(sales_amount) as sales_amount, markets_name
FROM transactions
JOIN markets
ON transactions.market_code = markets.markets_code
GROUP BY markets_name
ORDER BY revenue DESC
LIMIT 1;

-- 2.4) show the customer who bought the most product Prod048.
SELECT custmer_name
FROM transactions
JOIN customers
ON transactions.customer_code = customers.customer_code
WHERE product_code = "Prod048"
GROUP BY custmer_name;

-- 2.5) show the average number of products sold per month
SELECT YEAR(Order_date) as year_date, MONTH(Order_date) as month_date, COUNT(sales_qty) AS sales_count 
FROM transactions 
GROUP BY year_date, month_date;

-- 2.6) show top 10 customers who have made the most purchases in 2017
SELECT custmer_name, COUNT(sales_qty) as purchases_amount 
FROM transactions
JOIN customers
ON transactions.customer_code = customers.customer_code
WHERE YEAR(order_date) = "2017"
GROUP BY custmer_name
ORDER BY purchases_amount DESC
LIMIT 10;