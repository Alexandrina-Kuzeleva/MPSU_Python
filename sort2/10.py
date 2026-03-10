n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

flat = []
for i in range(n):
    for j in range(m):
        flat.append((a[i][j], i, j))

flat_sorted = sorted(flat, key=lambda x: x[0])
pos = {}
for idx, (val, i, j) in enumerate(flat_sorted):
    pos[val] = (idx // m, idx % m)

current = {}
for i in range(n):
    for j in range(m):
        current[a[i][j]] = (i, j)

swaps = []

for val in range(1, n*m + 1):
    ci, cj = current[val]
    ti, tj = pos[val]
    while (ci, cj) != (ti, tj):
        other_val = a[ti][tj]
        a[ci][cj], a[ti][tj] = a[ti][tj], a[ci][cj]
        swaps.append((ci+1, cj+1, ti+1, tj+1))
        current[val] = (ti, tj)
        current[other_val] = (ci, cj)
        ci, cj = current[val]

print(len(swaps))
for x1, y1, x2, y2 in swaps:
    print(x1, y1, x2, y2)
