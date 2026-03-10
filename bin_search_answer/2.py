N = int(input())
K = int(input())
l, r = 1, 2 * 10**9
while l < r:
    mid = (l + r) // 2
    total = mid * (2 * K + mid - 1) // 2
    if total >= N:
        r = mid
    else:
        l = mid + 1
print(l)
