import sys

def sift_up(i, heap):
    while i > 1 and heap[i] > heap[i // 2]:
        parent = i // 2
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent

input_data = sys.stdin.read().split()
n = int(input_data[0])
heap = [0] * (n + 1)

for i in range(1, n + 1):
    heap[i] = int(input_data[i])
    sift_up(i, heap)
    
print(*(heap[1:]))
