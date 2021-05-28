#  初级程序---需要优化
red_balls=[]
blue_balls=[]


count=0
while count < 6:
    chioce = eval(input(f"第{count+1}个红球："))
    if 0 < chioce <33 and chioce not in red_balls:
        red_balls.append(chioce)
        count+=1
count = 0
while count < 1:
    chioce = eval(input(f"第{count + 1}个蓝球："))
    if 0 < chioce < 16and chioce not in blue_balls:
        blue_balls.append(chioce)
        count += 1
print(red_balls,blue_balls)


# 进阶程序

red_balls=[]
blue_balls=[]

li=[[6,33,"红球",red_balls],[1,16,"蓝球",blue_balls]]

for item in li:
    count = 0
    print(f"开始输入{item[2]}的数字：".center(50,"-"))
    while count < item[0]:
        chioce = eval(input(f"第{count + 1}个{item[2]}："))
        if item[0] < chioce < item[1] and chioce not in item[3]:
            item[3].append(chioce)
            count += 1
else:
    print(red_balls,blue_balls)