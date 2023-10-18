-- 6-states.sql

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table states if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data into states
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');

-- Display the contents of the table
SELECT * FROM states;
