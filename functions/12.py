def f(s, i=0, count=0):
    if i == len(s):
        return count
    if s[i] in '0123456789':
        count += 1
    return f(s, i + 1, count)

s = input().strip()
print(f(s))