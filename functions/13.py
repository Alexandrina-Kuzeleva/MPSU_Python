def f(s, i=0):
    if i == len(s) - 1:
        return s[i]
    return s[i] + "*" + f(s, i + 1)

s = input().strip()
print(f(s))