def solve_short(n):
    if n == 1:
        return [1]
    else:
        prev = solve_short(n-1)
        return prev + [-1] + [n] + [1]

n = int(input())
result = solve_short(n)
print(' '.join(map(str, result)))
