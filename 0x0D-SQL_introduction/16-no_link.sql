-- List all records of the table second_table without rows without a name value
SELECT * FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
