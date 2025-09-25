x = int(input())
n = int(input())  
table = []
for i in range(n):
    row = list(map(int, input().split()))
    table.append(row)

for j in range(n):
    found = False
    for i in range(n): 
        if table[i][j] == x:
            found = True
            break
    print("YES" if found else "NO")