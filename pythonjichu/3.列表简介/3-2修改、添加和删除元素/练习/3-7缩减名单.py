#加入客人
jiabin=['Tom','Jack','James']
jiabin.insert(0,'tim')
jiabin.insert(2,'liu')
jiabin.append('wang')
print('我找到了一个更大的餐桌'+"我将邀请"+jiabin[0]+"、"+jiabin[1]+"、"+jiabin[2]+"、"+jiabin[3]+"、"+jiabin[-1]+"和"+jiabin[-2]+"参加聚餐。")
print("\n")
print(jiabin)
keren=jiabin.pop(0)
print(keren+",不好意思不能让你来参加聚餐了。")
keren=jiabin.pop(0)
print(keren+",不好意思不能让你来参加聚餐了。")
keren=jiabin.pop(0)
print(keren+",不好意思不能让你来参加聚餐了。")
keren=jiabin.pop(0)
print(keren+",不好意思不能让你来参加聚餐了。")
print(jiabin)
print(jiabin[0]+"，我将邀请你来聚餐！")
print(jiabin[1]+"，我将邀请你来聚餐！")
del jiabin[0]
del jiabin[0]
print(jiabin)