text=input("Enter string= ")

max_char=""
max_count=0

for ch in text:
    count=text.count(ch)

    if count>max_count:
        max_count=count
        max_char=ch
print("Highest frequency character:", max_char)
print("Count:", max_count)