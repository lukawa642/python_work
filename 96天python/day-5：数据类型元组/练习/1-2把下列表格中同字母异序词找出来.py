arr=['cat','dog','tac','god','act']
dicts= {}
for i in arr:
    to_key=list(i)
    to_key.sort()
    to_key=tuple(to_key)
    if to_key not in dicts:
        dicts[to_key] = [ i ]
    else:
        dicts[to_key].append(i)
print(dicts)

print(tuple(dicts.values()))