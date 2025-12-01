def gen_seq(n, k, start=None, seq=None):
    if seq is None:
        seq = []
    if start is None:
        start = n
    
    if len(seq) == k:
        print(' '.join(map(str, seq)))
        return
    
    for x in range(start, 0, -1):
        seq.append(x)
        gen_seq(n, k, x - 1, seq)
        seq.pop()

n, k = map(int, input().split())
gen_seq(n, k)