try:
    # File handling
    file = open("p_task3.txt", "r")
    print(file.read())
    file.close()

    # Division operation
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except FileNotFoundError:
    print("Error: File not found.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input.")