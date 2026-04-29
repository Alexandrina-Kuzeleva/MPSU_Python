import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def count_integer_points_on_segment(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1
    return gcd(dx, dy) + 1

data = sys.stdin.read().strip().split()
n = int(data[0])

points = []
for i in range(n):
    x = int(data[2*i + 1])
    y = int(data[2*i + 2])
    points.append((x, y))

total_points = 0

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    
    total_points += count_integer_points_on_segment(x1, y1, x2, y2) - 1

print(total_points)
