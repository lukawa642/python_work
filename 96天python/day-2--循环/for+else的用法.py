for i in range(2,101):# i=9
    for j in range(2,i):#拿2-8之前所有数，跟9相除，如果能被9整除，代表9不是素数
        if i % j == 0 :
         break
    else:
        print(i,"是素数........")
