def solve(n, source, target, auxiliary):
    if n == 0:
        return []
    moves = []
    moves.extend(solve(n-1, source, auxiliary, target))
    moves.append(source)
    moves.extend(solve(n-1, auxiliary, target, source))
    return moves

N = int(input())
moves = solve(N, 1, 3, 2)

result = []
for move in moves:
    if move == 1:
        result.append('1')
    elif move == 3:
        result.append(str(N))
    else:
        for i in range(2, N):
            if move == i:
                result.append(str(i))

print(' '.join(result))