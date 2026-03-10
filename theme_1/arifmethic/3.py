x = int(input())

nums = []

i = 1
while i * i <= x:
    if x % i == 0:
        nums.append(i)
        if i != x // i:
            nums.append(x // i)
    i += 1

nums.sort()

print(' '.join(map(str, nums)))