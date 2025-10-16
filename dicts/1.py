n = int(input())
accounts = {}

for i in range(n):
    data = input().split()
    operation = int(data[0])
    
    if operation == 1:
        name = data[1]
        amount = int(data[2])
        accounts[name] = accounts.get(name, 0) + amount
    elif operation == 2:
        name = data[1]
        if name in accounts:
            print(accounts[name])
        else:
            print("ERROR")