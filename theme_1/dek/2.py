deque = []

while True:
    string = input().split()
    if string[0] == 'exit':
        print('bye')
        break
    elif string[0] == 'push_front' :
        deque.insert(0, string[1])
        print('ok')
    elif string[0] == 'push_back' :
        deque.append(string[1])
        print('ok')
    elif string[0] == 'pop_front' :
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print('error')
    elif string[0] == 'pop_back' :
        if len(deque) > 0:
            print(deque.pop())
        else:
            print('error')
    elif string[0] == 'front':
        if len(deque) > 0:
            print(deque[0])
        else:
            print('error')
    elif string[0] == 'back' :
        if len(deque) > 0:
            print(deque[-1])
        else:
            print('error')
    elif string[0] == 'size':
        print(len(deque))
    elif string[0] == 'clear' :
        deque = []
        print("ok")