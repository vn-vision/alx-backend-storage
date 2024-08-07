-- creates a table users with attributes:
-- id, email, name. If users exists script should not fail

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id),
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
