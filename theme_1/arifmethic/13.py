n = int(input())

d = 2
count = 0
while d * d <= n:
    if n % d == 0:
        count += 1
        n //= d
        if count > 1 or n % d == 0:
            print("NO")
            break
    d += 1
else:
    if count == 1 and n > 1 and n != d:
        print("YES")
    else:
        print("NO")