import sys

def sift_down(i, heap, n):
    while 2 * i <= n:
        left = 2 * i
        right = left + 1
        largest = left
        
        if right <= n and heap[right] > heap[left]:
            largest = right
            
        if heap[i] >= heap[largest]:
            break
            
        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest
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
    
    heap[i] -= x
    new_index = sift_down(i, heap, n)
    print(new_index)

print(*(heap[1:]))

