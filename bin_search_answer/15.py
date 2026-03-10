n, k = map(int, input().split())

def find_nth(n, k):
    res = 0
    length = 1
    cnt = k - 1
    total = 0
    while True:
        odd_count = cnt ** length
        if total + odd_count >= n:
            break
        total += odd_count
        length += 1
    n -= total
    digits = []
    for _ in range(length):
        base = cnt ** (length - 1)
        d = (n - 1) // base
        digits.append(d)
        n -= d * base
        length -= 1
    num = 0
    for d in digits:
        if d >= 1:
            num = num * k + d
        else:
            num = num * k
    num *= k
    return num

print(find_nth(n, k))
