n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
print(min(numbers, key=lambda num: abs(num - x)))