# Module 2 – Introduction to Programming 







Q1.	Write an essay covering the history and evolution of C programming. Explain its importance and why it is still used today.

->	C was created by Dennis Ritchie at Bell Labs between 1971 and 1973. It descends from CPL (1963) → BCPL (1967, Martin Richards) → B 	(1969, Ken Thompson). B was typeless and too limited for the byte-addressable PDP-11, so Ritchie added a type system and a native-	code compiler, producing C. In 1973 the Unix kernel was rewritten in C, proving that an operating system could be written in a 	high-level language and ported between machines.

	Evolution: K&R C (1978) → ANSI C / C89 (1989), ISO C90 (function prototypes, standard library) → C99 (inline functions, // 	comments, long long, stdint.h) → C11 (threads, atomics, _Generic) → C17 (bug fixes) → C23 (nullptr, constexpr, #embed, bool as 	keyword).

	Importance: It is the foundation of operating systems (Unix, Linux, Windows kernel parts), compilers, databases, and embedded 	firmware, and it influenced C++, Java, C#, Go, and many other languages. It also taught the industry the value of portable 	software.

	Why it is still used: (1) very fast, with minimal runtime overhead; (2) direct hardware and memory access; (3) runs on nearly 	every processor; (4) small, stable language with huge legacy codebases; (5) dominant in embedded and real-time systems; (6) a 	mature ecosystem of tools and libraries; (7) a good way to learn how computers work.




Q2.	Describe the steps to install a C compiler (e.g., GCC) and set up an Integrated

->	To install GCC, use MinGW/MSYS2 on Windows (then add its bin folder to PATH), sudo apt install build-essential on Linux, or xcode-	select --install on Windows (MinGW-w64 via MSYS2):
	1. Download and install MSYS2 from msys2.org.
	2. Open the MSYS2 terminal and run: pacman -S mingw-w64-ucrt-x86_64-gcc
	3. Add the compiler's bin folder (e.g., C:\msys64\ucrt64\bin) to the system PATH environment variable.
	4. Open a new Command Prompt and verify with gcc --version . 
	Check with gcc --version. For an IDE, install Code::Blocks or Dev-C++ 	(both bundle a compiler), or VS Code with the Microsoft 	C/C++ extension. Compile with gcc file.c -o file.



Q3.	Explain the basic structure of a C program, including headers, main function, comments, data types, and variables. Provide 	examples.

->	A C program has these parts, in order:
	1. Documentation/comments
	2. Preprocessor directives (header files, macros)
	3. Global declarations
	4. The main() function
	5. User-defined functions

	-> Program: Basic structure demo 
	#include <stdio.h>      
	#define PI 3.14159      

	int main(void)          
	{
    	int age = 20;      
    	float height = 5.8f;
    	char grade = 'A';
    	printf("Age=%d Height=%.1f Grade=%c\n", age, height, grade);
    	return 0;           
	}
	Headers: files included with #include that declare library functions. <stdio.h> provides printf and scanf; <stdlib.h> provides 	malloc and exit; <string.h> provides string functions; <math.h> provides math functions.
	main function: execution always begins here. int main(void) returns an integer to the operating system, where 0 means success.
	Comments: ignored by the compiler. Single-line: // text. Multi-line: /* text */.
	
	Data types:
	--------------------------------------------------------------------------------------	
	Category			Types			Example
	--------------------------------------------------------------------------------------
	Basic: 			int, char, float, double	int x = 5;
	Modifiers		short, long, signed, unsigned	unsigned int u;
	Derived			arrays, pointers, functions	int a[5];
	User-defined		struct, union, enum, typedef	struct S {int a;};
	Void			void				void f(void)

	Variables: named memory locations. Syntax: type name = value;. Rules: the name must start with a letter or underscore, contain 	only letters, digits, and underscores, not be a keyword, and is case-sensitive. A variable must be declared before it is used. 	Constants are declared with const int x = 10; or #define.


Q4.	Write notes explaining each type of operator in C: arithmetic, relational, logical, assignment, increment/decrement, bitwise, and 	conditional operators

->	An operator is a symbol that tells the compiler to perform a specific operation on operands.
 	
	1. Arithmetic operators: + addition, - subtraction, * multiplication, / division, % modulus (remainder, integers only). Example: 	10 % 3 gives 1. Integer division truncates: 7 / 2 gives 3.

	2. Relational operators: compare two values and return 1 (true) or 0 (false): ==, !=, >, <, >=, <=. Example: 5 > 3 gives 1.

	3. Logical operators: combine conditions. && (AND: true if both are true), || (OR: true if either is true), ! (NOT: reverses 	truth). They use short-circuit evaluation: in a && b, if a is false, b is not evaluated.

	4. Assignment operators: = assigns a value.Compound forms: +=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=. Example:x += 5 means x = x 	+ 5.

	5. Increment/decrement operators: ++ and --. Prefix (++x) changes the value first, then uses it. Postfix (x++) uses the value 	first, then changes it. If x = 5, then y = ++x gives y=6, x=6, while y = x++ gives y=5, x=6.

	6. Bitwise operators: work on individual bits of integers.
	-------------------------------------------------------------------------------
	Operator		Meaning			Example (a=5 0101, b=3 0011)
	-------------------------------------------------------------------------------
	&			AND			a & b = 1
	|			OR			a | b = 7
	^			XOR			a ^ b = 6
	~			NOT (complement)	~a = -6
	<<			Left shift 		a << 1 = 10
	>>			Right shift 		a >> 1 = 2

	7. Conditional (ternary) operator: condition ? value_if_true : value_if_false;. It is the only operator that takes three operands. 	Example: max = (a > b) ? a : b;
	Other operators: sizeof (size in bytes), , (comma), & (address-of), * (dereference), -> and . (member access).





Q5.	Explain decision-making statements in C (if, else, nested if-else, switch).Provide examples of each.

->	Decision-making statements let a program choose which block of code to run based on a condition. In C, any non-zero value is true 	and zero is false.

	1. if statement: runs a block only if the condition is true.
	int n = 10;
	if (n > 0) {
    		printf("Positive\n");
	}

	2. if-else statement: chooses between two blocks.
	if (n % 2 == 0)
    	printf("Even\n");
	else
    	printf("Odd\n");

	3. Nested if-else (and else if ladder): tests multiple conditions in sequence; the first true one runs.
	int marks = 82;
	if (marks >= 90)
    		printf("Grade A\n");
	else if (marks >= 75)
    		printf("Grade B\n");
	else if (marks >= 50)
    		printf("Grade C\n");
	else
    		printf("Fail\n");

	A nested if places one if inside another: if (a > 0) { if (b > 0) printf("Both positive"); }.
	
	4. switch statement: selects one of many blocks based on the value of an integer or character expression. Each case ends with 	break to prevent fall-through. default runs when no case matches.
	int day = 3;
	switch (day) {
    		case 1: printf("Monday\n"); break;
    		case 2: printf("Tuesday\n"); break;
    		case 3: printf("Wednesday\n"); break;
    		default: printf("Invalid day\n");
	}

	Rules for switch: the expression must be an integer or char (not float or string); case labels must be unique constants. Use 	switch for many fixed values and if-else for ranges and complex conditions.


Q6.	Compare and contrast while loops, for loops, and do-while loops. Explain the scenarios in which each loop is most appropriate.

->	Loops repeat a block of statements while a condition holds.

	// while: condition checked first
	int i = 1;
	while (i <= 5) { 
		printf("%d ", i);
		 i++; 
		}

	// for: initialization, condition, update in one line
	for (int i = 1; i <= 5; i++){ 
		printf("%d ", i);
		}

	// do-while: body runs first, condition checked after
	int j = 1;
	do { 
		printf("%d ", j); 
		j++; }
		while (j <= 5);
	---------------------------------------------------------------------------------------------------------------------
	Feature				while				for				do-while
	----------------------------------------------------------------------------------------------------------------------
	Type				Entry-controlled		Entry-controlled		Exit-controlled
	Condition checked		Before each iteration		Before each iteration		After each iteration
	Minimum executions		0				0				1
	Initialization/update		Written separately		Together in the header		Written separately
	Semicolon after condition	No				No				Yes
	When to use each:

	• for: when the number of iterations is known in advance (counting, iterating over arrays, tables).

	• while: when the number of iterations is unknown and depends on a condition (reading input until the end, processing digits of a 	number, searching).

	• do-while: when the body must run at least once (menu-driven programs, input validation such as "enter a number until it is 	positive").
	All three can express the same logic; the choice is mainly about readability.




Q7.	Explain the use of break, continue, and goto statements in C. Provide examples of each.
->	break: immediately terminates the nearest enclosing loop or switch and transfers control to the statement after it.
	for (int i = 1; i <= 10; i++) 
	{
    		if (i == 5) {
		break;
		}
	        printf("%d ", i);
	}

	continue: skips the rest of the current iteration and jumps to the next iteration (in a for loop, to the update expression).
	for (int i = 1; i <= 5; i++) {
    		if {
			i == 3) continue;  
		    }
    		printf("%d ", i);       
	}
	goto: unconditionally jumps to a labeled statement in the same function.
	int n = 1;
	start:
    		printf("%d ", n);
    		n++;
    		if (n <= 3) {
		goto start;   
		}

	goto makes code hard to follow ("spaghetti code") and is generally avoided. Its accepted use is breaking out of deeply nested 	loops or jumping to a common error-cleanup section.


Q8.	What are functions in C? Explain function declaration, definition, and how to call a function. Provide examples.

->	A function is a named, reusable block of code that performs a specific task. Functions reduce repetition, improve readability, and 	make programs modular and easier to test. C has library functions (printf, sqrt) and user-defined functions.
	Function declaration (prototype): tells the compiler the function's name, return type, and parameter types before it is used. 	Syntax: return_type name(parameter_list);

	int add(int a, int b);   

	Function definition: contains the actual body of the function.
	
	int add(int a, int b) {  
    	return a + b;
	}

	Function call: executes the function by passing arguments.
	
	int result = add(5, 3);  

	Complete example:
	#include <stdio.h>

	int square(int x);            

	int main(void) {
   		printf("%d\n", square(4)); 
    		return 0;
	}

	int square(int x) {           
    		return x * x;
	}

	Key points: a function may return a value or void; arguments (actual values) are passed to parameters (formal variables). C uses 	call by value by default, so changes to parameters do not affect the caller's variables; to modify the originals, pass pointers 	(call by reference). Functions can call themselves (recursion).


Q9.	Explain the concept of arrays in C. Differentiate between one-dimensional and multi-dimensional arrays with examples. 

->	An array is a collection of elements of the same data type stored in contiguous memory locations and accessed by an index. I	ndexing starts at 0. C does not check array bounds, so accessing an invalid index causes undefined behavior.

	One-dimensional array: a linear list of elements.
	int marks[5] = {70, 80, 90, 60, 85};
	printf("%d", marks[2]);   
	for (int i = 0; i < 5; i++) {

		printf("%d ", marks[i]);
	}
	Multi-dimensional array: an array of arrays. The most common is the two-dimensional array (matrix), with rows and columns.
	int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
	printf("%d", m[1][2]);    
	for (int i = 0; i < 2; i++){
    		for (int j = 0; j < 3; j++){
        		printf("%d ", m[i][j]);
		}
	}
	------------------------------------------------------------------------------------------
	Feature			1-D array		Multi-D array
	------------------------------------------------------------------------------------------
	Structure		Single row/list		Rows and columns (table/matrix)
	Declaration		int a[5];		int a[3][3];
	Indices needed		1			2 or more
	Loops to traverse	1			One nested loop per dimension
	Use			Lists, marks, scores	Matrices, grids, tables

	Multi-dimensional arrays are stored in row-major order in memory. Arrays can be initialized at declaration; unspecified elements 	become 0.


Q10.	Explain what pointers are in C and how they are declared and initialized. Why are pointers important in C?

->	A pointer is a variable that stores the memory address of another variable.

	Declaration: data_type *pointer_name; Example: int *p;

	Initialization: assign the address of a variable using the address-of operator &.

	int x = 10;
	int *p = &x;        
	printf("%d", *p);  
	*p = 25;  
          
	• &x gives the address of x.
	• *p (dereference operator) accesses the value at the address stored in p.
	• A pointer with no valid target should be set to NULL. An uninitialized pointer (a "wild pointer") is dangerous.
	• Pointer arithmetic: p + 1 moves to the next element of the pointed-to type. For an array a, the name a acts as a pointer to 	a[0], so *(a + i) equals a[i].

	Why pointers are important:

	1. Call by reference: functions can modify the caller's variables (e.g., a swap function).
	2. Dynamic memory allocation: malloc, calloc, realloc, and free return and use pointers, letting programs allocate memory at 	runtime.
	3. Efficient array and string handling: strings and arrays are accessed through pointers.
	4. Data structures: linked lists, trees, and graphs depend on pointers.
	5. Efficiency: passing a pointer to a large structure avoids copying it.
	6. Hardware access: pointers can address specific memory locations, which is essential for embedded and systems programming.
	7. Function pointers: enable callbacks and flexible designs.
	Pointers give C its power, but misuse (dangling pointers, null dereference, buffer overflows, memory leaks) causes serious bugs.


Q11.	Explain string handling functions like strlen(), strcpy(), strcat(), strcmp(), and strchr(). Provide examples of when these 	functions are

->	In C, a string is an array of char terminated by the null character '\0'. For example, char s[] = "Hello"; occupies 6 bytes. The 	functions below are declared in <string.h>.

	strlen(s): returns the length of the string, excluding '\0'.

	strlen("Hello");  

	Useful for: validating input length, loops over characters, allocating memory.

	strcpy(dest, src): copies src (including '\0') into dest. The destination must be large enough.
	
	char a[20];
	strcpy(a, "Hello");   // a = "Hello"
	
	Useful for: assigning a string value to a character array (C does not allow a = "Hello").
	strcat(dest, src): appends src to the end of dest.

	char s[30] = "Hello ";
	strcat(s, "World");   // s = "Hello World"

	Useful for: building full names, file paths, or messages.
	strcmp(s1, s2): compares two strings alphabetically. Returns 0 if equal, a negative value if s1 < s2, and a positive value if s1 > 	s2.

	strcmp("abc", "abc");   // 0
	strcmp("abc", "abd");   // negative

	Useful for: password checks, sorting names, searching. Note that == compares addresses, not contents, so strcmp must be used.
	strchr(s, c): returns a pointer to the first occurrence of character c in s, or NULL if not found.

	char *p = strchr("hello", 'l');   // points to "llo"

	Useful for: finding a delimiter (such as @ in an email or . in a filename) and splitting strings.
	Safety note: strcpy and strcat do not check buffer size, which can cause buffer overflows; safer alternatives are strncpy, 	strncat, and snprintf.

Q12.	Explain the concept of structures in C. Describe how to declare, initialize, and access structure members.

->	A structure (struct) is a user-defined data type that groups variables of different data types under a single name. Each variable 	inside is a member. It is used to represent real-world entities such as a student, employee, or book.

	Declaration:

	struct Student {
    		char name[30];
    		int roll;
    		float marks;
	};

	This defines a template only; no memory is allocated until variables are created: struct Student s1;

	Initialization:	

	struct Student s1 = {"Asha", 101, 88.5};
	// or by member name (designated initializer)
	struct Student s2 = { .name = "Ravi", .roll = 102, .marks = 79.0 };

	Accessing members:
		• Dot operator . with a structure variable: s1.roll = 105; printf("%s", s1.name);
		• Arrow operator -> with a structure pointer:

	struct Student *p = &s1;
	printf("%d", p->roll);    // same as (*p).roll

	Other points: structures can be stored in arrays (struct Student cls[3];), nested inside other structures, passed to functions by 	value or by pointer, and renamed with typedef. Memory for a structure is the sum of its members plus possible padding for 	alignment. Unlike a union (whose members share the same memory), a structure's members each have their own storage.



Q13.	Explain the importance of file handling in C. Discuss how to perform file operations like opening, closing, reading, and writing 	files.

->	Importance: Variables live in memory and disappear when a program ends. File handling lets programs store data permanently on 	disk, read large amounts of input without typing it, share data between programs, keep logs and records, and process data that is 	too large for memory. Files are accessed through a file pointer of type FILE * (from <stdio.h>).

	1. Opening a file: FILE *fp = fopen("data.txt", "mode"); It returns NULL on failure, so always check.
	-----------------------------------------------------------------------------------
	Mode				Meaning
	-----------------------------------------------------------------------------------
	"r"				Read (file must exist)
	"w"				Write (creates file or erases existing content)
	"a"				Append (adds to the end)
	"r+"				Read and write (file must exist)
	"w+"				Read and write (creates or erases)
	"a+"				Read and append
	add b (e.g., "rb")		Binary mode

	2. Writing: fprintf(fp, "format", ...), fputs(str, fp), fputc(ch, fp), fwrite(...) (binary).
	3. Reading: fscanf(fp, "format", ...), fgets(buffer, size, fp), fgetc(fp), fread(...) (binary).
	4. Closing: fclose(fp); flushes buffered data and releases the file. Forgetting it can lose data.
	Other useful functions: feof(fp) (checks end of file), fseek, ftell, rewind (move or report position), remove, rename.

	Example:
	#include <stdio.h>

	int main(void) {
    		FILE *fp = fopen("test.txt", "w");   
    		if (fp == NULL) { 
			printf("Error!\n"); 
			return 1; 
			}
    		fputs("Hello, file handling!", fp);   
    		fclose(fp);                           
    		char buf[100];
    		fp = fopen("test.txt", "r");         
    		fgets(buf, sizeof buf, fp);           
    		printf("%s\n", buf);
    		fclose(fp);
    		return 0;
	}
	Types of files: text files (human-readable characters) and binary files (raw bytes, more compact and faster, used for structures 	and images).