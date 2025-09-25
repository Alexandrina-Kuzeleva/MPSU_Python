string = input()
print(string[:string.find('h')] + string[string.rfind('h') + 1:])