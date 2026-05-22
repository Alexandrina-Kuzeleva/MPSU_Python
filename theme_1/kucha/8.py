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

input_data = sys.stdin.read().split()
n = int(input_data[0])
heap = [0] + [int(x) for x in input_data[1:n+1]]

for i in range(n // 2, 0, -1):
    sift_down(i, heap, n)
    
print(*(heap[1:n+1]))

sorted_elements = []
current_size = n

for _ in range(n - 1):
    max_val = heap[1]
    sorted_elements.append(max_val)
    
    heap[1] = heap[current_size]
    current_size -= 1
    
    sift_down(1, heap, current_size)
    print(*(heap[1:current_size+1]))
    
sorted_elements.append(heap[1])
sorted_elements.reverse()

print(*sorted_elements)