import sys

def sift_up(i, heap):
    while i > 1 and heap[i] > heap[i // 2]:
        parent = i // 2
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
    return i


input_data = sys.stdin.read().split()

n = int(input_data[0])
heap = [0] + [int(x) for x in input_data[1:n+1]]
q = int(input_data[n+1])

idx = n + 2
for _ in range(q):
    i = int(input_data[idx])
    x = int(input_data[idx+1])
    idx += 2
    heap[i] += x
    new_index = sift_up(i, heap)
    print(new_index)
print(*(heap[1:]))

