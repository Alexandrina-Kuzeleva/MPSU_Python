import sys

def maximal_rectangle(matrix):
    if not matrix:
        return 0
    
    n, m = len(matrix), len(matrix[0])
    heights = [0] * m
    max_area = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                heights[j] += 1
            else:
                heights[j] = 0
        
        stack = []
        for j in range(m + 1):
            h = heights[j] if j < m else 0
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(j)
    
    return max_area


data = sys.stdin.read().strip().split()
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1

matrix = []
for i in range(n):
    row = []
    for _ in range(m):
        row.append(int(data[idx])); idx += 1
    matrix.append(row)

print(maximal_rectangle(matrix))

