
SELECT * FROM sales;


SELECT *
FROM sales
WHERE region = 'East';

SELECT *
FROM sales
WHERE total_price > 500;


SELECT *
FROM sales
ORDER BY total_price DESC;


SELECT category, SUM(total_price) AS total_revenue
FROM sales
GROUP BY category;


SELECT AVG(total_price) AS average_order_value
FROM sales;


SELECT COUNT(*) AS total_orders
FROM sales;


SELECT
    customer_name,
    SUM(total_price) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 5;

SELECT
    order_id,
    customer_name,
    total_price,
    CASE
        WHEN total_price >= 500 THEN 'High Value'
        WHEN total_price >= 200 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS order_type
FROM sales;

SELECT
    sales.order_id,
    sales.customer_name,
    sales.total_price,
    customer_summary.total_orders,
    customer_summary.total_spent
FROM sales
JOIN customer_summary
ON sales.customer_name = customer_summary.customer_name;


SELECT *
FROM sales
WHERE total_price > (
    SELECT AVG(total_price)
    FROM sales
);