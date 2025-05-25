BEGIN TRANSACTION;
DROP TABLE IF EXISTS "tipos_reservas";
CREATE TABLE IF NOT EXISTS "tipos_reservas" (
	"tipo_reserva_id"	INTEGER NOT NULL,
	"nombre"	varchar(255) NOT NULL,
	"requiere_jornadas"	tinyint(1) NOT NULL DEFAULT '0',
	"requiere_habitaciones"	tinyint(1) NOT NULL DEFAULT '0',
	PRIMARY KEY("tipo_reserva_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "tipos_cocina";
CREATE TABLE IF NOT EXISTS "tipos_cocina" (
	"tipo_cocina_id"	INTEGER NOT NULL,
	"nombre"	varchar(255) NOT NULL,
	PRIMARY KEY("tipo_cocina_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "salones";
CREATE TABLE IF NOT EXISTS "salones" (
	"salon_id"	INTEGER NOT NULL UNIQUE,
	"nombre"	varchar(255) NOT NULL,
	PRIMARY KEY("salon_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Clientes";
CREATE TABLE IF NOT EXISTS "Clientes" (
	"Id"	INTEGER,
	"Nombre"	TEXT NOT NULL,
	"Apellidos"	TEXT NOT NULL,
	"Num_Identificacion"	TEXT NOT NULL UNIQUE,
	"Fec_Nac"	date,
	"Pais"	TEXT,
	"Telefono"	TEXT,
	"email"	TEXT,
	"Sexo"	TEXT,
	"Menores"	INTEGER,
	PRIMARY KEY("Id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "reservas";
CREATE TABLE IF NOT EXISTS "reservas" (
	"reserva_id"	INTEGER NOT NULL,
	"tipo_reserva_id"	INTEGER NOT NULL,
	"salon_id"	INTEGER NOT NULL,
	"tipo_cocina_id"	INTEGER NOT NULL,
	"id_Cliente"	INTEGER NOT NULL,
	"fecha"	date NOT NULL,
	"ocupacion"	INTEGER NOT NULL,
	"jornadas"	INTEGER NOT NULL,
	"habitaciones"	INTEGER NOT NULL DEFAULT '0',
	FOREIGN KEY("id_Cliente") REFERENCES "Clientes"("id"),
	FOREIGN KEY("salon_id") REFERENCES "salones"("salon_id"),
	PRIMARY KEY("reserva_id" AUTOINCREMENT),
	FOREIGN KEY("tipo_cocina_id") REFERENCES "tipos_cocina"("tipo_cocina_id"),
	UNIQUE("salon_id","fecha"),
	FOREIGN KEY("tipo_reserva_id") REFERENCES "tipos_reservas"("tipo_reserva_id")
);
INSERT INTO "tipos_reservas" ("tipo_reserva_id","nombre","requiere_jornadas","requiere_habitaciones") VALUES (1,'Banquete',0,0),
 (2,'Jornada',0,0),
 (3,'Congreso',1,1);
INSERT INTO "tipos_cocina" ("tipo_cocina_id","nombre") VALUES (1,'Bufé'),
 (2,'Carta'),
 (3,'Pedir cita con el chef'),
 (4,'No precisa');
INSERT INTO "salones" ("salon_id","nombre") VALUES (1,'Salón Habana'),
 (2,'Otro Salón');
INSERT INTO "Clientes" ("Id","Nombre","Apellidos","Num_Identificacion","Fec_Nac","Pais","Telefono","email","Sexo","Menores") VALUES (1,'Iván','Cuartango Del Río','2W','08/02/2003','España','416568265','icuartan@gmail.com','H',1),
 (2,'María Azucena','García Mayor','3A','13/06/2003','España','602724480','mgarcía@gmail.com','M',1),
 (3,'Álvaro','Gómez Tejada','4G','11/09/2006','Reino Unido','721376842','ágómez t@gmail.com','H',0),
 (4,'Adrián','Gregorio Ortiz','5M','07/02/2005','Nigeria','659641230','agregori@gmail.com','H',0),
 (5,'Alonso','Guerrero García','6Y','06/09/1983','Somalia','1697052230','aguerrer@gmail.com','H',0),
 (6,'Bilal','Hamdach El Amri','7F','16/10/2002','Tailandia','393331228','bhamdach@gmail.com','M',1),
 (7,'Sergio','Lapeña Martínez','8P','17/07/2006','Irán','726568228','slapeña@gmail.com','H',0),
 (8,'Pablo','Menéndez Mendoza','9D','08/04/1991','España','222837147','pmenénde@gmail.com','H',0),
 (9,'DanielA','Monje Malvar','10X','31/05/2004','Colombia','1357985817','dmonje m@gmail.com','M',0),
 (10,'Javier','Muela Mazarío','11B','21/04/2006','USA','726775466','jmuela m@gmail.com','N',0),
 (11,'Raimundo Jesús Atuba','Nguema Ayetebe','12N','08/07/2003','España','474131221','rnguema@gmail.com','N',1),
 (12,'César','Nicolás Carrascosa','13J','26/02/2000','España','497856212','cnicolás@gmail.com','H',1),
 (13,'Borislav','Nikolaev Mladenov','14Z','25/04/2005','Países Bajos','630812215','bnikolae@gmail.com','M',1),
 (14,'Sergio','Romero Tejedor','15S','03/01/2004','México','1629071747','sromero@gmail.com','H',1),
 (15,'David','Vargas Del Santo','16Q','16/11/2006','Reino Unido','703998180','dvargas@gmail.com','H',0),
 (17,'Diego','Barroso Torres','1R','28/07/2006','España','711133226','dbarroso@gmail.com','H',0);
INSERT INTO "reservas" ("reserva_id","tipo_reserva_id","salon_id","tipo_cocina_id","id_Cliente","fecha","ocupacion","jornadas","habitaciones") VALUES (1,1,1,1,1,'20/12/2024',35,0,0),
 (2,2,2,2,2,'14/01/2025',2,0,0),
 (3,1,2,1,3,'17/01/2025',1,0,0),
 (4,2,2,1,4,'20/01/2025',3,0,0),
 (5,1,1,2,5,'20/11/2024',35,0,0),
 (6,1,1,1,6,'21/11/2024',3,0,0),
 (7,3,2,3,7,'10/01/2025',2,0,0),
 (8,1,1,1,8,'21/10/2024',1,0,0),
 (9,1,2,1,9,'13/01/2025',1,0,0),
 (10,3,1,2,10,'01/12/2024',3,1,1),
 (11,2,1,2,11,'01/10/2024',5,0,0),
 (12,2,1,2,12,'02/10/2024',5,0,0),
 (14,1,1,2,14,'25/12/2024',3,0,0),
 (15,2,2,1,15,'23/01/2025',3,0,0),
 (16,2,2,1,10,'27/12/2024',4,0,0),
 (17,2,2,3,17,'22/01/2025',4,0,0);
COMMIT;
