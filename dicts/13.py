n = int(input())
electors = {}
votes = {}
for i in range(n):
    s, e = input().split()
    electors[s] = int(e)
    votes[s] = {}
while True:
    try:
        st, c = input().split()
        votes[st][c] = votes[st].get(c, 0) + 1
    except:
        break
res = {}
for st in votes:
    m = max(votes[st].values())
    w = [k for k in votes[st] if votes[st][k] == m]
    w = min(w)
    res[w] = res.get(w, 0) + electors[st]
for st in votes:
    for c in votes[st]:
        if c not in res:
            res[c] = 0
for c, v in sorted(res.items(), key=lambda x: (-x[1], x[0])):
    print(c, v)
