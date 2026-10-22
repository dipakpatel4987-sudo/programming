import random

l=["rock","paper","cijer"]

system=random.choice(l)

print("*******************rock peper game*********************")
while True:
    choice=input("Enter your move!!!:")

    if choice=="rock" and system=="rock":
        print(" game draw")
    elif choice=="rock" and system=="paper":
        print("you are lose")
    elif choice=="rock" and system=="cijer":
        print("you are win")
    elif choice=="paper" and system=="paper":
        print("draw")
    elif choice=="paper" and system=="rock":
        print("you are lose")
    elif choice=="paper" and system=="cijer":
        print("you are lose")

