"""
主要的类
datetime.date() 处理日期（年月日）
datetime.time() 处理时间（时分秒、毫秒）
datetime.datetime() 处理时间+日期
datetime.timedelta() 处理时段（时间间隔）
"""
"""
import datetime
>>>获取今天的时间
datetime.date.today()
datetime.datetime.now()
>>>修改日期格式
使用strftime格式化
datetime.datetime.isoformat()
"""

import datetime

TodayTime = datetime.date.today()
NowTime = datetime.datetime.now()
print(TodayTime)
print(NowTime)

TodayTime = datetime.date.today().isoformat()
NowTime = datetime.datetime.now().strftime("%m-%Y-%d %H:%M:%S")
print(TodayTime)
print(NowTime)

"""
时间戳
时间戳是指格林威治时间1970年01月01日00时00分00秒起至现在的总秒数
将日期转换为时间戳
*timetuple函数
将时间转换成struct_time格式
time.mktime函数
返回用秒数来表示时间的浮点数
"""
import time,datetime
today= datetime.date.today()
print(today.timetuple())
print(time.mktime(today.timetuple()))
"""将时间戳转换为日期"""
d=time.mktime(today.timetuple())
print(datetime.date.fromtimestamp(d))

"""
timedelta()方法
表示两个时间点的间隔
"""
import datetime
today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=2)
print(yesterday)
hours=today-datetime.timedelta(hours=1)
print(hours)

