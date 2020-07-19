def palindrome(x):
    a = ""
    x = str(x)
    for i in range(len(x), 0, -1):
        a += x[i-1]
#    print(a)
    if a == x:
        print(x, '- палиндром')

j = 99
while j > 10:
    m = j*j
    palindrome(m)
    j -= 1