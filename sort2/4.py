n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

print("YES" if a == b else "NO")
