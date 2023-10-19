-- Assuming the table is named 'temperatures' and has columns 'state' and 'temperature'
SELECT state, MAX(temperature) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
