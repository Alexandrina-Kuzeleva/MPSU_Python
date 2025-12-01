import sys

def SwapColumns(A, i, j):
    for row in A:
        row[i], row[j] = row[j], row[i]

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1

A = []
for row_idx in range(n):
    row = [int(data[index + col_idx]) for col_idx in range(m)]
    A.append(row)
    index += m

i = int(data[index])
j = int(data[index + 1])

SwapColumns(A, i, j)

for row in A:
    print(' '.join(map(str, row)))