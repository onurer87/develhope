--Deletes the table if already exists
DROP TABLE IF EXISTS clients;


--Creates table
CREATE TABLE clients (
	"surname" TEXT NOT NULL,
	"name" TEXT NOT NULL,
	"city" TEXT NOT NULL,
	"salary" INTEGER NOT NULL,
	"age" INTEGER NOT NULL
);

--Inserts data into table
INSERT INTO clients(surname, name, city, salary, age) 
VALUES	("Bianchi","Mario",	"Rimini", 1000, 20),
		("Bianchi","Ettore","Milano", 0, 15),
		("Casadei","Mario", "Rimini", 3000, 35),
		("Rossi","Mario","Bologna", 1500, 50),
		("Rossi","Fabio","Firenze", 8000, 40),
		("Bianchi", "Ettore","Rimini", 4500, 25),
		("Neri", "Fabio", "Arezzo", 3500, 35);

--Ex5.1
SELECT name, surname FROM clients
WHERE salary>3000;

--Ex5.2
SELECT surname, name FROM clients
WHERE city="Rimini";

--Ex5.3
SELECT surname, name FROM clients
WHERE city="Rimini" AND salary>3000;

--Ex5.4
SELECT surname, name, salary FROM clients
WHERE age>=20 AND age<=35;

--Ex5.5
SELECT surname, name, salary FROM clients
WHERE city="Rimini" AND age NOT BETWEEN 20 AND 30  ;