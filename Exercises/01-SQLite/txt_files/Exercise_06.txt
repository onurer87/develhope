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

--Ex6.1
SELECT MAX(salary) FROM clients;

--Ex6.2
SELECT AVG(age) FROM clients; 

--Ex6.3
SELECT MAX(salary) FROM clients c 
WHERE city="Rimini";

--Ex6.4
SELECT MAX(salary) FROM clients c 
WHERE age>=25 AND AGE<=40;

--Ex6.5
SELECT COUNT(age) FROM clients c 
WHERE age<25 OR age>35;