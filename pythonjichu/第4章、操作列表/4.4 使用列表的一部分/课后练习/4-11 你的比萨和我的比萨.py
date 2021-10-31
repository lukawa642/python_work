my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
friend_foods = my_foods[:]
friend_foods.append("sda")
my_foods.append("sadadasd")
print(friend_foods)
print(my_foods)
for i in my_foods:
    print("My favorite pizzas are:"+i)
for i in friend_foods:
    print("My friend's favorite pizzas are:" + i)