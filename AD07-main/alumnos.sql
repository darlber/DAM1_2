-- crear database
DROP DATABASE IF EXISTS instituto;
CREATE DATABASE instituto CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
-- usuario 
DROP USER IF EXISTS 'usuario'@'%';
CREATE USER 'usuario'@'%' IDENTIFIED WITH mysql_native_password BY 'usuario';
GRANT ALL PRIVILEGES ON *.* TO 'usuario'@'%';
FLUSH PRIVILEGES;

USE instituto;
-- tabla alumnos
CREATE TABLE IF NOT EXISTS alumnos (
    DNI VARCHAR(9) NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(70) NOT NULL,
    Direccion VARCHAR(100) NOT NULL,
    FechaNac DATE NOT NULL,
    PRIMARY KEY (DNI)
);

-- insertamos en alumnos
INSERT INTO alumnos VALUES
('11111111X', 'Laura', 'Sánchez Romero', 'Calle Sol, nº5, Bajo B', '1995-05-22'),
('22222222Y', 'Pablo', 'Martínez López', 'Avda. América, nº12, 3ºA', '1993-09-17'),
('33333333Z', 'Clara', 'Torres Gil', 'C/Granada, nº8, 2ºC', '1994-01-30'),
('44444444W', 'Adrián', 'Ruiz Morales', 'Paseo de la Paz, nº19, 5ºD', '1996-12-03');

-- creamos la tabla matrículas que pide el enunciado
CREATE TABLE IF NOT EXISTS matriculas (
    DNI VARCHAR(9) NOT NULL,
    NombreModulo VARCHAR(60) NOT NULL,
    Curso VARCHAR(5) NOT NULL,
    Nota DOUBLE,
    FOREIGN KEY (DNI) REFERENCES alumnos(DNI)
);

-- Insertar valores de prueba en matriculas (4 por cada DNI)
INSERT INTO matriculas VALUES
-- Matrículas de Laura (DNI: 11111111X)
('11111111X', 'Matemáticas', '24-25', 9.1),
('11111111X', 'Física', '24-25', 8.4),
('11111111X', 'Historia', '24-25', 7.5),
('11111111X', 'Química', '24-25', 8.0),

-- Matrículas de Pablo (DNI: 22222222Y)
('22222222Y', 'Anatomía', '24-25', 7.8),
('22222222Y', 'Fisiología', '24-25', 8.2),
('22222222Y', 'Bioquímica', '24-25', 7.9),
('22222222Y', 'Microbiología', '24-25', 8.1),

-- Matrículas de Clara (DNI: 33333333Z)
('33333333Z', 'Biología', '23-24', 6.9),
('33333333Z', 'Genética', '23-24', 7.0),
('33333333Z', 'Ecología', '23-24', 7.3),
('33333333Z', 'Botánica', '23-24', 8.0),

-- Matrículas de Adrián (DNI: 44444444W)
('44444444W', 'Geografía', '24-25', 7.6),
('44444444W', 'Historia del Arte', '24-25', 8.2),
('44444444W', 'Literatura', '24-25', 7.8),
('44444444W', 'Filosofía', '24-25', 8.3);