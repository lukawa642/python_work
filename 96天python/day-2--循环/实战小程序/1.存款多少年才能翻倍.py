# for i in range(1000):
#     count =1*(1+0.0325)
#     if count >=2:
#         print(f"连本带息{i}年能翻倍")
#     exit()
#     自己做的
base=10000
interest=0.0325
year=0
while base<=20000:
    year +=1
    base =base*(1+interest)
    print(year,base)
else:
    print(f"经过{year}年盈利翻倍。")
    