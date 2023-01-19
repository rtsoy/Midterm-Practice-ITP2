-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 19, 2023 at 05:14 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `midterm-practice`
--

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL,
  `brand` varchar(24) DEFAULT NULL,
  `model` varchar(24) DEFAULT NULL,
  `release_year` varchar(24) DEFAULT NULL,
  `engine_capacity` decimal(4,1) DEFAULT NULL,
  `color` varchar(24) DEFAULT NULL,
  `price` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`id`, `brand`, `model`, `release_year`, `engine_capacity`, `color`, `price`) VALUES
(1, 'Mercedes-Benz', 'CLA 200', '2014', '1.6', 'Black', 25000),
(3, 'BMW', 'M5', '2022', '4.4', 'Yellow', 100000),
(5, 'Audi', 'A8L', '2016', '4.0', 'Black', 25000),
(6, 'Nissan', 'Almera', '2009', '2.4', 'Yellow', 9000),
(7, 'Bentley', 'Continental GT', '2014', '6.0', 'Black', 105000),
(8, 'Toyota', 'Land Cruiser Prado Luxe', '2022', '4.0', 'White', 100000),
(9, 'Infiniti', 'QX80', '2021', '5.6', 'Black', 150000),
(10, 'Porsche', '911', '2023', '3.7', 'Green', 332000),
(11, 'Jaguar', 'F-Pace', '2021', '2.0', 'Red', 100000),
(12, 'Toyota', 'Camry', '2021', '3.5', 'White', 62000),
(13, 'Kia', 'K5', '2022', '2.5', 'Blue', 53000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
