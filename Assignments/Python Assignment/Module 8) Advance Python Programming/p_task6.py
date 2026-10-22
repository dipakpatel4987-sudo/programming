file=open("p_task4.txt","r")
position=file.tell()

print("current position of file cursor",position)
data=file.read(10)

position = file.tell()

print("Position after reading 10 characters:", position)



file.close()    