import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    
    p = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            break
            
    if p == 1:
        print(1, n - 1)
    else:
        d = n // p
        print(d, n - d)
