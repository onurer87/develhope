DROP TABLE IF EXISTS salesman;

--creates table

CREATE TABLE salesman (
	'salesman_id' INTEGER,
	'name' TEXT,
	'city' TEXT,
	'commission' FLOAT);

--insert values into table

INSERT INTO salesman 
VALUES (5001, "James Hoog", "New York", 0.15),
		(5002, "Nail Knite", "Paris", 0.13),
		(5005, "Pit Alex", "London", 0.11),
		(5006, "Mc Lyon", "Paris", 0.14),
		(5007,"Paul Adam", "Rome", 0.13),
		(5003,"Lauson Hen", "San Jose", 0.12);


--EX1.1	
SELECT * FROM salesman;

--Ex1.2
SELECT name FROM salesman ;
SELECT commission FROM salesman;