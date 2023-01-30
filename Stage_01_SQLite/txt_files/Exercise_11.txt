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

--Ex11.1
SELECT salesman_id, MAX(purch_amt) FROM orders
WHERE salesman_id>=5003 and salesman_id<=5008
GROUP BY salesman_id
ORDER BY salesman_id;