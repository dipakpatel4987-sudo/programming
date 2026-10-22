student={}

roll=int(input("Enter your roll no."))
marks=int(input("Enter your marks:"))

student[roll]={
    "roll":roll,
    "marks":marks
}

print(student.items())
