import sys

data = list(map(int, sys.stdin.read().split()))
p = 0

N = data[p]
p += 1
a = data[p:p+N]
p += N

M = data[p]
p += 1
queries = data[p:p+M]

def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m + 1
        else:
            r = m
    return l

out = []
for q in queries:
    l = lower_bound(a, q)
    r = upper_bound(a, q) - 1
    if l <= r:
        out.append(f"{l+1} {r+1}")
    else:
        out.append("0 0")

print("\n".join(out))
