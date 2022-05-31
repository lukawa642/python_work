def cls(a, b):
    c = a + b
    return c



print(cls(10,20))

res = cls(b=10, a=20)  # =左侧的变量的名称称为  关键字参数根据a和b进行对应的传参数
print(res)

def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    arg2.append(202)
    print('arg1',arg1)
    print('arg2',arg2)
n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)
print('n1',n1)
print('n2',n2)

def fun(num):
    odd=[] #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

#函数的调用
lst=[10,29,34,23,44,53,55]
print(fun(lst))
def fun1():
    print('hello')
    #return
fun1()
def fun2():
    return 'hello'
res=fun2()
print(res)
def fun3():
    return 'hello','world'
uhu=fun3()
print(uhu)
