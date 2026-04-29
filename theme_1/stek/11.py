
n = int(input())
prices = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and prices[stack[-1]] > prices[i]:
        idx = stack.pop()
        result[idx] = i
    stack.append(i)

print(' '.join(map(str, result)))
