dictionary={'k0':0,'k1':1,'k2':2,'k3':3,'k4':4,'k5':5,'k6':6,'k7':7,'k8':8,'k9':9}
keys=dictionary.keys()
for i in keys:
    if dictionary[i]%2==0:
        dictionary[i] = -1
print(dictionary)