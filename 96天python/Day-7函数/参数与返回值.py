# 形参实参
def say_hi(name):
    print(f"hello,{name},nihao!")
say_hi("lcx")
print(say_hi("lcx"))


# 返回值
"""
特点
默认值是NONE
可以返回多个值
返回值类型可以多样
"""
def mobile_check(phone_num):
    if len(phone_num)==11:
        if phone_num.isdigit():
            if phone_num.startswith('1'):
                return True
s="23530623205"
if mobile_check(s):
    print(f"{s}是合法手机号。。。")