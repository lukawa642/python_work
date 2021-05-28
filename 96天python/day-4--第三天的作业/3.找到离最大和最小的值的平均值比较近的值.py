li = [8, 3, 12, 1, 2, 34, 54, 12, 34, 11, 12, 14, 9, 1, 10, 15, 17, 18, 99, 1, 3, 5, 10]


max_n=li[0]
min_n=li[1]
for i in li:
    if min_n > i:min_n = i
    if max_n < i:max_n = i
    # if min_n > i:
    #     min_n = i
    # elif max_n < i:
avg=(max_n+min_n)/2
print(max_n,min_n,avg)
close_n=li[0]
for i in li:
    if abs(i - avg) < abs(close_n-avg):
        close_n=i
print(close_n)