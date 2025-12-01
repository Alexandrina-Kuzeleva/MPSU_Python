def generate_binary_strings(n, prefix=""):
    if len(prefix) == n:
        print(prefix)
        return
    
    generate_binary_strings(n, prefix + "0")
    generate_binary_strings(n, prefix + "1")

N = int(input())
generate_binary_strings(N)