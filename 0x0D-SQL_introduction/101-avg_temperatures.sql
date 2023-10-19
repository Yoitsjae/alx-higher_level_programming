-- Assuming the table is named 'temperatures' and has columns 'city' and 'temperature'
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
