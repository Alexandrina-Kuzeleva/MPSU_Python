n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

result = []
for i in range(n):
    j = i - k
    if 0 <= j < n:
        result.append(a[i][j])

print(*result)