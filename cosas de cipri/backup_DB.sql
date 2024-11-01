-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: bi3gapjnxdlclrphs3w9-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 01-11-2024 a las 22:01:49
-- Versión del servidor: 8.0.22-13
-- Versión de PHP: 8.2.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bi3gapjnxdlclrphs3w9`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Inscripciones`
--

CREATE TABLE `Inscripciones` (
  `ID` int NOT NULL,
  `Equipo` varchar(100) NOT NULL,
  `Colegio` varchar(100) NOT NULL,
  `Deporte` varchar(20) NOT NULL,
  `Categoria` varchar(20) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `DNI` int NOT NULL,
  `Correo` varchar(50) NOT NULL,
  `Miembros` int NOT NULL,
  `Acompañantes` int NOT NULL,
  `Vegetariano` varchar(5) NOT NULL,
  `Celiaco` varchar(5) NOT NULL,
  `Diabetico` varchar(5) NOT NULL,
  `Comprobante` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'no se cargo',
  `Autorizacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'no se cargo',
  `QR` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'no se cargo',
  `Grupo` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT 'sin definir',
  `Estado` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `Inscripciones`
--

INSERT INTO `Inscripciones` (`ID`, `Equipo`, `Colegio`, `Deporte`, `Categoria`, `Telefono`, `DNI`, `Correo`, `Miembros`, `Acompañantes`, `Vegetariano`, `Celiaco`, `Diabetico`, `Comprobante`, `Autorizacion`, `QR`, `Grupo`, `Estado`) VALUES
(3, 'Equipo C', 'Colegio 3', 'Futbol', 'Masculino mayor', '456123789', 45612378, 'equipoC@ejemplo.com', 10, 1, '1', '1', '1', '', '', '', '3C', 1),
(4, 'Equipo D', 'Colegio 4', 'Futbol', 'Masculino mayor', '321654987', 32165478, 'equipoD@ejemplo.com', 11, 2, '1', '1', '1', '', '', '', '4B', 1),
(5, 'Equipo E', 'Colegio 5', 'Baloncesto', 'Sub-14', '654321789', 65432178, 'equipoE@ejemplo.com', 9, 4, 'Sí', 'Sí', 'No', '', '', '3', '3', 1),
(6, 'Equipo F', 'Colegio 6', 'Futbol', 'Masculino mayor', '789456123', 78945612, 'equipoF@ejemplo.com', 10, 1, '1', '1', '1', '', '', '', '5', 1),
(18, 'infumables', 'san pablo', 'Voley', 'Masculino mayor', '3513431730', 47173704, 'tomas1230@gmail.com', 8, 2, '2', 'NO', 'NO', 'no se cargo', 'no se cargo', 'no se cargo', 'sin definir', 1),
(19, 'test300', 'ipem 2332', 'Voley', 'Masculino menor', '4504054', 47173704, 'tomas120000@gmail.com', 10, 1, 'NO', 'NO', '1', 'no se cargo', 'no se cargo', 'https://docs.google.com/document/d/196EundkSN7scUxNmZl-9_T2YWWY1yjII_RZch3jKgf8/edit?usp=drivesdk', 'sin definir', 1),
(21, 'Los diablitos', 'ipem 2332', 'Futbol', 'Masculino mayor', '3513431739', 47173704, 'tomas1234@gmail.com', 9, 1, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'no se cargo', 'sin definir', 1),
(24, 'Los diablitos', 'villada de la rosa de la independencia de 1872', 'Futbol', 'Masculino mayor', '363636', 47173704, 'tomas1234@gmail.com', 8, 2, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'https://docs.google.com/document/d/1Si6u7ZN_hR3B4KAg4CHmdrVhbDiZfhFbQzdhi3mQi8s/edit?usp=drivesdk', 'sin definir', 1),
(25, 'saltin', 'instituto arguello', 'Voley', 'masculino mayor', '+593512654852', 31555555, 'literariocba@gmail.com', 8, 1, 'NO', 'NO', 'NO', 'https://drive.google.com/open?id=1k2I7KI4i24Mk8YbabScS0L6PUTOk725C', 'https://drive.google.com/open?id=1p3USypt6tABxqaLDLpPYLyeerd1m13Gm', 'no se cargo', 'sin definir', 1),
(26, 'Los furryequipo', 'Colegio', 'Voley', 'Masculino mayor', '+54546879', 474742858, 'jgosj@gmail.com', 9, 2, 'NO', '2', 'NO', 'https://drive.google.com/open?id=1UgDu9ftPCh2RiGIJl_BuedB9Rcl0wKe7', 'https://drive.google.com/open?id=1iXjL7pANVrLB33cx49xKzM4doIN_3B0C', 'no se cargo', 'sin definir', 1),
(27, 'Chinchulones', 'Sagrado', 'Basquet', 'masculino menor', '+513431739', 12345678, 'tomas@gmail.com', 6, 1, 'NO', 'NO', '1', 'https://drive.google.com/open?id=1znbonHuHqiWY63GOxKy5ofMA-IxmNFHW', 'https://drive.google.com/open?id=1yqqoV0B_aMjsTpEf6-JLkRkP86KZN9B1', 'no se cargo', 'sin definir', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Partidos`
--

CREATE TABLE `Partidos` (
  `ID` int NOT NULL,
  `Equipo` varchar(100) NOT NULL,
  `Deporte` varchar(20) NOT NULL,
  `Grupo` int NOT NULL,
  `Empates` int NOT NULL,
  `Victorias` int NOT NULL,
  `Derrotas` int NOT NULL,
  `GF` int NOT NULL,
  `GC` int NOT NULL,
  `Puntos` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Settings`
--

CREATE TABLE `Settings` (
  `deporte` varchar(20) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `cupos` int NOT NULL,
  `cierre` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `Settings`
--

INSERT INTO `Settings` (`deporte`, `categoria`, `cupos`, `cierre`) VALUES
('Fútbol', 'Masculino Mayor', 0, '1970-01-01'),
('Fútbol', 'Masculino Menor', 0, '1970-01-01'),
('Fútbol', 'Femenino Mayor', 0, '1970-01-01'),
('Fútbol', 'Femenino Menor', 0, '1970-01-01'),
('Básquet', 'Masculino Mayor', 0, '1970-01-01'),
('Básquet', 'Masculino Menor', 0, '1970-01-01'),
('Básquet', 'Femenino Mayor', 0, '1970-01-01'),
('Básquet', 'Femenino Menor', 0, '1970-01-01'),
('Voley', 'Masculino Mayor', 0, '1970-01-01'),
('Voley', 'Masculino Menor', 0, '1970-01-01'),
('Voley', 'Femenino Mayor', 0, '1970-01-01'),
('Voley', 'Femenino Menor', 0, '1970-01-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuarios`
--

CREATE TABLE `Usuarios` (
  `ID` int NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Gmail` varchar(30) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `ROL` tinytext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Inscripciones`
--
ALTER TABLE `Inscripciones`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `Partidos`
--
ALTER TABLE `Partidos`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `Usuarios`
--
ALTER TABLE `Usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Inscripciones`
--
ALTER TABLE `Inscripciones`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `Partidos`
--
ALTER TABLE `Partidos`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Usuarios`
--
ALTER TABLE `Usuarios`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
