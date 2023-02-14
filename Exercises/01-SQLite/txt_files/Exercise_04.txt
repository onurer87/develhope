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

--Display the table
SELECT * FROM clients;




--Ex4.1
SELECT surname FROM clients;

--Ex4.2

SELECT name FROM clients;

--Ex4.3

SELECT name, surname FROM clients;

--Ex4.4

SELECT name, surname, city FROM clients;

--Ex4.5
SELECT * FROM clients;