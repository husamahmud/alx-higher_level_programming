-- lists all the cities of California that can be found
SELECT
	id, name
FROM
	states
WHERE
	name = `California`
ORDER BY
	id DESC;
