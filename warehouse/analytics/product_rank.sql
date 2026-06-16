SELECT
    p.product_name,
    SUM(f.amount) AS revenue,
    RANK() OVER(
        ORDER BY SUM(f.amount) DESC
    ) AS revenue_rank
FROM fact_sales f
JOIN dim_product p
    ON f.product_id = p.product_id
GROUP BY p.product_name;