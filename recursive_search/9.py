def generate(n, k, current, result):
    if len(current) == k:
        result.append(current[:])
        return
    
    if not current:
        min_val = k
        for x in range(min_val, n + 1):
            current.append(x)
            generate(n, k, current, result)
            current.pop()
    else:
        prev = current[-1]
        min_val = k - len(current)
        max_val = prev - 1
        for x in range(min_val, max_val + 1):
            current.append(x)
            generate(n, k, current, result)
            current.pop()

n, k = map(int, input().split())
result = []
generate(n, k, [], result)

for seq in result:
    print(' '.join(map(str, seq)))
