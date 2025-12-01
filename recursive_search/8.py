def gen_seq(n, k, start=1, seq=None):
    if seq is None:
        seq = []
    
    if len(seq) == k:
        print(' '.join(map(str, seq)))
        return
    
    for x in range(start, n - k + len(seq) + 2):
        seq.append(x)
        gen_seq(n, k, x + 1, seq)
        seq.pop()

n, k = map(int, input().split())
gen_seq(n, k)