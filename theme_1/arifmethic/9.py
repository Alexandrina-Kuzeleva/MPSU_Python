M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

p = 2
while p * p <= N:
    if is_prime[p]:
        for i in range(p * p, N + 1, p):
            is_prime[i] = False
    p += 1

found = False
for i in range(M, N + 1):
    if is_prime[i]:
        print(i)
        found = True

if not found:
    print("Absent")