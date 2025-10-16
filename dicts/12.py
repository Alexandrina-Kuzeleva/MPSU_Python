costums = {}
while True:
    try:
        data = input().split()
        costum, prod, qulit = data[0], data[1], int(data[2])
        if costum not in costums:
            costums[costum]= {}
        costums[costum][prod] = costums[costum].get(prod, 0) + qulit
    except:
        break

for costum in sorted(costums.keys()):
    print(f"{costum}:")
    for product in sorted(costums[costum].keys()):
        print(f"{product} {costums[costum][product]}")