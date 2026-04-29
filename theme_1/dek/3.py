from collections import deque

data = deque()

while True:
    string = input().split()
    if string[0] == 'exit':
        print('bye')
        break
    elif string[0] == 'push_front' :
        data.insert(0, string[1])
        print('ok')
    elif string[0] == 'push_back' :
        data.append(string[1])
        print('ok')
    elif string[0] == 'pop_front' :
        if len(data) > 0:
            print(data.pop(0))
        else:
            print('error')
    elif string[0] == 'pop_back' :
        if len(data) > 0:
            print(data.pop())
        else:
            print('error')
    elif string[0] == 'front':
        if len(data) > 0:
            print(data[0])
        else:
            print('error')
    elif string[0] == 'back' :
        if len(data) > 0:
            print(data[-1])
        else:
            print('error')
    elif string[0] == 'size':
        print(len(data))
    elif string[0] == 'clear' :
        data = []
        print("ok")