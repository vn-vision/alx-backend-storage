-- create trigger that resets attribute valid_email
-- only when the email has been changed

DELIMITER //

CREATE TRIGGER valid
BEFORE UPDATE ON holberton.users
-- before updating the users table, check if the new email is different from the last
-- change value to 1 if it changed
FOR EACH ROW
	BEGIN
		IF NEW.email <> OLD.email THEN
			-- if the new email is different from the old one
			-- toggle the value: boolean 1 | 0
			SET NEW.valid_email = IF(OLD.valid_email = 1, 0, 1);
		END IF;
	END;

	//
DELIMITER ;
