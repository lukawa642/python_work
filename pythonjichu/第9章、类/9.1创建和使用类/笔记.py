class Dog:
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name=name
        self.age=age
    def sit(self):
        """初始化属性name和age"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
