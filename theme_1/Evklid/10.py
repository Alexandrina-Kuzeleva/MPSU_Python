import sys
from math import gcd


input_data = sys.stdin.read().split()


idx = 0
k_tests = int(input_data[idx])
idx += 1

for _ in range(k_tests):
    n = int(input_data[idx])
    a = int(input_data[idx+1])
    b = int(input_data[idx+2])
    c = int(input_data[idx+3])
    idx += 4
    
    num_start = a * c + b
    den_start = c
    
    k = (num_start * (n - 1) // (n * den_start)) + 1
    
    res_num = k * n
    res_den = n - 1
    
    if res_num >= n * res_den:
        res_num = 0
        res_den = 1
    
    ans_a = res_num // res_den
    ans_b = res_num % res_den
    ans_c = res_den
    
    common = gcd(ans_b, ans_c)
    print(f"{ans_a} {ans_b // common} {ans_c // common}")
