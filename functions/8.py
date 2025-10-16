def solve(n):
    if n == 1:
        return ["1"]
    
    prev = solve(n - 1)
    result = []
    
    result.extend(prev)
    result.append(str(n))
    result.extend(prev)
    
    return result

N = int(input())
if N == 1:
    print("1")
else:
    solution = solve(N)
    print(" ".join(solution))