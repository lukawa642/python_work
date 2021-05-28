test_list=[4,6,6,4,2,2,4,8,5,8]
dict_list={}
for i in test_list:
    if i not in dict_list:
        dict_list[i]=[i,]
    else:
        dict_list[i].append(i)
print(dict_list)

