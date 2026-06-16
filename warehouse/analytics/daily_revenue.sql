SELECT
    DATE(created_at) AS sales_date,
    SUM(amount) AS total_revenue
FROM fact_sales
GROUP BY DATE(created_at)
ORDER BY sales_date;