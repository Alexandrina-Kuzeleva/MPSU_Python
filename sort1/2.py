n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    max_index = i
    for j in range(i):
        if arr[j] > arr[max_index]:
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]

print(*arr)