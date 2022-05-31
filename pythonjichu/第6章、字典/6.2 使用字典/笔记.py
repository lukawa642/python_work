# 6.2.1 访问字典中的值

alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])

new_point = alien_0['point']
print(new_point)
print("You just earned " + str(new_point) + " points!")

print()

# 6.2.2 添加键-值对
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print()
print(alien_0)

# 6.2.3 先创建一个空字典
print()
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

# 6.2.4 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

print()
alien_0 = {'x_position': 0, 'y_position': 25}
alien_0['speed'] = 'medium'
print("Orginal x-position: " + str(alien_0['x_position']))
# 向右移动外星人，根据外星人的速度决定其移动多远
if alien_0['speed'] == 'slow':
    alien_0['x_position'] = alien_0['x_position'] + 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] = alien_0['x_position'] + 2
else:
    alien_0['x_position'] = alien_0['x_position'] + 3
print("New  x-position: " + str(alien_0['x_position']))

# 6.2.5 删除键-值对
alien_0 = {'x_position': 0, 'y_position': 25}
del alien_0[ 'y_position']
print(alien_0)#'''删除是永久删除'''

print("# 6.2.6 由类似对象组成的字典")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " +favorite_languages['sarah'].title() +  ".")
print("Phil's favorite language is " +favorite_languages['phil'].title() +  ".")
