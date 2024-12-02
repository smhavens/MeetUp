-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema meetup
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema meetup
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `meetup` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `meetup` ;

-- -----------------------------------------------------
-- Table `meetup`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meetup`.`user` (
  `userID` VARCHAR(8) NOT NULL,
  `firstName` VARCHAR(15) NULL DEFAULT NULL,
  `lastName` VARCHAR(15) NULL DEFAULT NULL,
  `email` VARCHAR(20) NULL DEFAULT NULL,
  `phone` VARCHAR(15) NULL DEFAULT NULL,
  `password` VARCHAR(25) NULL DEFAULT NULL,
  PRIMARY KEY (`userID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `meetup`.`event`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meetup`.`event` (
  `eventID` VARCHAR(8) NOT NULL,
  `eventName` VARCHAR(20) NOT NULL,
  `eventDay` VARCHAR(15) NOT NULL,
  `eventTime` VARCHAR(10) NOT NULL,
  `budget` FLOAT NULL DEFAULT NULL,
  `totalCost` FLOAT NULL DEFAULT '0',
  `userID` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`eventID`),
  INDEX `userID` (`userID` ASC) VISIBLE,
  CONSTRAINT `event_ibfk_1`
    FOREIGN KEY (`userID`)
    REFERENCES `meetup`.`user` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `meetup`.`activity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meetup`.`activity` (
  `activityName` VARCHAR(20) NOT NULL,
  `activityTotalCost` FLOAT NULL DEFAULT '0',
  `eventId` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`eventId`, `activityName`),
  CONSTRAINT `activity_ibfk_1`
    FOREIGN KEY (`eventId`)
    REFERENCES `meetup`.`event` (`eventID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `meetup`.`invitedto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meetup`.`invitedto` (
  `userID` VARCHAR(8) NOT NULL,
  `eventID` VARCHAR(8) NOT NULL,
  `rsvp` VARCHAR(10) NULL DEFAULT NULL,
  PRIMARY KEY (`userID`, `eventID`),
  INDEX `eventID` (`eventID` ASC) VISIBLE,
  CONSTRAINT `invitedto_ibfk_1`
    FOREIGN KEY (`userID`)
    REFERENCES `meetup`.`user` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `invitedto_ibfk_2`
    FOREIGN KEY (`eventID`)
    REFERENCES `meetup`.`event` (`eventID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `meetup`.`plus_one`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meetup`.`plus_one` (
  `name` VARCHAR(20) NOT NULL,
  `userID` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`userID`, `name`),
  CONSTRAINT `plus_one_ibfk_1`
    FOREIGN KEY (`userID`)
    REFERENCES `meetup`.`user` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `meetup`.`task`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `meetup`.`task` (
  `taskName` VARCHAR(8) NOT NULL,
  `cost` FLOAT NULL DEFAULT NULL,
  `userID` VARCHAR(8) NULL DEFAULT NULL,
  `activityName` VARCHAR(20) NOT NULL,
  `eventID` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`eventID`, `activityName`, `taskName`),
  INDEX `userID` (`userID` ASC) VISIBLE,
  CONSTRAINT `task_ibfk_1`
    FOREIGN KEY (`eventID` , `activityName`)
    REFERENCES `meetup`.`activity` (`eventId` , `activityName`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `task_ibfk_2`
    FOREIGN KEY (`userID`)
    REFERENCES `meetup`.`user` (`userID`)
    ON DELETE SET NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `meetup` ;

-- -----------------------------------------------------
-- procedure add_activity
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_activity`(IN name VARCHAR(20), IN eventID VARCHAR(8))
BEGIN
	INSERT INTO activity(activityName, eventID)
    VALUES(name, eventID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure add_plus_one
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_plus_one`(IN userID VARCHAR(8), IN guestName VARCHAR(20))
BEGIN
	DECLARE hasPlusOne INT;
    
    SELECT COUNT(*) INTO hasPlusOne
    FROM plus_one
    WHERE userID=userID;
    
    IF (hasPlusOne = 0) THEN
		INSERT INTO plus_one(name, userID)
		VALUES(guestName, userID);
	ELSE
		SET SQL_SAFE_UPDATES = 0;
		UPDATE plus_one
        SET name=guestName
        WHERE userID=userID;
        SET SQL_SAFE_UPDATES = 1;
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure add_task
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_task`(IN name VARCHAR(8), IN taskCost FLOAT, IN uID VARCHAR(8), IN aName VARCHAR(20), IN eID VARCHAR(8))
BEGIN
	SET SQL_SAFE_UPDATES = 0;
	INSERT INTO task(taskName, cost, userID, activityName, eventID)
    VALUES(name, taskCost, uID, aName, eID);
    SET SQL_SAFE_UPDATES = 1;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure create_event
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_event`(IN eventID VARCHAR(8), IN eventName VARCHAR(20), IN eventDay VARCHAR(15), IN eventTime VARCHAR(10), IN budget FLOAT, IN userID VARCHAR(8))
BEGIN
	INSERT INTO event(eventID, eventName, eventDay, eventTime, budget, userID) 
    VALUES(eventID, eventName, eventDay, eventTime, budget, userID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure create_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_user`(IN uID VARCHAR(8), IN fName VARCHAR(15), IN lName VARCHAR(15), IN e VARCHAR(20), IN p VARCHAR(15), IN pass VARCHAR(25))
BEGIN
	INSERT INTO user(userID, firstName, lastName, email, phone, password)
    VALUES(uID, fName, lName, e, p, pass);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function event_cost
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `event_cost`(eventID VARCHAR(8)) RETURNS float
    DETERMINISTIC
BEGIN
	DECLARE cost FLOAT;
    
    SELECT totalCost into cost
    FROM event
    WHERE eventID = eventID;
    
    IF cost IS NULL THEN
		SET cost = 0;
	END IF;
    
    RETURN cost;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function have_plus_one
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `have_plus_one`(userID VARCHAR(8)) RETURNS tinyint(1)
    DETERMINISTIC
BEGIN
	# Return true if have plus one, false otherwise
    DECLARE hasPlusOne INT;
    
    # See if user has a plus one
    SELECT COUNT(*) INTO hasPlusOne
	FROM plus_one
    WHERE userID=userID;
    
    # If they have a plus one, return true
    IF (hasPlusOne = 1) THEN
		RETURN TRUE;
	ELSE
		RETURN FALSE;
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure invite_guest
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `invite_guest`(IN guestID VARCHAR(8), IN eventID VARCHAR(8))
BEGIN
	DECLARE userName VARCHAR(8);
    
	SELECT userID INTO userName
    FROM user
    WHERE userID = guestID;
    
    INSERT INTO invitedto(userID, eventID) VALUES(userName, eventID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_accepted_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_accepted_invitees`(IN eventID VARCHAR(8))
BEGIN
	SELECT firstName, lastName, email, phone
    FROM user u JOIN invitedto i ON u.userID=i.userID
    WHERE i.eventID=eventID AND rsvp='Going'
    ORDER BY firstName;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_events_for_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_events_for_user`(IN userID VARCHAR(8))
BEGIN
	SELECT eventName, eventDay, eventTime FROM event e 
		JOIN user u ON e.userID=u.userID
	WHERE u.userID=userID
	ORDER BY eventName, eventDay, eventTime ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_hosted_events_for_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_hosted_events_for_user`(IN userID VARCHAR(8))
BEGIN
	SELECT eventID, eventName, eventDay, eventTime FROM event e 
		JOIN user u ON e.userID=u.userID
	WHERE u.userID=userID
	ORDER BY eventName, eventDay, eventTime ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_invited_to_events
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_invited_to_events`(IN uID VARCHAR(8))
BEGIN
	SELECT e.eventID, e.eventName, e.eventDay, e.eventTime FROM event e 
		JOIN invitedto i ON e.eventID=i.eventID
	WHERE i.userID=uID
	ORDER BY eventName, eventDay, eventTime ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_invitedto_and_hosted_events
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_invitedto_and_hosted_events`(IN uID VARCHAR(8))
BEGIN
	SELECT DISTINCT e.eventID, e.eventName, e.eventDay, e.eventTime 
    FROM event e LEFT JOIN invitedto i ON e.eventID=i.eventID
    WHERE i.userID = uID OR e.userID = uID
	ORDER BY e.eventName, e.eventDay, e.eventTime ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_invitees`(IN eventID VARCHAR(8))
BEGIN
	SELECT firstName, lastName, email, phone
    FROM user u JOIN invitedto i ON u.userID=i.userID
    WHERE i.eventID=eventID
    ORDER BY firstName;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function num_accepted_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `num_accepted_invitees`(eventID VARCHAR(8)) RETURNS int
    DETERMINISTIC
BEGIN
	DECLARE invitee_count INT;
    
    SELECT COUNT(*) INTO invitee_count
    FROM invitedto
    WHERE eventID=eventID and rsvp='Going';
    
    IF invitee_count IS NULL THEN
		SET invitee_count = 0;
	END IF;
    
    RETURN invitee_count;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function num_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `num_invitees`(eventID VARCHAR(8)) RETURNS int
    DETERMINISTIC
BEGIN
	DECLARE invitee_count INT;
    
    SELECT COUNT(*) INTO invitee_count
    FROM invitedto
    WHERE eventID=eventID;
    
    IF invitee_count IS NULL THEN
		SET invitee_count = 0;
	END IF;
    
    RETURN invitee_count;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function pending_invites
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `pending_invites`(uID VARCHAR(8)) RETURNS tinyint(1)
    DETERMINISTIC
BEGIN
	# Declare variable to keep track of number of invites
	DECLARE inviteCount INT;
    
	# Return True if pending invites, false otherwise
    SELECT COUNT(*) INTO inviteCount 
    FROM invitedto
    WHERE userID=uID AND rsvp IS NULL;
    
    # If there are pending invites, return true
    IF (inviteCount > 0) THEN
		RETURN TRUE;
	ELSE 
		RETURN FALSE;
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure rsvp_for_event
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `rsvp_for_event`(IN userID VARCHAR(8), IN eventID VARCHAR(8), IN response VARCHAR(10))
BEGIN
	IF (response IN ('Going', 'Not Going')) THEN
		SET SQL_SAFE_UPDATES = 0;
		UPDATE invitedto 
        SET rsvp=response
        WHERE userID=userID AND eventID=eventID;
        SET SQL_SAFE_UPDATES = 1;
	END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function valid_login
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `valid_login`(loginUserID VARCHAR(8), loginPassword VARCHAR(25)) RETURNS tinyint(1)
    DETERMINISTIC
BEGIN
	DECLARE validUser INT;

	SELECT COUNT(*) INTO validUser
    FROM user
    WHERE userID=loginUserID AND password=loginPassword;
    
	# If user exists, return true
    IF validUser = 0 THEN
		RETURN FALSE;
	ELSE
		RETURN TRUE;
	END IF;
END$$

DELIMITER ;
USE `meetup`;

DELIMITER $$
USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`activity_AFTER_DELETE`
AFTER DELETE ON `meetup`.`activity`
FOR EACH ROW
BEGIN
	-- Add activity cost to event total cost
    UPDATE event
    SET totalCost = totalCost - old.activityTotalCost
    WHERE eventID = OLD.eventID;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`activity_AFTER_INSERT`
AFTER INSERT ON `meetup`.`activity`
FOR EACH ROW
BEGIN
	-- Add activity cost to event total cost
    UPDATE event
    SET totalCost = totalCost + NEW.activityTotalCost
    WHERE eventID = NEW.eventID;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`activity_AFTER_UPDATE`
AFTER UPDATE ON `meetup`.`activity`
FOR EACH ROW
BEGIN
	-- Declare variable
	DECLARE costDifference FLOAT;
    
    IF OLD.activityTotalCost > NEW.activityTotalCost THEN
		-- Calculate the cost difference
		SET costDifference = NEW.activityTotalCost - OLD.activityTotalCost;
	ELSE
		-- Calculate the cost difference
		SET costDifference = OLD.activityTotalCost + NEW.activityTotalCost;
	END IF;
    
    -- Add activity cost difference to event total cost
    UPDATE event
    SET totalCost = totalCost + costDifference
    WHERE eventID = NEW.eventID;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`task_AFTER_DELETE`
AFTER DELETE ON `meetup`.`task`
FOR EACH ROW
BEGIN
	-- Subtract task cost to activity total cost
    UPDATE activity
    SET activityTotalCost = activityTotalCost - OLD.cost
    WHERE activityName = OLD.activityName;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`task_AFTER_INSERT`
AFTER INSERT ON `meetup`.`task`
FOR EACH ROW
BEGIN
	-- Add task cost to activity total cost
    UPDATE activity
    SET activityTotalCost = activityTotalCost + NEW.cost
    WHERE activityName = NEW.activityName;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`task_AFTER_UPDATE`
AFTER UPDATE ON `meetup`.`task`
FOR EACH ROW
BEGIN
	-- Declare variable
	DECLARE costDifference FLOAT;
    
    IF OLD.cost > NEW.cost THEN
		-- Calculate the cost difference
		SET costDifference = NEW.cost - OLD.cost;
	ELSE
		-- Calculate the cost difference
		SET costDifference = OLD.cost + NEW.cost;
	END IF;
    
    -- Add task cost difference to activity total cost
    UPDATE activity
    SET activityTotalCost = activityTotalCost + costDifference
    WHERE activityName = NEW.activityName;
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
