import sys
from collections import defaultdict

data = list(map(int, sys.stdin.read().split()))
N, K = data[0], data[1]
a = data[2:]

cnt = defaultdict(int)
have = 0
l = 0
best_len = N + 1
best = (0, N - 1)

for r in range(N):
    if cnt[a[r]] == 0:
        have += 1
    cnt[a[r]] += 1

    while have == K:
        if r - l + 1 < best_len:
            best_len = r - l + 1
            best = (l, r)
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            have -= 1
        l += 1

print(best[0] + 1, best[1] + 1)
