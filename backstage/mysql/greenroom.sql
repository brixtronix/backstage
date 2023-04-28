-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema greenroom
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema greenroom
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `greenroom` DEFAULT CHARACTER SET utf8 ;
USE `greenroom` ;

-- -----------------------------------------------------
-- Table `greenroom`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(255) NULL,
  `biography` LONGTEXT NULL,
  `avatar` LONGBLOB NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post` LONGTEXT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`likes` (
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`post_id`, `user_id`),
  INDEX `fk_posts_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_posts_has_users_posts1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_has_users_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `greenroom`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`chops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`chops` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `skill` VARCHAR(255) NULL,
  `studied_for` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_chops_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_chops_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`ups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`ups` (
  `user_id` INT NOT NULL,
  `chop_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `chop_id`),
  INDEX `fk_users_has_chops_chops1_idx` (`chop_id` ASC) VISIBLE,
  INDEX `fk_users_has_chops_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_chops_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_chops_chops1`
    FOREIGN KEY (`chop_id`)
    REFERENCES `greenroom`.`chops` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`projects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` LONGTEXT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_projects_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_projects_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`releases`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`releases` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `description` LONGTEXT NULL,
  `release_date` DATETIME NULL,
  `project_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_releases_projects2_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_releases_projects2`
    FOREIGN KEY (`project_id`)
    REFERENCES `greenroom`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`gigs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`gigs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `description` LONGTEXT NULL,
  `date` DATETIME NULL,
  `project_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_gigs_projects1_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_gigs_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `greenroom`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `greenroom`.`media`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `greenroom`.`media` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `description` LONGTEXT NULL,
  `photo` LONGBLOB NULL,
  `video` LONGBLOB NULL,
  `user_id` INT NOT NULL,
  `project_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_media_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_media_projects1_idx` (`project_id` ASC) VISIBLE,
  CONSTRAINT `fk_media_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `greenroom`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_media_projects1`
    FOREIGN KEY (`project_id`)
    REFERENCES `greenroom`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
