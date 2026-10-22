Module 8) Advance Python Programming



Q1. 	Introduction to the `print()` Function in Python

->	print() is a built-in function that displays output on the screen (standard output). It converts values to text and writes them, followed by a newline by default.
	print("Hello, World!")
	print("Name:", "Asha", "Age:", 20)      # multiple values, separated by a space
	print("a", "b", "c", sep="-")           # a-b-c   (sep changes the separator)
	print("Hello", end=" ")                 # end changes the ending (default is "\n")
	print("World")                          # Hello World
	print("Line1\nLine2\tTabbed")           # escape characters
	Parameters: sep (separator between values), end (what is printed at the end), file (output destination, e.g., a file), and flush. Python 3 uses print() as a function; Python 2 used 	a statement.


Q2. 	How do you format output using f-strings and format()?

->	Formatting lets you insert variables into text and control how numbers appear.
	f-strings (Python 3.6+): prefix the string with f and put expressions in { }.
	name, age, price = "Asha", 20, 1234.5678
	print(f"My name is {name} and I am {age} years old.")
	print(f"Next year I will be {age + 1}")        # expressions allowed
	print(f"Price: {price:.2f}")                    # 2 decimals -> 1234.57
	print(f"{price:,.1f}")                          # thousands separator -> 1,234.6
	print(f"{name:>10}|{name:<10}|{name:^10}")     # right, left, center alignment
	print(f"{age:05d}")                             # zero-padded -> 00020
	str.format(): uses {} placeholders filled by the method's arguments.
	print("My name is {} and I am {} years old.".format(name, age))
	print("{1} is {0}".format(age, name))           # positional index
	print("{n} is {a}".format(n=name, a=age))       # named placeholders
	print("Price: {:.2f}".format(price))
	Old style %: print("Name: %s, Age: %d" % (name, age)). F-strings are the preferred modern method because they are shorter, more readable, and faster.


Q3. 	How do you use the input() function to read user input?

->	input(prompt) displays an optional prompt, waits for the user to type and press Enter, and returns what was typed always as a string (str).
	name = input("Enter your name: ")
	print("Hello,", name)

	x = input("Enter a number: ")
	print(type(x))        # <class 'str'>, even if the user typed 5
	print(x + x)          # '55' (string concatenation, not 10)
	Several values can be read from one line using split(): a, b = input("Enter two words: ").split(). Python 2's raw_input() is equivalent to Python 3's input().


Q4. 	Converting User Input into Different Data Types

->	 Because input() returns a string, wrap it in a type-conversion function: int(), float(), bool(), list(), and so on.
	age = int(input("Enter age: "))          # integer
	height = float(input("Enter height: "))  # decimal
	print(f"{age + 1} {height * 2}")

	nums = list(map(int, input("Enter numbers: ").split()))   # '1 2 3' -> [1, 2, 3]
	If the text cannot be converted (for example int("abc")), Python raises a ValueError, which should be handled with try/except:
	try:
    		n = int(input("Enter a number: "))
	except ValueError:
    		print("Invalid input")
	Note that int("3.5") fails; use int(float("3.5")) instead.
	Since `input()` returns a \*\*string\*\*, you need to convert it to other data types when required.


Q5. 	Opening Files in Different Modes

->	-------------------------------------------------------------------------------------------------------------
	Mode		Meaning			If the file does not exist		Existing content
	-------------------------------------------------------------------------------------------------------------
	'r'		Read (default)		Error (FileNotFoundError)		Kept; cannot write
	'w'		Write			Created					Erased (truncated)
	'a'		Append			Created					Kept; new data added at the end
	'r+'		Read and write		Error					Kept; writing starts at the beginning (overwrites)
	'w+'		Write and read		Created					Erased
	'a+'		Append and read		Created					Kept

	Add b for binary mode ('rb', 'wb'), used for images, audio, and other non-text files. Add t for text (the default). The mode 'x' creates a file and fails if it already exists.


Q6. 	How do you use the open() function to create and access files?

->	open(filename, mode) returns a file object (file handle) used for reading or writing. If mode is omitted it defaults to 'r'.
	f = open("data.txt", "w")     # creates data.txt (or erases it) for writing
	f.write("Hello, file!")
	f.close()

	f = open("data.txt", "r")     # opens for reading
	print(f.read())
	f.close()
	Useful arguments: encoding="utf-8" for text encoding and a full path such as open("C:/docs/data.txt"). Useful attributes: f.name, f.mode, f.closed. The recommended way is the with 	statement, which closes the file automatically (even if an error occurs):
	with open("data.txt", "w") as f:
    	f.write("Hello")
	# file is closed here


Q7. 	Why and how do you close files using close()?

->	file.close() ends the connection between the program and the file. It is important because it:
	1. Flushes buffered data so everything written is actually saved to disk.
	2. Frees system resources (the operating system limits how many files can be open).
	3. Releases the file so other programs can use it, and avoids data corruption.
	f = open("data.txt", "w")
	f.write("Saved")
	f.close()
	print(f.closed)      # True
	# f.write("x")       # ValueError: I/O operation on closed file
	If an error occurs before close() is reached, the file stays open; so use try/finally or, better, the with statement, which calls close() automatically.


Q8. 	Reading from a File

->	Suppose data.txt contains three lines: Apple, Banana, Mango.
	---------------------------------------------------------------------------------------------------
	Method			What it does						Returns
	---------------------------------------------------------------------------------------------------
	read()			Reads the entire file (or read(n) for n characters)	One string
	readline()		Reads one line at a time (including \n)			A string
	readlines()		Reads all lines						A list of strings

	with open("data.txt", "r") as f:
    		print(f.read())               # 'Apple\nBanana\nMango'

	with open("data.txt") as f:
    		print(f.readline())           # 'Apple\n'
    		print(f.readline())           # 'Banana\n'

	with open("data.txt") as f:
    		print(f.readlines())          # ['Apple\n', 'Banana\n', 'Mango']

	with open("data.txt") as f:
    		for line in f:                # memory-efficient: one line at a time
        		print(line.strip())

	The file cursor moves as data is read. f.tell() returns the current position and f.seek(n) moves it (f.seek(0) returns to the start). read() on a very large file loads it all into 	memory, so looping over the file is better.

	Python provides different methods to read data from a file.


Q9. 	Writing to a File

->	• write(string) writes one string and returns the number of characters written. It does not add a newline automatically.
	• writelines(list_of_strings) writes every string in a list or iterable. It does not add newlines either, so include \n yourself.
	with open("out.txt", "w") as f:
    	f.write("Hello\n")
    	f.write("Welcome to Python\n")

	lines = ["Apple\n", "Banana\n", "Mango\n"]
	with open("fruits.txt", "w") as f:
    		f.writelines(lines)

	with open("fruits.txt", "a") as f:      # append without erasing
    		f.write("Orange\n")
	Use mode 'w' to overwrite and 'a' to append. Only strings can be written; convert numbers first: f.write(str(25)). Data may stay in a buffer until the file is closed or flush() is 	called.


Q10. 	Introduction to Exceptions and Exception Handling

->	An exception is an error that occurs during program execution and, if not handled, stops the program (for example dividing by zero or opening a missing file). Exception handling 	lets the program respond to errors gracefully and continue.
	try:
    		a = int(input("Enter a: "))
    		b = int(input("Enter b: "))
    		result = a / b
	except ZeroDivisionError:
    		print("Cannot divide by zero")
	except ValueError:
    		print("Please enter valid numbers")
	else:
    		print("Result:", result)          # runs only if no exception occurred
	finally:
    		print("Done")                     # ALWAYS runs
	• try: the block of code that might raise an exception.
	• except: runs if a matching exception occurs.
	• else: runs if the try block succeeds.
	• finally: always runs, with or without an exception; used for cleanup such as closing files or connections.
	• raise: deliberately raises an exception (raise ValueError("Bad value")).
	Common built-in exceptions: ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, FileNotFoundError, NameError, ImportError.


Q11. 	Multiple Exceptions

->	Multiple exceptions: use several except blocks, or group them in a tuple. Python runs the first block that matches.
	try:
    		f = open("missing.txt")
    		x = 10 / 0
	except FileNotFoundError:
    		print("File not found")
	except (ZeroDivisionError, ValueError) as e:     # one block for several types
    		print("Math or value error:", e)
	except Exception as e:                           # catch-all (put last)
    		print("Unexpected error:", e)
	File handling with finally:
	f = None
	try:
    		f = open("data.txt")
    		print(f.read())
	except FileNotFoundError:
    		print("File not found")
	finally:
    		if f:
        		f.close()        # always closes the file

	Custom exceptions: create a class that inherits from Exception, then raise it.

	class AgeError(Exception):
    		def __init__(self, age, message="Age must be 18 or above"):
        		self.age = age
        		super().__init__(f"{message} (got {age})")

		def check_age(age):
    			if age < 18:
        			raise AgeError(age)
    				print("Valid age")

		try:
    			check_age(15)
		except AgeError as e:
    			print("Custom exception:", e)

	Custom exceptions make error messages meaningful for a specific application.

	

Q12. 	Custom Exceptions

->	• Class: a blueprint or template that defines the data and behavior of a type of object. Created with the class keyword.
	• Object (instance): a real entity created from a class, with its own data.
	• Attributes: variables that store data in a class or object. Instance attributes belong to each object (set in __init__); class attributes are shared by all objects.
	• Methods: functions defined inside a class that describe behavior. The first parameter is self, which refers to the current object.
	• Constructor: __init__() runs automatically when an object is created and initializes its attributes.

	class Student:
    		school = "ABC School"              # class attribute (shared)

    		def __init__(self, name, roll):    # constructor
        		self.name = name               # instance attributes
        		self.roll = roll

    		def display(self):                 # method
        		print(f"{self.name} ({self.roll}) - {Student.school}")

	s1 = Student("Asha", 101)              # object creation
	s2 = Student("Ravi", 102)
	print(s1.name)                         # access attribute: Asha
	s2.display()                           # call method
	s1.roll = 150                          # modify attribute
	OOP's main ideas are encapsulation, inheritance, polymorphism, and abstraction. Python marks "private" attributes by convention with a leading underscore (_x) or name-mangled 	double underscore (__x).


Q13. 	Understanding Classes, Objects, Attributes, and Methods in Python

->	------------------------------------------------------------------------------------------------------
	Feature				Local variable				Global variable
	-----------------------------------------------------------------------------------------------------
	Defined				Inside a function or method		Outside all functions and classes (module level)
	Accessible			Only within that function		Everywhere in the module
	Lifetime			While the function runs			Until the program ends
	Modify inside a function	Directly				Needs the global keyword

	count = 100                    # global variable

	class Demo:
    		def show(self):
        		x = 5                  # local variable (exists only in show)
        		print("Local:", x)
        		print("Global:", count)

    		def change(self):
        		global count           # needed to modify the global
        		count = 200

	d = Demo()
	d.show()
	d.change()
	print(count)                   # 200
	# print(x)                     # NameError: x is not defined outside the method
	If a local variable has the same name as a global one, the local one shadows it inside the function. Python looks up names in the order Local, Enclosing, Global, Built-in (LEGB). 	Instance variables (self.x) are different from local variables: they live as long as the object does.


Q14. 	Difference Between Local and Global Variables

->	-----------------------------------------------------------------------------------------------------------------
	Feature					Local variable				Global variable
	-----------------------------------------------------------------------------------------------------------------
	Defined					Inside a function or method		Outside all functions and classes (module level)
	Accessible				Only within that function		Everywhere in the module
	Lifetime				While the function runs			Until the program ends
	Modify inside a function		Directly				Needs the global keyword

	count = 100                    # global variable

	class Demo:
    		def show(self):
        		x = 5                  # local variable (exists only in show)
        		print("Local:", x)
        		print("Global:", count)

    		def change(self):
        		global count           # needed to modify the global
        		count = 200

	d = Demo()
	d.show()
	d.change()
	print(count)                   # 200
	# print(x)                     # NameError: x is not defined outside the method
	If a local variable has the same name as a global one, the local one shadows it inside the function. Python looks up names in the order Local, Enclosing, Global, Built-in (LEGB). 	Instance variables (self.x) are different from local variables: they live as long as the object does.


Q15. 	Types of Inheritance in Python

->	Inheritance lets a child (derived) class acquire the attributes and methods of a parent (base) class, promoting code reuse. Syntax: class Child(Parent):.
	1. Single: one child, one parent.
	class Animal:
    		def eat(self): print("Eating")
	class Dog(Animal):
    		def bark(self): print("Barking")

	2. Multilevel: a chain of inheritance (grandparent → parent → child).
	class A:
    		def a(self): print("A")
	class B(A):
    		def b(self): print("B")
	class C(B):
    		def c(self): print("C")      # C can use a(), b(), c()

	3. Multiple: one child with more than one parent.
	class Father:
    		def skills(self): print("Gardening")
	class Mother:
    		def hobby(self): print("Cooking")
	class Child(Father, Mother):
    	pass

	4. Hierarchical: several children inherit from one parent.
	class Vehicle:
    		def start(self): print("Start")
	class Car(Vehicle): pass
	class Bike(Vehicle): pass

	5. Hybrid: a combination of two or more of the above (for example multilevel plus multiple).
	class A: pass
	class B(A): pass
	class C(A): pass
	class D(B, C): pass              # diamond shape: hierarchical + multiple
	In multiple and hybrid inheritance, Python decides which parent's method to use with the Method Resolution Order (MRO), which can be viewed with D.__mro__ or D.mro().


Q16. 	Using the 'super()' Function

->	super() returns a proxy to the parent class, so a child class can call the parent's methods or constructor without naming the parent explicitly. It is most often used to run the 	parent's __init__() and in method overriding to extend (not replace) parent behavior.
	class Person:
    		def __init__(self, name, age):
        		self.name = name
        		self.age = age
    		def show(self):
        		print(f"{self.name}, {self.age}")

	class Student(Person):
    		def __init__(self, name, age, roll):
        		super().__init__(name, age)      # call the parent constructor
        		self.roll = roll
    		def show(self):
        		super().show()                   # reuse the parent method
        		print("Roll:", self.roll)

	Student("Asha", 20, 101).show()

	Benefits: avoids repeating code, makes the class easier to maintain if the parent changes, and works correctly with multiple inheritance by following the MRO. If a child defines 	__init__ and does not call super().__init__(), the parent's initialization is skipped.


Q17. 	Method Overloading in Python

->	Method overloading means defining several methods with the same name but different parameters (number or type), with the right one chosen at call time. This is compile-time 	polymorphism in languages like Java and C++.
	Python does not support true method overloading. If you define two methods with the same name, the last definition replaces the earlier one:
	class Demo:
    		def add(self, a, b):
        		return a + b
    		def add(self, a, b, c):      # replaces the first add()
        		return a + b + c

	d = Demo()
	# d.add(1, 2)    # TypeError: missing argument 'c'
	Overloading behavior is achieved with these techniques:
	class Calculator:
    	# 1. Default arguments
    		def add(self, a, b, c=0):
        		return a + b + c

   	 # 2. Variable-length arguments
    		def total(self, *args):
        		return sum(args)

    	# 3. Type checks inside one method
    		def show(self, x):
        		if isinstance(x, int):
            			print("Integer:", x)
        		elif isinstance(x, str):
            			print("String:", x)

	c = Calculator()
	print(c.add(1, 2))          # 3
	print(c.add(1, 2, 3))       # 6
	print(c.total(1, 2, 3, 4))  # 10
	The @singledispatch and @singledispatchmethod decorators from functools provide overloading by argument type, and operators can be overloaded with special methods such as __add__.
	\*\*Method overloading\*\* means defining multiple methods with the \*\*same name\*\* but different parameters. Python does \*\*not support true method overloading\*\*. It is 	usually achieved using \*\*default arguments\*\* or `\*args`.



Q18.	Method Overriding in Python

->	Method overriding means a child class redefines a method that already exists in its parent class, with the same name and parameters, to provide its own behavior. It is run-time 	polymorphism: the method that runs depends on the object's actual class. Python fully supports it.
	class Animal:
    		def sound(self):
        		print("Some sound")

	class Dog(Animal):
    		def sound(self):                 # overrides Animal.sound
        		print("Bark")

	class Cat(Animal):
    		def sound(self):
        		print("Meow")

	for a in [Animal(), Dog(), Cat()]:
    	a.sound()                        # Some sound, Bark, Meow

	The parent's version can still be called with super().sound().
	----------------------------------------------------------------------------------------------------------
	Feature				Overloading				Overriding
	----------------------------------------------------------------------------------------------------------
	Where				Within one class			Between parent and child classes
	Signature			Same name, different parameters		Same name, same parameters
	Inheritance needed		No					Yes
	Python support			Not directly (use defaults, *args)	Fully supported
	Polymorphism type		Compile time				Run time


Q19. 	Introduction to SQLite3 and PyMySQL

->	A database connector (driver) is a library that lets a Python program talk to a database server.
	SQLite3:
	• A built-in Python module (import sqlite3); nothing to install.
	• Uses a serverless, lightweight database stored in a single file (or in memory with ":memory:").
	• Ideal for learning, small apps, mobile apps, and prototypes.
	• Standard SQL with limited data types.

	PyMySQL:
	• A third-party pure-Python library for MySQL/MariaDB, installed with pip install pymysql.
	• Connects to a MySQL server over a network using host, user, password, and database name.
	• Suitable for larger, multi-user applications.
	-----------------------------------------------------------------------------------------------------------------------------------------------
	Feature				SQLite3					PyMySQL
	-----------------------------------------------------------------------------------------------------------------------------------------------
	Installation			Built in				pip install pymysql
	Architecture			Serverless, file based			Client-server (MySQL needed)
	Users				Single or few				Many concurrent users
	Connect				sqlite3.connect("file.db")		pymysql.connect(host=..., user=..., password=..., database=...)

	Both follow Python's DB-API standard, so the code looks very similar: connect, create a cursor, execute SQL, commit, and close.


Q20. 	Creating and Executing SQL Queries from Python

->	The general steps are: (1) import the module, (2) connect to the database, (3) create a cursor, (4) execute SQL, (5) commit changes (for INSERT/UPDATE/DELETE), (6) fetch results 	(for SELECT), and (7) close the connection.
	SQLite3 example:

	import sqlite3

	conn = sqlite3.connect("school.db")        # creates the file if absent
	cur = conn.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS students (
                  	id INTEGER PRIMARY KEY,
                  	name TEXT NOT NULL,
                  	age INTEGER)""")

	cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Asha", 20))
	cur.executemany("INSERT INTO students (name, age) VALUES (?, ?)",
                	[("Ravi", 21), ("Meena", 19)])
	conn.commit()                              # save changes

	cur.execute("SELECT * FROM students")
	for row in cur.fetchall():                 # fetchone(), fetchmany(n), fetchall()
    	print(row)

	conn.close()

	PyMySQL example:

		import pymysql

		conn = pymysql.connect(host="localhost", user="root",
                       		password="pass", database="school_db")
		cur = conn.cursor()
		cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Asha", 20))
		conn.commit()
		cur.execute("SELECT * FROM students")
		print(cur.fetchall())
		conn.close()
		Key points: use parameterized queries (? in SQLite, %s in PyMySQL) instead of building SQL with string formatting, which prevents SQL injection; call commit() after changes 		or rollback() on error; and close the connection (or use with / try/finally). SQLite3 can also run conn.execute(...) directly as a shortcut.

Q21. 	How are re.search() and re.match() used for pattern matching in Python's re module?

->	The re module provides regular expressions: patterns that describe text to find. Both functions take a pattern and a string and return a match object if found, or None if not.

	import re

	text = "Python is fun and Python is powerful"

	m = re.search(r"fun", text)           # finds the first match anywhere
	if m:
    		print("Found:", m.group())        # fun
    		print("Position:", m.start(), m.end())   # 10 13

	m2 = re.match(r"Python", text)        # must match at the start
	print(m2.group() if m2 else "No match")      # Python

	Match object methods: group() (matched text), start(), end(), span(). Common pattern symbols:
	--------------------------------------------------------------------------
	Symbol					Meaning
	--------------------------------------------------------------------------
	.					Any character except newline
	^ / $					Start / end of string
	\d, \w, \s				Digit, word character, whitespace
	*, +, ?					0 or more, 1 or more, 0 or 1
	[abc]					One of a, b, or c
	{n}					Exactly n repetitions

	Related functions: re.findall() (all matches as a list), re.finditer(), re.sub() (replace), re.split(), and re.compile() (precompile a pattern). Use raw strings (r"...") for 	patterns.


Q22. 	What is the difference between search and match?

->	---------------------------------------------------------------------------------------------------------------------------------
	Feature			re.match()					re.search()
	---------------------------------------------------------------------------------------------------------------------------------
	Where it looks		Only at the beginning of the string		Anywhere in the string
	Returns			Match object if the start matches, else None	Match object for the first occurrence, else None
	Typical use		Validate that a string starts with a pattern	Find a pattern inside text

	import re
	s = "I love Python"

	print(re.match(r"Python", s))       # None  (string does not START with Python)
	print(re.search(r"Python", s))      # <re.Match object; span=(7, 13), match='Python'>

	print(re.match(r"I love", s))       # matches, because it is at the start
	Both stop at the first match; to find all occurrences use re.findall(). To require the entire string to match, use re.fullmatch(). Always test the result for None before 	calling .group(), otherwise an AttributeError occurs.
