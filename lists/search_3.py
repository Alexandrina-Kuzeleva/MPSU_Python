n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

indices = [i + 1 for i in range(n) if numbers[i] == x]

if indices:
    print(*indices)