n, r, c = map(int, input().split())
heights = sorted([int(input()) for _ in range(n)])

def can_form_teams(max_inconvenience):
    count = 0
    i = 0
    while i + c - 1 < n:
        if heights[i + c - 1] - heights[i] <= max_inconvenience:
            count += 1
            i += c
        else:
            i += 1
    return count >= r

left, right = 0, heights[-1] - heights[0]
while left < right:
    mid = (left + right) // 2
    if can_form_teams(mid):
        right = mid
    else:
        left = mid + 1

print(left)