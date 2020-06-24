from math import sqrt
n =  60 #int(input("n="))
lst=[]
for i in range(3, n+1, 2):
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print(lst)