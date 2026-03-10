n = int(input())

if n == 2:
    print("prime")
elif n % 2 == 0:
    print("composite")
else:
    is_prime = True
    d = 3
    while d * d <= n:
        if n % d == 0:
            is_prime = False
            break
        d += 2
    print("prime" if is_prime else "composite")