1. 	What are the key differences between Procedural Programming and Object Oriented Programming (OOP)?

->	POP organizes a program as a sequence of procedures (functions) that operate on shared data. OOP organizes a program around 	
	objects that bundle data and the functions that act on it.
	--------------------------------------------------------------------------------------------------------------------------
	Feature			Procedural (POP)				Object-Oriented (OOP)
	--------------------------------------------------------------------------------------------------------------------------
	Basic unit		Function					Object (instance of a class)
	Approach		Top-down					Bottom-up
	Data and functions	Separate; data is often global			Combined inside classes
	Data security		Little; global data is open to all functions	High; data hiding via access specifiers
	Code reuse		Through functions				Through inheritance and composition
	Extensibility		Hard to extend as programs grow			Easy to extend with new classes
	Polymorphism		Not supported					Supported (overloading, overriding)
	Real-world modelling	Weak						Strong
	Examples		C, Pascal, FORTRAN				C++, Java, Python, C#




Q2.	List and explain the main advantages of OOP over POP.

->	1. Data hiding and security: private members can be reached only through public functions, so data cannot be changed accidentally.
	2. Reusability: inheritance lets new classes reuse and extend existing, tested code.
	3. Modularity: each class is a self-contained unit, so large programs are split into manageable parts.
	4. Easier maintenance: a change inside one class rarely affects the rest of the program.
	5. Real-world modelling: entities such as Student or Bank Account map directly to classes.
	6. Polymorphism: one interface can have many implementations, which makes code flexible.
	7. Scalability: OOP systems grow more easily than large procedural ones.
	8. Easier teamwork and debugging: classes can be developed and tested independently.


Q3.	Explain the steps involved in setting up a C++ development environment.

->	You need a compiler (turns source into an executable) and an editor or IDE.
	1. Install a compiler (g++/GCC):
    		◦ Windows: install MSYS2 (or MinGW-w64), run pacman -S mingw-w64-ucrt-x86_64-gcc, and add its bin folder to the PATH.
    		◦ Linux: sudo apt install build-essential.
    		◦ macOS: xcode-select --install (provides Clang as g++).
	2. Verify: open a terminal and run g++ --version.
	3. Install an IDE or editor: options are Visual Studio Code (add the Microsoft C/C++ extension), Code::Blocks (download the 	version bundled with MinGW), Dev-C++, or Visual Studio (Windows, bundles the MSVC compiler).
	4. Configure the IDE: point it to the compiler path if it is not detected automatically, and set the C++ standard (e.g., -std=c++	17).
	5. Write the first program: create hello.cpp.
	#include <iostream>
	using namespace std;

	int main() {
    		cout << "Hello, World!" << endl;
   		return 0;
	}
	6. Compile and run: g++ hello.cpp -o hello then ./hello (Windows: hello.exe). In an IDE, use the Build and Run button.


Q4.	What are the main input/output operations in C++? Provide examples.

->	C++ uses streams from the <iostream> header. A stream is a flow of data between the program and a device.
	--------------------------------------------------------------------------
	Object		Purpose					Operator
	--------------------------------------------------------------------------
	cin		Standard input (keyboard)		>> (extraction)
	cout		Standard output (screen)		<< (insertion)
	cerr		Standard error, unbuffered		<<
	clog		Standard error, buffered (logging)	<<

	#include <iostream>
	#include <string>
	using namespace std;

	int main() {

    		int age;
    		string name;

    		cout << "Enter your age: ";
    		cin >> age;                    
    		cin.ignore();                  
    		cout << "Enter your full name: ";
    		getline(cin, name);            

    		cout << "Name: " << name << ", Age: " << age << endl;
    		cerr << "This is an error message" << endl;
    		return 0;
	}
	Notes: << and >> can be chained (cin >> a >> b;). endl inserts a newline and flushes the buffer ('\n' only inserts a newline). 	Formatting is done with manipulators from <iomanip> such as setw(), setprecision(), and fixed. File I/O uses ifstream and ofstream 	from <fstream>.


Q5. 	What are the different data types available in C++? Explain with examples.

	----------------------------------------------------------------------------------------------------------------
->	Category			Types						Example
	----------------------------------------------------------------------------------------------------------------
	Basic (primitive)	int, char, float, double, bool, void, wchar_t		int x = 5;
	Modifiers		short, long, signed, unsigned				unsigned long n;
	Derived			array, pointer, reference, function			int a[5]; int *p;
	User-defined		struct, class, union, enum, typedef/using		class Car {};

	Typical sizes (platform dependent): char 1 byte, bool 1 byte, short 2, int 4, long long 8, float 4, double 8 bytes.

	int age = 20;            // whole numbers
	float price = 99.5f;     // single-precision decimal
	double pi = 3.14159265;  // double-precision decimal
	char grade = 'A';        // single character
	bool passed = true;      // true (1) or false (0)

	void means "no value" (used for functions that return nothing). enum Color {RED, GREEN, BLUE}; creates named integer constants. 	C++ also provides the library type std::string for text.
	

Q6.	Explain the difference between implicit and explicit type conversion in C++.

->	Implicit conversion (type promotion/coercion) is done automatically by the compiler when types differ in an expression. A smaller 	type is promoted to the larger one (char → int → long → float → double).


	int a = 5;
	double b = a;        // int -> double automatically, b = 5.0
	int c = 5 + 2.5;     // 7.5 is truncated to 7 on assignment (data loss)

	Explicit conversion (type casting) is requested by the programmer.
	int x = 7, y = 2;
	double r1 = (double)x / y;               // C-style cast, 3.5
	double r2 = static_cast<double>(x) / y;  // C++ style cast, 3.5

	C++ casts: static_cast (normal, compile-time-checked conversions), dynamic_cast (safe downcast in class hierarchies), const_cast 	(add/remove const), reinterpret_cast (low-level pointer reinterpretation).
	-------------------------------------------------------------------------
	Aspect		Implicit			Explicit
	-------------------------------------------------------------------------
	Done by		Compiler			Programmer
	Syntax		None				Cast operator
	Risk		Silent data loss possible	Intentional, clearer



Q7. 	What are the different types of operators in C++? Provide examples.

	---------------------------------------------------------------------------------
->	Type			Operators			Example
	---------------------------------------------------------------------------------
	Arithmetic		+ - * / %			10 % 3 = 1
	Relational		== != > < >= <=			5 > 3 is true
	Logical			&& || !				(a > 0) && (b > 0)
	Assignment		= += -= *= /= %=		x += 5;
	Increment/Decrement	++ --				++x (prefix), x++ (postfix)
	Bitwise			& | ^ ~ << >>			5 & 3 = 1, 5 << 1 = 10
	Conditional (ternary)	?:				max = (a > b) ? a : b;
	Other			sizeof, ,, ::, ., ->, &, *	sizeof(int) = 4

	Logical operators short-circuit: in a && b, b is not evaluated if a is false. Prefix ++x increments before use; postfix x++ 	increments after use. Integer division truncates (7 / 2 = 3), and % works only on integers.



Q8. 	Explain the purpose and use of constants and literals in C++.

->	A literal is a fixed value written directly in the source code. A constant is a named value that cannot change after it is 	defined.

	Literals:
	• Integer: 10, 0x1F (hex), 075 (octal), 0b101 (binary, C++14)
	• Floating-point: 3.14, 2.5e3, 1.5f
	• Character: 'A', '\n'
	• String: "Hello"
	• Boolean: true, false
	• Pointer: nullptr

	Constants:
	const double PI = 3.14159;    // cannot be modified later
	constexpr int SIZE = 10;      // evaluated at compile time
	#define MAX 100               // preprocessor macro (no type checking)
	enum Day { MON, TUE, WED };   // named integer constants

	Purpose: constants make code readable (PI instead of 3.14159), prevent accidental modification (the compiler gives an error), and 	let a value be changed in one place. const and constexpr are preferred over #define because they are type-safe and scoped.


Q9. 	What are conditional statements in C++? Explain the if-else and switch statements.

->	Conditional statements choose which code runs based on a condition (non-zero or true means true).
	if, if-else, and else if:

	int marks = 82;
	if (marks >= 90) {
    		cout << "Grade A";
	} 
	else if (marks >= 75) {
    		cout << "Grade B";
	}
	else if (marks >= 50) {
    		cout << "Grade C";
	} 
	else {
   		cout << "Fail";
	}

	The first condition that is true runs, and the rest are skipped. else runs if none match.
	switch: selects among many fixed values of an integer, char, or enum expression. Each case normally ends with break to avoid fall-	through; default handles all other values.

	int day = 3;
	switch (day) {
    		case 1: cout << "Mon"; break;
    		case 2: cout << "Tue"; break;
    		case 3: cout << "Wed"; break;
    		default: cout << "Invalid";
	}

	Use if-else for ranges and complex conditions, and switch for a single variable compared against many constants.


Q10. 	What is the difference between for, while, and do-while loops in C++?

->	for (int i = 1; i <= 5; i++) {
		cout << i << " "; 
	} 
      
	int j = 1;
	while (j <= 5) { 
		cout << j << " "; j++; 
	}  
           
	int k = 1;
	do { 
		cout << k << " "; k++; 
	} while (k <= 5);         
	
	-------------------------------------------------------------------------------------------------------------------------------
	Feature			for				while					do-while
	-------------------------------------------------------------------------------------------------------------------------------	
	Type			Entry-controlled		Entry-controlled			Exit-controlled
	Condition checked	Before each pass		Before each pass			After each pass
	Minimum runs		0				0					1
	Init/update		In the loop header		Written separately			Written separately
	Best for		Known number of iterations	Unknown iterations, condition-driven	Body must run at least once 
	C++11 also adds the range-based for: for (int x : arr) cout << x;.


Q11. 	How are break and continue statements used in loops? Provide examples.

->	break immediately exits the nearest loop (or switch).
	for (int i = 1; i <= 10; i++) {
    		if (i == 5) {
			break;
		}       
    		cout << i << " ";      
	}

	continue skips the rest of the current iteration and moves to the next one.

	for (int i = 1; i <= 5; i++) {
    		if (i == 3){
			 continue;
		}   
    		cout << i << " ";        
	}
	In nested loops, break and continue affect only the innermost loop.


Q12. 	Explain nested control structures with an example.

->	A nested control structure is one control statement placed inside another: an if inside a loop, a loop inside a loop, or an if 	inside an if. It is used for patterns, matrices, tables, and multi-level decisions.
	// Right-angled triangle of stars (nested for loops)

	int n = 4;
	for (int i = 1; i <= n; i++) {        // outer loop: rows
    		for (int j = 1; j <= i; j++) {    // inner loop: stars in the row
        		cout << "* ";
   	 	}
    		cout << endl;
	}

	Output:
	*
	* *
	* * *
	* * * *

	The outer loop runs 4 times; for each pass, the inner loop runs i times. Another example is an if inside a loop: for (...) { if (i 	% 2 == 0) cout << i; } prints even numbers.



Q13. 	What is a function in C++? Explain function declaration, definition, and calling.

->	A function is a named block of code that performs a task, can take inputs (parameters), and can return a value. Functions avoid 	repetition and make programs modular.
	• Declaration (prototype): tells the compiler the name, return type, and parameter types. int add(int a, int b);
	• Definition: contains the body. int add(int a, int b) { return a + b; }
	• Call: runs the function with arguments. int s = add(3, 4);

	#include <iostream>
	using namespace std;

	int square(int x);            
	int main() {
    		cout << square(5);        
    		return 0;
	}

	int square(int x) {            
  		return x * x;
	}

	Parameters can be passed by value (copy), by reference (int &x, changes affect the original), or by pointer. C++ also supports 	function overloading (same name, different parameters) and default arguments. A function returning nothing uses void.




Q14. 	What is the scope of variables in C++? Differentiate between local and global scope.

->	Scope is the region of the program where a variable can be accessed.

	--------------------------------------------------------------------------------------------------------------
	Feature		|	Local					Global
	--------------------------------------------------------------------------------------------------------------
	Declared	|	Inside a function or block		Outside all functions
	Accessible	|	Only in that block			Throughout the file, in all functions
	Lifetime	|	Created on entry, destroyed on exit	Whole program run
	Default value	|	Garbage (uninitialized)			0
	Memory		|	Stack					Static data area

	int g = 10;                   
	void show() {
    		int l = 5;               
    		cout << g << " " << l;    
	}

	int main() {
    		cout << g;               
   		// cout << l;            
	}

	If a local variable has the same name as a global one, the local one shadows it; the global can still be reached with the scope 	resolution operator ::g. Other scopes are block scope (inside { }), function scope, and class scope. static local variables keep 	their value between calls. Overuse of globals is discouraged because it makes code harder to debug.


Q15. 	Explain recursion in C++ with an example.

->	Recursion is when a function calls itself to solve a smaller version of the same problem. Every recursive function needs a base 	case (stops the recursion) and a recursive case (calls itself with a smaller input).

	int factorial(int n) {
    		if (n <= 1) return 1;           // base case
    		return n * factorial(n - 1);    // recursive case
	}
	// factorial(4) = 4 * 3 * 2 * 1 = 24

	Execution of factorial(4): 4×factorial(3) → 3×factorial(2) → 2×factorial(1) → 1, then the values return back up the chain.
	Advantages: short, clear code for problems such as factorial, Fibonacci, tree traversal, and Tower of Hanoi. Disadvantages: uses 	stack memory for each call, can be slower than loops, and a missing base case causes infinite recursion and stack overflow.


Q16. 	What are function prototypes in C++? Why are they used?

->	A function prototype is a declaration that gives the function's name, return type, and parameter types (names optional) and ends 	with a semicolon: double area(double r);

	Why they are used:
	1. Call before definition: the compiler must know a function's signature before it sees a call, so prototypes let main() appear 	before the function bodies.
	2. Type checking: the compiler verifies the number and types of arguments and the return type, catching errors at compile time.
	3. Automatic conversions: arguments are converted to the declared parameter types.
	4. Header files: prototypes are placed in headers so many source files can use the same functions.
	5. Readability: they give a quick overview of a program's functions.
	In C++, a prototype is mandatory if a function is used before it is defined (unlike old C, which allowed implicit declarations).



Q17. 	What are arrays in C++? Explain the difference between single-dimensional and multi-dimensional arrays.

->	An array is a fixed-size collection of elements of the same type stored in contiguous memory, accessed by an index starting at 0. 	C++ does not check bounds, so an invalid index causes undefined behavior.
	Single-dimensional array: a linear list.

		int marks[5] = {70, 80, 90, 60, 85};
		cout << marks[2];     // 90

	Multi-dimensional array: an array of arrays; the common form is the 2D array (rows and columns).
		int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
		cout << m[1][2];      // 6
	------------------------------------------------------------------------------------------------
	Feature			1D array		Multi-dimensional array
	------------------------------------------------------------------------------------------------
	Structure		Single list		Table/matrix (or higher)
	Declaration		int a[5];		int a[3][3];
	Indices			1			2 or more
	Traversal		One loop		Nested loops
	Memory layout		Contiguous		Contiguous, row by row (row-major)
	Use			Marks, scores, lists	Matrices, grids, tables




Q18.	Explain string handling in C++ with examples.

->	C++ has two ways to handle strings.
	1. C-style strings: a char array ending with the null character '\0'.
	char s[] = "Hello";        // 6 bytes: H e l l o \0
	char t[20];
	cin >> t;                  
	cin.getline(t, 20);       

	2. std::string class (from <string>): the preferred way. It grows automatically, supports +, ==, and has many member functions.
	
	#include <string>
	string a = "Hello";
	string b = "World";
	string c = a + " " + b;    
	cout << c.length();       
	if (a == "Hello"){
		 cout << "Equal";
	}
	getline(cin, c);  
        
	std::string is safer than C-style strings because it manages memory itself and avoids buffer overflows.



Q19. 	How are arrays initialized in C++? Provide examples of both 1D and 2D arrays.

->	1D arrays:
	int a[5] = {1, 2, 3, 4, 5};    // full initialization
	int b[] = {10, 20, 30};        // size deduced as 3
	int c[5] = {1, 2};             // rest become 0: {1,2,0,0,0}
	int d[5] = {0};                // all zeros
	int e[5] = {};                 // all zeros (C++)

	2D arrays:
	int m[2][3] = { {1, 2, 3}, {4, 5, 6} };   // row by row
	int n[2][3] = {1, 2, 3, 4, 5, 6};         // flat, filled row-major
	int p[][3]  = { {1, 2, 3}, {4, 5, 6} };   // row count deduced
	int z[3][3] = {0};                        // all zeros

	For 2D arrays, only the first dimension may be omitted. Elements can also be set at runtime using loops with cin. Uninitialized 	local arrays contain garbage values.





Q20. 	Explain string operations and functions in C++. 

->	C-style functions (<cstring>):

	---------------------------------------------------------
	Function		Purpose
	---------------------------------------------------------
	 strlen(s)		Length (excluding '\0')
	strcpy(d, s)		Copy s into d
	strcat(d, s)		Append s to d
	strcmp(a, b)		Compare (0 if equal)
	strchr(s, c)		First occurrence of a character
	strstr(s, sub)		First occurrence of a substring

	std::string member functions and operators:

	---------------------------------------------------------
	Operation		Example
	---------------------------------------------------------
	Length			s.length() or s.size()
	Concatenate		s1 + s2, s1.append(s2)
	Compare			s1 == s2, s1.compare(s2)
	Access character	s[0], s.at(0)
	Substring		s.substr(2, 3)
	Find			s.find("lo") (returns string::npos if absent)
	Insert / erase		s.insert(2, "xx"), s.erase(1, 2)
	Replace			s.replace(0, 2, "ab")
	Check empty / clear	s.empty(), s.clear()
	Convert			stoi("42"), to_string(42)


	string s = "Hello World";
	cout << s.length();          // 11
	cout << s.substr(0, 5);      // Hello
	cout << s.find("World");     // 6
	s.append("!");               // Hello World!


Q21. 	Explain the key concepts of Object-Oriented Programming (OOP).

->	1. Class: a blueprint or template that defines the data (attributes) and functions (methods) of a kind of entity.
	2. Object: an instance of a class, with its own copy of the data.
	3. Encapsulation: bundling data and methods into one unit and restricting direct access to the data (private), exposing it only 	through public functions.
	4. Abstraction: showing only the essential features and hiding implementation details (e.g., you drive a car without knowing the 	engine's internals). Achieved with classes and abstract classes.
	5. Inheritance: a derived class acquires the properties and behavior of a base class, which promotes reuse.
	6. Polymorphism: "many forms": the same function name behaves differently. Compile-time via function and operator overloading; 	run-time via virtual functions and overriding.
	7. Message passing and dynamic binding: objects communicate by calling each other's member functions, and virtual calls are 	resolved at run time.


Q22. 	What are classes and objects in C++? Provide an example.

->	A class is a user-defined type that groups data members and member functions. It describes what an object will have but uses no 	memory itself. An object is a real instance of the class created in memory. Members are accessed with the dot operator (.), or -> 	through a pointer. Access specifiers are private (default for classes), public, and protected.

	#include <iostream>
	#include <string>
	using namespace std;

	class Student {
		private:
    			string name;
    			int roll;
		public:
    			Student(string n, int r) {    // constructor
        		name = n;
        		roll = r;
    	}

    	void display() {              // member function
        		cout << name << " (Roll " << roll << ")" << endl;
    		}
	};

	int main() {
    		Student s1("Asha", 101);      // object
    		Student s2("Ravi", 102);
    		s1.display();
    		s2.display();
    		return 0;
	}

	Member functions can be defined inside the class or outside using the scope resolution operator: void Student::display() { ... }. 	A constructor initializes an object when it is created; a destructor (~Student()) runs when it is destroyed.



Q23. 	What is inheritance in C++? Explain with an example.

->		Inheritance lets a new class (derived/child class) acquire the members of an existing class (base/parent class). It models 	an "is-a" relationship (a Student is a Person) and promotes code reuse.
	Syntax: class Derived : public Base { ... };

	#include <iostream>
	#include <string>
	using namespace std;

	class Person {                    // base class
		protected:
   			string name;
    			int age;
		public:
    			Person(string n, int a) : name(n), age(a) {}
    		void showPerson() { 
			cout << name << ", " << age << endl; 
			}
		};

	class Student : 
		public Person {  
			 // derived class
    			int roll;
		public:
    			Student(string n, int a, int r) : Person(n, a), roll(r) {}

    		void showStudent() {
        			showPerson();             // reused from base
        			cout << "Roll: " << roll << endl;
    			}
		};

	int main() {
    		Student s("Asha", 20, 101);
   		s.showStudent();
    		return 0;
	}
	Types of inheritance: single, multilevel, multiple (one class with several bases), hierarchical (many classes from one base), and 	hybrid. With public inheritance, public base members stay public and protected members stay protected; private members of the base 	are never directly accessible to the derived class.



Q24. 	What is encapsulation in C++? How is it achieved in classes?

->	Encapsulation is the bundling of data and the functions that operate on it into a single unit (a class), while hiding the internal 	data from outside access. It protects data from unintended changes and lets the class control how its data is used and validated.
	How it is achieved:
	1. Declare data members as private (or protected).
	2. Provide public member functions (getters and setters, or operations like deposit) as the only interface.
	3. Put validation logic inside those functions.

	#include <iostream>
	using namespace std;

	class BankAccount {
		private:
   			double balance;               // hidden data
		public:
    			BankAccount() : balance(0) {}
    		void deposit(double amt) {
        		if (amt > 0) {
			balance += amt;
			}
    		}

    		bool withdraw(double amt) {
        		if (amt > 0 && amt <= balance) { 
				balance -= amt; return true; 
				}
        		return false;           
    			}
	    		double getBalance() const { return balance; }
		};

	int main() {
    	BankAccount acc;
    	acc.deposit(500);
    	acc.withdraw(200);
    	cout << acc.getBalance();     // 300
    	// acc.balance = 1000000;     // ERROR: balance is private
	}
	Benefits: data security, controlled access, easier maintenance (internal details can change without affecting users of the class), 	and validation of data. Encapsulation is the basis of data hiding.
