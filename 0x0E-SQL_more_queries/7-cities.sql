-- 7-cities.sql

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table cities if not exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert data into cities
INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco');

-- Display the contents of the table
SELECT * FROM cities;

-- Attempt to insert data violating FOREIGN KEY constraint
INSERT INTO cities (state_id, name) VALUES (10, 'Paris');
