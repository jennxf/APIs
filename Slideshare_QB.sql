-- phpMyAdmin SQL Dump
-- version 4.0.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 21, 2013 at 10:55 AM
-- Server version: 5.5.33-log
-- PHP Version: 5.5.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `jenndb`
--

-- --------------------------------------------------------

--
-- Table structure for table `Slideshare_Quickbase`
--

CREATE TABLE `Slideshare_Quickbase` (
  `Presentations` varchar(99) DEFAULT NULL,
  `Views` int(4) DEFAULT NULL,
  `Downloads` int(2) DEFAULT NULL,
  `Favorites` int(1) DEFAULT NULL,
  `Comments` int(1) DEFAULT NULL,
  `Email_Shares` int(2) DEFAULT NULL,
  `FB_Shares` int(2) DEFAULT NULL,
  `Tweets` int(2) DEFAULT NULL,
  `Linkedin_Shares` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Slideshare_Quickbase`
--

INSERT INTO `Slideshare_Quickbase` (`Presentations`, `Views`, `Downloads`, `Favorites`, `Comments`, `Email_Shares`, `FB_Shares`, `Tweets`, `Linkedin_Shares`) VALUES
('5 Keys to Succeed in Today''s Collaborative Workplace - Guest Speaker Jacob Morgan Chess Media Group', 251, 12, 0, 0, 3, 0, 0, 0),
('Intuit QuickBase at MassTLC Cloud Summit - Drivers of Cloud Adoption with Allison Mnookin', 28, 0, 0, 0, 0, 0, 0, 0),
('Develop A Players through Collaboration Enabled by QuickBase', 141, 5, 0, 0, 1, 0, 0, 0),
('Tips for Running Effective Meetings', 118, 7, 0, 1, 1, 0, 3, 2),
('QuickBase Customer Webinar - Information Systems Manager Shares His App Success', 337, 5, 0, 0, 0, 0, 0, 0),
('Intuit QuickBase Webinar: Solve More Problems - with QuickBase', 802, 3, 1, 0, 0, 7, 11, 3),
('Website Integration with QuickBase - Joshua McGinnis', 5560, 53, 1, 0, 15, 2, 0, 0),
('Building Smart Workflows - Dan Diebolt', 2878, 24, 0, 0, 2, 0, 0, 0),
('Magic Buttons - George Courtsunis', 1989, 32, 0, 0, 0, 0, 0, 0),
('Extending Basic QuickBase - Kirk Trachy', 2120, 28, 0, 0, 1, 0, 0, 0),
('Website Integration With QuickBase - Joshua McGinnis', 1, 0, 0, 0, 0, 16, 0, 0),
('Magic Buttons - George Courtsunis', 0, 0, 0, 0, 0, 16, 0, 0),
('Building A Quick Base Mobile Application - Phil Gross', 3374, 28, 0, 0, 1, 0, 0, 0),
('Integrating QuickBase With Web Services - Gareth Lewis', 4310, 27, 1, 0, 0, 1, 0, 0),
('Saving Time And Effort With QuickBase Api - Sergio Haro', 5834, 65, 1, 0, 15, 0, 0, 0),
('Building Smart Workflows - Dan Diebolt', 1, 0, 0, 0, 0, 16, 0, 0),
('Extending Basic Quick Base - Kirk', 0, 0, 0, 0, 0, 16, 0, 0),
('Connecting Quick Base With DBs - Peter Fearey', 3918, 52, 0, 0, 19, 2, 0, 0),
('How QuickBase Works Behind The Scenes - Jim Salem', 2482, 46, 0, 0, 7, 0, 0, 0);
