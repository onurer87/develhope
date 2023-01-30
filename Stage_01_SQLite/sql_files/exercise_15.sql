--ex15.1

DROP TABLE customer 

CREATE TABLE customer(
	customer_id INTEGER NOT NULL,
	cust_name TEXT NOT NULL,
	city TEXT NOT NULL,
	grade INTEGER NULL,
	salesman_id INTEGER NOT NULL);

INSERT INTO customer
VALUES 	(3002,"Nick Rimando", "New York", 100, 5001),
		(3005, "Graham Zusi","California", 200, 5002),
		(3004, "Fabian Johnson","Paris", 300, 5006),
		(3007,"Brad Davis","New York", 200, 5001),
		(3009,"Geoff Cameron","Berlin", 100, 5003),
		(3008,"Julian Green","London", 300, 5002),
		(3001,"Brad Guzan","London",NULL, 5005),
		(3003,"Jozy Altidore","Moscow", 200, 5007);

DROP TABLE orders 

CREATE TABLE orders(
ord_no INTEGER NOT NULL,
purch_amt FLOAT NOT NULL,
ord_date DATE "YYYY-MM-DD" NOT NULL,
customer_id INTEGER NOT NULL,
salesman_id INTEGER NOT NULL);

INSERT INTO orders 
VALUES 	(70001, 150.5, 2012-10-05, 3005, 5002),
		(70009, 270.65, 2012-09-10, 3001, 5005),
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


	
SELECT orders.ord_no, orders.purch_amt, customer.cust_name, customer.city
FROM orders
JOIN customer ON orders.customer_id = customer.customer_id
WHERE orders.purch_amt <2000 and orders.purch_amt > 500;