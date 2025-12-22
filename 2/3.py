n, k = map(int, input().split())
s = input().strip()

count = [0] * 26
left = 0
max_len = 0
start_pos = 0

for right in range(n):
    idx = ord(s[right]) - ord('a')
    count[idx] += 1
    
    while count[idx] > k:
        left_idx = ord(s[left]) - ord('a')
        count[left_idx] -= 1
        left += 1
    
    cur_len = right - left + 1
    if cur_len > max_len:
        max_len = cur_len
        start_pos = left + 1

print(max_len, start_pos)