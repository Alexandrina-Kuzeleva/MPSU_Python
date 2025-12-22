n, k = map(int, input().split())
ropes = [int(input()) for _ in range(n)]

left = 0
right = 10**7 + 1

while left < right:
    mid = (left + right + 1) // 2
    total = 0
    for rope in ropes:
        total += rope // mid
    if total >= k:
        left = mid
    else:
        right = mid - 1

print(left)