import random
student={}
class Student:
    def registration(self):
        name=input("Enter Your Name:")
        roll=int(input("Enter Your Roll No.:"))
        gmail=input("Enter Your Gmail:")
        course=input("Enter Your COURSE:")
        phone=int(input("Enter Your Phone no.:"))
        if phone<=5 and phone>=10:
            otp=random.randint(1000,9999)
            s_id=random.randint(1,100)
            print("OTP:",otp)
            user_otp=int(input("Enter Your OTP:"))
            if otp==user_otp:
                print("REGITRATION IN PROSSECCING!!!")
                print("Student Name:",name)
                print("Student ROLL NO:",roll)
                print("Student GMAIL:",gmail)
                print("Student COURSE:",course)
                print("Student PHONE NO.:",phone)
                print("Student ID:",s_id)
            else:
                print("Wrong OTP!!!")
            
           

        self.name=name
        self.roll=roll
        self.gmail=gmail
        self.course=course
        self.phone=phone
        

        student[roll]={
            "name":self.name,
            "roll":self.roll,
            "gamil":self.gmail,
            "course":self.course,
            "phone":self.phone,
            "student_ID":s_id
        }

        

        print("REGITRATION COMPLETED SUCCESSFULLY!!!")

    def login(self):
        name=input("Enter Your Name:")
        roll=int(input("Enter Your Roll No.:"))
        s_id=int(input("Enter Your Student ID:"))

        if student[roll]["s_id"]==s_id:
            otp=random.randint(1000,9999)
            print("OTP:",otp)
            user_otp=int(input("Enter Your OTP:"))
            if otp==user_otp:
                print("Login IN PROSSECCING!!!")
                if roll in student:
                    print("===== student =====")
                    print("STUDENT NAME:",student[roll]["name"])
                    print("STUDENT ROLL NO.:",student[roll]["roll"])
                    print("STUDENT GMAIL:",student[roll]["gamail"])
                    print("STUDENT COURSE:",student[roll]["course"])
                    print("STUDENT ID:",student[roll]["student_id"])
                    print("STUDENT PHONE NO.:",student[roll]["phone"])
                else:
                    print("STUDENT DON'T FOUND!!!")
            else:
                print("Wrong OTP!!!")
        else:
            print("STUDENT DON'T FOUND!!!")
    def all_student(self):
        for roll,data in student.items():
            print("*"*20,"student","*"*20)
            print("STUDENT NAME:",data[roll]["name"])
            print("STUDENT ROLL NO.:",data[roll]["roll"])
            print("STUDENT GMAIL:",data[roll]["gamail"])
            print("STUDENT COURSE:",data[roll]["course"])
            print("STUDENT ID:",data[roll]["student_id"])
            print("STUDENT PHONE NO.:",data[roll]["phone"])

obj=Student()
while True:
    mainu="""
1.REGITRATION
2.LOGIN
3.ALL STUDENT LIST
4.EXIT
"""
    print(mainu)
    choice=int(input("Enter your choice:"))
    if choice==1:
        obj.registration()
    elif choice==2:
        obj.login()
    elif choice==3:
        obj.all_student()
    elif choice==4:
        print("Thank you!!")
        break
    else:
        print("somthing wrong!!!")


        






