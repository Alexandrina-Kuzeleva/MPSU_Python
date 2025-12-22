n = int(input())
k = int(input())

left = 0
right = 2 * (10**9)

while left < right:
    mid = (left + right) // 2
    if (k + mid) * 3 >= n + mid:
        right = mid
    else:
        left = mid + 1

print(left)