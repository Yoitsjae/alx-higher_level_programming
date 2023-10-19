-- Assuming the table is named 'temperatures' and has columns 'city', 'temperature', 'month'
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
