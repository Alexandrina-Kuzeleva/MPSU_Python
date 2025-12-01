n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

for j in range(m):
    for i in range(n):
        print(a[i][j], end=' ')
    print()