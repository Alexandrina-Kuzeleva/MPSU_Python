def f(n):
    if n == 1:
        return True
    if n < 1:
        return False
    return f(n-3) or f(n-5)

n = int(input())
if f(n):
    print("YES")
else:
    print("NO")
    