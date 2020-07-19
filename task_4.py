def palindrome(x):
    a = ""
    x = str(x)
    for i in range(len(x), 0, -1):
        a += x[i-1]
    if a == x:
        x = int(x)
        lst.append(x)

lst = []
for j in range(999, 100, -1):
    k = 999
    while k > 100:
        m = j*k
        palindrome(m)
        k -= 1
    j -= 1
print(max(lst))