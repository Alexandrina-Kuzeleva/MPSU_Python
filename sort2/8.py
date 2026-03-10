n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

res = 1
for x in a:
    if x > res:
        break
    res += x

print(res)
