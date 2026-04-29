s = input().strip()

stack = 0
removals = 0

for char in s:
    if char == '(':
        stack += 1
    else:
        if stack > 0:
            stack -= 1
        else:
            removals += 1

removals += stack
print(removals)