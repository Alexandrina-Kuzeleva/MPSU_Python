def generate_strings(n, k, prefix=""):
    if len(prefix) == n:
        print(prefix)
        return
    
    for i in range(k-1, -1, -1):
        if i < 10:
            char = str(i)
        else:
            char = chr(ord('a') + i - 10)
        generate_strings(n, k, prefix + char)

N, K = map(int, input().split())
generate_strings(N, K)