n, m = map(int, input().split())
max_value = None
max_i = -1
max_j = -1

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if max_value is None or row[j] > max_value:
            max_value = row[j]
            max_i = i
            max_j = j
        elif row[j] == max_value:
            if i < max_i:
                max_i = i
                max_j = j
            elif i == max_i and j < max_j:
                max_j = j

print(max_i + 1, max_j + 1)