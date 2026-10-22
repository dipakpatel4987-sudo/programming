import random
student={}
marks=[]
class Student:
    def User(self):
        stdname=input("Enter Student Name:")
        roll=int(input("Enter student RollNO.:"))
        marks=int(input("Enter marks"))
        subject=input("Enter Subject Name:")

        student[roll] ={
            "name":stdname,
            "Roll_no.":roll,
            "marks":marks,
            "subject":subject
        }
        print("Student Add Seccessfully!!!")
class Grede(Student):
    def grede(self):
        
