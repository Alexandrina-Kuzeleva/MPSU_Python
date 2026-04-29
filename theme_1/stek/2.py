s = input().strip()

stack = []
brackets = {')': '(', ']': '[', '}': '{'}

for char in s:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if not stack or stack[-1] != brackets[char]:
            print("no")
            break
        stack.pop()
else:
    print("yes" if not stack else "no")