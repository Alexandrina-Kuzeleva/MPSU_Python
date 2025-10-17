def f(s, i=0, m=0):
    if i == len(s):
        return m
    d = int(s[i])
    if d > m:
        m = d
    return f(s, i + 1, m)

s = input().strip()
print(f(s))