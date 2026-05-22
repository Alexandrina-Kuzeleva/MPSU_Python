from collections import deque
import sys

data = sys.stdin.read().split()

n = int(data[0])
k = int(data[1])
arr = list(map(int, data[2:2+n]))

dq = deque()
result = []

for i in range(k):
    while dq and arr[dq[-1]] >= arr[i]:
        dq.pop()
    dq.append(i)

result.append(str(arr[dq[0]]))

for i in range(k, n):
    if dq and dq[0] == i - k:
        dq.popleft()
    
    while dq and arr[dq[-1]] >= arr[i]:
        dq.pop()
    dq.append(i)
    
    result.append(str(arr[dq[0]]))

sys.stdout.write("\n".join(result))
