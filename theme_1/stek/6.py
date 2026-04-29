n = int(input())
stacks = []
for _ in range(n):
    data = list(map(int, input().split()))
    if data[0] == 0:
        stacks.append([])
    else:
        stacks.append(data[1:])

actions = []

for target in range(n):
    need = target + 1
    
    while True:
        found = -1
        for i in range(n):
            if stacks[i] and stacks[i][-1] == need:
                found = i
                break
        
        if found == -1:
            print(0)
        
        if found == target:
            stacks[target].pop()
            break
        
        for i in range(n):
            if stacks[i] and i != found and stacks[i][-1] != need:
                actions.append((found + 1, i + 1))
                stacks[i].append(stacks[found].pop())
                break

print('\n'.join(f"{a} {b}" for a, b in actions))