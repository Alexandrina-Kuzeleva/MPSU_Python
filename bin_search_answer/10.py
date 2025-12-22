n = int(input())
a = [int(input()) for _ in range(n)]

left = 0
right = a[-1]

def can_achieve(max_time):
    remaining = 0
    for pancakes in a:
        if pancakes > max_time:
            remaining += pancakes - max_time
        else:
            remaining -= min(max_time - pancakes, remaining)
    return remaining <= 0

while left < right:
    mid = (left + right) // 2
    if can_achieve(mid):
        right = mid
    else:
        left = mid + 1

print(left)