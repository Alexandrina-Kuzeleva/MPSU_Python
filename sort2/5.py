n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
pos = {v: i for i, v in enumerate(b)}
visited = [False] * n
res = 0
global_min = min(a)

for i in range(n):
    if visited[i] or b[i] == a[i]:
        visited[i] = True
        continue
    cycle_sum = 0
    cycle_min = float('inf')
    count = 0
    j = i
    while not visited[j]:
        visited[j] = True
        val = a[j]
        cycle_min = min(cycle_min, val)
        cycle_sum += val
        j = pos[val]
        count += 1
    if count > 1:
        cost1 = cycle_sum + (count - 2) * cycle_min
        cost2 = cycle_sum + cycle_min + (count + 1) * global_min
        res += min(cost1, cost2)

print(res)
