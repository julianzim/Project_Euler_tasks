last = 0
now = 1
y = 0
while now < 4000000:
    sum = last + now
    x = now % 2
    if x == 0: 
        print('чётное число Фибоначчи:', now)
        y = y + now
        print('текущая сумма:', y)
    last = now
    now = sum
print('ОТВЕТ:', y)