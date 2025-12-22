import sys

def gen_seq(x1, d1, a, c, m, L):
    x = x1
    d = d1
    for _ in range(L):
        yield x
        nd = (a * d + c) % m
        x += d
        d = nd

def left_median(p, q, L):
    a = next(p)
    b = next(q)
    cnt = 0
    last = 0

    while cnt < L:
        if a <= b:
            last = a
            cnt += 1
            a = next(p, 10**20)
        else:
            last = b
            cnt += 1
            b = next(q, 10**20)

    return last

data = list(map(int, sys.stdin.read().split()))
it = iter(data)

N = next(it)
L = next(it)

params = []
for _ in range(N):
    params.append((next(it), next(it), next(it), next(it), next(it)))

out = []

for i in range(N):
    for j in range(i + 1, N):
        p = gen_seq(*params[i], L)
        q = gen_seq(*params[j], L)
        out.append(str(left_median(p, q, L)))

print("\n".join(out))
