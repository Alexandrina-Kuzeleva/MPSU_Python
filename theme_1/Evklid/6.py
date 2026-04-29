import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a, b, c, d = map(int, input().split())

dx = c - a
dy = d - b

if dx == 0 and dy == 0:
    result = 0
elif dx == 0:
    result = abs(dy) - 1 if b % 1 == 0 else abs(dy)
elif dy == 0:
    result = abs(dx) - 1 if a % 1 == 0 else abs(dx)
else:
    result = abs(dx) + abs(dy) - gcd(abs(dx), abs(dy))

result = max(0, result)

print(result)