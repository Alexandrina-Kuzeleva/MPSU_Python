A, K, B, M, X = map(int, input().split())

left = 0
right = 2 * (10**18)

while left < right:
    days = (left + right) // 2
    work_days_d = days - days // K
    work_days_f = days - days // M
    trees = A * work_days_d + B * work_days_f
    if trees >= X:
        right = days
    else:
        left = days + 1

print(left)