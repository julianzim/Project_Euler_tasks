spis = []
for i in range(2, 101):
    for j in spis:
        if i % j == 0:
            break
    else:
        spis.append(i)
print(spis)