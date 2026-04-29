import sys

data = sys.stdin.buffer.read().split()

n = int(data[0])
a = list(map(int, data[1:1 + n]))

stack = []
count = 0

for i in range(n):
    min_val = a[i]
    max_val = a[i]
    
    while stack and stack[-1][0] >= min_val:
        prev_min, prev_max = stack.pop()
        min_val = min(min_val, prev_min)
        max_val = max(max_val, prev_max)
    
    stack.append((min_val, max_val))
    
    if stack[-1][0] == a[i] and stack[-1][1] == a[i]:
        count += 1
        stack.pop()

print(count)

