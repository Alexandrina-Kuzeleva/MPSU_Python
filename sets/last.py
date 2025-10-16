n, *nums = map(int, open(0).read().split())

arr = []
res = []

for x in nums:
    i = 0
    while i < len(arr) and arr[i] < x:
        i += 1
    arr.insert(i, x)
    mid = (len(arr) + 1) // 2 - 1
    res.append(arr[mid])

print(*res)
