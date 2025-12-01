def generate_strings(n, k, prefix=""):
    if len(prefix) == n:
        print(prefix)
        return
    
    for i in range(k):
        generate_strings(n, k, prefix + str(i))

N, K = map(int, input().split())
generate_strings(N, K)