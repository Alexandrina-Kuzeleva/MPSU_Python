def generate_binary_strings(n, k, prefix="", ones=0):
    remaining_positions = n - len(prefix)
    
    if ones > k or ones + remaining_positions < k:
        return
    
    if len(prefix) == n:
        if ones == k:
            print(prefix)
        return
    
    generate_binary_strings(n, k, prefix + "0", ones)
    generate_binary_strings(n, k, prefix + "1", ones + 1)

N, K = map(int, input().split())
generate_binary_strings(N, K)