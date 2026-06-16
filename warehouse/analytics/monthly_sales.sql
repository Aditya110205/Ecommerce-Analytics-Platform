SELECT
    d.year,
    d.month,
    SUM(f.amount) AS total_revenue
FROM fact_sales f
JOIN dim_date d
    ON DATE(f.created_at) = d.date_key
GROUP BY
    d.year,
    d.month
ORDER BY
    d.year,
    d.month;