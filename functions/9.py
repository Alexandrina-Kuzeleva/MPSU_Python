def f(n, k=2):
    if n == 0 or n == 1:
        return n
    if k == 1:
        return n
    
    res = n + 1
    for x in range(1, n + 1):
        broken = f(x - 1, k - 1)
        not_broken = f(n - x, k)
        res = min(res, 1 + max(broken, not_broken))
    return res

n = int(input())
print(f(n))