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

--Ex7.1
SELECT AVG(age) FROM clients

--Ex7.2
SELECT city, AVG(age) FROM clients c 
GROUP BY city;

--Ex7.3
SELECT MAX(salary) FROM clients c 
WHERE city="Rimini";

--Ex7.4
SELECT city, COUNT(name), AVG(age) FROM clients c 
GROUP BY city;

--Ex7.5
SELECT city, COUNT(name) FROM clients c 
GROUP BY city
ORDER BY COUNT(name);