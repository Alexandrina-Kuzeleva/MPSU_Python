n = int(input())
a = [int(input()) for _ in range(n)]
l, r = 0, max(a)
while l < r:
    mid = (l + r) // 2
    total_excess = sum(max(0, x - mid) for x in a)
    if total_excess <= mid:
        r = mid
    else:
        l = mid + 1
print(l)
