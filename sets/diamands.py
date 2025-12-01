import sys

input = sys.stdin.read
data = input().split()

idx = 0
N = int(data[idx]); idx += 1
a = int(data[idx]); idx += 1
b = int(data[idx]); idx += 1
K = int(data[idx]); idx += 1

d = b - a

weighings = []
diffs = []

for _ in range(K):
    w = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    stones = {int(data[idx + i]) for i in range(m)}
    idx += m
    
    diff = w - a * m
    diffs.append(diff)
    weighings.append(stones)

candidates = []
for i in range(1, N + 1):
    possible = True
    for j in range(K):
        expected = d if i in weighings[j] else 0
        if diffs[j] != expected:
            possible = False
            break
    if possible:
        candidates.append(i)

if not candidates:
    if any(diff != 0 for diff in diffs):
        print("Impossible")
    else:
        print("Fail")
else:
    print(len(candidates))
    print(*sorted(candidates))