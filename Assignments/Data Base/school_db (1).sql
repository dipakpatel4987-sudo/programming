-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:4307
-- Generation Time: Mar 30, 2026 at 11:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `school_db`
--

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `student_name`, `age`, `class`, `address`, `teacher_id`) VALUES
(6, 'virat', 30, 'C2', 'komal nagar', 1),
(5, 'harsh', 10, 'B1', 'gita nagar', 2),
(4, 'yash', 25, 'A3', 'mahavir nagar', 3),
(3, 'sham', 12, 'A1', 'gutam nagar', 4),
(2, 'ram', 2, 'A2', 'amraiwadi', 5),
(1, 'deepak', 20, 'A2', 'gopal nagar', 6);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
