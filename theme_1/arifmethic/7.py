import sys

data = sys.stdin.read().split()
if data:
    k = int(data[0])
    if k == 1:
        print(2)
    else:
        limit = 15500000
        size = (limit - 1) // 2
        sieve = bytearray([1]) * (size + 1)
        sieve[0] = 0
        
        for i in range(1, int(limit**0.5) // 2 + 1):
            if sieve[i]:
                p = 2 * i + 1
                start = 2 * i * (i + 1)
                sieve[start::p] = bytearray((size - start) // p + 1)
        
        count = 0
        target = k - 1
        idx = -1
        curr_count = 0
        for i, val in enumerate(sieve):
            if val:
                curr_count += 1
                if curr_count == target:
                    print(2 * i + 1)
                    break
