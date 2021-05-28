
#while 循环 day2 的内容
count = 0
black_girl_age = 25
while count < 3:
    guess = input("猜黑姑娘的年龄>:")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("不识别指令，请重新输入新的数值.....")
        continue
    if guess > black_girl_age:
        print("猜大了，往小了猜....")
    elif guess < black_girl_age:
        print("猜小了，往大了猜.......")
    else:
        print("恭喜你，猜对了")
        break
    count +=1
    if count == 3:
        cmd = input("还要不要试一把.........（Y/N）")
        if cmd in ["Y","y","yes"]:
            count=0
        else:
            print("byebye..............")




