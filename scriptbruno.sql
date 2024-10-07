-- MySQL Workbench Synchronization
-- Generated: 2024-10-07 11:37
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Ambiente

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `caso`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

ALTER TABLE `caso`.`donaciones` 
DROP FOREIGN KEY `fk_donaciones_formu_dona_obj1`;

ALTER TABLE `caso`.`comentarios` 
DROP FOREIGN KEY `fk_comentarios_usuario`;

ALTER TABLE `caso`.`usuario` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
CHANGE COLUMN `idusuario` `idusuario` INT(11) NOT NULL AUTO_INCREMENT ;

ALTER TABLE `caso`.`donaciones` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
CHANGE COLUMN `iddonaciones` `iddonaciones` INT(11) NOT NULL AUTO_INCREMENT ,
ADD INDEX `fk_donaciones_usuario1_idx` (`usuario_idusuario` ) ,
ADD INDEX `fk_donaciones_formu_dona_obj1_idx` (`formu_dona_obj_id_donante` ) ,
DROP INDEX `fk_donaciones_formu_dona_obj1_idx` ,
DROP INDEX `fk_donaciones_usuario1_idx` ;
;

ALTER TABLE `caso`.`comentarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
CHANGE COLUMN `id_comentarios` `id_comentarios` INT(11) NOT NULL AUTO_INCREMENT ,
ADD INDEX `fk_comentarios_usuario_idx` (`usuario_idusuario` ) ,
DROP INDEX `fk_comentarios_usuario_idx` ;
;

ALTER TABLE `caso`.`formu_dona_obj` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
DROP COLUMN `donacion`,
ADD COLUMN `obj_a_donar` VARCHAR(400) NOT NULL AFTER `apellido_donante`,
CHANGE COLUMN `id_donante` `id_donante` INT(11) NOT NULL AUTO_INCREMENT ;

ALTER TABLE `caso`.`donaciones` 
DROP FOREIGN KEY `fk_donaciones_usuario1`;

ALTER TABLE `caso`.`donaciones` ADD CONSTRAINT `fk_donaciones_usuario1`
  FOREIGN KEY (`usuario_idusuario`)
  REFERENCES `caso`.`usuario` (`idusuario`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_donaciones_formu_dona_obj1`
  FOREIGN KEY (`formu_dona_obj_id_donante`)
  REFERENCES `caso`.`formu_dona_obj` (`id_donante`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `caso`.`comentarios` 
ADD CONSTRAINT `fk_comentarios_usuario`
  FOREIGN KEY (`usuario_idusuario`)
  REFERENCES `caso`.`usuario` (`idusuario`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
