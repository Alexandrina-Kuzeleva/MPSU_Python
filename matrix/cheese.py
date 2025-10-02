n, m = map(int, input().split())
cheese = []
for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append('.')
        else:
            row.append('*')
    cheese.append(row)
for row in cheese:
    print(' '.join(row))