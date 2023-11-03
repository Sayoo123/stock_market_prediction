/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - 22_stock_prediction
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`22_stock_prediction` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `22_stock_prediction`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaints` varchar(100) DEFAULT NULL,
  `c_date` date DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `r_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`c_id`,`user_id`,`complaints`,`c_date`,`reply`,`r_date`) values (1,14,'hello','2022-03-13','hello','2022-03-15'),(2,14,'not working','2022-03-14','change password','2022-03-14'),(19,14,'gvjhjhgv','2022-03-14',NULL,NULL),(20,14,'server down','2022-03-14','fgfgf','2022-04-30'),(21,15,'server up','2022-03-14','it will work','2022-03-14'),(22,14,'svdown',NULL,'pending',NULL),(23,14,'hhhhh',NULL,NULL,NULL),(24,14,'ttttt',NULL,NULL,NULL),(25,14,'mmmmmm',NULL,NULL,NULL),(26,17,'Bad!!!!!!!!!!!!','2022-04-30','llllllllllllll','2022-04-30');

/*Table structure for table `dataset` */

DROP TABLE IF EXISTS `dataset`;

CREATE TABLE `dataset` (
  `d_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(30) DEFAULT NULL,
  `open` varchar(10) DEFAULT NULL,
  `high` varchar(10) DEFAULT NULL,
  `low` varchar(10) DEFAULT NULL,
  `close` varchar(10) DEFAULT NULL,
  `volume` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`d_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `dataset` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `f_date` date DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`f_id`,`user_id`,`feedback`,`f_date`) values (1,14,'goood','2000-01-09'),(2,14,'gud work','2022-03-14'),(3,15,'good work','2022-03-14'),(4,15,'nice job','2022-03-14'),(5,14,'gud job2233','2022-03-24'),(6,17,'Need improve','2022-04-30');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values (1,'admin@gmail.com','admin','admin'),(14,'sayoojsunil2000@gmail.com','12345','user'),(15,'sayoojsunil20001@gmail.com','12345','user'),(16,'sadhasd@gmail.com','12345','user'),(17,'a@gmail.com','123','user'),(24,'anu@gmail.com','1234','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  `n_date` date DEFAULT NULL,
  PRIMARY KEY (`n_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

/*Data for the table `notification` */

insert  into `notification`(`n_id`,`notification`,`n_date`) values (17,'hey','2022-03-24'),(18,'helllo','2022-03-24'),(19,'alll up good to go','2022-03-24');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_name`,`phone`,`email`,`dob`) values (14,'sayooj','1237123213','sayoojsunil2000@gmail.com','2022-03-15'),(15,'suraj','8547503908','sayoojsunil20001@gmail.com','2022-02-18'),(16,'sayooj','12345678','sadhasd@gmail.com','2000-12-12'),(17,'anu','9876543210','a@gmail.com','1995-07-29'),(24,'anu','9876543210','anu@gmail.com','1995-07-24');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
