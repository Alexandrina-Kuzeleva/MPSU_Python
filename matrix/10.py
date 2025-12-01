import sys

def Transpose(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1

A = []
for i in range(n):
    row = [int(data[index + j]) for j in range(n)]
    A.append(row)
    index += n

Transpose(A)

for row in A:
    print(' '.join(map(str, row)))