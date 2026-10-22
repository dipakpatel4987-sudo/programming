import random

student={}

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        roll=int(input("Enter your roll no.: "))

        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        course=input("Enter your course:")
        marks=float(input("Enter your marks:"))

        student[roll]={
            "name":name,
            "age":age,  
            "course":course,
            "marks":marks
        }
        print("student Add seccessfolly!!!")

    elif choice==2:
        roll=int(input("Enter your roll no.: "))

        if roll in student:
            print("\n Student Details!!!")
            print("Name   :",student[roll]["name"])
            print("age    :",student[roll]["age"])
            print("course :",student[roll]["course"])
            print("marks  :",student[roll]["marks"])
        else:
            print("student not found!!")
    elif choice==3:
        roll=int(input("Enter your roll no,:"))

        if roll in student:
            student[roll]["name"]=input("Enter your name   :")
            student[roll]["age "]=input("Enter your age    :")
            student[roll]["course"]=input("Enter your course :")
            student[roll]["marks"]=input("Enter your marck  :")

            print("update seccessfolly!!!")
        else:
            print("sudent not found!!")
    elif choice==4:
            roll=int(input("Enter your roll no,:"))
            otp=random.randint(1001,9999)
            print("\n yuor otp:",otp)
            student_otp=int(input("Enter your otp for varification:"))
            if student_otp==otp:

                if roll in student:
                    del student[roll]

                    print("Student Deleted Successfully! ")
                else:
                    print("student not found!!!")
            else:
                print("wrong otp")
    elif choice==5:
        if len(student)==0:
            print("No Student Records Found!")
        
        else:
            print("\n===== ALL STUDENTS =====")

            for roll,data in student.items():
                print("\nRoll No.:",roll)
                print("name  :",data["name"])
                print("age   :",data["age"])
                print("course:",data["course"])
                print("marks :",data["marks"])
    elif choice==6:
        print("program ended!!!" \
        "Good bye!!")
        break
    else:
        print("Invaild choice!!!")


