import sys

data = list(map(int, sys.stdin.read().split()))
N, W = data[0], data[1]
L, R = data[2], data[3]
posts = data[4:]

points = [(L, -1)]
for i, x in enumerate(posts):
    points.append((x, i))
points.append((R, -1))

points.sort(key=lambda x: x[0])

best = None
best_pair = None

j = 0
for i in range(len(points)):
    while j < len(points) and points[j][0] - points[i][0] < W:
        j += 1
    if j == len(points):
        break
    removed = j - i - 1
    if best is None or removed < best:
        best = removed
        best_pair = (i, j)

if best is None:
    print(-1)
    sys.exit()

print(best)
if best > 0:
    i, j = best_pair
    res = []
    for k in range(i + 1, j):
        idx = points[k][1]
        if idx != -1:
            res.append(idx + 1)
    print("\n".join(map(str, res)))
