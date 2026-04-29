from collections import deque
import sys

input = sys.stdin.read().splitlines()

queue_1 = deque()
queue_2 = deque()

N = int(input[0])

for line in input[1:]:
    string = line.split()
    op = string[0]
    
    if op == '+':
        queue_2.append(string[1])
    elif op == '*':
        queue_1.append(string[1])
    elif op == '-':
        print(queue_1.popleft())

    if len(queue_1) < len(queue_2):
        queue_1.append(queue_2.popleft())
    elif len(queue_1) > len(queue_2) + 1:
        queue_2.appendleft(queue_1.pop())