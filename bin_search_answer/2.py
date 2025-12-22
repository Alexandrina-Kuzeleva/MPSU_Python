n = int(input())
k = int(input())

left = 0
right = 2 * (10**9) + 1

def can_solve(days, n, k):
    if days <= k:
        return days * (days + 1) // 2 >= n
    else:
        extra = days - k
        total = k * (k + 1) // 2
        total += (k - 1 + k - extra) * extra // 2
        return total >= n

while left < right:
    mid = (left + right) // 2
    if can_solve(mid, n, k):
        right = mid
    else:
        left = mid + 1

print(left)