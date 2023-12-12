-- lists all records of the table second_table
SELECT
	score, name
WHERE
	name IS NOT NULL
ORDER BY
	score;
