n, m = map(int, input().split())
cinema = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

result = 0
for i in range(n):
    row = cinema[i]
    cnt = 0
    for j in range(m):
        if row[j] == 0:
            cnt += 1
            if cnt == k:
                result = i + 1
                break
        else:
            cnt = 0
    if result:
        break

print(result)