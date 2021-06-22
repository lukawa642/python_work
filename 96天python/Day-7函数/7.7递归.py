
# n = 100
# while n > 0:
#     n=int(n/2)
#     print(n)
#自己调用自己
def func(n):
    n=int(n/2)
    print(n)
    if n>0:
        func(n)#调用自己
    print(n)
    return n

res=func(5)
print(res)

