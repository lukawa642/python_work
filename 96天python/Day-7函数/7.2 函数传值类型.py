def charge_date(name,hobbies):#定义函数
    name="liuchongxun"#修改只在函数中生效
    hobbies.append("大保健")#在函数中添加列表
    hobbies[1]="xiaoyun"
    print("in func:",name,hobbies)#输入函数中的返回值

my_name="guoshuai"#不可变类型
my_hobbies=["money","beibei"]#可变类型

charge_date(my_name,my_hobbies)
print(my_name,my_hobbies)
