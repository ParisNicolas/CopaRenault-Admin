-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: bi3gapjnxdlclrphs3w9-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 09-02-2025 a las 23:18:13
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
-- Estructura de tabla para la tabla `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('8961bd1b5f2a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cupos`
--

CREATE TABLE `cupos` (
  `deporte` varchar(20) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `cupos` int NOT NULL,
  `cupos_restantes` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `cupos`
--

INSERT INTO `cupos` (`deporte`, `categoria`, `cupos`, `cupos_restantes`) VALUES
('Fútbol', 'Masculino Mayor', 25, 20),
('Fútbol', 'Masculino Menor', 20, 20),
('Fútbol', 'Femenino Mayor', 20, 20),
('Fútbol', 'Femenino Menor', 20, 20),
('Básquet', 'Masculino Mayor', 25, 20),
('Básquet', 'Masculino Menor', 20, 20),
('Básquet', 'Femenino Mayor', 20, 20),
('Básquet', 'Femenino Menor', 20, 20),
('Voley', 'Masculino Mayor', 20, 20),
('Voley', 'Masculino Menor', 24, 20),
('Voley', 'Femenino Mayor', 20, 20),
('Voley', 'Femenino Menor', 20, 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `colegio` varchar(100) NOT NULL,
  `deporte` varchar(100) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `grupo` varchar(1) NOT NULL,
  `victorias` int NOT NULL,
  `empates` int NOT NULL,
  `derrotas` int NOT NULL,
  `puntos` int NOT NULL,
  `diferncia_gol` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`id`, `nombre`, `colegio`, `deporte`, `categoria`, `grupo`, `victorias`, `empates`, `derrotas`, `puntos`, `diferncia_gol`) VALUES
(20, 'TestTeam', 'elCipri', 'Futbol', 'Masculino mayor', 'A', 1, 0, 0, 3, 1),
(23, 'TestTeam4', 'elJoaco', 'Futbol', 'Masculino mayor', 'C', 0, 0, 0, 0, 0),
(24, 'Chinchulones', 'Sagrado', 'Basquet', 'masculino menor', 'B', 0, 0, 0, 0, 0),
(25, 'Bot1', 'botardos', 'Basquet', 'Masculino menor', 'A', 0, 0, 0, 0, 0),
(26, 'Bot2', 'malardos', 'Basquet', 'Masculino menor', 'B', 0, 0, 0, 0, 0),
(27, 'Bot3', 'Bunardovichs', 'Basquet', 'Masculino menor', 'A', 0, 0, 0, 0, 0),
(28, 'LosWarriorDePedroAsnars', 'Nuestra Señora del Sagrado Corazón', 'Basquet', 'Femenino mayor', 'E', 0, 0, 0, 0, 0),
(29, 'nigers2', 'renault', 'Basquet', 'Femenino mayor', 'E', 0, 0, 0, 0, 0),
(30, 'nigers', 'renault', 'Basquet', 'Femenino mayor', 'E', 0, 0, 0, 0, 0),
(31, 'hola', 'lol', 'Basquet', 'Femenino mayor', 'E', 0, 0, 0, 0, 0);

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
  `Dudas` varchar(2048) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `QR` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'no se cargo',
  `Grupo` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT 'sin definir',
  `Estado` tinyint(1) NOT NULL DEFAULT '0',
  `equipo_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `Inscripciones`
--

INSERT INTO `Inscripciones` (`ID`, `Equipo`, `Colegio`, `Deporte`, `Categoria`, `Telefono`, `DNI`, `Correo`, `Miembros`, `Acompañantes`, `Vegetariano`, `Celiaco`, `Diabetico`, `Dudas`, `QR`, `Grupo`, `Estado`, `equipo_id`) VALUES
(31, 'TestTeam4', 'elJoaco', 'Futbol', 'Masculino mayor', '3513741621', 47174991, 'bhdfh@abndfs.com', 10, 1, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'C', 1, 23),
(33, 'Bot2', 'malardos', 'Basquet', 'Masculino menor', '3513741624', 47174996, 'hsdbfhsbfgs@gmmail.com', 5, 2, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'B', 1, 26),
(34, 'Bot3', 'Bunardovichs', 'Basquet', 'Masculino menor', '3513741627', 47174999, 'isbvbsdibs@gmail.com', 8, 1, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'sin definir', 1, 27),
(35, 'hola', 'lol', 'Basquet', 'Femenino mayor', '67589i', 47173704, 'tomas1234@gmail.com', 9, 2, '1', 'NO', 'NO', 'no se cargo', 'no se cargo', 'E', 1, 31),
(36, 'nigers', 'renault', 'Basquet', 'Femenino mayor', '3513431739', 47173704, 'tomas1234@gmail.com', 7, 1, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'E', 1, 30),
(37, 'nigers2', 'renault', 'Basquet', 'Femenino mayor', '3513431739', 47173704, 'tomas1234@gmail.com', 7, 1, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'E', 1, 29),
(39, 'este', 'man', 'Futbol', 'Masculino mayor', '3519809896', 47173704, 'hkbhsbf@gmail.com', 12, 2, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'sin definir', 1, NULL),
(40, '1234', 'lol', 'Basquet', 'Masculino mayor', '3513431730', 47174997, 'tomas1234@gmail.com', 7, 2, 'NO', 'NO', 'NO', 'no se cargo', 'no se cargo', 'sin definir', 1, NULL),
(42, 'infumables', 'renault', 'Voley', 'Masculino mayor', '4504054', 47173704, 'tomas1234@gmail.com', 7, 2, 'NO', 'NO', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1ESnR1M3CU1otjBk8-stSgbLtEInFXwPifU8zqmguelg/edit?usp=drivesdk', 'sin definir', 1, NULL),
(43, 'LosWarriorDePedroAsnars', 'Nuestra Señora del Sagrado Corazón', 'Basquet', 'Femenino mayor', '549351234564', 22354988, 'gege420@gmail.com', 10, 1, '2', 'NO', '3', 'https://drive.google.com/open?id=1TeONcnH3u9TDNJpZ_8jbv9Oohj0HNMqr', 'https://docs.google.com/document/d/1TAO4SsFofoDqkFHKkLSUfR5G6lESsN6_mZ7nZoyfOYk/edit?usp=drivesdk', 'E', 1, 28),
(44, 'nigers', 'lol', 'Basquet', 'Femenino mayor', '3513431739', 47174997, 'tomas1234@gmail.com', 9, 2, 'NO', 'NO', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1svMJ0S8qFBLV5rOhaITFPiF2XWF_o3JkNIIIr4zixsE/edit?usp=drivesdk', 'sin definir', 1, NULL),
(45, 'infumables', 'lol', 'Futbol', 'Masculino mayor', 'ertert', 47173704, 'hkbhsbf@gmail.com', 9, 2, 'NO', '2', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1QXCvcyCjgvkZoAZk_jqvOtq9YmMVD_wFxSdID0vWBsE/edit?usp=drivesdk', 'sin definir', 1, NULL),
(46, '1234', 'renault', 'Futbol', 'Masculino menor', 'ertert', 47173704, 'tomas12340000@gmail.com', 9, 2, 'NO', '1', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1e9hnjBZNQFiYlSThKW2GQUXtbfQAw4qylq2tieWH6Co/edit?usp=drivesdk', 'sin definir', 1, NULL),
(47, 'rururr', 'ipem 2332', 'Voley', 'Femenino menor', 'ertert', 47173704, 'tomas1234@gmail.com', 7, 2, 'NO', 'NO', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1lO9WibNImgSXB-kBx5FO6KQaz6gtDJRxfL7HmFSmQlw/edit?usp=drivesdk', 'sin definir', 1, NULL),
(48, 'yLaQuesoo', 'UTN', 'Futbol', 'Masculino mayor', '3512346754', 54894356, 'luululu@gmail.com', 8, 1, 'NO', '3', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1E14iBSiFs-MSPcBHQWoUZ6kxrVDg-uVw5OqLoa8B3zw/edit?usp=drivesdk', 'sin definir', 1, NULL),
(49, 'ositos cariñositos', 'san pablo', 'Basquet', 'Masculino mayor', '325324625476', 47173704, 'tomas1230@gmail.com', 9, 1, 'NO', 'NO', '2', 'no se cargo', 'https://docs.google.com/document/d/165CXF8JH3cOBxi2SgukHJy9Kod8Kh5T2Go7NhCT9vr8/edit?usp=drivesdk', 'sin definir', 1, NULL),
(51, 'LosJuansitos', 'IntitutoTecnicoRenault', 'Futbol', 'masculino mayor', '3612347854', 47478374, 'goodmorning@gmial.com', 10, 1, 'NO', 'NO', 'NO', 'https://drive.google.com/open?id=1f0TQXSi8Y2dDDVwYghOsFwAjIX3ZBg6w', 'https://docs.google.com/document/d/1swh1HRsGFbltbc1OpsFPBXoPYnojJgInCjJNpyiLxh4/edit?usp=drivesdk', 'sin definir', 1, NULL),
(52, 'rusia', 'q', 'Basquet', 'Masculino menor', '9876543', 12, 'hkbhsbf@gmail.com', 4, 2, 'NO', 'NO', '1', 'no se cargo', 'https://docs.google.com/document/d/18T_rXzHdh3Yrf7GU4SyOdJWEHhAXlAXpo3qlJkYDbRo/edit?usp=drivesdk', 'sin definir', 1, NULL),
(53, 'glory to 86s', 'republic', 'Futbol', 'Masculino mayor', '3519809896', 86, 'hkbhsbf@gmail.com', 7, 1, 'NO', 'NO', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1TIs9nNY6sWu5MQ0W4PeqY-iSytmgUk3sxK0eJiNxNwo/edit?usp=drivesdk', 'sin definir', 1, NULL),
(54, 'nigers', 'renault', 'Basquet', 'Masculino mayor', '234', 47173704, 'tomas1230@gmail.com', 34, 2, 'NO', 'NO', 'NO', 'no se cargo', 'https://docs.google.com/document/d/1uYvbuITiQXOA4ghkvEKRz7NJb0ZelW1-Xnwvc4HXCAM/edit?usp=drivesdk', 'sin definir', 1, NULL),
(55, 'Tyfus', 'Hajs', 'Basquet', 'masculino menor', '1200000000', 47173704, 'tomascipriano2003@gmail.com', 6, 1, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(56, 'Fedora', 'San Pablo Apostol', 'Basquet', 'masculino menor', '3512626548', 54757394, 'gege420@gmail.com', 10, 1, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(57, 'Fedora23', 'San Pablo Apostol', 'Basquet', 'masculino menor', '3512645857', 45673423, 'gege420@gmail.com', 10, 1, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(58, 'Tiashi', 'Uqudhsk', 'Basquet', 'masculino menor', '3515030371', 47173704, 'tomascipriano2003@gmail.com', 6, 1, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(59, 'Fedora34', 'San Pablo Apostol', 'Basquet', 'masculino menor', '3516356486', 54487898, 'gege420@gmail.com', 10, 1, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(60, 'rudo', 'ipom', 'Basquet', 'masculino menor', '35153784234', 47173704, 'tomascipriano2003@gmail.com', 7, 2, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(61, '5342', '5243', 'Basquet', 'masculino menor', '4563456452', 25536363, '33245@gmail.cm', 8, 1, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(62, 'pari', 'pariii', 'Basquet', 'masculino mayor', '7362547862135', 47173704, 'tomascipriano2003@gmail.com', 6, 2, 'NO', 'NO', '2', '', 'no se cargo', 'sin definir', 0, NULL),
(63, '1234', '1234', 'Basquet', 'masculino mayor', '1234567897', 1234567, 'tomascipriano2003@gmail.com', 6, 2, 'NO', 'NO', 'NO', '', 'no se cargo', 'sin definir', 0, NULL),
(64, 'roopo', 'upc', 'Futbol', 'masculino mayor', '0900999999', 78787878, 'tomascipriano2003@gmail.com', 6, 2, 'NO', 'NO', 'NO', 'lol', 'no se cargo', 'sin definir', 0, NULL),
(65, 'popin', 'asus', 'Futbol', 'masculino menor', '0909090909', 1234567, 'tomascipriano2003@gmail.com', 7, 2, '1', 'NO', 'NO', 'se vale parry', 'no se cargo', 'sin definir', 0, NULL),
(66, 'hola  ami', 'kok', 'Futbol', 'masculino mayor', '1234546371', 47173345, 'tomascipriano2003@gmail.com', 6, 2, 'NO', '1', '2', 'No tengo ninguna duda', 'no se cargo', 'sin definir', 0, NULL),
(67, 'rompeportones', 'surich', 'Futbol', 'masculino menor', '8237498223', 1234567, 'tomascipriano2003@gmail.com', 8, 2, 'NO', 'NO', 'NO', 'sexo?', 'no se cargo', 'sin definir', 0, NULL),
(68, '1010001', 'binar', 'Futbol', 'masculino mayor', '11111111111', 47127638, 'tomascipriano2003@gmail.com', 6, 1, '1', '1', '1', 'se puede llevar chori', 'no se cargo', 'sin definir', 0, NULL),
(69, '23424', '23424', 'Futbol', 'masculino mayor', '2345234544', 46349345, 'tomascipriano2003@gmail.com', 6, 1, 'NO', 'NO', 'NO', 'se puede llevar c4', 'no se cargo', 'sin definir', 0, NULL),
(70, 'Juanis', 'Jovenes Argentinos', 'Futbol', 'masculino menor', '55457815152', 46768343, 'gege420@gmail.com', 6, 1, 'NO', 'NO', 'NO', 'Puedo traer a mi golden retriver?', 'no se cargo', 'sin definir', 0, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partidos`
--

CREATE TABLE `partidos` (
  `id` int NOT NULL,
  `deporte` varchar(100) NOT NULL,
  `categoria` varchar(20) NOT NULL,
  `horario` datetime DEFAULT NULL,
  `cancha` int DEFAULT NULL,
  `equipo1_id` int NOT NULL,
  `equipo2_id` int NOT NULL,
  `puntaje1` int DEFAULT NULL,
  `puntaje2` int DEFAULT NULL,
  `estado` varchar(20) NOT NULL,
  `grupo` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `partidos`
--

INSERT INTO `partidos` (`id`, `deporte`, `categoria`, `horario`, `cancha`, `equipo1_id`, `equipo2_id`, `puntaje1`, `puntaje2`, `estado`, `grupo`) VALUES
(9, 'Futbol', 'Masculino Mayor', NULL, NULL, 20, 23, NULL, NULL, 'Pendiente', 'A'),
(25, 'Basquet', 'Masculino menor', NULL, NULL, 25, 26, NULL, NULL, 'Pendiente', 'A'),
(26, 'Basquet', 'Masculino menor', NULL, NULL, 25, 27, NULL, NULL, 'Pendiente', 'A'),
(27, 'Basquet', 'Masculino menor', NULL, NULL, 26, 27, NULL, NULL, 'Pendiente', 'A'),
(28, 'Basquet', 'Femenino mayor', NULL, NULL, 28, 29, NULL, NULL, 'Pendiente', 'E'),
(29, 'Basquet', 'Femenino mayor', NULL, NULL, 28, 30, NULL, NULL, 'Pendiente', 'E'),
(30, 'Basquet', 'Femenino mayor', NULL, NULL, 28, 31, NULL, NULL, 'Pendiente', 'E'),
(31, 'Basquet', 'Femenino mayor', NULL, NULL, 29, 30, NULL, NULL, 'Pendiente', 'E'),
(32, 'Basquet', 'Femenino mayor', NULL, NULL, 29, 31, NULL, NULL, 'Pendiente', 'E'),
(33, 'Basquet', 'Femenino mayor', NULL, NULL, 30, 31, NULL, NULL, 'Pendiente', 'E');

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
('Fútbol', 'Masculino Mayor', 2, '1970-01-01'),
('Fútbol', 'Masculino Menor', 2, '1970-01-01'),
('Fútbol', 'Femenino Mayor', 2, '1970-01-01'),
('Fútbol', 'Femenino Menor', 2, '1970-01-01'),
('Básquet', 'Masculino Mayor', 2, '1970-01-01'),
('Básquet', 'Masculino Menor', 2, '1970-01-01'),
('Básquet', 'Femenino Mayor', 2, '1970-01-01'),
('Básquet', 'Femenino Menor', 2, '1970-01-01'),
('Voley', 'Masculino Mayor', 2, '1970-01-01'),
('Voley', 'Masculino Menor', 2, '1970-01-01'),
('Voley', 'Femenino Mayor', 2, '1970-01-01'),
('Voley', 'Femenino Menor', 2, '1970-01-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `gmail` varchar(30) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `descripcion` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `contraseña`, `gmail`, `rol`, `descripcion`) VALUES
(1, 'admin', 'scrypt:32768:8:1$uVn5gAJE6aHvXxoO$5813900f6f28edc6f49c691c6bf628808ce6bddb01342e65aea1decaa914c88069fd02365beebb9c3704f67cedd30fa9e6d4ee0174c00eac09132fbbbf17d733', 'd47474935@alumnos.itr.edu.ar', 'admin', NULL),
(2, 'pepe', 'scrypt:32768:8:1$CB3skurtLw8v7cOS$ad128bc78260841226382f8bb99762a99cb323b0a89895e3670a057fe993743784addf56f8f4fa53e72288276c676121c2c939d68cbcd76632d559f3b849611e', 'd47474935@alumnos.itr.edu.ar', 'planillero', 'Un usuario normal');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_deporte_categoria` (`deporte`,`categoria`);

--
-- Indices de la tabla `Inscripciones`
--
ALTER TABLE `Inscripciones`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `equipo_id` (`equipo_id`);

--
-- Indices de la tabla `partidos`
--
ALTER TABLE `partidos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `equipo1_id` (`equipo1_id`),
  ADD KEY `equipo2_id` (`equipo2_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `Inscripciones`
--
ALTER TABLE `Inscripciones`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT de la tabla `partidos`
--
ALTER TABLE `partidos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Inscripciones`
--
ALTER TABLE `Inscripciones`
  ADD CONSTRAINT `Inscripciones_ibfk_1` FOREIGN KEY (`equipo_id`) REFERENCES `equipos` (`id`);

--
-- Filtros para la tabla `partidos`
--
ALTER TABLE `partidos`
  ADD CONSTRAINT `partidos_ibfk_1` FOREIGN KEY (`equipo1_id`) REFERENCES `equipos` (`id`),
  ADD CONSTRAINT `partidos_ibfk_2` FOREIGN KEY (`equipo2_id`) REFERENCES `equipos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
