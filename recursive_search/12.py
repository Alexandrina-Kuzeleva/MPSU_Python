def gen_partitions(n, current, start, result):
    if n == 0:
        result.append(tuple(current))
        return
    
    for x in range(start, n + 1):
        current.append(x)
        gen_partitions(n - x, current, x, result)
        current.pop()

def main():
    n = int(input())
    all_partitions = []
    gen_partitions(n, [], 1, all_partitions)
    all_partitions.sort()
    for p in all_partitions:
        print(' '.join(map(str, p)))

if __name__ == "__main__":
    main()