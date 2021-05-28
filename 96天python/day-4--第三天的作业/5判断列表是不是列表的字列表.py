li = [8, 3, 12, 1, 2, 34, 54, 12, 34, 11, 12, 14, 9, 1, 10, 15, 17, 18, 99, 1, 3, 5, 10]
li2 = [8,2, 12]
is_ziliebiao = True
for i in range(len(li2)):
    if li2[i] not in li:
        is_ziliebiao = False
if is_ziliebiao:
    print("是字列表")
else:
    print("不是字列表")

# 是字列表怎么处理？

