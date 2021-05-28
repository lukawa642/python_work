#最大值的求法
list_shuzi=[100,2,3,4,5,8,9,45,24,14]
max_shuzi=list_shuzi[0]
for i in range(10):
    if list_shuzi[i] >max_shuzi:
        max_shuzi=list_shuzi[i]
else:
    print(f"列表中最大值是{max_shuzi}")
#最小值的求法
list_shuzi=[100,2,3,4,5,8,9,45,24,14]
min_shuzi=list_shuzi[0]
for i in list_shuzi:
    if i <min_shuzi:
        min_shuzi=i
else:
    print(f"列表中最小值是{min_shuzi}")