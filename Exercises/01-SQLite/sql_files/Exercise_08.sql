--Deletes the table if already exists
DROP TABLE IF EXISTS customer;

--Creates table
CREATE TABLE customer(
	"customer_id" INTEGER NOT NULL,
	"cust_name" TEXT NOT NULL,
	"city" TEXT NOT NULL,
	"grade" INTEGER,
	"salesman_id" INTEGER NOT NULL);


--Insert values
INSERT INTO	customer
VALUES  (3002, "Nick Rimando","New York",100,5001),
		(3005,"Graham Zusi","California", 200, 5002),
		(3004,"Fabian Johnson","Paris", 300, 5006),
		(3007,"Brad Davis","New York", 200, 5001),
		(3009,"Geoff Cameron","Berlin", 100, 5003),
		(3008,"Julian Green","London", 300, 5002),
		(3003,"Jozy Altidore","Moscow", 200, 5007),
		(3001,"Brad Guzan", "London",NULL , 5005);
	
SELECT * FROM customer;

--Ex8
SELECT city,MAX(grade) as "Maximum Grade" FROM customer
GROUP BY city;







