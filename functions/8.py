n = int(input())
res = []

def place(l, r):
    if l > r:
        return
    res.append(l)
    place(l + 1, r)
    if l != 1:
        res.append(-l)

place(1, n)
print(*res)
