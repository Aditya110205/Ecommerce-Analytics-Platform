CREATE TABLE IF NOT EXISTS etl_metadata
(
    pipeline_name VARCHAR(100) PRIMARY KEY,
    last_processed_id INT NOT NULL DEFAULT 0
);