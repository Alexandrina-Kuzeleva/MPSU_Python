from collections import deque
import sys

N = int(sys.stdin.readline())
data = deque(map(int, sys.stdin.readline().split()))

seen = set()
result = []

for x in reversed(data):
    if x not in seen:
        seen.add(x)
        result.append(x)

result.reverse()

print(len(result))
print(' '.join(map(str, result)))