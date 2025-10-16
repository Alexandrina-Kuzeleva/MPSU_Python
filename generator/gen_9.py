n = 5
m = [[min(i, n - 1 - j) for j in range(n)] for i in range(n)]
for row in m:
    print(row)