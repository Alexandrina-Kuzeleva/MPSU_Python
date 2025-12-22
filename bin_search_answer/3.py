a = int(input())
b = int(input())
c = int(input())

def check(x):
    total_pts = 2*a + 3*b + 4*c + 5*x
    total_cnt = a + b + c + x
    return total_pts * 2 >= 7 * total_cnt

left = 0
right = 2 * (a + b + c) + 1

while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1

print(left)