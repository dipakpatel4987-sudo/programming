try:
    file = open("example.txt", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("Error: File does not exist.")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("File was not opened.")
        