for i in range(2,101):# i=9
    is_prime_num = True
    for j in range(2,i) :#拿2-8之前所有数，跟9相除，如果能被9整除，代表9不是素数
        if i % j == 0 :
            is_prime_num = False
        #     break
        # # else:
        # #     print(i,"is prime num")
    if  is_prime_num == True:
        print(i,"是素数........")
