n1 = int(input())
caps = sorted(map(int, input().split()))
n2 = int(input())
shirts = sorted(map(int, input().split()))
n3 = int(input())
pants = sorted(map(int, input().split()))
n4 = int(input())
shoes = sorted(map(int, input().split()))

arrays = [caps, shirts, pants, shoes]
indices = [0, 0, 0, 0]
n = 4

best_diff = float('inf')
best_colors = [0, 0, 0, 0]

while True:
    current = [arrays[i][indices[i]] for i in range(n)]
    min_val = min(current)
    max_val = max(current)
    diff = max_val - min_val
    
    if diff < best_diff:
        best_diff = diff
        best_colors = current.copy()
    
    min_index = 0
    for i in range(1, n):
        if arrays[i][indices[i]] < arrays[min_index][indices[min_index]]:
            min_index = i
    
    indices[min_index] += 1
    if indices[min_index] >= len(arrays[min_index]):
        break

print(*best_colors)