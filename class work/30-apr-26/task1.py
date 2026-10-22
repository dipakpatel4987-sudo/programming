# s= input("Enter Number:").lower()

# if s==s[::-1]:
#     print("palindrome!!!")
# else:
#     print("not palindrome!!")

s=input("Enter name")

if len(s)%2==0:
    print(s)
else:
    mid=len(s)//2
    print(s[mid-1]+s[mid]+s[mid+1])