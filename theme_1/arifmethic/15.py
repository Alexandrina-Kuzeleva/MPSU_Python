k = int(input())

div_sum = [1] * (k + 1)
div_sum[0] = 0
div_sum[1] = 0

for d in range(2, k // 2 + 1):
    for multiple in range(d * 2, k + 1, d):
        div_sum[multiple] += d

found = False
for a in range(2, k + 1):
    b = div_sum[a]
    if b <= k and b > a and div_sum[b] == a:
        print(a, b)
        found = True

if not found:
    print()