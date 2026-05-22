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
n = int(input_data)
heap = + [int(x) for x in input_data[1:n+1]]
for i in range(n // 2, 0, -1):
    sift_down(i, heap, n)
    
print(*(heap[1:]))

