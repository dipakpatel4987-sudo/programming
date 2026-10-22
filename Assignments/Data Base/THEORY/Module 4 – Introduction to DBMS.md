Module 4 – Introduction to DBMS



Q1. 	What is SQL, and why is it essential in database management?

->	SQL (Structured Query Language) is the standard language used to create, store, retrieve, modify, and control data in relational databases. It is declarative: you state what data 	you want, and the database decides how to get it.
	It is essential because: (1) it is a universal standard supported by MySQL, Oracle, SQL Server, PostgreSQL, and others; (2) it handles all database tasks, from defining structure 	to securing data; (3) it processes large volumes of data efficiently; (4) it is easy to learn, with English-like commands; and (5) nearly every application with a database relies 	on it.

Q2. 	Explain the difference between DBMS and RDBMS.

->	A DBMS is software that stores and manages data. An RDBMS is a DBMS that stores data in related tables (rows and columns) and uses SQL.
	
	-------------------------------------------------------------------------------------------------------------------------
	Feature			DBMS						RDBMS
	--------------------------------------------------------------------------------------------------------------------------
	Data storage		Files, hierarchical or navigational form	Tables with rows and columns
	Relationships		Not supported or weak				Tables linked by primary and foreign keys
	Normalization		Not supported					Supported
	Integrity constraints	Limited						Full support
	ACID properties		Not guaranteed					Supported
	Users			Usually single user				Multi-user
	Examples		File system, XML stores				MySQL, Oracle, SQL Server, PostgreSQL




3. 	Describe the role of SQL in managing relational databases.

->	SQL is the interface to an RDBMS. It is used to define structures (DDL: CREATE, ALTER, DROP), manipulate data (DML: INSERT, UPDATE, DELETE), query data (DQL: SELECT), control 	access (DCL: GRANT, REVOKE), and manage transactions (TCL: COMMIT, ROLLBACK, SAVEPOINT). It also enforces integrity through constraints, combines tables using joins, and supports 	reusable logic through views, stored procedures, and triggers.


4. 	What are the key features of SQL?

->	1. Simple and English-like syntax.
	2. Declarative: describes the result, not the procedure.
	3. Standardized (ANSI/ISO), so skills transfer between databases.
	4. Complete data handling: definition, manipulation, querying, control.
	5. Data integrity through constraints.
	6. Security through privileges and roles.
	7. Powerful querying: filtering, sorting, grouping, aggregation, joins, subqueries.
	8. Transaction support with ACID guarantees.
	9. Programmability: views, stored procedures, functions, triggers.
	10. Multi-user and scalable.


Q5. 	What are the basic components of SQL syntax?

->	• Keywords: reserved words such as SELECT, FROM, WHERE (not case-sensitive).
	• Identifiers: names of databases, tables, and columns.
	• Literals: fixed values such as 10, 'Asha', '2024-01-15'.
	• Operators: arithmetic (+ - * /), comparison (= <> > < >= <=), logical (AND OR NOT), plus LIKE, IN, BETWEEN, IS NULL.
	• Expressions: combinations of values and operators, such as price * 1.1.
	• Clauses: parts of a statement such as WHERE, ORDER BY.
	• Functions: COUNT(), SUM(), UPPER().
	• Comments: -- single line and /* multi line */.
	• Terminator: statements end with a semicolon ;.

Q6. 	Write the general structure of an SQL `SELECT` statement.

->	SELECT   column1, column2, aggregate_function(column)
	FROM     table_name
	[WHERE    condition]
	[GROUP BY column1, column2]
	[HAVING   group_condition]
	[ORDER BY column1 [ASC | DESC]]
	[LIMIT    n];
	Example: SELECT student_name, age FROM students WHERE age > 10 ORDER BY age DESC; The logical execution order is FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.


Q7. 	Explain the role of clauses in SQL statements.

->	A clause is a component of a statement that performs a specific job.
	• SELECT: chooses the columns to return.
	• FROM: names the source table(s).
	• WHERE: filters rows before grouping.
	• GROUP BY: groups rows that share values.
	• HAVING: filters groups after aggregation.
	• ORDER BY: sorts the result.
	• LIMIT (or TOP/FETCH): restricts the number of rows.
	Clauses let you build precise queries step by step.


Q8. 	What are constraints in SQL? List and explain the different types of constraints.

->	Constraints are rules applied to columns or tables to keep data accurate and consistent. Invalid data is rejected.
	------------------------------------------------------------------------------------------------------------------------------
	Constraint		Purpose							Example
	------------------------------------------------------------------------------------------------------------------------------
	NOT NULL		Column cannot hold NULL					name VARCHAR(50) NOT NULL
	UNIQUE			All values in the column are distinct			email VARCHAR(50) UNIQUE
	PRIMARY KEY		Uniquely identifies each row (NOT NULL + UNIQUE)	id INT PRIMARY KEY
	FOREIGN KEY		Links a column to the primary key of another table	FOREIGN KEY (tid) REFERENCES teachers(tid)
	CHECK			Values must satisfy a condition				CHECK (price > 0)
	DEFAULT			Supplies a value when none is given			city VARCHAR(20) DEFAULT 'Delhi'


Q9. 	How do PRIMARY KEY and FOREIGN KEY constraints differ? 	

->	
	----------------------------------------------------------------------------------------------------------------------------------
	Feature			PRIMARY KEY					FOREIGN KEY
	----------------------------------------------------------------------------------------------------------------------------------
	Purpose			Uniquely identifies a row in its own table	Creates a link to another table
	Duplicates		Not allowed					Allowed
	NULL			Not allowed					Allowed
	Per table		Only one (may be composite)			Many allowed
	Dependence		Independent					Must match an existing primary (or unique) key in the parent table
	
	A foreign key maintains referential integrity: you cannot insert a child row that points to a non-existent parent, or delete a parent that still has children (unless ON DELETE 	CASCADE or similar is set).


Q10. 	What is the role of NOT NULL and UNIQUE constraints?

->	NOT NULL ensures a column always has a value, so mandatory fields (such as teacher_name) cannot be left empty. UNIQUE ensures no two rows have the same value in that column (such 	as email). A UNIQUE column can hold NULL (the number of NULLs allowed depends on the database), and a table can have many UNIQUE constraints, unlike PRIMARY KEY.



Q11. 	Define the SQL Data Definition Language (DDL).

->	DDL is the group of SQL commands that define and change the structure of database objects (databases, tables, indexes, views). Commands: CREATE (make objects), ALTER (modify them), 	DROP (delete them), TRUNCATE (remove all rows quickly), and RENAME. DDL changes are generally auto-committed and cannot be rolled back in most databases.


Q12. 	Explain the CREATE command and its syntax.

->	CREATE builds new database objects.

	CREATE DATABASE school_db;

	CREATE TABLE table_name (
    		column1 datatype [constraint],
    		column2 datatype [constraint],
    		...
    		[table_constraints]
	);

	CREATE TABLE courses (
    		course_id      INT PRIMARY KEY,
    		course_name    VARCHAR(50) NOT NULL,
    		course_credits INT
	);

	Other forms: CREATE VIEW, CREATE INDEX, CREATE PROCEDURE, CREATE TRIGGER.


Q13. 	What is the purpose of specifying data types and constraints during table creation?

->	 Data types (INT, VARCHAR(n), DATE, DECIMAL(p,s)) define what kind of data a column accepts, which controls storage size, valid operations, and sorting behavior. Constraints 	enforce business rules (required values, uniqueness, valid ranges, relationships). Together they guarantee data integrity and accuracy, save space, improve performance, and stop 	invalid data entering at the database level.


Q14. 	What is the use of the `ALTER` command in SQL?

->	 ALTER is a DDL command that changes the structure of an existing table without deleting it or its data. It can add, modify, or drop columns, add or drop constraints, and rename 	the table or columns.

Q15. 	How can you add, modify, and drop columns from a table using ALTER?

->	-- Add a column
	ALTER TABLE courses ADD course_duration VARCHAR(20);

	-- Modify a column's data type/size
	ALTER TABLE courses MODIFY course_name VARCHAR(100);   -- MySQL / Oracle
	-- SQL Server: ALTER TABLE courses ALTER COLUMN course_name VARCHAR(100);

	-- Drop a column
	ALTER TABLE courses DROP COLUMN course_credits;
	Constraints can be handled similarly, for example ALTER TABLE courses ADD CONSTRAINT chk CHECK (course_credits > 0);. Dropping a column permanently deletes its data.


Q16. 	What is the function of the DROP command in SQL?

->	DROP is a DDL command that permanently removes a database object, including its structure and data: DROP TABLE teachers;, DROP DATABASE school_db;, DROP VIEW v1;. IF EXISTS avoids 	errors if the object is missing: DROP TABLE IF EXISTS teachers;.


Q17. 	What are the implications of dropping a table from a database?

->	1. All data and structure are permanently lost, and DDL usually cannot be rolled back.
	2. Dependent objects (views, triggers, stored procedures) may become invalid.
	3. Foreign key references from other tables can block the drop until those constraints are removed (or the child tables are dropped first).
	4. Indexes and privileges tied to the table are removed.
	5. Always take a backup first.
	Compare: DELETE removes selected rows (can be rolled back), TRUNCATE removes all rows but keeps the table, and DROP removes the table itself.


Q18. 	Define the INSERT, UPDATE, and DELETE commands in SQL.

->	DML commands change the data inside tables.

	-- INSERT: adds new rows
	INSERT INTO courses (course_id, course_name, course_duration)
	VALUES (1, 'SQL Basics', '3 months');

	-- UPDATE: modifies existing rows
	UPDATE courses SET course_duration = '4 months' WHERE course_id = 1;

	-- DELETE: removes rows
	DELETE FROM courses WHERE course_id = 1;


Q19. 	What is the importance of the WHERE clause in UPDATE and DELETE operations?

->	WHERE selects which rows are affected. Without it, UPDATE changes every row and DELETE removes every row in the table, usually a serious mistake. WHERE provides precision and 	safety. Good practice: run a SELECT with the same WHERE first to confirm the rows, and use transactions so errors can be rolled back.


Q20. 	Explain the use of the ORDER BY and WHERE clauses in SQL queries.

->	WHERE filters rows using conditions (=, >, BETWEEN, IN, LIKE, IS NULL, combined with AND/OR). ORDER BY sorts the result by one or more columns, ascending (ASC, default) or 	descending (DESC).
	SELECT * FROM courses
	WHERE course_credits >= 3
	ORDER BY course_name ASC;
	WHERE reduces the rows; ORDER BY arranges what remains. WHERE comes before ORDER BY in the statement.


Q21. 	What is the purpose of GRANT and REVOKE in SQL?

->	 DCL controls access to data. GRANT gives privileges to users or roles; REVOKE takes them back. This protects data by allowing each user to do only what they need.
	GRANT SELECT ON courses TO user1;
	REVOKE SELECT ON courses FROM user1;


Q22. 	How do you manage privileges using these commands?

->	CREATE USER user1 IDENTIFIED BY 'pass123';             -- MySQL form
	GRANT SELECT, INSERT ON courses TO user1;              -- object privileges
	GRANT ALL PRIVILEGES ON courses TO user2;
	GRANT SELECT ON courses TO user1 WITH GRANT OPTION;    -- user1 may pass it on
	REVOKE INSERT ON courses FROM user1;
	Privilege types: object privileges (SELECT, INSERT, UPDATE, DELETE, EXECUTE on a specific object) and system privileges (CREATE TABLE, CREATE USER). Group privileges into roles 	(CREATE ROLE, GRANT role TO user) to manage many users easily. Follow the principle of least privilege.

	
Q23. 	What is the purpose of the COMMIT and ROLLBACK commands in SQL?

->	 A transaction is a group of statements treated as one unit. COMMIT makes all changes in the transaction permanent. ROLLBACK undoes all changes since the last commit (or to a 	savepoint).
	INSERT INTO courses VALUES (4, 'Java', '2 months');
	COMMIT;       -- saved permanently

	INSERT INTO courses VALUES (5, 'C++', '2 months');
	ROLLBACK;     -- the C++ insert is undone

	
Q24. 	Explain how transactions are managed in SQL databases.

->	A transaction starts with the first DML statement (or START TRANSACTION/BEGIN) and ends with COMMIT or ROLLBACK. Databases guarantee the ACID properties:
	• Atomicity: all steps succeed or none do.
	• Consistency: data moves from one valid state to another.
	• Isolation: concurrent transactions do not interfere with each other (controlled by isolation levels and locks).
	• Durability: committed data survives crashes (via transaction logs).
	TCL commands: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION. Example: in a bank transfer, debit and credit must both succeed, otherwise the whole transaction is rolled back. Many 	systems have auto-commit on by default (MySQL), and DDL statements commit implicitly.


Q25. 	Explain the concept of JOIN in SQL. What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?

->	A JOIN combines rows from two or more tables based on a related column (usually a foreign key matching a primary key).
	----------------------------------------------------------------------------------------------------------------------------------------------------------------
	Join				Result
	----------------------------------------------------------------------------------------------------------------------------------------------------------------
	INNER JOIN			Only rows with matching values in both tables
	LEFT JOIN (LEFT OUTER)		All rows from the left table plus matches from the right; unmatched right columns are NULL
	RIGHT JOIN (RIGHT OUTER)	All rows from the right table plus matches from the left; unmatched left columns are NULL
	FULL OUTER JOIN			All rows from both tables; NULLs where there is no match (not supported in MySQL; emulate with UNION of LEFT and RIGHT joins)
	Other joins: CROSS JOIN (every combination) and SELF JOIN (a table joined with itself).


Q26. 	How are joins used to combine data from multiple tables?

->	Data is split across tables to avoid duplication (normalization). Joins bring it back together using a common column in the ON clause.
	SELECT e.emp_name, d.dept_name
	FROM employees e
	INNER JOIN departments d ON e.dept_id = d.dept_id;

	-- All departments, even those with no employees
	SELECT d.dept_name, e.emp_name
	FROM departments d
	LEFT JOIN employees e ON d.dept_id = e.dept_id;
	More than two tables can be joined by chaining joins. Table aliases (e, d) keep queries short.


Q27. 	What is the GROUP BY clause in SQL? How is it used with aggregate functions?

->	GROUP BY groups rows that have the same values in specified columns so that aggregate functions can be applied to each group: COUNT(), SUM(), AVG(), MIN(), MAX().
	SELECT dept_id, COUNT(*) AS total_employees, AVG(salary) AS avg_salary
	FROM employees
	GROUP BY dept_id
	HAVING COUNT(*) > 2;
	Every non-aggregated column in SELECT must appear in GROUP BY. HAVING filters groups after aggregation, while WHERE filters rows before grouping.


Q28. Explain the difference between GROUP BY and ORDER BY.

->
	----------------------------------------------------------------------------------------
	Feature				GROUP BY			ORDER BY
	Purpose				Groups rows for aggregation	Sorts the result rows
	Output rows			One row per group		Same number of rows as the input
	Aggregate functions		Typically used with them	Not required
	Filter option			HAVING				None
	Position			After WHERE			Near the end of the query
	
	They can be combined: ... GROUP BY dept_id ORDER BY COUNT(*) DESC;

Q29. 	What is a stored procedure in SQL, and how does it differ from a standard SQL query?

->	A stored procedure is a named, precompiled set of SQL statements stored in the database and executed by calling its name. It can accept parameters (IN, OUT, INOUT), contain logic 	(variables, IF, loops), and run multiple statements.
	DELIMITER //
	CREATE PROCEDURE get_emp_by_dept (IN d_id INT)
	BEGIN
    		SELECT * FROM employees WHERE dept_id = d_id;
	END //
	DELIMITER ;

	CALL get_emp_by_dept(10);
	------------------------------------------------------------------------------------------------------------
	Feature			Standard query				Stored procedure
	------------------------------------------------------------------------------------------------------------
	Storage			Sent from the client each time		Stored on the server
	Reuse			Retyped					Called by name
	Parameters		None					Supported
	Logic			Single statement			Multiple statements, conditions, loops
	Performance		Parsed each time			Precompiled and cached




Q30. 	Explain the advantages of using stored procedures.

->	1. Performance: precompiled execution plans, less parsing.
	2. Reusability: write once, call from many applications.
	3. Reduced network traffic: one call instead of many statements.
	4. Security: users can be granted EXECUTE without direct table access; helps prevent SQL injection when parameterized.
	5. Maintainability: business logic changes in one place.
	6. Consistency: the same logic is applied everywhere.
	7. Transaction handling can be encapsulated inside.

Q31. 	What is a view in SQL, and how is it different from a table?

->	A view is a virtual table defined by a stored SELECT query. It stores no data of its own; the data is fetched from the base tables each time the view is used.
	CREATE VIEW emp_dept_view AS
	SELECT e.emp_name, d.dept_name
	FROM employees e JOIN departments d ON e.dept_id = d.dept_id;

	SELECT * FROM emp_dept_view;
	------------------------------------------------------------------------------------------------------------------------
	Feature				Table				View
	------------------------------------------------------------------------------------------------------------------------
	Data storage			Physically stores data		No data stored (virtual)
	Created by			CREATE TABLE			CREATE VIEW ... AS SELECT
	Updates				Always updatable		Updatable only if simple (single table, no aggregates)
	Space				Uses storage			Almost none


Q32. 	Explain the advantages of using views in SQL databases.

->	1. Security: expose only selected columns or rows and hide sensitive data.
	2. Simplicity: wrap complex joins and calculations in a simple name.
	3. Reusability and consistency: the same query logic is used everywhere.
	4. Logical data independence: the view can stay stable even if the underlying structure changes.
	5. Customized presentation: different users see different views of the same data.
	6. No extra storage (for ordinary views).


Q33. 	What is a trigger in SQL? Describe its types and when they are used.

->	A trigger is a special stored program that runs automatically when a specified event (INSERT, UPDATE, or DELETE) occurs on a table. It cannot be called directly.
	Types by timing: BEFORE (runs before the event, useful for validation and changing values), AFTER (runs after, useful for logging and auditing), and INSTEAD OF (replaces the event, 	mainly on views in Oracle and SQL Server).
	Types by level: row-level (runs once for each affected row) and statement-level (runs once per statement).
	Uses: auditing and logging changes, enforcing complex business rules, automatically updating related tables or timestamps, and validating data.

	CREATE TRIGGER trg_emp_log
	AFTER INSERT ON employees
	FOR EACH ROW
	INSERT INTO emp_log (emp_id, action, log_time)
	VALUES (NEW.emp_id, 'INSERT', NOW());


Q34. 	Explain the difference between INSERT, UPDATE, and DELETE triggers.

->	
	--------------------------------------------------------------------------------------------------------------------------------
	Trigger			Fires when			Available row values		Typical use
	--------------------------------------------------------------------------------------------------------------------------------
	INSERT			A new row is added		NEW only			Log new records, set defaults
	UPDATE			An existing row changes		OLD and NEW			Update last_modified, audit changes
	DELETEA 		row is removed			OLD only			Archive deleted data, block deletion

	NEW holds the incoming values and OLD holds the previous values (in Oracle, :NEW and :OLD). Triggers should be used carefully, since hidden logic can slow operations and complicate 	debugging.

Q35. 	What is PL/SQL, and how does it extend SQL's capabilities?

->	 PL/SQL (Procedural Language/SQL) is Oracle's procedural extension of SQL. SQL is declarative and runs one statement at a time; PL/SQL adds programming features: variables and 	constants, conditions (IF), loops, exception handling, procedures, functions, packages, triggers, and cursors. Code is written in blocks:
	DECLARE
    		v_count NUMBER;
	BEGIN
    		SELECT COUNT(*) INTO v_count FROM employees;
    		DBMS_OUTPUT.PUT_LINE('Total employees: ' || v_count);
	EXCEPTION
    		WHEN OTHERS THEN
        		DBMS_OUTPUT.PUT_LINE('Error occurred');
	END;


Q36. 	List and explain the benefits of using PL/SQL.

->	1. Procedural power: conditions, loops, and variables alongside SQL.
	2. Better performance: a whole block is sent to the server in one call, reducing network traffic.
	3. Tight SQL integration: SQL statements and data types are used directly.
	4. Error handling: EXCEPTION blocks catch and manage runtime errors.
	5. Modularity and reusability: procedures, functions, and packages.
	6. Security: logic stored on the server with controlled access.
	7. Portability across Oracle platforms.


Q37. 	What are control structures in PL/SQL? Explain the IF-THEN and LOOP control structures.

->	Control structures control the order in which statements run. They are conditional (IF, CASE), iterative (LOOP, WHILE, FOR), and sequential (GOTO, EXIT, CONTINUE).
	IF-THEN:
	IF v_salary > 50000 THEN
    		DBMS_OUTPUT.PUT_LINE('High');
	ELSIF v_salary > 30000 THEN
    		DBMS_OUTPUT.PUT_LINE('Medium');
	ELSE
    		DBMS_OUTPUT.PUT_LINE('Low');
	END IF;

		LOOP types:

	-- Basic LOOP (needs EXIT)
	LOOP
    		i := i + 1;
    		EXIT WHEN i > 5;
	END LOOP;

	-- WHILE LOOP
	WHILE i <= 5 LOOP
    		i := i + 1;
	END LOOP;

	-- FOR LOOP
	FOR i IN 1..5 LOOP
    		DBMS_OUTPUT.PUT_LINE(i);
	END LOOP;


Q38. 	How do control structures in PL/SQL help in writing complex queries?

->	Plain SQL cannot make decisions or repeat actions. Control structures let you apply business rules (for example, give different bonuses by department), process data row by row 	(loop through a cursor), validate data before changing it, repeat operations (batch updates), and handle different outcomes with conditions and exceptions. This makes it possible 	to build multi-step logic, calculations, and reports that a single SQL statement cannot express.


Q39. 	What is a cursor in PL/SQL? Explain the difference between implicit and explicit cursors.

->	A cursor is a pointer to the private memory area (context area) where the result set of a SQL statement is held, letting a program process the returned rows one at a time.
	-----------------------------------------------------------------------------------------------------------------------------------------------------------------
	Feature					Implicit cursor									Explicit cursor
	-----------------------------------------------------------------------------------------------------------------------------------------------------------------
	Created by			Oracle automatically for each DML statement and single-row SELECT INTO		The programmer, for a multi-row SELECT
	Control				None										Full: DECLARE, OPEN, FETCH, CLOSE
	Rows				One row (SELECT INTO) or DML result						Multiple rows, processed one by one
	Attributes			SQL%FOUND, SQL%NOTFOUND, SQL%ROWCOUNT						cur%FOUND, cur%NOTFOUND, cur%ROWCOUNT, cur%ISOPEN

	DECLARE
    		CURSOR c_emp IS SELECT emp_name, salary FROM employees;
    		v_name employees.emp_name%TYPE;
    		v_sal  employees.salary%TYPE;
	BEGIN
    		OPEN c_emp;
    		LOOP
        		FETCH c_emp INTO v_name, v_sal;
        		EXIT WHEN c_emp%NOTFOUND;
        		DBMS_OUTPUT.PUT_LINE(v_name || ' - ' || v_sal);
    	END LOOP;
    	CLOSE c_emp;
	END;
	/


Q40. 	When would you use an explicit cursor over an implicit one?

->	Use an explicit cursor when: (1) a query returns multiple rows that must be processed one at a time (an implicit SELECT INTO fails with TOO_MANY_ROWS); (2) you need precise control 	over opening, fetching, and closing; (3) you want to apply different logic to each row; (4) you need cursor attributes during processing; or (5) you want a parameterized or 	reusable query. Use implicit cursors for simple DML and queries that return exactly one row.


Q41. 	Explain the concept of SAVEPOINT in transaction management. How do ROLLBACK and COMMIT interact with savepoints?

->	A SAVEPOINT marks a point inside a transaction to which you can later roll back without undoing the whole transaction.

	INSERT INTO courses VALUES (1, 'SQL', '3 months');
	SAVEPOINT sp1;
	INSERT INTO courses VALUES (2, 'PL/SQL', '2 months');
	SAVEPOINT sp2;
	INSERT INTO courses VALUES (3, 'Java', '4 months');

	ROLLBACK TO sp1;   -- undoes inserts 2 and 3; insert 1 remains (still uncommitted)
	COMMIT;            -- makes insert 1 permanent
	Interaction: ROLLBACK TO savepoint undoes changes made after that savepoint and discards any later savepoints, but the transaction stays active. A plain ROLLBACK undoes everything 	since the last commit and removes all savepoints. COMMIT makes all remaining changes permanent and erases all savepoints. RELEASE SAVEPOINT name removes a savepoint.


Q42. 	When is it useful to use savepoints in a database transaction?

->	Savepoints are useful when: (1) a long transaction has several steps and only the failed step should be undone; (2) you want to retry part of an operation after an error; (3) error 	handling in procedures needs to undo a partial failure but continue the rest; (4) you want to test or experiment with changes safely; and (5) batch processing should keep the good 	records and skip only the bad ones. They give finer control than rolling back the entire transaction.
	Savepoints are useful when:

