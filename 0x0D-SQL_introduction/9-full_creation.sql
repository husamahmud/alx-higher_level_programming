-- creates a table second_table in the database and add multiples rows
CREATE TABLE
	IF NOT EXISTS hbtn_0c_0.second_table (
		id INT AUTO_INCREMENT,
		name VARCHAR(256),
		score INT,
		PRIMARY KEY (id)
	);

INSERT INTO
	hbtn_0c_0.second_table (name, score)
VALUES
	('John', 10),
	('Alex', 3),
	('Bob', 14),
	('George', 8);
