# l = []
# ev = []
# od = []
# for i in range(1,31):
#     l.append(i)

#     if i%2==0:
#         ev.append(i)

#     else:
#         od.append(i) 
# print(l)
# print(ev)
# print(od)


# l = [56,24,21,11,6]

# l.sort()

# print("Smallest : ",l[0])
# print("Largest : ",l[-1])
# print("Second largest : ",l[-2])


l = [16,62,24,62,16,31]
uni = []
dup = []
for i in l:
    if i not in uni:
        uni.append(i)
    else:
        dup.append(i)
 
print(uni)
print(dup)