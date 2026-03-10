def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True

n = int(input())

for a in range(2, n // 2 + 1):
    b = n - a
    if is_prime(a) and is_prime(b):
        print(a, b)
        break