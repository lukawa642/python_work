# 必备参数
def stu_form(name, age, major, phone):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


stu_form("lcx", 22, "shuxue", 15230623205)


# 关键字参数（与位置参数相似）
def stu_form(name, age, major, phone):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


stu_form(name="lcx", age=22, major="shuxue", phone=15230623205)  # 顺序可以改变


# 混用比较
def stu_form(name, age, major, phone):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


stu_form("lcx", age=22, major="shuxue", phone=15230623205)


# 默认参数
def stu_form(name, age, major, phone="1523062320589"):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


stu_form(name="lcx", age=22, major="shuxue")
stu_form(name="lcx", age=22, major="shuxue", phone=15230623205)


# 不定长参数  **args **kwargs
def stu_form(name, age, major, phone, *args, **kwargs):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)
    print("不定长列表参数：", args, kwargs)


stu_form("lcx", 22, "shuxue", 15230623205, "ss", homsda="saj")


# 不定参数妙用
def stu_form(name, age, major, phone):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


shuju = ("lcx", 22, "shuxue", 15230623205)
stu_form(*shuju)


# stu_form("lcx", 22, "shuxue", 15230623205,"ss",homsda="saj")

def stu_form(name, age, major, phone):
    info = f'''
    Name:{name},
    Age:{age},
    Major:{major},
    Phone:{phone}
    '''
    print(info)


SHUJU = {
    "name": "lcx",
    "age": 22,
    "major": "shuxue",
    "phone": 15230623205
}

stu_form(**SHUJU)
