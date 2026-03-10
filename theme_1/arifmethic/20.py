def factorize(k):
    factors = {}
    d = 2
    while d * d <= k:
        while k % d == 0:
            factors[d] = factors.get(d, 0) + 1
            k //= d
        d += 1 if d == 2 else 2
    if k > 1:
        factors[k] = factors.get(k, 0) + 1
    return factors

N, K = map(int, input().split())

factors = factorize(K)

min_zeros = float('inf')
for p, a in factors.items():
    power = 0
    pp = p
    while pp <= N:
        power += N // pp
        pp *= p
    zeros = power // a
    if zeros < min_zeros:
        min_zeros = zeros

print(min_zeros)