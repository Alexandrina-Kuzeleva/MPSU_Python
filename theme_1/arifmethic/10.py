import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    
    res = [0] * (n + 1)
    primes = []
    
    for i in range(2, n + 1):
        if res[i] == 0:
            res[i] = 1
            primes.append(i)
        
        for p in primes:
            if p * i > n:
                break
            res[p * i] = res[i] + 1
            
            if i % p == 0:
                break
                
    ans = [res[i] + 1 if i > 0 else 1 for i in range(1, n + 1)]
    
    sys.stdout.write(str(max(ans)) + "\n")
    sys.stdout.write(" ".join(map(str, ans)) + "\n")
