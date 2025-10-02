n = int(input())
snow = [['.' for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == n // 2:
            snow[i][j] = '*'
        elif j == n // 2:
            snow[i][j] = '*'
        elif i == j:
            snow[i][j] = '*'
        elif i + j == n - 1:
            snow[i][j] = '*'

for row in snow:
    print(' '.join(row))