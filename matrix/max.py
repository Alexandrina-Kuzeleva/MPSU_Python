n, m = map(int, input().split())
best_val = -10**18
best_i = -1
best_j = -1

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] > best_val:
            best_val = row[j]
            best_i = i
            best_j = j

print(best_i, best_j)