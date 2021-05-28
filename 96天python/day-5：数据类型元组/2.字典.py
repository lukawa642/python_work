#什么是dictionary 类型
staff_list=(['alex',23,"CEO",66000],["黑姑娘",24,"行政",4000],["佩奇",26,"讲师",40000])
print(staff_list)

for i in staff_list:
    if i[0] == "黑姑娘":
        print(i)
        break
staff_list={
    'alex':[23,"CEO",66000],
    "黑姑娘":[24,"行政",4000],
    "佩奇":[26,"讲师",40000]
}
print(staff_list)
#定义 dictionary
info = {
    "name":"Alex Li",
    "age": 26,
    "s":"Jacke"
}
print(info)
#dict 用法
#创建
#定义1
into=dict(name=[1,2,3],age=[23,25,45])
into["jobs"]=["教师"]
into.setdefault("hsid","sahjd")
print(into)
into.pop("jobs")
print(into)
into.setdefault("name","jsdak")
print(into)
print(into["name"])
into["name"][0]=20
print(into)
#合并修改
staff_list.update(into)
print(staff_list)
for k in into:
    staff_list[k]=into[k]
print(staff_list)
print(staff_list.get("mame"))
print(staff_list.get("name"))
print(staff_list["name"])
print("name" in staff_list)



print(staff_list.keys())
print(staff_list.values())
print(staff_list.items())
print(staff_list.pop("alex"))

print(staff_list)

print(into.popitem())
print(into)
for i in staff_list:
    print(i,staff_list[i])
    dict.fromkeys
    staff_list.copy()
