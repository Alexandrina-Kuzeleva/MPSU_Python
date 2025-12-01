s, n = map(int, input().split())
volumes = [int(input()) for _ in range(n)]

volumes.sort()

total = 0
count = 0
for volume in volumes:
    if total + volume <= s:
        total += volume
        count += 1
    else:
        break

print(count)