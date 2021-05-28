




li = [8, 3, 12, 1, 2, 34, 54, 12, 34, 11, 12, 14, 9, 1, 10, 15, 17, 18, 99, 1, 3, 5, 10]
duplicate_nums = []
for i in li:
    i_show_count=li.count(i)
    if i_show_count>1 and [i,i_show_count ] not in duplicate_nums:
        duplicate_nums.append([i,i_show_count])
print(duplicate_nums)

for item in duplicate_nums:
    duplicate_n,duplicate_time=item
    for j in range(duplicate_time-1):
        li.remove(duplicate_n)
    print(f"对{duplicate_n}删除了{duplicate_time-1}次")
print(li)

