DROP TABLE IF EXISTS salesman

CREATE TABLE salesman (
salesman_id integer NOT NULL,
name text NOT NULL,
city text NULL,
commission integer NOT NULL);

INSERT INTO salesman
VALUES	(5001, "JamesHoog", "New York", 0.15),
		(5002, "Nail Knite", "Paris", 0.13),
		(5005, "Pit Alex", "London", 0.11),
		(5006, "Mc Lyon", "Paris",  0.14),
		(5007, "Paul Adam", "Rome", 0.13),
		(5003, "Lauson Hen", NULL,  0.12);



DROP TABLE IF EXISTS customer
		
CREATE TABLE customer (
	customer_id integer NOT NULL,
	cust_name text NOT NULL,
	city text NOT NULL,
	grade integer,
	salesman_id integer NOT NULL)
			 
INSERT INTO customer
VALUES	(3002, "Nick Rimando", "New York", 100, 5001),
		(3005, "Graham Zusi", "California", 200, 5002),
		(3004, "Fabian Johnson", "Paris", 300, 5006),
		(3007, "Brad Davis", "New York", 200, 5001),
		(3009, "Geoff Cameron", "Berlin", 100, 5003),
		(3008, "Julian Green", "London", 300, 5002),
		(3003, "Jozy Altidore", "Moscow", 200, 5007),
		(3001, "Brad Guzan", "London", 0, 5005);



--ex16.1
	
SELECT customer.cust_name as"Customer Name", customer.city as "customer city", salesman.name as "Salesman", salesman.commission
FROM salesman
JOIN customer ON customer.salesman_id = salesman.salesman_id
WHERE salesman.commission >0.12;