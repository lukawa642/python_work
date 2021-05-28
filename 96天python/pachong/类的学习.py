# 例子1

# class Ticket:
#     def __init__(self, checi, fstation, tstation, fdate, ftime, ttime):
#         self.checi = checi
#         self.fstation = fstation
#         self.tstation = tstation
#         self.fdate = fdate
#         self.ftime = ftime
#         self.ttime = ttime
#
#     def printinfo(self):
#         print("车次：", self.checi)
#         print("出发站：", self.fstation)
#         print("到达站：", self.tstation)
#         print(''"出发时间：", self.fdate, self.ftime)
#         print("到达时间：", self.fdate, self.ttime)
#
#
# # 创建a1对象
# a1 = Ticket("G11", "xian", "beijing", '2019-01-20', '13:00', '18:00')
# # 创建a2对象
# a2 = Ticket("T11", "xian", "beijing", '2019-01-21', '13:00', '19:00')
# a1.printinfo()
# a2.printinfo()
# 例子2
import requests
class Station():
    #__init__()方法是一种特殊的方法，被称为类的初始化方法，当创建这个类的实例时就会调用该方法
    # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    def __init__(self,code,cn,qp,jp):
        self.code=code
        self.cn=cn
        self.qp=qp
        self.jp=jp
    #类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
    def printinfo(self):
        print(self.code,self.cn,self.jp,self.qp)
    #self代表类的实例,表示当前对象的地址  self.__class__ 则指向类
    def test(self):
        print(self)
        print(self.__class__)
url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9077"
#url='https://kyfw.lesson10_1.cn/otn/resources/js/framework/station_name.js?station_version=1.9090'
html_text=requests.get(url).text
infos=html_text[:-2].split("@")[1:]
stations=[]

for info in infos:
    station_list=info.split("|")
    #直接将类的对象添加到列表中，通过__init__()方法接受参数
    stations.append(Station(station_list[2],station_list[1],station_list[3],station_list[4]))
#遍历列表，每个元素为类的一个对象
for i in stations[:10]:
    i.printinfo()
    i.test()
# 例子3
