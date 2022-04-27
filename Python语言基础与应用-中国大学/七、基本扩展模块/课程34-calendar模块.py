"""calendar模块
   跟日历相关的若干函数和类，可以生成文本形式的日历
常用函数
calendar.calendar(<年>)
calendar.month(<年>,<月>)
calendar.prmonth(<年>,<月>)
calendar.prcal(<年>)
"""
# 制作电子日历：一个月
# calendar.month(<年>,<月>)
import calendar

print(calendar.month(2022, 1))
# 制作电子日历：一整年
# * calendar.calendar(<年>)
# 返回多行字符串
# * calendar.prcal(<年>)
# 相当于print (calendar.prcal (<年>))
print(calendar.calendar(2022))

# 将日历列表化
# calendar.monthcalendar()
# *返回某一年的某一个月份日历，是一个嵌套列表
# *最里层的列表含有七个元素，代表一周(从周一到周日) *如果没有本月的日期，则为0
import calendar

print(calendar.monthcalendar(2000, 2))
# 与日历相关的计算
# 判别闰年
# *普通闰年：能被4整除但不能被100整除的年
# *世纪闰年：能被400整除的年份
# calendar.isleap(<年>)
# 计算某月共有多少天，从周几开始
# * 从0开始，依次为周一、周二… 〉 计算某天是周几
# *返回值为0~6，依次对应的是周一到周日
print(calendar.isleap(2001))

print(calendar.monthrange(2022, 9))

print(calendar.weekday(2022,9,12))


