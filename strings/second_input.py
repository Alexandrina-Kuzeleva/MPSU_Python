string = input()
first = string.find('f')

if first == -1:
    print(-2)
else:
    second = string.find('f', first + 1) 
    if second == -1:
        print(-1)
    else:
        print(second)