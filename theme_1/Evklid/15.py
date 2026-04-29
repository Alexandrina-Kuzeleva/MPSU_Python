import sys

data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = int(data[1])
    
    count = 0
    while b > 0:
        count += a // b
        a, b = b, a % b
        
    print(count)
