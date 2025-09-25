n = int(input())
s = set()  
for i in range(n):
    query = input().split()
    if query[0] == 'ADD':
        num = int(query[1])
        s.add(num)
    elif query[0] == 'PRESENT':
        num = int(query[1])
        print('YES' if num in s else 'NO')
    elif query[0] == 'COUNT':
        print(len(s))