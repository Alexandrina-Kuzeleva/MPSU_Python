n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for ш in range(n)]
row_min = [min(row) for row in matrix]
col_max = [max(matrix[i][j] for i in range(n)) for j in range(m)]
count = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
            count += 1
print(count)