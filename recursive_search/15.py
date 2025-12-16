N = int(input())
parent = {}
for _ in range(N):
    msg, p = map(int, input().split())
    parent[msg] = p

k = int(input())
to_delete = set([k])
stack = [k]

while stack:
    current = stack.pop()
    for msg, p in parent.items():
        if p == current and msg not in to_delete:
            to_delete.add(msg)
            stack.append(msg)

print(len(to_delete))
