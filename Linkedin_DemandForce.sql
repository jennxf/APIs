-- phpMyAdmin SQL Dump
-- version 4.0.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 21, 2013 at 04:50 PM
-- Server version: 5.5.33-log
-- PHP Version: 5.5.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `jenndb`
--

-- --------------------------------------------------------

--
-- Table structure for table `Linkedin_DemandForce`
--

CREATE TABLE `Linkedin_DemandForce` (
  `id` int(2) NOT NULL DEFAULT '0',
  `Timestamp` varchar(19) DEFAULT NULL,
  `Num_Followers` int(4) DEFAULT NULL,
  `clicks` int(2) DEFAULT NULL,
  `comments` int(1) DEFAULT NULL,
  `engagement` decimal(9,8) DEFAULT NULL,
  `impressions` int(5) DEFAULT NULL,
  `likes` int(2) DEFAULT NULL,
  `shares` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Linkedin DemandForce Account';

--
-- Dumping data for table `Linkedin_DemandForce`
--

INSERT INTO `Linkedin_DemandForce` (`id`, `Timestamp`, `Num_Followers`, `clicks`, `comments`, `engagement`, `impressions`, `likes`, `shares`) VALUES
(1, '2013-10-01 00:00:00', 2153, 75, 1, 0.00570224, 16134, 15, 1),
(2, '2013-09-01 00:00:00', 2099, 54, 0, 0.00648495, 9869, 8, 2),
(3, '2013-08-01 00:00:00', 2026, 48, 3, 0.00659722, 8640, 6, 0),
(4, '2013-07-01 00:00:00', 1965, 46, 1, 0.00721189, 6933, 3, 0),
(5, '2013-06-01 00:00:00', 1893, 23, 0, 0.00430347, 6274, 4, 0),
(6, '2013-05-01 00:00:00', 1811, 35, 3, 0.00556729, 10418, 16, 4),
(7, '2013-04-01 00:00:00', 1709, 92, 0, 0.00867679, 11064, 4, 0),
(8, '2013-03-01 00:00:00', 1614, 50, 0, 0.00444846, 14387, 13, 1),
(9, '2013-02-01 00:00:00', 1520, 0, 0, 0.00000000, 0, 0, 0),
(10, '2013-01-01 00:00:00', 1452, 0, 0, 0.00000000, 0, 0, 0),
(11, '2012-12-01 00:00:00', 1358, 0, 0, 0.00000000, 0, 0, 0),
(12, '2012-11-01 00:00:00', 1313, 0, 0, 0.00000000, 0, 0, 0);
