import random
'''
1 for snake
-1 for water
0 for gun
'''
while True:
    computer=random.choice([-1,0,1])

    youstr=input("Enter you choice:")
    youdect={"s":1,"w":-1,"g":0}
    reversedict={1:"Snake",-1:"Water",0:"Gun"}

    you=youdect[youstr]

    print(f"you choice{reversedict[you]}\n computer choice{reversedict[computer]}")


    if(computer==you):
        print("It's a draw")
        break

    else:
        if(computer==-1 and you==1):
            print("You Win!!")
    
        elif(computer==-1 and you==0):
            print("You Los!!")
    
        elif(computer==1 and you==0):
            print("You Win!!")
    
        elif(computer==1 and you==-1):
            print("You Los!")

        elif(computer==0 and you==-1):
         print("You Win!!")

        elif(computer==0 and you==1):
            print("You Los!!")
    
        else:
            print("Somthing Wrong:")
            break
    
    