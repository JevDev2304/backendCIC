-- Configuración inicial de MySQL
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Creación del esquema de la aplicación
CREATE SCHEMA IF NOT EXISTS `my_app` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `my_app`;

-- -----------------------------------------------------
-- Tabla `products` - Almacena los productos del sistema
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `my_app`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `price` INT NOT NULL,
  `image` VARCHAR(512) NULL DEFAULT NULL,
  `creationAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `description` TEXT NULL DEFAULT NULL,
  `category` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `unique_title_price` (`title` ASC, `price` ASC)
)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- Restauración de configuraciones originales
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;