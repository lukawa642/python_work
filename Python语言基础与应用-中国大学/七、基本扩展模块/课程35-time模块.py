"""
时间相关：time
〉 获取时间戳
〉 获取日期格式
〉 利用索引获取时间信息
〉 让程序睡一会
"""
# 获取时间戳
# time.time()方法
import time

t1 = time.time()
a = 0
n = 100000
for i in range(n):
    a += i
print(a)
t2 = time.time()
print(t2 - t1)

# 获取日期格式
# 获得当前的时间
print(time.asctime())
print(time.ctime())
# 将元组数据转化为日期
t = (2018, 8, 13, 11, 42, 32, 1, 0, 0)
print(time.asctime(t))

# 利用索引获取时间信息
# struct_time类
print(time.localtime())


# 索引获取时间信息
t=time.localtime()
year=t[0]
print(year)

# 让程序睡一会
# 让程序运行到某处便暂停几秒
# time.sleep()

for x in range(3):
    print(x)
    t1=time.time()
    time.sleep(10)
    t2=time.time()
    print(t2-t1)