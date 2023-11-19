-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 17:29
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5btepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_jacopo_vioni`
--

CREATE TABLE `dipendenti_jacopo_vioni` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(20) NOT NULL,
  `posizionelavorativa` varchar(20) NOT NULL,
  `dataassunzione` varchar(20) NOT NULL,
  `eta` int(11) NOT NULL,
  `stipendioxmese` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `dipendenti_jacopo_vioni`
--

INSERT INTO `dipendenti_jacopo_vioni` (`id`, `nome`, `cognome`, `posizionelavorativa`, `dataassunzione`, `eta`, `stipendioxmese`) VALUES
(1, 'jacopo', 'vioni', 'dipendente', '10/05/2006', 22, 1500),
(2, 'andrea', 'skenderi', 'dipendente', '11/10/2022', 18, 950);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_jacopo_vioni`
--
ALTER TABLE `dipendenti_jacopo_vioni`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_jacopo_vioni`
--
ALTER TABLE `dipendenti_jacopo_vioni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
