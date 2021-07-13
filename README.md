A dataset containing pet rescue details was created and sql commands were written for the following queries

-- Drop the PETRESCUE table in case it exists
drop table PETRESCUE;
-- Create the PETRESCUE table 
create table PETRESCUE (
	ID INTEGER NOT NULL,
	ANIMAL VARCHAR(20),
	QUANTITY INTEGER,
	COST DECIMAL(6,2),
	RESCUEDATE DATE,
	PRIMARY KEY (ID)
	);
-- Insert sample data into PETRESCUE table
insert into PETRESCUE values 
	(1,'Cat',9,450.09,'2018-05-29'),
	(2,'Dog',3,666.66,'2018-06-01'),
	(3,'Dog',1,100.00,'2018-06-04'),
	(4,'Parrot',2,50.00,'2018-06-04'),
	(5,'Dog',1,75.75,'2018-06-10'),
	(6,'Hamster',6,60.60,'2018-06-11'),
	(7,'Cat',1,44.44,'2018-06-11'),
	(8,'Goldfish',24,48.48,'2018-06-14'),
	(9,'Dog',2,222.22,'2018-06-15')
	
;

## Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.

SELECT SUM(COST) From PETRESCUE;

-- Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.

SELECT SUM(COST) as SUM_OF_COST FROM PETRESCUE;

-- Query A3: Enter a function that displays the maximum quantity of animals rescued.

SELECT max(ANIMAL) FROM Petrescue;

-- Query A4: Enter a function that displays the average cost of animals rescued.

SELECT AVG(COST) FROM Petrescue;

-- Query A5: Enter a function that displays the average cost of rescuing a dog.

select AVG( COST / QUANTITY ) FROM PETRESCUE where ANIMAL = 'Dog';



--Query B1: Enter a function that displays the rounded cost of each rescue.

SELECT ROUND(COST) FROM PETRESCUE;  

--Query B2: Enter a function that displays the length of each animal name.

SELECT length(animal) FROM petrescue;

--Query B3: Enter a function that displays the animal name in each rescue in uppercase.

SELECT ucase(animal) FROM petrescue;

--Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.

select distinct(ucase(animal)) FROM petrescue;

--Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.

select * FROM petrescue where lcase(animal) = 'cat';



--Query C1: Enter a function that displays the day of the month when cats have been rescued.

SELECT DAY(rescuedate) FROM Petrescue;

--Query C2: Enter a function that displays the number of rescues on the 5th month.

SELECT SUM(Quantity) FROM Petrescue WHERE MONTH(rescuedate) = '05';

--Query C3: Enter a function that displays the number of rescues on the 14th day of the month.

SELECT SUM(Quantity) FROM Petrescue WHERE DAY(rescuedate) = '14';

--Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.

SELECT (rescuedate + 3 DAYS) FROM petrescue;

--Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between today’s date and the rescue date.

SELECT (CURRENT_DATE - rescuedate) FROM petrescue;
