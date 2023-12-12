-- displays the average temperature by city ordered by temperature
SELECT
	city,
	AVG(VALUE) AS avg_temp
FROM
	temperatures
GROUP BY
	city
ORDER BY
	avg_temp DESC;
