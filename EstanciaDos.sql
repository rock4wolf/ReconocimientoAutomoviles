DROP database Estanciados;
CREATE DATABASE Estanciados;
USE Estanciados;

CREATE TABLE Usuario(
Id_Usuario INT PRIMARY KEY auto_increment NOT NULL,
Nombre varchar(50) not null,
Correo varchar(50) not null,
Contraseña varchar(30) not null); 
 

CREATE TABLE Entrenamiento(
Id_Entre INT PRIMARY KEY auto_increment,
Ruta VARCHAR(100),
FechaEntre DATE);


CREATE TABLE Bitacora(
Id_Entre INT,
Id_Bit INT PRIMARY KEY NOT NULL auto_increment,
Id_Usuario INT  NOT NULL,
Agre_Fecha datetime  NOT NULL,
Pre DOUBLE NOT NULL,
Resultado VARCHAR(50)  NOT NULL,
Reporte INT NOT NULL,
FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario),
FOREIGN KEY (Id_Entre) REFERENCES Entrenamiento(Id_Entre));



select * from Usuario;
INSERT INTO `estanciados`.`Usuario` (`Nombre`, `Correo`, `Contraseña`) VALUES ('Hugo', 'gmho182862@upemor.edu.mx', 'hugogerardo');
INSERT INTO `estanciados`.`Usuario` (`Nombre`, `Correo`, `Contraseña`) VALUES ('Erik', 'azeo17000@upemor.edu.mx', 'erika');
INSERT INTO `estanciados`.`entrenamiento` (`Ruta`, `FechaEntre`) VALUES ('D:\\desarrollo\\Reconocimiento\\Modelo.model', '2020-11-20 23:59:59');
select * from Usuario;