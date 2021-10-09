li = [8, 3, 12, 1, 2, 34, 54, 12, 34, 11, 12, 14, 9, 1, 10, 15, 17, 18, 99, 1, 3, 5, 10]
#用冒泡法进行排序
for n in range(len(li)）:
    for insert in range(len(li)-1):
        i = li[insert]
        if li[insert]>li[insert+1]:
            li[insert]=li[insert+1]
            li[insert+1]=i
    print(li)
print(f"列表中第二大的值是：{li[-2]}")
