def add_brackets(s):
    n = len(s)
    if n <= 2:
        if n == 1:
            return s
        else:
            return f"({s})" if n == 2 else s
    
    return s[0] + '(' + add_brackets(s[1:-1]) + ')' + s[-1]

string = input().strip()
print(add_brackets(string))