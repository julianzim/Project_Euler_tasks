n = 60
lst = []
for i in range(2, n+1):
    lst.append(i)
print(lst)

sp = []

ii = 2
while ii <= n:
    if lst[ii] != 0:
        sp.append(lst[ii])
        for j in range(ii, n+1, ii):
            lst[j] = 0
    ii += 1
print(sp)