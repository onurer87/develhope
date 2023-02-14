--Deletes the table if exists
DROP TABLE IF EXISTS orders

--Creates the table
CREATE TABLE orders(
"ord_no" INTEGER NOT NULL,
"purch_amt" FLOAT NOT NULL,
"ord_date" DATE "yyyy-MM-dd" NOT NULL,
"customer_id" INTEGER NOT NULL,
"salesman_id" INTEGER NOT NULL);

--Insert the values
INSERT INTO orders
VALUES	(70001, 150.5, 2012-10-05, 3005, 5002),
		(70009, 270.65, 2012-09-10,3001,5005),
		(70002, 65.26, 2012-10-05, 3002, 5001),
		(70004, 110.5, 2012-08-17, 3009, 5003),
		(70007, 948.5, 2012-09-10, 3005, 5002),
		(70005, 2400.6, 2012-07-27, 3007, 5001),
		(70008, 5760, 2012-09-10, 3002, 5006),
		(70010, 1983.43, 2012-10-10, 3004, 5006),
		(70003, 2480.4, 2012-10-10, 3009, 5003),
		(70012, 250.45, 2012-06-27, 3008, 5002),
		(70011, 75.29, 2012-08-17, 3003, 5007),
		(70013, 3045.6, 2012-04-25, 3002, 5001);

--Show the table
SELECT * FROM orders;

--***QUESTION***: I couldn't manage to return date values as YYY-MM-DD format. Could you comment how to do it?

--Ex9.1
SELECT customer_id, ord_date, MAX(purch_amt) FROM orders
WHERE purch_amt>=2000 and purch_amt<=6000
GROUP BY customer_id;