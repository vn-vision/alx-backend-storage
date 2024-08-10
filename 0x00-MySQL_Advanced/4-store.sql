-- creates trigger that decreases quantity of an item
-- after adding a new order. Item quantity can be negative

DROP TRIGGER IF EXISTS new_order;
DELIMITER //

CREATE TRIGGER new_order
AFTER INSERT ON holberton.orders
FOR EACH ROW
BEGIN
	UPDATE holberton.items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END

//

DELIMITER ;
