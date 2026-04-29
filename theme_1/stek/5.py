n = int(input())
wagons = list(map(int, input().split()))

stack = []
actions = []
current = 1
idx = 0

while current <= n:
    if idx < n and wagons[idx] == current:
        actions.append((1, 1))
        actions.append((2, 1))
        idx += 1
        current += 1
    elif stack and stack[-1] == current:
        actions.append((2, 1))
        stack.pop()
        current += 1
    elif idx < n:
        actions.append((1, 1))
        stack.append(wagons[idx])
        idx += 1
    else:
        break

if current == n + 1 and not stack:
    for action in actions:
        print(action[0], action[1])
else:
    print(0)
