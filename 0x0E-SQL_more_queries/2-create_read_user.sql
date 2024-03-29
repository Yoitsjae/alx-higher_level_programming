-- 2-create_read_user.sql

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant USAGE on all databases to the user
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grant SELECT privilege on the hbtn_0d_2 database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
