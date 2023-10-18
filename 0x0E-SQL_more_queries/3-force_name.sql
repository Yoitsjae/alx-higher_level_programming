-- 3-force_name.sql

USE hbtn_0d_2;

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
