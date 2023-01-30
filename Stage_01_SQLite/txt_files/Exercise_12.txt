--Deletes the table if exists
DROP TABLE IF EXISTS salesman


--Creates the table
CREATE TABLE salesman( 
"salesman_id" INTEGER NOT NULL,
"name" TEXT NOT NULL,
"city" TEXT NULL,
"commission" FLOAT NOT NULL);


--Insert the values into the table
INSERT INTO salesman
VALUES 	(5001,"James Hoog","New York",0.15),
		(5002,"Nail Knite","Paris",0.13),
		(5005,"Pit Alex","London",0.11),
		(5006,"Mc Lyon","Paris",0.14),
		(5003,"Lauson Hense",NULL,0.12),
		(5007,"Paul Adam","Rome",0.13);
	
--Show the table
SELECT * FROM salesman


--Ex12.1
SELECT city, COUNT(salesman_id) as "Number of Salespeople" FROM salesman
Group by city;