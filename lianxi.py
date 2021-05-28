# class student(object):
#     def speak(self):  ## 哪个对象调用了这个方法，self就是那个对象；可以把self理解为一个形参
#         print(f"{self.name} 说：我今年{self.age}岁" )
#
# # 类student 实例化一个对象john
# john = student()
# # 给对象添加属性
# john.name = "约翰"
# john.age = 19
# # 调用类中的 speak()方法
# john.speak()
#
class student(object):
    # 定义构造方法
    def __init__(self, n, a):  # __init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用；
        # 设置属性
        self.name = n
        self.age = a

    # 定义普通方法
    def speak(self):
        print("%s 说：我今年%s岁" % (self.name, self.age))


# 类student 实例化一个对象john
john = student("约翰", 19)

# 调用类中的 speak()方法
john.speak()
# >>>约翰 说：我今年19岁

