sum = 0
a = 1
b = int(input('найти сумму до:'))
while a < b:
    x = a % 3
    y = a % 5
    if x == 0:
        print('добавляем', a)
        sum = sum + a
        print('сумма: ', sum)
    elif y == 0:
        print(a)
        sum = sum + a
        print('сумма: ', sum)
    a += 1