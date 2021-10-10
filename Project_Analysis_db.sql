-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 01, 2018 at 10:44 AM
-- Server version: 5.7.22-0ubuntu0.16.04.1
-- PHP Version: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Project_Analysis_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `Grimoire`
--

CREATE TABLE `Grimoire` (
  `Project_ID` varchar(40) DEFAULT NULL,
  `assignee_email` varchar(25) DEFAULT NULL,
  `assignee_domain` varchar(55) DEFAULT NULL,
  `assignee_location` varchar(75) DEFAULT NULL,
  `assignee_login` varchar(20) DEFAULT NULL,
  `assignee_name` varchar(70) DEFAULT NULL,
  `assignee_org` varchar(20) DEFAULT NULL,
  `author_name` varchar(40) DEFAULT NULL,
  `closed_at` varchar(80) DEFAULT NULL,
  `created_at` varchar(80) DEFAULT NULL,
  `github_repo` char(30) DEFAULT NULL,
  `grimoire_creation_date` varchar(50) DEFAULT NULL,
  `id` varchar(85) DEFAULT NULL,
  `id_in_repo` int(25) DEFAULT NULL,
  `is_github_issue` char(15) DEFAULT NULL,
  `item_type` char(15) DEFAULT NULL,
  `labels` text,
  `metadata__enriched_on` varchar(50) DEFAULT NULL,
  `metadata__gelk_backend_name` varchar(20) DEFAULT NULL,
  `metadata__gelk_version` varchar(20) DEFAULT NULL,
  `metadata__timestamp` varchar(100) DEFAULT NULL,
  `metadata__updated_on` varchar(50) DEFAULT NULL,
  `ocean-unique-id` varchar(85) DEFAULT NULL,
  `origin` varchar(40) DEFAULT NULL,
  `offset` varchar(50) DEFAULT NULL,
  `pull_request` char(15) DEFAULT NULL,
  `repository` varchar(70) DEFAULT NULL,
  `state` char(50) DEFAULT NULL,
  `tag` varchar(70) DEFAULT NULL,
  `time_open_days` varchar(65) DEFAULT NULL,
  `time_to_close_days` varchar(65) DEFAULT NULL,
  `title` varchar(250) DEFAULT NULL,
  `title_analyzed` varchar(250) DEFAULT NULL,
  `updated_at` varchar(50) DEFAULT NULL,
  `url` varchar(80) DEFAULT NULL,
  `url_id` varchar(75) DEFAULT NULL,
  `user_email` varchar(70) DEFAULT NULL,
  `user_domain` varchar(55) DEFAULT NULL,
  `user_location` varchar(65) DEFAULT NULL,
  `user_login` varchar(25) DEFAULT NULL,
  `user_name` varchar(65) DEFAULT NULL,
  `user_org` varchar(25) DEFAULT NULL,
  `uuid` varchar(65) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `PHPQA`
--

CREATE TABLE `PHPQA` (
  `Project_ID` varchar(40) DEFAULT NULL,
  `loc` varchar(65) DEFAULT NULL,
  `lloc` varchar(65) DEFAULT NULL,
  `cyclomaticComplexity` varchar(65) DEFAULT NULL,
  `maintainabilityIndex` varchar(45) DEFAULT NULL,
  `volume` varchar(55) DEFAULT NULL,
  `vocabulary` varchar(55) DEFAULT NULL,
  `difficulty` varchar(55) DEFAULT NULL,
  `effort` varchar(55) DEFAULT NULL,
  `bugs` varchar(55) DEFAULT NULL,
  `time` varchar(55) DEFAULT NULL,
  `tag` varchar(65) DEFAULT NULL,
  `intelligentContent` varchar(55) DEFAULT NULL,
  `commentWeight` varchar(55) DEFAULT NULL,
  `length` varchar(55) DEFAULT NULL,
  `lcom` varchar(55) DEFAULT NULL,
  `instability` varchar(55) DEFAULT NULL,
  `efferentCoupling` varchar(55) DEFAULT NULL,
  `afferentCoupling` varchar(55) DEFAULT NULL,
  `sysc` varchar(55) DEFAULT NULL,
  `rsysc` varchar(55) DEFAULT NULL,
  `dc` varchar(55) DEFAULT NULL,
  `rdc` varchar(55) DEFAULT NULL,
  `sc` varchar(55) DEFAULT NULL,
  `rsc` varchar(55) DEFAULT NULL,
  `noc` varchar(55) DEFAULT NULL,
  `noca` varchar(55) DEFAULT NULL,
  `nocc` varchar(55) DEFAULT NULL,
  `noi` varchar(55) DEFAULT NULL,
  `nom` varchar(55) DEFAULT NULL,
  `namespace` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `Login_Name` varchar(25) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Password` varchar(40) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `UserProject` varchar(40) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `PHPQA_ProjectID` varchar(40) CHARACTER SET utf8 DEFAULT NULL,
  `Grimoire_ProjectID` varchar(40) CHARACTER SET utf8 DEFAULT NULL,
  `User_Name` varchar(25) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
