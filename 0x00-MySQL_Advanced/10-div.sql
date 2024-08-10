-- create a function SafeDiv that divides and returns
-- first by sec num or 0 if second num is 0


DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC  -- returns the same results for the same parameters
BEGIN
	DECLARE val FLOAT;
	IF b = 0 THEN RETURN 0;
	ELSE
		SET val = a / b;
		RETURN val;
	END IF;
END
//

DELIMITER ;
