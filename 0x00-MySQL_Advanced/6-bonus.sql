-- creates stored procedure AddBonus
-- it adds a new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN 
-- declare variable to store project_id
DECLARE project_id INT;

-- initialize project ID to NULL
SET project_id = NULL;

SELECT id INTO project_id FROM projects WHERE name = project_name;

-- check if the project exists
IF project_id IS NULL THEN
	INSERT INTO projects(name) VALUES (project_name);
	
	-- set the id to the last insert, the new project_id
	SET project_id = LAST_INSERT_ID();
END IF;

INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, project_id, score);

END
//
DELIMITER ;
