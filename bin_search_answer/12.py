m, n = map(int, input().split())
a = list(enumerate(map(int, input().split()), 1))
b = list(enumerate(map(int, input().split()), 1))
a.sort(key=lambda x: x[1])
b.sort(key=lambda x: x[1])
res = []
i = j = 0
used = set()
while i < m:
    while j + 1 < n and b[j+1][1] <= a[i][1]:
        j += 1
    if j + 1 < n:
        e1 = b[j][0] if b[j][0] not in used else b[j+1][0]
        e2 = b[j+1][0] if b[j+1][0] not in used else b[j][0]
        if e1 not in used and e2 not in used:
            used.add(e1)
            used.add(e2)
            res.append((a[i][0], e1, e2))
            i += 1
        else:
            j += 1
    else:
        break
print(len(res))
for x in res:
    print(*x)
