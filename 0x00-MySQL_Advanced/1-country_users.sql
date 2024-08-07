-- creates a table users with attributes:
-- id, email, name, country. If users exists script should not fail
-- country enumeration: us, co, tn (countries to choose from)

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(id),
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM("US", "CO", "TN") NOT NULL
);

-- if enum value is declared not null, default value
-- is the first element of the list of permitted values 
