def partitions(n, current, start, sum_so_far, all_partitions):
    if sum_so_far == n:
        all_partitions.append(current[:])
        return
    for x in range(start, n - sum_so_far + 1):
        if sum_so_far + x <= n:
            current.append(x)
            partitions(n, current, x, sum_so_far + x, all_partitions)
            current.pop()

def main():
    n = int(input())
    all_partitions = []
    partitions(n, [], 1, 0, all_partitions)
    all_partitions.sort(reverse=True)
    for p in all_partitions:
        print(' '.join(map(str, p)))

if __name__ == "__main__":
    main()