def SwapDiagonals(A):
    n = len(A)
    for i in range(n):
        A[i][i], A[n-1-i][i] = A[n-1-i][i], A[i][i]
    
n = int(input())
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

SwapDiagonals(A)

for row in A:
    print(' '.join(map(str, row)))