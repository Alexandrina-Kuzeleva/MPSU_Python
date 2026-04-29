import sys
import math

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    k = int(data[1])
    print((n * k) // math.gcd(n, k))
