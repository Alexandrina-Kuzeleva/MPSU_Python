import sys


n = int(sys.stdin.readline())
ans = [''] * (n + 1)
stack = [(1, n)]

def query(l, r):
    print(f"? {l} {r}")
    sys.stdout.flush()
    return sys.stdin.readline().strip() == "Yes"

while stack:
    l, r = stack.pop()
    if l >= r:
        continue
    
    low, high = l + 1, r
    while low < high:
        mid = (low + high) // 2
        if query(l, mid):
            high = mid
        else:
            low = mid + 1
    m = low
    
    ans[l] = '('
    ans[m] = ')'
    
    if l + 1 <= m - 1:
        stack.append((l + 1, m - 1))
    if m + 1 <= r:
        stack.append((m + 1, r))

print("!" + "".join(ans[1:]))

