import sys
import heapq

read = sys.stdin.readline
write = sys.stdout.write

n = int(read())

left = []
right = []

first = True
for x in map(int, read().split()):
    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if len(left) < len(right):
        heapq.heappush(left, -heapq.heappop(right))
    elif len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))

    if first:
        write(str(-left[0]))
        first = False
    else:
        write(" " + str(-left[0]))
