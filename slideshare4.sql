-- phpMyAdmin SQL Dump
-- version 4.0.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 25, 2013 at 11:30 AM
-- Server version: 5.5.33-log
-- PHP Version: 5.5.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `socialdash`
--

-- --------------------------------------------------------

--
-- Table structure for table `slideshare_quickbase`
USE socialdash;
CREATE TABLE `slideshare_quickbase` (
  `id` int(2) DEFAULT NULL,
  `Timestamp` varchar(19) DEFAULT NULL,
  `Presentation` varchar(99) DEFAULT NULL,
  `Views` int(4) DEFAULT NULL,
  `Downloads` int(2) DEFAULT NULL,
  `Favorites` int(1) DEFAULT NULL,
  `Comments` int(1) DEFAULT NULL,
  `Email_Shares` varchar(2) DEFAULT NULL,
  `Fb_Shares` varchar(2) DEFAULT NULL,
  `Tweets` varchar(2) DEFAULT NULL,
  `Linkedin_Shares` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




--
-- Dumping data for table `slideshare_quickbase`
--

INSERT INTO `slideshare_quickbase` (`id`, `Timestamp`, `Presentation`, `Views`, `Downloads`, `Favorites`, `Comments`, `Email_Shares`, `Fb_Shares`, `Tweets`, `Linkedin_Shares`) VALUES
(1, '2013-11-21 00:00:00', '5 Keys to Succeed in Today''s Collaborative Workplace - Guest Speaker Jacob Morgan Chess Media Group', 251, 12, 0, 0, '3', '0', '0', '0'),
(2, '2013-11-21 00:00:00', 'Intuit QuickBase at MassTLC Cloud Summit - Drivers of Cloud Adoption with Allison Mnookin', 28, 0, 0, 0, '0', '0', '0', '0'),
(3, '2013-11-21 00:00:00', 'Develop A Players through Collaboration Enabled by QuickBase', 141, 5, 0, 0, '1', '0', '0', '0'),
(4, '2013-11-21 00:00:00', 'Tips for Running Effective Meetings', 118, 7, 0, 1, '1', '0', '3', '2'),
(5, '2013-11-21 00:00:00', 'QuickBase Customer Webinar - Information Systems Manager Shares His App Success', 337, 5, 0, 0, '0', '0', '0', '0'),
(6, '2013-11-21 00:00:00', 'Intuit QuickBase Webinar: Solve More Problems - with QuickBase', 802, 3, 1, 0, '0', '7', '11', '3'),
(7, '2013-11-21 00:00:00', 'Website Integration with QuickBase - Joshua McGinnis', 5560, 53, 1, 0, '15', '2', '0', '0'),
(8, '2013-11-21 00:00:00', 'Building Smart Workflows - Dan Diebolt', 2878, 24, 0, 0, '2', '0', '0', '0'),
(9, '2013-11-21 00:00:00', 'Magic Buttons - George Courtsunis', 1989, 32, 0, 0, '0', '0', '0', '0'),
(10, '2013-11-21 00:00:00', 'Extending Basic QuickBase - Kirk Trachy', 2120, 28, 0, 0, '1', '0', '0', '0'),
(11, '2013-11-21 00:00:00', 'Website Integration With QuickBase - Joshua McGinnis', 1, 0, 0, 0, '0', '16', '0', '0'),
(12, '2013-11-21 00:00:00', 'Magic Buttons - George Courtsunis', 0, 0, 0, 0, '0', '16', '0', '0'),
(13, '2013-11-21 00:00:00', 'Building A Quick Base Mobile Application - Phil Gross', 3374, 28, 0, 0, '1', '0', '0', '0'),
(14, '2013-11-21 00:00:00', 'Integrating QuickBase With Web Services - Gareth Lewis', 4310, 27, 1, 0, '0', '1', '0', '0'),
(15, '2013-11-21 00:00:00', 'Saving Time And Effort With QuickBase Api - Sergio Haro', 5834, 65, 1, 0, '15', '0', '0', '0'),
(16, '2013-11-21 00:00:00', 'Building Smart Workflows - Dan Diebolt', 1, 0, 0, 0, '0', '16', '0', '0'),
(17, '2013-11-21 00:00:00', 'Extending Basic Quick Base - Kirk', 0, 0, 0, 0, '0', '16', '0', '0'),
(18, '2013-11-21 00:00:00', 'Connecting Quick Base With DBs - Peter Fearey', 3918, 52, 0, 0, '19', '2', '0', '0'),
(19, '2013-11-21 00:00:00', 'How QuickBase Works Behind The Scenes - Jim Salem', 2482, 46, 0, 0, '7', '0', '0', '0'),
(39, '2013-11-24 23:17:52', '5-keys-to-succeed-in-todays-collaborative-workplace', 275, 13, 0, 0, '', '', '', ''),
(40, '2013-11-24 23:17:52', 'drivers-of-cloud-adoption-the-business-users-view-allison-mnookin', 49, 0, 0, 0, '', '', '', ''),
(41, '2013-11-24 23:17:52', 'develop-a-players-through-collaboration-enabled-by-quickbase', 199, 5, 0, 0, '', '', '', ''),
(42, '2013-11-24 23:22:05', '5-keys-to-succeed-in-todays-collaborative-workplace', 275, 13, 0, 0, '', '', '', ''),
(43, '2013-11-24 23:22:05', 'drivers-of-cloud-adoption-the-business-users-view-allison-mnookin', 49, 0, 0, 0, '', '', '', ''),
(44, '2013-11-24 23:22:05', 'develop-a-players-through-collaboration-enabled-by-quickbase', 199, 5, 0, 0, '', '', '', ''),
(45, '2013-11-24 23:22:05', 'tips-for-running-effective-meetings', 197, 7, 0, 1, '', '', '', ''),
(46, '2013-11-24 23:22:05', 'quickbase-customer-webinar-ny-foundling', 486, 5, 0, 0, '', '', '', ''),
(47, '2013-11-24 23:22:05', 'intuit-quickbase-webinar-slides-solve-more-problems-with-quickbase', 1024, 3, 1, 0, '', '', '', ''),
(48, '2013-11-24 23:22:05', 'website-integration-with-quickbase-joshua-mcginnis-2368684', 6822, 63, 1, 0, '', '', '', ''),
(49, '2013-11-24 23:22:05', 'building-smart-workflows-dan-diebolt-2368487', 3552, 29, 0, 0, '', '', '', ''),
(50, '2013-11-24 23:22:05', 'magic-buttons-george-courtsunis-2368123', 2538, 39, 0, 0, '', '', '', ''),
(51, '2013-11-24 23:22:05', 'extending-basic-quickbase-kirk-trachy', 2747, 34, 0, 0, '', '', '', ''),
(52, '2013-11-24 23:22:05', 'building-a-quick-base-mobile-application-phil-gross', 4385, 36, 0, 0, '', '', '', ''),
(53, '2013-11-24 23:22:05', 'integrating-quickbase-with-web-services-gareth-lewis', 5510, 35, 1, 0, '', '', '', ''),
(54, '2013-11-24 23:22:05', 'saving-time-and-effort-with-quickbase-api-sergio-haro', 7086, 79, 1, 0, '', '', '', ''),
(55, '2013-11-24 23:22:05', 'connecting-quick-base-with-dbs-peter-fearey', 4850, 63, 0, 0, '', '', '', ''),
(56, '2013-11-24 23:22:05', 'extending-basic-quickbase-kirk-trachy', 2747, 34, 0, 0, '', '', '', ''),
(57, '2013-11-25 19:42:31', '5-keys-to-succeed-in-todays-collaborative-workplace', 277, 13, 0, 0, NULL, NULL, NULL, NULL),
(58, '2013-11-25 19:42:31', 'drivers-of-cloud-adoption-the-business-users-view-allison-mnookin', 50, 0, 0, 0, NULL, NULL, NULL, NULL),
(59, '2013-11-25 19:42:31', 'develop-a-players-through-collaboration-enabled-by-quickbase', 199, 5, 0, 0, NULL, NULL, NULL, NULL),
(60, '2013-11-25 19:42:31', 'tips-for-running-effective-meetings', 198, 7, 0, 1, NULL, NULL, NULL, NULL),
(61, '2013-11-25 19:42:31', 'quickbase-customer-webinar-ny-foundling', 486, 5, 0, 0, NULL, NULL, NULL, NULL),
(62, '2013-11-25 19:42:31', 'intuit-quickbase-webinar-slides-solve-more-problems-with-quickbase', 1025, 3, 1, 0, NULL, NULL, NULL, NULL),
(63, '2013-11-25 19:42:31', 'website-integration-with-quickbase-joshua-mcginnis-2368684', 6823, 63, 1, 0, NULL, NULL, NULL, NULL),
(64, '2013-11-25 19:42:31', 'building-smart-workflows-dan-diebolt-2368487', 3553, 29, 0, 0, NULL, NULL, NULL, NULL),
(65, '2013-11-25 19:42:31', 'magic-buttons-george-courtsunis-2368123', 2538, 39, 0, 0, NULL, NULL, NULL, NULL),
(66, '2013-11-25 19:42:31', 'extending-basic-quickbase-kirk-trachy', 2747, 34, 0, 0, NULL, NULL, NULL, NULL),
(67, '2013-11-25 19:42:31', 'building-a-quick-base-mobile-application-phil-gross', 4387, 36, 0, 0, NULL, NULL, NULL, NULL),
(68, '2013-11-25 19:42:31', 'integrating-quickbase-with-web-services-gareth-lewis', 5513, 35, 1, 0, NULL, NULL, NULL, NULL),
(69, '2013-11-25 19:42:31', 'saving-time-and-effort-with-quickbase-api-sergio-haro', 7088, 79, 1, 0, NULL, NULL, NULL, NULL),
(70, '2013-11-25 19:42:31', 'connecting-quick-base-with-dbs-peter-fearey', 4850, 63, 0, 0, NULL, NULL, NULL, NULL),
(71, '2013-11-25 19:42:31', 'extending-basic-quickbase-kirk-trachy', 2747, 34, 0, 0, NULL, NULL, NULL, NULL);
