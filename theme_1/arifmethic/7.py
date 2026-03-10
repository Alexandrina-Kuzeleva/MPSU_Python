import math

K = int(input())

if K <= 6:
    limit = 15
else:
    logK = math.log(K)
    limit = int(K * (logK + math.log(logK))) + 100000

is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

p = 2
while p * p <= limit:
    if is_prime[p]:
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False
    p += 1

primes = []
for i in range(2, limit + 1):
    if is_prime[i]:
        primes.append(i)
        if len(primes) == K:
            print(i)
            break