def insertSort(input_list):
    if len(input_list)==0:
        return []
    sort_list=input_list
    for i in range(1,len(sort_list)):
        temp=sort_list[i]
        j=i-1
        while j>=0 and temp<sort_list[j]:
            sort_list[j+1]=sort_list[j]
            j-=1
            sort_list[j+1]=temp
    return sort_list
if __name__ == '__main__':
    input_list = [6, 4, 8, 9, 2, 3, 1]
    print(f"排序前：{input_list}")
    sort_list=insertSort(input_list)
    print("排序前：",sort_list)
