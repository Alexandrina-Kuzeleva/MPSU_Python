def gen_partitions(n, max_val, current, all_parts):
    if n == 0:
        all_parts.append(current[:])
        return
    
    for x in range(min(max_val, n), 0, -1):
        current.append(x)
        gen_partitions(n - x, x, current, all_parts)
        current.pop()

def main():
    n = int(input())
    all_parts = []
    gen_partitions(n, n, [], all_parts)
    
    all_parts.sort()
    
    for p in all_parts:
        print(' '.join(map(str, p)))

if __name__ == "__main__":
    main()