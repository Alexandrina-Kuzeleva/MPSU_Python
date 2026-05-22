import sys

def sift_up(i, heap):
    while i > 1 and heap[i] > heap[i // 2]:
        parent = i // 2
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
    return i

def sift_down(i, heap, current_size):
    while 2 * i <= current_size:
        left = 2 * i
        right = left + 1
        largest = left
        
        if right <= current_size and heap[right] > heap[left]:
            largest = right
            
        if heap[i] >= heap[largest]:
            break
            
        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest
    return i

input_data = sys.stdin.read().split()
max_size = int(input_data[0])
m = int(input_data[1])

heap = [0] * (max_size + 1)
current_size = 0

idx = 2
for _ in range(m):
    q_type = int(input_data[idx])
    idx += 1
    
    if q_type == 1:
        if current_size == 0:
            print("-1")
        else:
            max_val = heap[1]
            last_val = heap[current_size]
            current_size -= 1
            
            if current_size == 0:
                print("0 " + str(max_val))
            else:
                heap[1] = last_val
                final_idx = sift_down(1, heap, current_size)
                print(str(final_idx) + " " + str(max_val))
                
    elif q_type == 2:
        val = int(input_data[idx])
        idx += 1
        
        if current_size >= max_size:
            print("-1")
        else:
            current_size += 1
            heap[current_size] = val
            final_idx = sift_up(current_size, heap)
            print(final_idx)
            
    elif q_type == 3:
        target_idx = int(input_data[idx])
        idx += 1
        
        if target_idx < 1 or target_idx > current_size:
            print("-1")
        else:
            removed_val = heap[target_idx]
            last_val = heap[current_size]
            current_size -= 1
            
            if target_idx == current_size + 1:
                print(removed_val)
            else:
                heap[target_idx] = last_val
                if target_idx > 1 and heap[target_idx] > heap[target_idx // 2]:
                    sift_up(target_idx, heap)
                else:
                    sift_down(target_idx, heap, current_size)
                print(removed_val)
            
if current_size > 0:
    print(*(heap[1:current_size + 1]))

