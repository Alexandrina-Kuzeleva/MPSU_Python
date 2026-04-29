def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

x1, y1, x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1

if dx == 0 and dy == 0:
    result = 1
else:
    result = gcd(abs(dx), abs(dy)) + 1

print(result)