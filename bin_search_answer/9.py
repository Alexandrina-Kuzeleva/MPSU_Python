def can_place_cows(stalls, k, distance):
    count = 1
    last_position = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]
            if count >= k:
                return True
    return False

n, k = map(int, input().split())
stalls = list(map(int, input().split()))

stalls.sort()
left = 0
right = stalls[-1] - stalls[0] + 1

while left < right:
    mid = (left + right) // 2
    if can_place_cows(stalls, k, mid):
        left = mid + 1
    else:
        right = mid

print(left - 1)