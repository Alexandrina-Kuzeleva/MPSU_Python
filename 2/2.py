def Intersection(A, B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            C.append(A[i])
            i += 1
            j += 1
    return C

A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = Intersection(A, B)
print(' '.join(map(str, result)))