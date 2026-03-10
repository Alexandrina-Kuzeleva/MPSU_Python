n, k = map(int, input().split())
jokes = []

for i in range(1, n + 1):
    params = list(map(int, input().split()))
    jokes.append((params, i))

jokes.sort(key=lambda x: x[0], reverse=True)
print(*[j[1] for j in jokes])
