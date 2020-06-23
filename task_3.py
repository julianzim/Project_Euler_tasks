a = 13195
deviders = []
prime_dev = []
for k in range(1, a+1):
    if a % k == 0:
        deviders.append(k)
#print('Список делителей числа', a, ':', deviders)
for i in deviders:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_dev.append(i)
#print('Из них простые:', prime_dev)
print('Наибольшее', prime_dev[-1])