import sys

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    heights.pop()
    return max_area


data = list(map(int, sys.stdin.read().strip().split()))
n = data[0]
heights = data[1:n+1]
print(largest_rectangle_area(heights))

