CREATE TABLE IF NOT EXISTS dim_customer
(
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(100)
);