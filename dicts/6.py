n = int(input())
files = {}
for i in range(n):
    name, *oper = input().split()
    files[name] = oper

m = int(input())
for i in range(m):
    oper, name = input().split()
    
    if oper == 'write':
        char = 'W'
    elif oper == 'read':
        char = 'R'
    else:
        char = 'X'
    
    if name in files and char in files[name]:
        print("OK")
    else:
        print("Access denied")