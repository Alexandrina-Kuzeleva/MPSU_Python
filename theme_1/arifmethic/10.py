N = int(input())

color = [0] * (N + 1)
max_color = 0

for i in range(2, N + 1):
    if color[i] == 0:
        max_color += 1
        for j in range(i, N + 1, i):
            color[j] = max_color

color[1] = 1
if max_color == 0:
    max_color = 1

print(max_color)
print(' '.join(map(str, color[1:])))