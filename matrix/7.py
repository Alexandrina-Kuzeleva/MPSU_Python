import sys

def IsSymmetric(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True

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

if IsSymmetric(A):
    print("YES")
else:
    print("NO")