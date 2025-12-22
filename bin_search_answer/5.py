n, x, y = map(int, input().split())

if n == 1:
    print(min(x, y))
else:
    left = 0
    right = 2 * 10**9
    
    while left < right:
        mid = (left + right) // 2
        copies = mid // x + mid // y
        if copies >= n - 1:
            right = mid
        else:
            left = mid + 1
    
    print(left + min(x, y))