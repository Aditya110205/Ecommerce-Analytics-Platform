SELECT
    c.customer_id,
    c.name,
    SUM(f.amount) AS total_spent
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.name
ORDER BY total_spent DESC
LIMIT 10;