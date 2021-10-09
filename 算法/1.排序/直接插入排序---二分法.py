# import time
# start=time.perf_counter()
def BinarySearch(input_list, lend, value):
    left = 0
    right = lend - 1
    while left <= right:
        middle = left + (right - left) // 2
        if input_list[middle] > value:
            right = middle - 1
        else:
            left = middle + 1

    return left if left < lend else -1


def BinaryInsertSort(input_list):
    if len(input_list) == 0:
        return []
    result = input_list
    for i in range(1, len(input_list)):
        j = i - 1
        temp = result[i]
        insert_index = BinarySearch(result, i, result[i])
        if insert_index != -1:
            while j >= insert_index:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = temp
    return result
input_list = [6, 4, 8, 9, 2, 3, 1]
print('排序前:', input_list)
sorted_list = BinaryInsertSort(input_list)
print('排序后:', sorted_list)
# end=time.perf_counter()
# print("运行时间："，end-start)