n = int(input())
parent = {}

for _ in range(n - 1):
    child, par = input().split()
    parent[child] = par

def is_ancestor(anc, desc):
    current = desc
    while current in parent:
        if parent[current] == anc:
            return True
        current = parent[current]
    return False

try:
    while True:
        line = input().split()
        if not line:
            break
        a, b = line[0], line[1]
        
        if is_ancestor(a, b):
            print(1)
        elif is_ancestor(b, a):
            print(2)
        else:
            print(0)
except EOFError:
    pass