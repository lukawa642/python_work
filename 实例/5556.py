student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# get方法可以使得在字典中缺少要查询的值时显示出默认或自定义的结果，而不是抛出异常
# 括号内第二个参数为自定义默认输出内容
print(student.get('name'))
print(student.get('phone', 'Sorry. Not Found~'))


# ------------------------
# 添加
student['phone'] = '199-8011-8011'
# 更新
student['name'] = 'Jane'

print(student)


# ------------------------
# 使用update可以一次更新多个值！！！
student.update({'name': 'Silk', 'age': 100, 'phone': '188-0525-7633'})

print(student)


# ------------------------
# 删除 方法一：使用del
del student['age']
# 删除 方法二：使用pop
# pop会删除该值，但也会同时返回删除的值，需用变量来接收
age = student.pop('age')
print(student)
print(age)


# ------------------------
# 查看长度
print(len(student))
# 查看键
print(student.keys())
# 查看值
print(student.values())
# 成对展现键与值
print(student.items())
