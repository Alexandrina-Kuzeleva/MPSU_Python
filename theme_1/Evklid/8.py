def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())

if n % 2 == 0:
    a = n // 2 - 1 
else:
    a = n // 2 

while a > 0:
    b = n - a
    if gcd(a, b) == 1:
        print(a, b)
    a -= 1

