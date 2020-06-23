from math import sqrt
a = 1314953434
deviders = []
prime_dev = []
for k in range(1, a+1):
    if a % k == 0:
        deviders.append(k)
#print('Список делителей числа', a, ':', deviders)
for i in deviders:
    for j in range(2, i):
        if j > int((sqrt(i)) + 1):
            prime_dev.append(i)
            break
        if i % j == 0:
            break
    else:
        prime_dev.append(i)
#print('Из них простые:', prime_dev)
print('Наибольшее', prime_dev[-1])