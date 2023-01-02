<<<<<<< HEAD
## A dataset containing pet rescue details was created using the attached sql script. The sql commands for the corresponding queries are listed below.

### Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.

SELECT SUM(COST) From PETRESCUE;

### Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.

SELECT SUM(COST) as SUM_OF_COST FROM PETRESCUE;

### Query A3: Enter a function that displays the maximum quantity of animals rescued.

SELECT max(ANIMAL) FROM Petrescue;

### Query A4: Enter a function that displays the average cost of animals rescued.

SELECT AVG(COST) FROM Petrescue;

### Query A5: Enter a function that displays the average cost of rescuing a dog.

select AVG( COST / QUANTITY ) FROM PETRESCUE where ANIMAL = 'Dog';



### Query B1: Enter a function that displays the rounded cost of each rescue.

SELECT ROUND(COST) FROM PETRESCUE;  

### Query B2: Enter a function that displays the length of each animal name.

SELECT length(animal) FROM petrescue;

### Query B3: Enter a function that displays the animal name in each rescue in uppercase.

SELECT ucase(animal) FROM petrescue;

### Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.

select distinct(ucase(animal)) FROM petrescue;

### Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.

select * FROM petrescue where lcase(animal) = 'cat';



### Query C1: Enter a function that displays the day of the month when cats have been rescued.

SELECT DAY(rescuedate) FROM Petrescue;

### Query C2: Enter a function that displays the number of rescues on the 5th month.

SELECT SUM(Quantity) FROM Petrescue WHERE MONTH(rescuedate) = '05';

### Query C3: Enter a function that displays the number of rescues on the 14th day of the month.

SELECT SUM(Quantity) FROM Petrescue WHERE DAY(rescuedate) = '14';

### Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.

SELECT (rescuedate + 3 DAYS) FROM petrescue;

### Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between today’s date and the rescue date.

SELECT (CURRENT_DATE - rescuedate) FROM petrescue;
=======
# Practice Repository
This repository is a collection of practice projects and exercises involving SQL, Jupyter notebooks, machine learning and APIs.

## Prerequisites
In order to run the code in this repository, you will need to have the following software installed:
- [Python 3.7 or higher](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/install)
- [SQLite3](https://www.sqlite.org/download.html)

You may also need to install additional libraries, such as 'pandas', 'sklearn' and 'requests', depending on the specific projects you are working on. These can be installed using pip.

## Getting Started
- Clone the repository to your local machine: git clone git@github.com:vishnu123r/Practice.git
- Navigate to the project directory: cd Practice
- Open a Jupyter Notebook by running jupyter notebook in the terminal
- From the Jupyter Notebook homepage, navigate to the project you want to work on and open the corresponding notebook file.

## Authors
Ramanah Visnupriyan
>>>>>>> bb05601fef5d07162ee473e215c46b1783fd8b78
