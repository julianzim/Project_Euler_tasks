from math import sqrt   
a = 60#0851475143
prime_dev = []
for k in range(3, a+1, 2):
    if a % k == 0:   
        if (k > 10) and (k % 10 == 5): 
            continue   
        for j in range(2, k):       
            if k % j == 0:   
                break
            if j > int((sqrt(k)) + 1):   
                prime_dev.append(k)   
                break
        else:
            prime_dev.append(k)   
print('Простые делители:', prime_dev)
print('Наибольший', prime_dev[-1])