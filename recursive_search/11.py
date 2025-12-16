def gen_partitions(n, max_term, current):
    if n == 0:
        print(' '.join(map(str, current)))
        return
    
    for term in range(min(max_term, n), 0, -1):
        current.append(term)
        gen_partitions(n - term, term, current)
        current.pop()

def main():
    n = int(input())
    gen_partitions(n, n, [])

if __name__ == "__main__":
    main()