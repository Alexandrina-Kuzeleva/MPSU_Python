n = int(input())

nums = []
d = 2
while d * d <= n:
    while n % d == 0:
        nums.append(d)
        n //= d
    d += 1 if d == 2 else 2  

if n > 1:
    nums.append(n)

print('*'.join(map(str, nums)))