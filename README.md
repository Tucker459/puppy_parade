# puppy_parade

--------
Go to the Results sections to see my comments about the data model, database, and programming lanaguages used. 
--------


You’re the first Data Engineer at NYC’s newest dog walking startup, Puppy Parade. Puppy
Parade is a marketplace for connecting dog-owning users with dog walkers. Users sign up for
the Puppy Parade app, drop off their house keys at Puppy Parade HQ, and let the app know
what days they want their dog to be walked. Every night the Puppy Parade algorithm assigns
routes for its dog-walkers to take.
Each morning, the dog walkers show up at Puppy Parade HQ for their shift and are given their
routes and sets of keys. Each walker goes through his or her route, picking up and dropping off
dogs along the way, ending up at Puppy Parade HQ to drop off their set of keys.
Your boss at Puppy Parade has given you your first assignment: Write a program to find out
some basic details about the Puppy Parade business on a given day. (Detailed below.)

## Input
You are given a database with the Puppy Parade route information for a single day for all the
dog walkers. The routes are stored as “stops” along the route where the dog walkers are
supposed to either pickup or drop-off a dog.
The database contains two tables route_stop and route_stop_time detailed below.

The route_stop table contains records with the dog walker ID, the dog info ID, the
address, whether the stop is a pickup or a drop-off, and the ID of the next stop in the
route. Each record is in the shape of (id, dog_walker_id, dog_info_id, address,
is_pickup, next_id) , where if is_pickup is true the stop is a pickup; otherwise it is a
drop-off. (Note that the initial pick up and final drop-off location of Puppy Parade HQ is
not included in this table.)

The route_stop_time table contains records of when the dog walker actually picks up
the dog using a GPS-enabled feature in the Puppy Parade dog walker app. The record
is in the shape of (route_stop_id, recorded_timestamp) .
The database also contains a fact table called dog_info about the registered dogs:

The dog_info table contains records important to know about the dogs, such as their
name, breed, and weight. Each record is in the shape of (id, name, breed, weight) .
You are guaranteed that there will be 1,000,000 rows or less in each table.
Here is a diagram of an example route. The Sample Input Dataset section below has
corresponding SQL queries that generates a database with this route.

## Output
For each dataset you’re given, output answers to following questions:

Which dog was outside the longest? Output this on a line as: Dog outside longest: "name"

Which breed of dog was outside the longest? Output this on a line as: Breed outside
longest: "breed"

What is the maximum number of dogs any walker has at any time throughout their
route? Output this on a line as: Most dogs any walker has: "number"
  
## Technical Instructions
Write a program that answers the above questions in a programming language from our list[*]
and using a database from our list[**]. Assume that the database is populated prior to running
your program; you do not need to write the code to populate the database.
[*] Languages: bash, C#, C++, Go, Java, JavaScript, python, Ruby, Scala, or SQL.
[**] Databases: PostgreSQL 9.5+, MySQL 5.7+, or SQLite3.
Additional details:

Your program may perform write operations to the database such as create new tables,
indexes, or views.

Your program should write its results to standard output.

We will run your program from start to finish against multiple datasets. The order of
grading execution for each dataset will be (1) we teardown any existing database
including tables, views, and indexes, (2) we load fresh data into the database, (3) we run
your program, and (4) compare its output to expected output.

## Sample Input Dataset
CREATE TABLE IF NOT EXISTS route_stop (
id INT,
dog_walker_id INT,
dog_info_id INT,
address TEXT,
is_pickup BOOLEAN,
next_id INT);

CREATE TABLE IF NOT EXISTS route_stop_time (
route_stop_id INT,
recorded_timestamp INT);

CREATE TABLE IF NOT EXISTS dog_info (
id INT,
breed TEXT,
name TEXT,
weight INT);

INSERT INTO dog_info (id, breed, name, weight) VALUES
(0, 'boxer', 'Jack', 5),
(1, 'beagle', 'Oliver', 23),
(2, 'poodle', 'Bella', 29);

INSERT INTO route_stop (id, dog_walker_id, dog_info_id, address, is_pickup,
next_id) VALUES
(0, 1, 0, '31 Mediterranean Ave', 'true', 1),
(1, 1, 1, '78 Baltic Ave', 'true', 2),
(2, 1, 2, '12 Oriental Ave', 'true', 3),
(3, 1, 2, '12 Oriental Ave', 'false', 4),
(4, 1, 1, '78 Baltic Ave', 'false', 5),
(5, 1, 0, '31 Mediterranean Ave', 'false', null);

INSERT INTO route_stop_time (route_stop_id, recorded_timestamp) VALUES
(0, 0),
(1, 186),
(2, 345),
(3, 518),
(4, 752),
(5, 1039);

## Sample Program Output
Dog outside longest: Jack

Breed outside longest: boxer

Most dogs any walker has: 3

# Results 

Programming Choice: SQL & Python
Database: Postgres 10.0

Running the Code:

Please run the ' wp_sql.sql ' file first using the below command.
Replace with correct username and database name that has access to database and tables:

psql -U christiantucker -d puppy_parade -a -f wp_sql.sql

Please run the ' wp_python.py ' file last using the below command.
Replace with correct username and database name that has access to database and tables:

./wp_python.py dbname username

e.g. ./wp_python.py puppy_parade christiantucker


Data Model:

I did assume there was a relationship between the id column from the route_stop table and the route_stop_id
column from the route_stop_time table. I assumed they had a direct relationship with each other. I also noted that the dog_info_id column had a direct relationship with the id column from the dog_info table. For tables route_stop_time and dog_info no nulls should be allowed or present in the table(in a magical world). All values shouldn't allow nulls except for the next_id column in the route_stop table. I also assumed there would be a primary key on both the route_stop_id column from the route_stop_time table and the id column from the dog_info table.
