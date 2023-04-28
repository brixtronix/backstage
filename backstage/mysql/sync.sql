-- MySQL Workbench Synchronization
-- Generated: 2023-04-20 00:37
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: LocalAdmin

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `greenroom`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

ALTER TABLE `greenroom`.`ups` 
DROP FOREIGN KEY `fk_users_has_chops_users1`;

ALTER TABLE `greenroom`.`media` 
DROP FOREIGN KEY `fk_media_users1`;

ALTER TABLE `greenroom`.`users` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

CREATE TABLE IF NOT EXISTS `greenroom`.`notations` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `notation` LONGTEXT NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

ALTER TABLE `greenroom`.`likes` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
CHANGE COLUMN `post_id` `notation_id` INT(11) NOT NULL ;

ALTER TABLE `greenroom`.`chops` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `greenroom`.`ups` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `greenroom`.`projects` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `greenroom`.`releases` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `greenroom`.`gigs` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `greenroom`.`media` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

DROP TABLE IF EXISTS `greenroom`.`notations` ;

ALTER TABLE `greenroom`.`likes` 
ADD CONSTRAINT `fk_posts_has_users_posts1`
  FOREIGN KEY (`notation_id`)
  REFERENCES `greenroom`.`notations` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_posts_has_users_users1`
  FOREIGN KEY (`user_id`)
  REFERENCES `greenroom`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `greenroom`.`chops` 
ADD CONSTRAINT `fk_chops_users1`
  FOREIGN KEY (`user_id`)
  REFERENCES `greenroom`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `greenroom`.`ups` 
ADD CONSTRAINT `fk_users_has_chops_users1`
  FOREIGN KEY (`user_id`)
  REFERENCES `greenroom`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_users_has_chops_chops1`
  FOREIGN KEY (`chop_id`)
  REFERENCES `greenroom`.`chops` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `greenroom`.`projects` 
ADD CONSTRAINT `fk_projects_users1`
  FOREIGN KEY (`user_id`)
  REFERENCES `greenroom`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `greenroom`.`releases` 
ADD CONSTRAINT `fk_releases_projects2`
  FOREIGN KEY (`project_id`)
  REFERENCES `greenroom`.`projects` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `greenroom`.`gigs` 
ADD CONSTRAINT `fk_gigs_projects1`
  FOREIGN KEY (`project_id`)
  REFERENCES `greenroom`.`projects` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `greenroom`.`media` 
ADD CONSTRAINT `fk_media_users1`
  FOREIGN KEY (`user_id`)
  REFERENCES `greenroom`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_media_projects1`
  FOREIGN KEY (`project_id`)
  REFERENCES `greenroom`.`projects` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
