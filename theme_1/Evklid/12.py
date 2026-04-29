import sys
import math

data = sys.stdin.read().split()
if data:
    nums = map(int, data[1:])
    print(math.gcd(*nums))
