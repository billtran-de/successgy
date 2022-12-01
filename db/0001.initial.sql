CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `emp_id` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `emp_name` varchar(255) DEFAULT NULL,
  `emp_role` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `emission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `energy_source` varchar(255) DEFAULT NULL,
  `month` int DEFAULT NULL,
  `year` int DEFAULT NULL,
  `amount` decimal(9,2) DEFAULT NULL,
  `carbon_emission` decimal(9,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `emission_source` (
  `id` int NOT NULL AUTO_INCREMENT,
  `scope` int DEFAULT NULL,
  `emission_source` varchar(255) DEFAULT NULL,
  `conversion_rate` decimal(6,4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `emission_source` (`scope`,`emission_source`,`conversion_rate`) 
VALUES 
  (1, 'gas', 91),
  (2, 'electricity', 0.0005);