def can_order(k, priorities):
    stack = []
    expected = sorted(priorities)
    idx = 0
    
    for priority in priorities:
        stack.append(priority)
        while stack and stack[-1] == expected[idx]:
            stack.pop()
            idx += 1
    
    return 1 if idx == k else 0

n = int(input())
results = []

for i in range(n):
    data = input().strip().split()
    k = int(data[0])
    priorities = [float(x) for x in data[1:1 + k]]
    results.append(can_order(k, priorities))

print("\n".join(map(str, results)))
