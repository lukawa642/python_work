dic = {'gfg':[5,6,7,8],'sda':[5,4,1,78],'gsdsafg':[12,26,57,38],'asdfg':[45,62,17,38]}
key = dic.keys()
print(key)
values=[]
for i in key:
    # print(i,dic[i])
    n=dic[i]
    for j in range(len(n)):
        print(n[j])
        if n[j] not in values:
            values.append(n[j])
print(values)


for u in range(len(values)):
    for g in range(len(values)-1):
        f = values[g]
        if values[g] > values[g+1]:
            values[g]=values[g+1]
            values[g+1]=f
print(values)


#         if key[i][j] not in values:
#             value.append(key[i][j])
