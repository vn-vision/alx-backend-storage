-- SQL Script that creates a vew need_meeting
-- lists all students that have a score under 80
-- no last meeting or more than 1 month

DELIMITER //
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
//
DELIMITER ;
