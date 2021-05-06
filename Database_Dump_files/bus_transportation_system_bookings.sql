-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: bus_transportation_system
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `bus_id` int NOT NULL,
  `depart` datetime DEFAULT NULL,
  `bk_from` varchar(45) DEFAULT NULL,
  `bk_to` varchar(45) DEFAULT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`booking_id`,`bus_id`,`user_id`),
  UNIQUE KEY `booking_id_UNIQUE` (`booking_id`),
  KEY `user_id_idx` (`user_id`),
  KEY `bus_id` (`bus_id`),
  CONSTRAINT `bus_id` FOREIGN KEY (`bus_id`) REFERENCES `buses` (`bus_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=224 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (201,101,303,'2021-03-01 00:00:00','MANGALORE','BANGALORE','2021-03-06 16:47:25'),(203,102,301,'2021-03-05 00:00:00','MANGALORE','BANGALORE','2021-03-08 11:04:50'),(210,103,307,'2021-03-06 00:00:00','BANGALORE','KURNOOL','2021-03-08 11:25:36'),(213,104,309,'2021-03-09 00:00:00','MANGALORE','GOA','2021-03-08 18:39:25'),(220,103,310,'2021-03-27 00:00:00','VIJAYAWADA','ARAKU','2021-03-25 12:08:12'),(221,109,304,'2021-03-26 00:00:00','MANGALORE','BANGALORE','2021-03-26 11:37:58'),(222,103,314,'2021-03-31 00:00:00','Manali','Missourie','2021-03-31 15:07:48'),(223,103,314,'2021-03-31 00:00:00','Manali','Missourie','2021-03-31 16:11:03');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-06 14:07:46
