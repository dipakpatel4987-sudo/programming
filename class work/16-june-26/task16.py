from task15 import *
import pymysql
mydb = pymysql.connect(host="localhost",user="root",password="", port=3307)
mycursor = mydb.cursor()

while True:
    mainu="""
press 1 for insert
press 2 for update
press 3 for delet
press 4 for fecth

"""
    print(mainu)
    choice=int(input("Enter your choice:"))

    if choice==1:
        roll=int(input("Enter roll no"))
        name=input("Enter your name:")
        
        
