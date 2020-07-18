from math import sqrt

x = 600851475143    #заданное число
z = 2
res = []
while z*z <= x:    #поиск всех делителей заданного числа
    if x % z == 0:
        res.append(z)
        z += 1
    else:
        z += 1
print(res)

res1 = []
for i in res:    #из делителей ищем наибольший простой
    for j in range(3, i, 2):
        if i % 5 == 0:
            break  
        if j > int((sqrt(i)) + 1): 
            res1.append(i)
            break   
        if i % j == 0:  
            break
    else:
        res1.append(i)
print('ответ:', max(res1))