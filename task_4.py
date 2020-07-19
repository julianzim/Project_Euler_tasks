a = maxi = 0
for x in range(100,1000) :
    for y in range(100,1000) :
        a = str(x*y) 
        if a == a[::-1] :
            if int(a) > int(maxi) :
                maxi = a
print(maxi)