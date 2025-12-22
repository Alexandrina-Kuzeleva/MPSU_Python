import sys

data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
arr = data[2:]

from collections import Counter

cnt = Counter(arr)
vals = sorted(cnt)
f = [cnt[v] for v in vals]
m = len(vals)

pref_f = [0]*(m+1)
pref_f2 = [0]*(m+1)
pref_c2 = [0]*(m+1)

for i in range(m):
    pref_f[i+1] = pref_f[i] + f[i]
    pref_f2[i+1] = pref_f2[i] + f[i]*f[i]
    pref_c2[i+1] = pref_c2[i] + f[i]*(f[i]-1)//2

res = 0
r = 0

for i in range(m):
    while r < m and vals[r] <= vals[i]*k:
        r += 1

    fi = f[i]

    if fi >= 3:
        res += 1

    if fi >= 2:
        s1 = pref_f[r] - pref_f[i+1]
        res += 3 * s1

    s2 = pref_c2[r] - pref_c2[i+1]
    res += 3 * s2

    s1 = pref_f[r] - pref_f[i+1]
    s1_sq = pref_f2[r] - pref_f2[i+1]
    pairs = (s1*s1 - s1_sq) // 2
    res += 6 * pairs

print(res)
