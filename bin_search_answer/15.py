def count_numbers_up_to(x, k):
    count = 0
    power = k
    while power <= x:
        count += x // power
        power *= k * k
    return count

n, k = map(int, input().split())

left = 0
right = 10**18

while left < right:
    mid = (left + right) // 2
    if count_numbers_up_to(mid, k) >= n:
        right = mid
    else:
        left = mid + 1

print(left)