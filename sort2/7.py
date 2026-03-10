n = int(input())
a = list(map(int, input().split()))
m = int(input())
candies = set()
for _ in range(m):
    x, y = map(int, input().split())
    candies.add((x, y))
    candies.add((y, x))

for _ in range(n - 1):
    for i in range(n - 1):
        if a[i] > a[i + 1] and (a[i], a[i + 1]) not in candies:
            a[i], a[i + 1] = a[i + 1], a[i]

print(*a)
