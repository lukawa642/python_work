#修改元素
motorcycles=["honna","yamaha","suzuki"]
print(motorcycles)

motorcycles[1]="hahaha"
print(motorcycles)
print('\n')
#添加元素
motorcycles=["honna","yamaha","suzuki"]
print(motorcycles)
motorcycles.append("hahaha")
print(motorcycles)
motorcycles=[]
motorcycles.append('honna')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#在任何位置插入元素
motorcycles.insert(0,'hahahha')
print(motorcycles)
print('\n')
#从列表中删除元素
motorcycles=["honna","yamaha","suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)#删除比较彻底
print('\n')
# 使用pop()的方法进行删除
motorcycles=["honna","yamaha","suzuki"]
print(motorcycles)
poped_motorcycles=motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)
print('\n')
#4 根据值删除
motorcycles=["honna","yamaha","suzuki"]
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
print('\n')
motorcycles=["honna","yamaha","suzuki"]
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA\t'+too_expensive.title()+"\tis too expensive for me.")


