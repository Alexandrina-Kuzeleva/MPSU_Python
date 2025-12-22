import sys

data = list(map(int, sys.stdin.read().split()))
ptr = 0

n = data[ptr]
ptr += 1
a = data[ptr:ptr+n]
ptr += n

m = data[ptr]
ptr += 1

INF = 10**18
maxp = 1000

best = [INF] * (maxp + 2)

for _ in range(m):
    b = data[ptr]
    c = data[ptr + 1]
    ptr += 2
    if c < best[b]:
        best[b] = c

for p in range(maxp - 1, 0, -1):
    if best[p + 1] < best[p]:
        best[p] = best[p + 1]

res = 0
for x in a:
    res += best[x]

print(res)
