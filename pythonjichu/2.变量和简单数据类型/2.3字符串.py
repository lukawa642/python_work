#2.3.1 使用方法修改字符串大小写
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#2.3.2合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name =first_name+" "+last_name
print(full_name)
message="hello,"+full_name.title()+"!"
print(message)
#2.3.3 使用制表符或换行符来添加空白
print("python")
print("\tpython")#添加空白
print("languages\npython\nC\nJavaScript")
#2.3.4删除空白
favorite_lauguage="python "
favorite_lauguage.rstrip()#在终端使用
favorite_lauguage.lstrip()#去除左侧空白
favorite_lauguage.rstrip()#去除右侧空白
favorite_lauguage.strip()#去除两侧空白

