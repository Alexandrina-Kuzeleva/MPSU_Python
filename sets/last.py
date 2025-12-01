import sys
import heapq

input = sys.stdin.read
data = input().split()

n = int(data[0])
nums = list(map(int, data[1:]))

left = []
right = []
result = []

for num in nums:
    if not left or num <= -left[0]:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    result.append(str(-left[0]))

print(' '.join(result))