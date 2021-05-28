juzi="Python is great and Java is also great"
l=[]
for i in juzi.split(" "):
    print(juzi.split(" "))
    if i not in l:
        l.append(i)
result=" ".join(l)
print(result)
# l = []
# s = "hello world hello python"
# for i in s.split(" "):
#     if i not in l:
#         l.append(i)
#
# result = " ".join(l)
# print(result)