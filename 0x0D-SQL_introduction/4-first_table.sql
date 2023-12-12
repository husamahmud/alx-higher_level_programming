-- creates a table called first_table in the current database
CREATE TABLE
	IF NOT EXISTS first_table (
		id INT AUTO_INCREMENT,
		name VARCHAR(256),
		PRIMARY KEY (id)
	);
