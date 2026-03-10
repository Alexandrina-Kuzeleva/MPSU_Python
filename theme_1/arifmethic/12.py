N, P = map(int, input().split())

M = 0
power = P

while power <= N:
    M += N // power
    power *= P

print(M)