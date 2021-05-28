height=100
distance=0
# for i in range(1,11):
#     distance=distance+height*0.5**(i-1)+height*0.5**i
#     print(i,distance,)
count=0
while count <10:
    distance+=height
    height=height/2
    distance+=height
    count +=1
    print(count,distance,height)
