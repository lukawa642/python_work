count_alpha=0
count_digit=0
count_space=0
count_special=0
while True:
    meg=input("请输入：").strip()
    if not meg:
         continue
    for i in meg:
        if i.isalpha():
            count_alpha+=1
        elif i.isdigit():
            count_digit+=1
        elif i.isspace():
            count_space+=1
        else:
            count_special+=1
    print(f"字母个数为{count_alpha},数字个数为{count_digit},空格个数为{count_space}，特殊符号个数为{count_special}")


