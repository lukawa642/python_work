# # -*- coding:utf-8 -*-
#
# def bubbleSort(input_list):
# 	'''
# 	函数说明:冒泡排序（升序）
# 	Author:
# 		www.cuijiahua.com
# 	Parameters:
# 		input_list - 待排序列表
# 	Returns:
# 		sorted_list - 升序排序好的列表
# 	'''
# 	if len(input_list) == 0:
# 		return []
# 	sorted_list = input_list
# 	for i in range(len(sorted_list) - 1):
# 		print(f"第{i+1}次排序")
# 		for j in range(len(sorted_list) - 1):
# 			if sorted_list[j + 1] < sorted_list[j]:
# 				sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
# 			print(sorted_list)
# 	return sorted_list
#
# if __name__ == '__main__':
# 	input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
# 	print('排序前:', input_list)
# 	sorted_list = bubbleSort(input_list)
# 	print('排序后:', sorted_list)
def maopaoshuanfa(list):
    n=1
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j]> list[j+1]:
                list[j+1],list[j] = list[j],list[j+1]
                print(f'第{n}次排序')
                print(list)
                n=n+1

list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100,25,1,23,3,25,5]
maopaoshuanfa(list)






