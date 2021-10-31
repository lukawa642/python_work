# 4.4.1 切片
# plays.py
players = ['charles','martina','michael','florence','eli']
print(players[0:3:1])
players = ['charles','martina','michael','florence','eli']
print(players[:4])
players = ['charles','martina','michael','florence','eli']
print(players[2:4])
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']



friend_pizzas = my_foods[:]
my_foods.append('cheese')  # 4-11-1
friend_pizzas.append('seafood')  # 4-11-2
for i in my_foods:
	print("My favorite pizzas are: " + i)
for i in friend_pizzas:
	print("My friend’s favorite pizzas are: " + i)
