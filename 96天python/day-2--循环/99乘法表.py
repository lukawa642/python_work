#99乘法表
for i in range(1,10):
    for j in range(1,i+1):#顾头不顾尾
        print(f"{j}x{i}={i*j}",end=" ")
    print()