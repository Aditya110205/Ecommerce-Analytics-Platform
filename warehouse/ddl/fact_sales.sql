CREATE TABLE IF NOT EXISTS fact_sales
(
    order_id INT PRIMARY KEY,

    customer_id INT,

    product_id INT,

    quantity INT,

    amount DECIMAL(10,2),

    created_at DATETIME
);