shuzi = []
for i in range(1,11):
    shuzi.append(i)
print(shuzi)
for i in shuzi:
    print(i)
for i in shuzi:
    if i < 2:
        print(str(i)+"st")
    elif i < 3:
        print(str(i) + "nd")
    elif i < 4:
        print(str(i) + "rd")
    else:
        print(f"{i}"+"th")

