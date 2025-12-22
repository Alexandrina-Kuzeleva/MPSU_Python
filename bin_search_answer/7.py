n, a, b, w, h = map(int, input().split())

def can_fit(d):
    new_a = a + 2 * d
    new_b = b + 2 * d
    count1 = (w // new_a) * (h // new_b)
    count2 = (w // new_b) * (h // new_a)
    return max(count1, count2) >= n

left = 0
right = 10**18

while left < right:
    mid = (left + right + 1) // 2
    if can_fit(mid):
        left = mid
    else:
        right = mid - 1

print(left)