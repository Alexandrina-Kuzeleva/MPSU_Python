import sys
from math import gcd

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    m = int(data[1])
    
    if n == 1 or m == 1:
        print(max(n, m))
    else:
        print(gcd(n - 1, m - 1) + 1)
