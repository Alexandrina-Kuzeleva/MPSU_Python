def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

a, b = map(int, input().split())

divisor = gcd(a, b)

c = a // divisor
d = b // divisor

print(c, d)