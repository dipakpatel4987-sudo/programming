Module 6) Python Fundamentals



Q1. 	Introduction to Python and its Features

->	Python is a general-purpose programming language known for readable, English-like code. Key features:
	• Simple and easy to learn: minimal syntax; no semicolons or braces.
	• High-level: you do not manage memory or hardware details.
	• Interpreted: code is executed line by line by the Python interpreter (it is first compiled to bytecode), so there is no separate 	compile step.
	• Dynamically typed: variable types are decided at run time (x = 5, then x = "hi").
	• Object-oriented and multi-paradigm: supports procedural, object-oriented, and functional styles.
	• Free and open source, with a large community.
	• Portable (cross-platform): runs on Windows, Linux, and macOS.
	• Extensive standard library ("batteries included") plus a huge third-party ecosystem (NumPy, pandas, Django, etc.).
	• Automatic memory management through garbage collection.


Q2. 	History and Evolution of Python

->	• Late 1989: Guido van Rossum begins Python at CWI in the Netherlands as a successor to the ABC language. The name comes from the 	comedy series Monty Python's Flying Circus.
	• 1991: first public release (version 0.9.0), already with classes, functions, exceptions, and core data types.
	• 1994: Python 1.0 adds functional tools (lambda, map, filter, reduce).
	• 2000: Python 2.0 adds list comprehensions and garbage collection.
	• 2001: the Python Software Foundation (PSF) is formed.
	• 2008: Python 3.0 is released. It cleaned up the language (print became a function, Unicode strings by default, integer division 	changes) and was not backward compatible.
	• 2020: Python 2 reaches end of life (January 1, 2020).
	• Since then: regular yearly releases of Python 3.x have added features such as f-strings, type hints, async/await, the walrus 	operator :=, and match statements. Python is now one 	of the most popular languages, driven by data science, AI, web 	development, and automation.


Q3. 	Advantages of Using Python over Other Programming Languages

->	1. Readability and shorter code: often 3 to 5 times shorter than equivalent Java or C++.
	2. Fast development: no compilation and dynamic typing allow quick prototyping.
	3. Huge library ecosystem: data science, machine learning, web, automation, scientific computing.
	4. Versatile: web, scripting, AI/ML, games, automation, IoT, and more.
	5. Cross-platform and open source.
	6. Large community and abundant learning resources.
	7. Easy integration with C/C++, Java, and other languages.
	8. Beginner friendly, widely used in education.
	Trade-off: Python is generally slower at raw execution than compiled languages such as C or C++, and uses more memory.


Q4. 	Installing Python and Setting Up the Development Environment

->	Install Python:
	1. Download the latest Python 3 installer from python.org.
	2. Run it and tick "Add Python to PATH" (Windows), then click Install Now.
	3. Verify in a terminal: python --version (or python3 --version on Linux/macOS).
	Linux often includes Python; otherwise use sudo apt install python3 python3-pip. On macOS, use the python.org installer or brew 	install python.
	Set up an environment (choose one):
	• Anaconda: download from anaconda.com and install. It bundles Python, conda, Jupyter Notebook, and data science libraries. Launch 	Anaconda Navigator or run jupyter notebook.
	• VS Code: install from code.visualstudio.com, add the Python extension by Microsoft, and select the interpreter with Ctrl+Shift+P 	→ "Python: Select Interpreter". Run a file with 	the Run button or python file.py.
	• PyCharm: install the free Community edition from jetbrains.com, create a new project (it can create a virtual environment 	automatically), then right-click a file and choose Run.
	Good practice: use a virtual environment per project: python -m venv env, then activate it. Install packages with pip install 	package_name.


Q5. 	Writing and Executing Your First Python Program

->	Create a file hello.py containing:
	print("Hello, World!")

	Run it:
	• Terminal: python hello.py
	• IDE: press Run (VS Code, PyCharm).
	• Interactive mode (REPL): type python, then enter print("Hello, World!") at the >>> prompt.
	• Jupyter: type the line in a cell and press Shift+Enter.
	The interpreter compiles the code to bytecode and executes it, printing Hello, World!. Python files use the .py extension.


Q6. 	Understanding Python's PEP 8 Guidelines

->	PEP 8 (Python Enhancement Proposal 8) is the official style guide for Python code, written by Guido van Rossum, Barry Warsaw, and Alyssa Coghlan. Its goal is consistent, 	readable code. Main rules:
	• Use 4 spaces per indentation level (never mix tabs and spaces).
	• Limit lines to 79 characters (72 for comments and docstrings).
	• Put two blank lines around top-level functions and classes, and one blank line between methods.
	• Put imports at the top, one per line, grouped as standard library, third-party, then local.
	• Put spaces around operators and after commas (x = a + b, f(a, b)), but not inside brackets or before a function call's parenthesis.
	• Follow the naming conventions in Q2.
	• Use docstrings for modules, functions, and classes.
	Tools such as flake8, pycodestyle, black, and pylint check or enforce PEP 8.


Q7. 	Indentation, Comments, and Naming Conventions in Python

->	Indentation: Python uses indentation (not braces) to define blocks. All statements in a block must be indented equally (4 spaces). Wrong indentation causes an Indentation 	Error.
	if x > 0:
    		print("Positive")     # inside the if block
	print("Done")             # outside the block

	Comments:
	• Single line: # This is a comment
	• Inline: x = 5  # two spaces before #
	• Docstrings (documentation for a function, class, or module) use triple quotes: """Return the sum of a and b."""
	Comments should explain why, not repeat what the code obviously does.
	
	Naming conventions:
	
	----------------------------------------------------------------------------------------
	Item			Style			Example
	----------------------------------------------------------------------------------------
	Variables, functions	snake_case		student_name, calculate_total()
	Classes			PascalCase (CapWords)	BankAccount
	Constants		UPPER_CASE		MAX_SIZE = 100
	Modules/packages	short lowercase		utils.py
	Private/internal	leading underscore	_helper

	Names must start with a letter or underscore, cannot be keywords (if, for, class), and are case-sensitive. Choose meaningful names 	(total_price, not tp).


Q8. 	Writing Readable and Maintainable Code

->	1. Follow PEP 8 consistently.
	2. Use meaningful names for variables, functions, and classes.
	3. Keep functions small and focused on one task (single responsibility).
	4. Avoid repeating code (DRY: Don't Repeat Yourself); use functions and loops.
	5. Write docstrings and useful comments.
	6. Avoid magic numbers; use named constants.
	7. Handle errors with try/except.
	8. Use type hints (def add(a: int, b: int) -> int:).
	9. Organize code into modules and keep related things together.
	10. Write tests and use version control (Git).
	11. Prefer clear code over clever one-liners ("Readability counts", from The Zen of Python, import this).

	
Q9. 	Understanding Data Types in Python

->	
	----------------------------------------------------------------------------------------------------------------------------------
	Type		Description						Mutable?			Example
	----------------------------------------------------------------------------------------------------------------------------------
	int		Whole numbers of unlimited size				No				x = 10
	float		Decimal numbers						No				y = 3.14
	str		Text (sequence of characters)				No				s = "Python"
	list		Ordered, changeable collection; allows duplicates	Yes				[1, 2, 3]
	tuple		Ordered, unchangeable collection			No				(1, 2, 3)
	dict		Key-value pairs; keys unique				Yes				{"name": "Asha", "age": 20}
	set		Unordered collection of unique items			Yes				{1, 2, 3}

	Other types: bool (True/False), complex (3+4j), NoneType (None), bytes, and frozenset.

	fruits = ["apple", "banana"]
	fruits.append("mango")            # lists can change
	point = (4, 5)                    # tuples cannot
	person = {"name": "Asha"}
	print(person["name"])             # Asha
	unique = {1, 2, 2, 3}             # {1, 2, 3}


Q10. 	Python Variables and Memory Allocation

->	A Python variable is a name (reference) that points to an object in memory; it is not a box holding a value. Assignment x = 10 	creates the object 10 (if needed) and binds the name 	x to it. No type declaration is needed (dynamic typing).
	• Everything is an object. id(x) shows the object's memory identity.
	• Multiple names can refer to one object: a = [1, 2]; b = a makes both names point to the same list, so a change through b is seen through a.
	• Mutable vs immutable: immutable objects (int, str, tuple) create a new object when changed; mutable objects (list, dict, set) change in place.
	• Memory management is automatic. Python uses a private heap, reference counting (an object is freed when no names refer to it), and a garbage collector that handles circular		references.
	• Small integers and some strings are cached/interned and reused.
	• is compares identity (same object); == compares values.

	x = 10
	print(id(x), type(x))   # memory identity and type
	x = "hello"   


Q11. 	Python Operators

->	
	---------------------------------------------------------------------------------------------------------------------------------
	Category			Operators			Example
	---------------------------------------------------------------------------------------------------------------------------------
	Arithmetic			+ - * / // % **			7 / 2 = 3.5, 7 // 2 = 3, 7 % 2 = 1, 2 ** 3 = 8
	Comparison			== != > < >= <=			5 > 3 → True
	Logical				and, or, not			(a > 0) and (b > 0)
	Bitwise				&, |, ^, ~, <<, >>		5 & 3 = 1, 5 | 3 = 7, 5 ^ 3 = 6, 5 << 1 = 10
	Assignment			= += -= *= /= //= %= **=	x += 2
	Membership			in, not in			3 in [1, 2, 3] → True
	Identity			is, is not			a is b


	/ always returns a float, // is floor division, and ** is exponentiation. and/or use short-circuit evaluation and return one of their operands. Comparison operators can be 	chained: 1 < x < 10.


Q12. What are conditional statements in Python (if, else, elif)?

->	Conditional statements run code only when a condition is true. Python treats 0, "", None, empty collections, and False as false; everything else is true. Blocks are defined by 	indentation after a colon.
	age = 20
	if age >= 18:
    		print("Adult")

	if age >= 18:
    		print("Adult")
	else:
    		print("Minor")

	marks = 72
	if marks >= 90:
    		print("A")
	elif marks >= 75:
    		print("B")
	elif marks >= 50:
    		print("C")
	else:
    		print("Fail")

	• if: runs a block if the condition is true.
	• else: runs when the if condition is false.
	• elif (else if): tests further conditions in order; the first true one runs.
	There is also a one-line conditional expression: status = "Adult" if age >= 18 else "Minor". Python has no switch statement before 3.10; newer versions provide match/case.
	Conditional statements are used to make decisions based on a condition.


Q13. 	 Explain nested if-else conditions.

->	A nested if is an if statement placed inside another if or else block. It checks a second condition only after the first one is satisfied. Indentation shows the nesting level.
	age = 25
	weight = 60

	if age >= 18:
    		if weight >= 50:
        		print("Eligible to donate blood")
    		else:
        		print("Underweight")
	else:
    		print("Too young")

	Nesting is useful for dependent conditions, but deep nesting hurts readability; combine conditions with and (if age >= 18 and weight >= 50:) or use elif where possible.


Q14. 	 Introduce the for and while loops in Python.

->	for loop: iterates over each item of a sequence or any iterable (list, tuple, string, dict, set, range()). Used when the number of iterations is known.
	for i in range(1, 6):        # 1 to 5
    		print(i)
	range(start, stop, step) generates numbers; stop is excluded.

	while loop: repeats as long as a condition is true. Used when the number of iterations is unknown.
	count = 1
	while count <= 5:
    		print(count)
    		count += 1               # update, otherwise infinite loop
	Both loops can have an optional else block, which runs when the loop ends normally (not through break).


Q15. 	How Loops Work in Python

->	• for: Python calls iter() on the iterable to get an iterator, then repeatedly calls next() and assigns each value to the loop 	variable until StopIteration is raised, which ends 	the loop.
	• while: the condition is evaluated before every iteration; if true the body runs and the condition is checked again; if false the loop ends. The body must change something that 	eventually makes the condition false.
	• Control inside loops: break exits the loop, continue skips to the next iteration, and pass does nothing.
	• Nested loops: a loop inside another; the inner loop completes fully for each outer iteration.
	• Useful helpers: enumerate() (index and value), zip() (parallel iteration), and reversed().

	for i in range(1, 6):
    		print("*" * i)   


Q16. 	Using Loops with Collections (Lists, Tuples, etc.)

->	fruits = ["apple", "banana", "mango"]
	for f in fruits:                       
    		print(f)

	for i, f in enumerate(fruits):         
    		print(i, f)

	for ch in "Python":                    
    		print(ch)

	for n in (1, 2, 3):                    
   		 print(n)

	person = {"name": "Asha", "age": 20}
	for key, value in person.items():      
    		print(key, value)

	for s in {1, 2, 3}:                    
    		print(s)

	squares = [x * x for x in range(5)]
    
	By default, looping over a dictionary gives its keys; use .values() or .items() for values or pairs. Avoid adding or removing items from a collection while looping over it.


Q17. 	Understanding How Generators Work in Python

->	A generator is a function that produces a sequence of values lazily, one at a time, using the yield keyword. Calling a generator 	function does not run it; it returns a 	generator object. Each next() call (or loop step) runs the function until the next 	yield, returns that value, and pauses, keeping its local state. When the function ends, 	Stop Iteration is raised.

	def even_numbers(n):
    		count = 0
    		num = 0
    		while count < n:
        		yield num
        		num += 2
        		count += 1

	for e in even_numbers(10):
    		print(e)                        # 0 2 4 ... 18

	gen = (x * x for x in range(5))     # generator expression

	Benefits: very memory efficient (values are not stored in a list), suitable for large or infinite sequences, and simple to write 	compared with writing an iterator class.


Q18. 	 What is the difference between yield and return?

->	
	--------------------------------------------------------------------------------------------------------------
	Feature				return						yield
	-----------------------------------------------------------------------------------------------------------------------------
	Effect				Ends the function and sends back a value	Pauses the function and sends back a value
	State				Local variables are lost			Local state is preserved for the next call
	Number of values		One result (could be a tuple or list)		Many values, one per resume
	Function type			Normal function					Generator function
	Returns				The value itself				A generator object
	Memory				Whole result built at once			Values created on demand

	def f():
    		return 1
    		return 2       # never reached

	def g():
    		yield 1
    		yield 2        


Q19. 	Understanding Iterators and Creating Custom Iterators

->	An iterable is an object you can loop over (list, tuple, string, dict). An iterator is an object that produces the next value on 	demand. It must implement two methods:
	• __iter__(): returns the iterator object itself.
	• __next__(): returns the next value, and raises StopIteration when finished.
	Built-in usage: it = iter([1, 2, 3]) then next(it) gives 1, 2, 3, then raises StopIteration.
	Custom iterator:

	class MyList:
    		def __init__(self, data):
        		self.data = data
        		self.index = 0

    		def __iter__(self):
        		return self

    		def __next__(self):
        		if self.index >= len(self.data):
            			raise StopIteration
        		value = self.data[self.index]
       		 	self.index += 1
        		return value

	for n in MyList([10, 20, 30]):
    		print(n)          # 10 20 30

	Every generator is an iterator, but writing a generator is usually simpler.


Q20. 	Defining and Calling Functions in Python

->	A function is a reusable block of code. Define it with def, followed by a name, parameters in parentheses, a colon, and an indented body. return sends a value back (without it, the 	function returns None). Call it by name with arguments.

	def add(a, b):
    		"""Return the sum of a and b."""
   		 return a + b

	result = add(3, 4)       # call
	print(result)            # 7

	Other forms: lambda (anonymous) functions such as square = lambda x: x * x; functions can return multiple values as a tuple (return a, b) and can call themselves (recursion). 	Functions are first-class objects: they can be assigned, passed as 	arguments, and returned.


Q21. 	Explain function arguments (positional, keyword, default).

->	
	def greet(name, msg="Hello"):
    		print(msg, name)

	greet("Asha")                   # positional; default msg used
	greet("Asha", "Hi")             # positional for both
	greet(msg="Welcome", name="Ravi")   # keyword arguments (any order)
	• Positional arguments: matched by position.
	• Keyword arguments: passed as name=value; order does not matter.
	• Default arguments: parameters with a preset value used when no argument is given. Defaults must come after non-default parameters. Avoid mutable defaults like [].
	• Variable-length: *args collects extra positional arguments into a tuple; **kwargs collects extra keyword arguments into a dictionary.
	def total(*args):
    		return sum(args)
	total(1, 2, 3)      # 6


Q22. 	Scope of Variables in Python

->	Scope is where a name can be accessed. Python follows the LEGB rule, searching in this order:
	1. Local: inside the current function.
	2. Enclosing: in outer (enclosing) functions.
	3. Global: at module level.
	4. Built-in: names like print and len.
	x = 10                 # global

	def show():
   		y = 5              # local
    		print(x, y)

	def change():
    		global x           # modify the global variable
    		x = 20
	A variable assigned inside a function is local unless declared with global (module-level) or nonlocal (enclosing function). Local variables exist only while the function runs. 	Reading a global inside a function works without a declaration, but assigning to 	it needs global.


Q23. 	Built-in Methods for Strings, Lists, etc.

->	String methods: upper(), lower(), title(), capitalize(), strip(), replace(a, b), split(sep), join(list), find(), count(), startswith(), endswith(), isdigit(), isalpha().
	List methods: append(x), insert(i, x), extend(list), remove(x), pop([i]), sort(), reverse(), index(x), count(x), copy(), clear().
	Dictionary methods: keys(), values(), items(), get(k, default), update(), pop(k), clear().
	Set methods: add(), remove(), discard(), union(), intersection(), difference().
	Tuple methods: count(), index().
	Built-in functions: len(), type(), sum(), min(), max(), sorted(), range(), input(), print(), abs(), round().

	"hello".upper()          # 'HELLO'
	nums = [3, 1, 2]
	nums.sort()              # [1, 2, 3]
	A method is a function that belongs to an object and is called with dot notation (obj.method()).


Q24.	 Explain the role of break, continue, and pass in Python loops.

->	break: exits the loop immediately. Execution continues after the loop (and the loop's else block is skipped).
	for f in ["apple", "banana", "mango"]:
    		if f == "banana":
        		break
    		print(f)             # prints: apple

	continue: skips the rest of the current iteration and goes to the next one.
	for f in ["apple", "banana", "mango"]:
    		if f == "banana":
        		continue
    		print(f)             # prints: apple, mango

	pass: does nothing; it is a placeholder where a statement is syntactically required but no action is wanted yet (empty loops, functions, classes, or conditions).
	for i in range(3):
    		pass                 # to be implemented later

	def todo():
    		pass

	The key difference: break ends the loop, continue skips one iteration, and pass has no effect on flow.


Q25.	Understanding How to Access and Manipulate Strings

->	A string is an immutable sequence of characters, written in single, double, or triple quotes ('a', "a", """multi-line"""). Characters are accessed by index (starting at 0; negative 	indexes count from the end).
	s = "Python"
	print(s[0])        # 'P'
	print(s[-1])       # 'n'
	print(len(s))      # 6
	for ch in s:       # iterate over characters
    		print(ch)
	# s[0] = 'J'       # ERROR: strings cannot be changed
	s = "J" + s[1:]   # create a new string instead: 'Jython'

	Because strings are immutable, every "modification" creates a new string. Other useful features: escape characters (\n, \t, \\), raw strings (r"C:\new"), and f-strings (f"Name: 	{name}").


Q26. 	What are the basic string operations (concatenation, repetition, string methods)?

->	a = "Hello"
	b = "World"
	print(a + " " + b)      # concatenation: Hello World
	print(a * 3)            # repetition: HelloHelloHello
	print("ell" in a)       # membership: True
	print(a == "Hello")     # comparison: True

	Common methods (each returns a new string):

	s = "  Hello Python  "
	s.upper()             # '  HELLO PYTHON  '
	s.lower()             # '  hello python  '
	s.strip()             # 'Hello Python'
	s.replace("Python", "World")
	s.split()             # ['Hello', 'Python']
	"-".join(["a", "b"])   # 'a-b'
	s.find("Py")          # index of first match, or -1
	s.count("l")          # number of occurrences
	"abc".startswith("a") # True

	Formatting: f"{name} is {age}", "{} is {}".format(name, age), or "%s"-style formatting.


Q27. 	String Slicing

->	Slicing extracts a part (substring) of a string using s[start:stop:step]. start is included, stop is excluded; omitted values default to the beginning, end, and step 1. Negative 	values count from the end.
	s = "Python"
	print(s[1:4])     # 'yth'  (index 1 to 3)
	print(s[:3])      # 'Pyt'  (up to the third character)
	print(s[2:])      # 'thon' (from index 2 onwards)
	print(s[-3:])     # 'hon'  (last three characters)
	print(s[::2])     # 'Pto'  (every second character)
	print(s[1::2])    # 'yhn'  (alternate from index 1)
	print(s[::-1])    # 'nohtyP' (reversed)
	Slicing never raises an index error for out-of-range values; it simply returns what is available.


Q28. 	How Functional Programming Works in Python

->	Functional programming is a style that builds programs by applying and combining functions, avoiding changing state and side effects. Python supports it alongside other paradigms 	through:
	• First-class functions: functions can be stored in variables, passed as arguments, and returned from other functions.
	• Higher-order functions: functions that take or return functions (map, filter, reduce, sorted(key=...)).
	• Lambda functions: small anonymous functions (lambda x: x * 2).
	• Comprehensions and generator expressions as concise alternatives.
	• Immutability (tuples, frozenset) and pure functions (same input always gives the same output, no side effects).
	• Tools in the functools and itertools modules.
	Benefits: code that is easier to test, reason about, and parallelize.


Q29. 	How are map(), reduce(), and filter() used for processing data?

->	map(function, iterable): applies a function to every item and returns an iterator of the results.
		nums = [1, 2, 3, 4, 5]
		squares = list(map(lambda x: x ** 2, nums))      # [1, 4, 9, 16, 25]

	filter(function, iterable): keeps only items for which the function returns true.
		odds = list(filter(lambda x: x % 2 != 0, nums))  # [1, 3, 5]
		evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]

	reduce(function, iterable): (from functools) repeatedly combines items into a single value.
		from functools import reduce
		product = reduce(lambda a, b: a * b, nums)       # 120
	--------------------------------------------------------------------------------------
	Function		Input → Output			Result size
	--------------------------------------------------------------------------------------
	map			Transforms each item		Same as input
	filter			Selects items by a condition	Same or smaller
	reduce			Combines all items		One value

	List comprehensions are often more readable: [x**2 for x in nums], [x for x in nums if x % 2 == 0].


Q30. 	Introduction to Closures and Decorators

->	Closure: an inner function that remembers variables from its enclosing function even after the outer function has finished. It is created when a nested function uses a variable 	from the outer scope and the outer function returns the inner one.
	def make_multiplier(n):
    		def multiply(x):
        		return x * n          # n is remembered
    		return multiply

	double = make_multiplier(2)
	print(double(5))              # 10

	Uses: data hiding without classes, function factories, callbacks, and the basis of decorators.
	Decorator: a function that takes another function, adds behavior to it, and returns the new function, without modifying the original code. It is applied with the @ syntax, which is 	shorthand for func = decorator(func).
	def log(func):
    		def wrapper(*args, **kwargs):
        		print("Calling", func.__name__)
        	result = func(*args, **kwargs)
        	print("Done")
        	return result
    	return wrapper

	@log
	def add(a, b):
    		return a + b

	print(add(2, 3))     # prints the log lines, then 5

	Uses: logging, timing, authentication checks, caching, and validation. Use functools.wraps(func) inside the decorator to preserve the original function's name and docstring. Python 	also has built-in decorators such as @staticmethod, @classmethod, and 	@property.
