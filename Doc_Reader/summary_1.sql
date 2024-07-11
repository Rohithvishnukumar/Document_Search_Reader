-- Database: `docsearchreader`


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



CREATE TABLE `summary` (
  `userid` int(11) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



ALTER TABLE `summary`
  ADD KEY `userid` (`userid`);


ALTER TABLE `summary`
  ADD CONSTRAINT `summary_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

