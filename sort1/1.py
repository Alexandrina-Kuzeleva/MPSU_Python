n = int(input())
arr = list(map(int, input().split()))

max_index = arr.index(max(arr))
arr[0], arr[max_index] = arr[max_index], arr[0]

print(*arr)