import random
import  string
names = ["liuchongxun","guoshuaishuai","black_gril","peiqi"]
f=open("mima","w")
password=string.punctuation+string.digits+string.printable
for i in names:
    passwd="".join(random.sample(password,5))
    f.write(f"{i}:={passwd}\n")
f.close()