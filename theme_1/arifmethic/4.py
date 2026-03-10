x = int(input())

count = 1
d = 2
while d * d <= x:
    power = 0
    while x % d == 0:
        x //= d
        power += 1
    if power > 0:
        count *= (power + 1)
    d += 1 if d == 2 else 2

if x > 1:
    count *= 2

print(count)