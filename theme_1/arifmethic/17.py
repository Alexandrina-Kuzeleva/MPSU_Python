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

def is_hyperprime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

a, b = map(int, input().split())

result = []
for num in range(a, b + 1):
    if is_hyperprime(num):
        result.append(num)

if result:
    print(' '.join(map(str, result)))
else:
    print(0)