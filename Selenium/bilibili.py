llg = {}
hyz = [1,2,1,2,1,2]

for i in hyz:
    if i not in llg:
        llg[i] = 1
    else:
        llg[i] += 1
print(llg)