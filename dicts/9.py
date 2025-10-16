accounts = {}

while True:
    try:
        data = input().split()
            
        if data[0] == 'DEPOSIT':
            name = data[1]
            amount = int(data[2])
            accounts[name] = accounts.get(name, 0) + amount
            
        elif data[0] == 'WITHDRAW':
            name = data[1]
            amount = int(data[2])
            accounts[name] = accounts.get(name, 0) - amount
            
        elif data[0] == 'BALANCE':
            name = data[1]
            if name in accounts:
                print(accounts[name])
            else:
                print('ERROR')
                
        elif data[0] == 'TRANSFER':
            name1, name2, amount = data[1], data[2], int(data[3])
            accounts[name1] = accounts.get(name1, 0) - amount
            accounts[name2] = accounts.get(name2, 0) + amount
            
        elif data[0] == 'INCOME':
            p = int(data[1])
            for name in accounts:
                if accounts[name] > 0:
                    interest = accounts[name] * p // 100
                    accounts[name] += interest
                    
    except EOFError:
        break