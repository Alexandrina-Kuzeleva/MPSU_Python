
data = list(map(int, input().split()))
n = data[0]
balls = data[1:]

stack = []

for color in balls:
    if stack and stack[-1][0] == color:
        stack[-1][1] += 1
    else:
        stack.append([color, 1])
    
    if stack[-1][1] >= 3:
        stack.pop()

removed = n - sum(count for _, count in stack)
print(removed)
