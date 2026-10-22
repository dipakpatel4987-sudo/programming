Module 7) Python – Collections, functions and Modules



Q1. 	Understanding How to Create and Access Elements in a List

->	A list is an ordered, mutable (changeable) collection of items written in square brackets, separated by commas. It can hold items 	of different data types and allows 	duplicates.

	nums = [10, 20, 30]
	mixed = [1, "hello", 3.14, True, [5, 6]]   # multiple data types, even a nested list
	empty = []
	from_range = list(range(5))               # [0, 1, 2, 3, 4]

	print(mixed[1])        # 'hello'
	print(len(mixed))      # 5  (length using len())
	Elements are accessed by their index inside square brackets: list_name[index]. Using an index that does not exist raises an 	IndexError. Nested elements are reached with 	repeated indexes (mixed[4][0] gives 5).

Q2. 	Indexing in Lists (Positive and Negative Indexing)

->	Every element has a position called an index.
	• Positive indexing starts at 0 for the first element and increases to the right.
	• Negative indexing starts at -1 for the last element and decreases to the left.

	fruits = ["apple", "banana", "mango", "orange"]
	#   index:   0        1         2        3
	#   negative: -4      -3        -2       -1

	print(fruits[0])     # apple
	print(fruits[2])     # mango
	print(fruits[-1])    # orange (last)
	print(fruits[-3])    # banana
	Because lists are mutable, an element can be changed through its index: fruits[1] = "grape". Negative indexing is convenient for 	reaching the end of a list without knowing 	its length.


Q3. 	Slicing a List: Accessing a Range of Elements

->	Slicing extracts a portion of a list using list[start:stop:step]. start is included, stop is excluded, and step is the gap between elements. Omitted values default to the 	beginning, the end, and 1. A slice always returns a new list.
	n = [10, 20, 30, 40, 50, 60]
	print(n[1:4])      # [20, 30, 40]
	print(n[:3])       # [10, 20, 30]
	print(n[3:])       # [40, 50, 60]
	print(n[-3:])      # [40, 50, 60]
	print(n[::2])      # [10, 30, 50]   (every second element)
	print(n[::-1])     # [60, 50, 40, 30, 20, 10]  (reversed)
	print(n[:])        # full copy
	Out-of-range slice values do not raise errors; Python returns whatever is available.


Q4. 	Common List Operations

->	a = [1, 2, 3]
	b = [4, 5]

	print(a + b)         # concatenation: [1, 2, 3, 4, 5]
	print(a * 2)         # repetition:    [1, 2, 3, 1, 2, 3]
	print(2 in a)        # membership:    True
	print(7 not in a)    # True
	• Concatenation (+) joins two lists into a new list.
	• Repetition (*) repeats a list a given number of times.
	• Membership (in, not in) checks whether a value exists in the list and returns True or False.
	Other common operations: len(a), min(a), max(a), sum(a), comparison (==), and del a[0].


Q5. 	Understanding List Methods

->	----------------------------------------------------------------------------------------------------------------------
	Method				Purpose								Example
	----------------------------------------------------------------------------------------------------------------------
	append(x)		Adds x at the end							a.append(4)
	insert(i, x)		Adds x at index i							a.insert(1, 99)
	extend(iterable)	Adds all items of another iterable					a.extend([7, 8])
	remove(x)		Removes the first occurrence of the value x (error if absent)		a.remove(99)
	pop([i])		Removes and returns the item at index i (default: last)			a.pop(), a.pop(0)
	clear()			Removes all items							a.clear()
	index(x)		Returns the index of the first x					a.index(3)
	count(x)		Counts occurrences of x							a.count(2)


	a = [1, 2, 3]
	a.append(4)        # [1, 2, 3, 4]
	a.insert(1, 99)    # [1, 99, 2, 3, 4]
	a.remove(99)       # [1, 2, 3, 4]
	last = a.pop()     # last = 4, a = [1, 2, 3]
	first = a.pop(0)   # first = 1, a = [2, 3]
	These methods change the list in place and mostly return None. remove() works by value and pop() works by index.


Q6. 	Iterating Over a List Using Loops

->	fruits = ["apple", "banana", "mango"]

	for f in fruits:                      # by item
    		print(f)

	for i in range(len(fruits)):          # by index
    		print(i, fruits[i])

	for i, f in enumerate(fruits):        # index and item together
    		print(i, f)

	i = 0
	while i < len(fruits):                # with a while loop
    		print(fruits[i])
    	i += 1

	A loop is also used to build a list:

	numbers = []
	for i in range(1, 6):
    		numbers.append(i)       # [1, 2, 3, 4, 5]
	A list comprehension does this concisely: [i for i in range(1, 6)]. Avoid adding or removing items from a list while looping over it.


Q7. 	Sorting and Reversing a List

->	-------------------------------------------------------------------------------------------------------------
	Feature				list.sort()		sorted(list)			list.reverse()
	-------------------------------------------------------------------------------------------------------------
	Type				Method			Built-in function		Method
	Changes original?		Yes, in place		No, returns a new list		Yes, in place
	Returns				None			New sorted list			None
	Works on			Lists only		Any iterable			Lists only

	n = [5, 2, 9, 1]

	s = sorted(n)                # s = [1, 2, 5, 9]; n unchanged
	n.sort()                     # n = [1, 2, 5, 9]
	n.sort(reverse=True)         # n = [9, 5, 2, 1]  (descending)
	n.reverse()                  # n = [1, 2, 5, 9]  (order flipped)

	words = ["banana", "kiwi", "apple"]
	words.sort(key=len)          # sort by length: ['kiwi', 'apple', 'banana']
	reverse() simply flips the current order; it does not sort. All items must be comparable (a list mixing numbers and strings cannot be sorted).


Q8. 	Basic List Manipulations

->	a = [10, 20, 30, 40]

	# Addition
	a.append(50)             # [10, 20, 30, 40, 50]
	a.insert(0, 5)           # [5, 10, 20, 30, 40, 50]
	a.extend([60, 70])       # adds several items

	# Updating (lists are mutable)
	a[1] = 15                # change one item
	a[2:4] = [25, 35]        # replace a slice

	# Deletion
	a.remove(60)             # by value
	del a[0]                 # by index
	x = a.pop()              # remove and return the last item
	del a[1:3]               # delete a slice

	# Slicing
	print(a[1:3])            # new list with a part of a
	Copying: b = a makes both names point to the same list; use b = a.copy() or b = a[:] for an independent copy.


Q9. 	Introduction to Tuples and Immutability

->	A tuple is an ordered collection of items written in round brackets ( ). Like a list it can hold mixed data types and duplicates, but it is immutable: once created, its elements 	cannot be changed, added, or removed.
	t = (1, "a", 2.5)
	# t[0] = 5          # TypeError: tuple does not support item assignment
	Why use tuples? They are faster and use less memory than lists, protect data from accidental changes, and can be used as dictionary keys (lists cannot). They suit fixed data such 	as coordinates, dates, or RGB colors. Note that a tuple holding a mutable object (like a list) can still have that inner object modified.

	-----------------------------------------------------------------------
	Feature			List			Tuple
	-----------------------------------------------------------------------
	Syntax			[1, 2]			(1, 2)
	Mutable			Yes			No
	Speed			Slower			Faster
	Methods			Many			Only count() and index()


Q10. 	Creating and Accessing Elements in a Tuple

->	t1 = (10, 20, 30)
	t2 = 10, 20, 30            # brackets are optional (packing)
	t3 = (5,)                  # single-element tuple needs a trailing comma
	t4 = ()                    # empty tuple
	t5 = tuple([1, 2, 3])      # convert a list to a tuple

	print(t1[0])               # 10 (first element)
	print(t1[-1])              # 30 (last element)

	a, b, c = t1               # unpacking: a=10, b=20, c=30
	(5) is just the integer 5; (5,) is a tuple. Tuples have the methods count(x) and index(x), and can be looped over like lists.


Q11. 	Basic Operations with Tuples

->	a = (1, 2)
	b = (3, 4)

	print(a + b)         # concatenation: (1, 2, 3, 4)
	print(a * 3)         # repetition:    (1, 2, 1, 2, 1, 2)
	print(2 in a)        # membership:    True
	print(len(a + b))    # 4
	These operations create new tuples; the originals are unchanged. To "modify" a tuple, convert it to a list, change it, and convert it back: t = tuple(list(t) + [5]).


Q12. 	Accessing Tuple Elements Using Positive and Negative Indexing

->	Tuples use the same indexing as lists. Positive indexes begin at 0 from the left; negative indexes begin at -1 from the right.
	t = ("a", "b", "c", "d", "e")
	#  index:   0    1    2    3    4
	#  negative: -5   -4   -3   -2   -1

	print(t[0])      # 'a'
	print(t[3])      # 'd'
	print(t[-1])     # 'e'
	print(t[-2])     # 'd'
	An out-of-range index raises IndexError. Because tuples are immutable, you can read items this way but not assign to them.


Q13. 	Slicing a Tuple to Access Ranges of Elements

->	Slicing uses tuple[start:stop:step] (stop excluded) and returns a new tuple.
	t = (10, 20, 30, 40, 50, 60, 70)
	print(t[1:5])      # (20, 30, 40, 50)
	print(t[:3])       # (10, 20, 30)
	print(t[4:])       # (50, 60, 70)
	print(t[1:6:2])    # (20, 40, 60)  alternate values between index 1 and 5
	print(t[-3:])      # (50, 60, 70)
	print(t[::-1])     # (70, 60, 50, 40, 30, 20, 10)
	The rules are identical to list and string slicing.


Q14. 	Introduction to Dictionaries: Key-Value Pairs

->	A dictionary (dict) stores data as key-value pairs inside curly braces: {key: value}. Keys are used to look up values quickly.
	student = {"name": "Asha", "age": 20, "city": "Surat"}
	Properties:
	• Keys must be unique and immutable (strings, numbers, tuples). Duplicate keys overwrite earlier values.
	• Values can be of any type and may repeat.
	• Dictionaries are mutable.
	• They keep insertion order (Python 3.7 and later).
	• Lookup by key is very fast (hash table).
	Create with {}, dict(), or dict(name="Asha", age=20).


Q15. 	Accessing, Adding, Updating, and Deleting Dictionary Elements

->	d = {"name": "Asha", "age": 20}

	# Access
	print(d["name"])              # 'Asha' (KeyError if missing)
	print(d.get("city"))          # None (no error)
	print(d.get("city", "N/A"))   # 'N/A' (default value)

	# Add
	d["city"] = "Surat"

	# Update
	d["age"] = 21
	d.update({"age": 22, "class": "BCA"})

	# Delete
	del d["city"]                 # remove a key
	d.pop("class")                # remove and return its value
	d.popitem()                   # remove the last inserted pair
	d.clear()                     # remove everything

	print("name" in d)            # check key existence
	Assigning to a new key adds it; assigning to an existing key updates it.


Q16. 	What are dictionary methods like keys(), values(), and items()?

->	d = {"name": "Asha", "age": 20, "city": "Surat"}

	print(d.keys())      # dict_keys(['name', 'age', 'city'])
	print(d.values())    # dict_values(['Asha', 20, 'Surat'])
	print(d.items())     # dict_items([('name', 'Asha'), ('age', 20), ('city', 'Surat')])
	• keys() returns a view of all keys.
	• values() returns a view of all values.
	• items() returns a view of (key, value) tuples, handy for looping.
	These views update automatically if the dictionary changes. Convert them with list(d.keys()). Other methods: get(), update(), pop(), popitem(), setdefault(), copy(), clear().


Q17. 	Iterating Over a Dictionary Using Loops

->	d = {"a": 1, "b": 2, "c": 3}

	for k in d:                      # keys (default)
    		print(k)

	for k in d.keys():               # keys (explicit)
    		print(k)

	for v in d.values():             # values
    		print(v)

	for k, v in d.items():           # key and value together
    		print(k, v)
	A dictionary comprehension builds one in a single line: squares = {x: x**2 for x in range(1, 4)} gives {1: 1, 2: 4, 3: 9}. Do not add or delete keys while iterating over the same 	dictionary.

	A dictionary can be iterated using a \*\*`for` loop\*\*.



Q18. 	Merging Two Lists into a Dictionary

->	One list supplies the keys and the other the values.
	keys = ["name", "age", "city"]
	values = ["Asha", 20, "Surat"]

	# Using a loop
	result = {}
	for i in range(len(keys)):
    		result[keys[i]] = values[i]

	# Using zip()
	result = dict(zip(keys, values))

	# Using a dictionary comprehension
	result = {k: v for k, v in zip(keys, values)}

	print(result)    # {'name': 'Asha', 'age': 20, 'city': 'Surat'}
	zip() pairs items from both lists by position and stops at the shorter list.


Q19. 	Counting Occurrences of Characters in a String Using Dictionaries

->	The character is the key and its count is the value.
	text = "hello world"
	count = {}

	for ch in text:
    		if ch in count:
        		count[ch] += 1
    		else:
        		count[ch] = 1

	print(count)
	# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

	# Shorter versions
	count = {}
	for ch in text:
    		count[ch] = count.get(ch, 0) + 1

	from collections import Counter
	count = Counter(text)
	The get(ch, 0) + 1 pattern avoids KeyError by using 0 for characters not yet seen.
	A dictionary can be used to count how many times each character appears in a string.


Q20. 	Defining Functions in Python

->	A function is a named, reusable block of code. It is defined with def, a name, parentheses with optional parameters, a colon, and an indented body. It runs only when called, and 	return sends a result back (otherwise it returns None).
	def greet(name):
    		"""Print a greeting."""
    		print("Hello,", name)

	greet("Asha")           # call -> Hello, Asha
	Benefits: reusability, modularity, easier testing, and shorter programs. Parameters are the names in the definition; arguments are the values passed in the call. Arguments can be 	positional, keyword (greet(name="Asha")), or default (def greet(name="Guest")), and *args / **kwargs accept a variable number of arguments.


Q21. 	Different Types of Functions

->	 1. No parameters, no return value
	def hello():
    		print("Hello")

	# 2. With parameters, no return value
	def add_print(a, b):
   		 print(a + b)

	# 3. No parameters, with return value
	def get_pi():
    		return 3.14

	# 4. With parameters and return value
	def add(a, b):
   		 return a + b

	hello()
	add_print(2, 3)       # prints 5
	x = get_pi()
	y = add(2, 3)         # y = 5
	-----------------------------------------------------------------------------
	Type			Takes input?			Gives back a value?
	-----------------------------------------------------------------------------
	No params, no return	No					No
	Params, no return	Yes					No
	No params, return	No					Yes
	Params and return	Yes					Yes

	In addition there are built-in functions (len, print), user-defined functions, recursive functions (a function calling itself), and lambda functions. A function can return several 	values at once as a tuple: return a, b.



Q22. 	Anonymous Functions (Lambda Functions)

->	A lambda function is a small, nameless function written in one line with the syntax lambda arguments: expression. It can take any number of arguments but holds only a single 	expression, whose value is returned automatically.
	square = lambda x: x * x
	print(square(5))                 # 25

	add = lambda a, b: a + b
	print(add(3, 4))                 # 7

	bigger = lambda a, b: a if a > b else b   # with a conditional expression
	Lambdas are most useful when passed to other functions:
	nums = [1, 2, 3, 4]
	print(list(map(lambda x: x * 2, nums)))         # [2, 4, 6, 8]
	print(list(filter(lambda x: x % 2 == 0, nums))) # [2, 4]
	words = ["kiwi", "apple", "fig"]
	words.sort(key=lambda w: len(w))                # sort by length
	Use def for anything longer or more complex than one expression.


Q22. 	Introduction to Python Modules and Importing Modules

->	A module is a Python file (.py) containing functions, classes, and variables that can be reused in other programs. Modules organize code, avoid repetition, and allow sharing. A 	collection of modules in a folder (with __init__.py) is a package.
	Ways to import:
	import math                      # import the whole module
	print(math.sqrt(16))

	import math as m                 # with an alias
	print(m.pi)

	from math import sqrt, pi        # import specific names
	print(sqrt(25))

	from math import *               # import everything (not recommended)
	Python searches for modules in the current directory, then the standard library and installed packages. Use dir(module) to list a module's contents and help(module) for 	documentation. Third-party packages are installed with pip install package_name.


Q23. 	What are the standard library modules math and random?

->	The standard library is the set of modules that ship with Python.
	math module:
	----------------------------------------------------------------------------------------------
	Function			Purpose				Example
	---------------------------------------------------------------------------------------------
	sqrt(x)				Square root			math.sqrt(16) = 4.0
	ceil(x)				Round up			math.ceil(4.2) = 5
	floor(x)			Round down			math.floor(4.8) = 4
	pow(x, y)			Power				math.pow(2, 3) = 8.0
	factorial(n)			Factorial			math.factorial(5) = 120
	fabs(x)				Absolute value (float)		math.fabs(-3) = 3.0
	sin, cos, tan, log, log10	Trigonometry and logarithms	math.log10(100) = 2.0
	pi, e				Constants			math.pi = 3.14159...

	random module:
	import random

	print(random.random())              # float between 0.0 and 1.0
	print(random.randint(1, 100))       # integer from 1 to 100 (both included)
	print(random.randrange(0, 10, 2))   # random even number from 0 to 8
	print(random.choice(["a", "b", "c"])) # random item from a sequence
	items = [1, 2, 3, 4]
	random.shuffle(items)               # shuffle a list in place
	print(random.sample(items, 2))      # 2 unique random items
	random.seed(42)                     # make results repeatable
	Other useful modules: datetime, os, sys, json, statistics, and collections.


Q24. 	Creating Custom Modules

->	Any Python file is a module. To create one, write functions in a file and import it by its file name (without .py).
	Step 1: create mymath.py:
	# mymath.py
	PI = 3.14159

	def add(a, b):
    		return a + b

	def area_circle(r):
    		return PI * r * r

	Step 2: in another file in the same folder, import and use it:
	import mymath
	print(mymath.add(2, 3))            # 5
	print(mymath.area_circle(2))       # 12.56636

	from mymath import add
	print(add(10, 20))                 # 30
	Tips: keep the module in the same directory or in a folder on sys.path; use clear, lowercase file names that do not clash with built-in modules (do not name a file math.py). The if 	__name__ == "__main__": block lets a file run its own test code only when executed directly and not when imported.
	You can create your own module by saving Python code in a `.py` file.

