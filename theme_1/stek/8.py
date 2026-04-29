import sys

data = sys.stdin.read().strip().split()
idx = 0
N = int(data[idx]); idx += 1
K = int(data[idx]); idx += 1
P = int(data[idx]); idx += 1

stacks = [[] for _ in range(K + 1)]
current_load = 0
max_load = 0

for _ in range(N):
    op = data[idx]; idx += 1
    A = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    
    if op == '+':
        if current_load >= P:
            print("Error")
            
        stacks[A].append(B)
        current_load += 1
        if current_load > max_load:
            max_load = current_load
    else:  # op == '-'
        if not stacks[A]:
            print("Error")
            
        top = stacks[A].pop()
        if top != B:
            print("Error")
            
        current_load -= 1

if current_load != 0:
    print("Error")
    
