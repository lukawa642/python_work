#maketrans   加密
#translate   解密
origin="1234567890"
incloud="0123456789"
code=str.maketrans(origin,incloud)
bianma="2564782"
jiemi=bianma.translate(code)
print(jiemi)
code2=str.maketrans(incloud,origin)
neirong=jiemi.translate(code2)
print(neirong)