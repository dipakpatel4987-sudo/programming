# Module 6: Python Fundamentals:

# Assessment:

#  Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.
def calculate_grade(avg):
    if avg >=90:
        return "A+"
    elif avg >=80:
        return "A"
    elif avg >=60:
        return "B"
    elif avg >=40:
        return "C"
    else:
       return "fail"

def input_marks():
    marks=[]
    n=int(input("Enter number of subject"))
    
    for i in range(n):
        mark=float(input(f"Enter number of subject{i+1}:"))
        marks.append(mark)
    
    return marks

def display_result(marks):
    total=sum(marks)
    avg=total/len(marks)
    grade =calculate_grade(avg)

    
    print("\n----- RESULT -----")
    print("Marks:", marks)
    print("Total:", total)
    print("Average:",avg)
    print("Grade:", grade)
    print("------------------\n")



while True:
    print("1. Enter Student Marks")
    print("2. Exit")

    choice=int(input("Enter Your choice:"))

    if choice==1:
        marks=input_marks()
        display_result(marks)
        break
    elif choice==2:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.\n")

