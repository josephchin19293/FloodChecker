-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:8889
-- Generation Time: Dec 08, 2018 at 03:53 PM
-- Server version: 5.5.42
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `FloodChecker`
--

-- --------------------------------------------------------

--
-- Table structure for table `Data`
--
Use ajh203;

CREATE TABLE `SensorData` (
  `dataId` int(255) NOT NULL,
  `sensor` varchar(255) DEFAULT NULL,
  `dataValue` int(60) DEFAULT NULL,
  `dataTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dataHardwareSerial` varchar(255) DEFAULT NULL,
  `dataLatitude` decimal(60,6) DEFAULT NULL,
  `dataLongitude` decimal(60,6) DEFAULT NULL,
  `dataAltitude` varchar(255) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=12209 DEFAULT CHARSET=latin1;
--
-- Indexes for table `Data`
--
ALTER TABLE `Data`
  ADD PRIMARY KEY (`dataId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Data`
--
ALTER TABLE `Data`
  MODIFY `dataId` int(255) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=12209;