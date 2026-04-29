def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b, c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d

divisor = gcd(numerator, denominator)
m = numerator // divisor
n = denominator // divisor

print(m, n)