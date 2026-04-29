import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    
    a, b = 0, 1
    c, d = 1, n
    
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        if a == 1 and b == 1:
            break
        if a != 0:
            sys.stdout.write(f"{a}/{b}\n")
