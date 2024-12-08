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
  CONSTRAINT `event_ibfk_1`
    FOREIGN KEY (`userID`)
    REFERENCES `meetup`.`user` (`userID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `userID` ON `meetup`.`event` (`userID` ASC) VISIBLE;

CREATE INDEX `event_info_index` ON `meetup`.`event` (`eventName` ASC, `eventDay` ASC, `eventTime` ASC) VISIBLE;


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

CREATE INDEX `eventID` ON `meetup`.`invitedto` (`eventID` ASC) VISIBLE;


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

CREATE INDEX `userID` ON `meetup`.`task` (`userID` ASC) VISIBLE;

USE `meetup` ;

-- -----------------------------------------------------
-- procedure add_activity
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_activity`(IN name VARCHAR(20), IN eID VARCHAR(8))
BEGIN
	-- Add an activity into the activity table
	INSERT INTO activity(activityName, eventID)
    VALUES(name, eID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure add_plus_one
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_plus_one`(IN uID VARCHAR(8), IN guestName VARCHAR(20))
BEGIN
	-- Declare variable
	DECLARE hasPlusOne INT;
    
    -- See if user has a plus one already
    SELECT COUNT(*) INTO hasPlusOne
    FROM plus_one
    WHERE userID=userID;
    
    -- If no plus one, add to plus_one table
    IF (hasPlusOne = 0) THEN
		INSERT INTO plus_one(name, userID)
		VALUES(guestName, uID);
	-- Else, update plus one with new person
	ELSE
		UPDATE plus_one
        SET name=guestName
        WHERE userID=userID;
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
	-- Insert a new task into the task table
	INSERT INTO task(taskName, cost, userID, activityName, eventID)
    VALUES(name, taskCost, uID, aName, eID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure create_event
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_event`(IN eID VARCHAR(8), IN eName VARCHAR(20), IN eDay VARCHAR(15), IN eTime VARCHAR(10), IN eBudget FLOAT, IN uID VARCHAR(8))
BEGIN
	-- Insert a new event into the event table
	INSERT INTO event(eventID, eventName, eventDay, eventTime, budget, userID) 
    VALUES(eID, eName, eDay, eTime, eBudget, uID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure create_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_user`(IN uID VARCHAR(8), IN fName VARCHAR(15), IN lName VARCHAR(15), IN e VARCHAR(20), IN p VARCHAR(15), IN pass VARCHAR(25))
BEGIN
	-- Insert a new user into the user table
	INSERT INTO user(userID, firstName, lastName, email, phone, password)
    VALUES(uID, fName, lName, e, p, pass);
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
	-- Return true if have plus one, false otherwise
    DECLARE hasPlusOne INT;
    
    -- See if user has a plus one
    SELECT COUNT(*) INTO hasPlusOne
	FROM plus_one
    WHERE userID=userID;
    
    -- If they have a plus one, return true
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
CREATE DEFINER=`root`@`localhost` PROCEDURE `invite_guest`(IN guestID VARCHAR(8), IN eID VARCHAR(8))
BEGIN
	-- Declare variable
	DECLARE userName VARCHAR(8);
    
    -- Grab the user from the user table
	SELECT userID INTO userName
    FROM user
    WHERE userID = guestID;
    
    -- If the user has an account, invite them to the event
    IF userName IS NOT NULL THEN
		INSERT INTO invitedto(userID, eventID) VALUES(userName, eID);
	-- Else, raise an error
	ELSE
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Guest does not have a valid user account';
    END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_accepted_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_accepted_invitees`(IN eID VARCHAR(8))
BEGIN
	-- Grab the contact info for all accepted invitees
	SELECT firstName, lastName, email, phone
    FROM user u JOIN invitedto i ON u.userID=i.userID
    WHERE i.eventID=eID AND rsvp='Going'
    ORDER BY firstName ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_accepted_invites_for_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_accepted_invites_for_user`(IN uID VARCHAR(8))
BEGIN
	-- Grab the all accepted invite event information for a given user
	SELECT e.eventID, e.eventName, e.eventDay, e.eventTime FROM event e
		JOIN invitedto i ON e.eventID=i.eventID
    WHERE i.userID=uID AND rsvp='Going'
    ORDER BY e.eventName, e.eventDay, e.eventTime ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_assigned_tasks_for_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_assigned_tasks_for_user`(IN eID VARCHAR(8), IN uID VARCHAR(8))
BEGIN
	-- Grab all tasks assigned to a user for an event
    SELECT taskName FROM task
    WHERE userID=uID and eventID=eID
    ORDER BY taskName ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_hosted_events_for_user
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_hosted_events_for_user`(IN uID VARCHAR(8))
BEGIN
	-- Grab the all hosted event information for a given user
	SELECT eventID, eventName, eventDay, eventTime FROM event e 
		JOIN user u ON e.userID=u.userID
	WHERE u.userID=uID
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
	-- Grab all pending invited event information for user
	SELECT e.eventID, e.eventName, e.eventDay, e.eventTime FROM event e 
		JOIN invitedto i ON e.eventID=i.eventID
	WHERE i.userID=uID AND i.rsvp is null
	ORDER BY eventName, eventDay, eventTime ASC;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure list_all_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `list_all_invitees`(IN eID VARCHAR(8))
BEGIN
	-- Grab contact information for all invitees of an event
	SELECT firstName, lastName, email, phone
    FROM user u JOIN invitedto i ON u.userID=i.userID
    WHERE i.eventID=eID
    ORDER BY firstName;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function num_accepted_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `num_accepted_invitees`(eID VARCHAR(8)) RETURNS int
    DETERMINISTIC
BEGIN
	-- Declare variable
	DECLARE invitee_count INT;
    
    -- Grab total number of accepted invitees
    SELECT COUNT(*) INTO invitee_count
    FROM invitedto
    WHERE eID=eventID and rsvp='Going';
    
    -- If no accepted invitees, set it to 0
    IF invitee_count IS NULL THEN
		SET invitee_count = 0;
	END IF;
    
    -- Return count
    RETURN invitee_count;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function num_invitees
-- -----------------------------------------------------

DELIMITER $$
USE `meetup`$$
CREATE DEFINER=`root`@`localhost` FUNCTION `num_invitees`(eID VARCHAR(8)) RETURNS int
    DETERMINISTIC
BEGIN
	-- Declare variable
	DECLARE invitee_count INT;
    
    -- Grab total number of invitees
    SELECT COUNT(*) INTO invitee_count
    FROM invitedto
    WHERE eID=eventID;
    
    -- If no invitees, set it to 0
    IF invitee_count IS NULL THEN
		SET invitee_count = 0;
	END IF;
    
    -- Return count
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
	-- Declare variable to keep track of number of invites
	DECLARE inviteCount INT;
    
	-- Return True if pending invites, false otherwise
    SELECT COUNT(*) INTO inviteCount 
    FROM invitedto
    WHERE userID=uID AND rsvp IS NULL;
    
    -- If there are pending invites, return true
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
CREATE DEFINER=`root`@`localhost` PROCEDURE `rsvp_for_event`(IN uID VARCHAR(8), IN eID VARCHAR(8), IN response VARCHAR(10))
BEGIN
	-- Update RSVP for an event if they are Going or Not Going
	UPDATE invitedto 
    SET rsvp=response
    WHERE uID=userID AND eID=eventID;
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
	-- Declare variable
	DECLARE validUser INT;

	-- Grab if user exists
	SELECT COUNT(*) INTO validUser
    FROM user
    WHERE userID=loginUserID AND password=loginPassword;
    
	-- If user exists, return true
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
TRIGGER `meetup`.`event_BEFORE_INSERT`
BEFORE INSERT ON `meetup`.`event`
FOR EACH ROW
BEGIN
	-- Verify new budget is a positive number
    IF NEW.budget < 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'EVENT.budget must be greater than 0.';
    END IF;
END$$

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
	-- Add activity cost difference to event total cost
    UPDATE event
    SET totalCost = totalCost - OLD.activityTotalCost + NEW.activityTotalCost
    WHERE eventID = NEW.eventID;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`invitedto_BEFORE_UPDATE`
BEFORE UPDATE ON `meetup`.`invitedto`
FOR EACH ROW
BEGIN
	-- Verify when RSVPing, response is either 'Going' or 'Not Going'
    IF NEW.rsvp NOT IN ('Going', 'Not Going') THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'INVITEDTO.rsvp must be either "Going" or "Not Going"';
    END IF;
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
    -- Add task cost difference to activity total cost
    UPDATE activity
    SET activityTotalCost = activityTotalCost - OLD.cost + NEW.cost
    WHERE activityName = NEW.activityName;
END$$

USE `meetup`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `meetup`.`task_BEFORE_INSERT`
BEFORE INSERT ON `meetup`.`task`
FOR EACH ROW
BEGIN
	-- Declare variable
    DECLARE going INT;
    
    -- Verify cost of task is positive
    IF NEW.cost < 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'TASK.cost must be 0 or greater';
	END IF;
    
    -- See if the user has accepted invite
    SELECT count(*) INTO going FROM invitedto
	WHERE NEW.userID=userID AND NEW.eventID=eventID AND rsvp='Going';
    
    -- If not, send error message
    IF going = 0 THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'TASK.userID must accept invite to event first';
    END IF;
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
