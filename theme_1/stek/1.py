class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, n):
        self.items.append(n)
        return "ok"
    
    def pop(self):
        return self.items.pop()
    
    def back(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        return "ok"
    
    def exit(self):
        return "bye"


stack = Stack()

while True:
    command = input().strip()
    
    if command.startswith("push"):
        _, n = command.split()
        print(stack.push(int(n)))
    elif command == "pop":
        print(stack.pop())
    elif command == "back":
        print(stack.back())
    elif command == "size":
        print(stack.size())
    elif command == "clear":
        print(stack.clear())
    elif command == "exit":
        print(stack.exit())
        break