def wrap(s):
    if len(s) < 2:
        return s
    mid = len(s) // 2
    return wrap(s[:mid]) + f"({s[mid:mid+(len(s)%2==0)+1]})" + wrap(s[mid+(len(s)%2==0)+1:])

print(wrap(input().strip()))