N = int(input())

sieve = [0] * (N + 1)
primes = []

for i in range(2, N + 1):
    if sieve[i] == 0:
        primes.append(i)
        for j in range(i * i, N + 1, i):
            if sieve[j] == 0:
                sieve[j] = i

result = []
for i in range(2, N + 1):
    n = i
    cnt = 0
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            cnt += 1
            while n % p == 0:
                n //= p
    if n > 1:
        cnt += 1
    if cnt >= 3:
        result.append(i)

print(' '.join(map(str, result)))