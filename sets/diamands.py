N, a, b, K = map(int, input().split())
weighings = []
for _ in range(K):
    data = list(map(int, input().split()))
    wi = data[0]
    stones = data[2:]
    weighings.append((wi, stones))

status = [0] * N 

for wi, stones in weighings:
    m = len(stones)
    s_all = a * m
    s_one = (m - 1) * a + b
    if wi != s_all and wi != s_one:
        print("Impossible")
        exit()
    if wi == s_all:
        for s in stones:
            status[s - 1] = 1
    elif wi == s_one:
        for s in stones:
            if status[s - 1] == 1:
                continue
            status[s - 1] = 2

possible = []
for i in range(N):
    if status[i] != 1:
        possible.append(i + 1)

if not possible:
    print("Fail")
else:
    print(len(possible))
    print(*possible)
