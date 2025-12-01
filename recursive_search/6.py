def generate_permutations(n, prefix=[]):
    if len(prefix) == n:
        print(''.join(map(str, prefix)))
        return
    
    for i in range(1, n + 1):
        if i not in prefix:
            generate_permutations(n, prefix + [i])

N = int(input())
generate_permutations(N)