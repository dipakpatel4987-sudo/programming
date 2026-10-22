import random
book={}

        

class Add_book:
    def add(self):
        book_name=input("Enter BOOK Name:")
        book_id=random.randint(1,999)

        book[id]={
            "name":book_name,
            "ID":book_id
        }
        print("BOOk ADD seccessfully !!!")
        print("BOOK NAME:",book_name)
        print("BOOK ID:",book_id)
obj=Add_book()


while True:

    print("-"*20,"mainu","-"*20)
    print("ADD book")
    print("View All Books")
    print("Sreach Book")
    print("Delete Book")

    choice=int(input("Enter choice:"))
    if choice==1:

