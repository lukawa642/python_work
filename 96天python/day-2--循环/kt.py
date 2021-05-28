for count in range(10):
    print("hello,I love this world and black girl.", count)
for name in ["lcx", "akkd", "dsa", "ajs", 'sad']:
    print(name)

    # 打印0-100的奇偶数
for i in range(100, 50, -1):
    print(i)
for i in range(100):
    if i % 2 == 0:
        print(i)
# 奇数
for i in range(100):
    if i % 2 != 0:
        print(i)
# 循环嵌套（一般不要超过4层）
for floor in range(1, 7):
    print(f"当前在{floor}层".center(50, '-'))
    for room in range(1, 10):
        print(f"当前房间是{floor}0{room}室")
# 三、break & continue
# 1、楼层打印进阶
for floor in range(1, 7):
    print(f"当前在{floor}层".center(50, '-'))
    if floor == 3:
        print("不走3层")
        continue  # 停止本次循环，进入下次计算
    for room in range(1, 10):
        print(f"当前房间是{floor}0{room}室")
# 怎么实现404停止
for floor in range(1, 7):
    print(f"当前在{floor}层".center(50, '-'))
    if floor == 3:
        print("不走3层")
        continue
    if floor == 4 and room==4:#不走404
        print("见鬼了。。。。。。。。。。。")
        break # 结束整个循环
    for room in range(1, 10):
        if floor == 4 and room == 4:  # 不走404
            print("见鬼了。。。。。。。。。。。")
            exit()            #全部退出
            # break  # 结束某个循环
        print(f"当前房间是{floor}0{room}室")
