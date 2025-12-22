def find_closest(arr, x):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    if left == 0:
        return arr[0]
    
    if left == len(arr):
        return arr[-1]
    
    if abs(arr[left] - x) < abs(arr[left-1] - x):
        return arr[left]
    elif abs(arr[left] - x) > abs(arr[left-1] - x):
        return arr[left-1]
    else:
        return min(arr[left], arr[left-1])

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    print(find_closest(arr, q))