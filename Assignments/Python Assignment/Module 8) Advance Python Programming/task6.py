try:
    num1=int(input("Enter your number:"))
    num2=int(input("Enter your number:"))

    result=num1/num2

    print("result",result)


except ZeroDivisionError :
    print("number not zero")
except ValueError:
    print("wrong input")

except Exception as e:
    print("calculater is incompate!!")
finally:
    print("calculator program complate!!")