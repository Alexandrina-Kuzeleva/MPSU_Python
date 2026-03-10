n = int(input())

factors = {}
d = 2
while d * d <= n:
    while n % d == 0:
        factors[d] = factors.get(d, 0) + 1
        n //= d
    d += 1 if d == 2 else 2
if n > 1:
    factors[n] = factors.get(n, 0) + 1

parts = []
for p in sorted(factors.keys()):
    if factors[p] == 1:
        parts.append(str(p))
    else:
        parts.append(f"{p}^{factors[p]}")

print('*'.join(parts))