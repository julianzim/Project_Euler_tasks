last = 0
now = 1
while now < 4000000:
    sum = last + now
    x = now % 2
    if x == 0: 
        print(now)
    last = now
    now = sum