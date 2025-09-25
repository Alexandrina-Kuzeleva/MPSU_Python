string = str(input())
print(string[:string.find('h') + 1] + string[string.find('h') + 1:string.rfind('h')]*2 + string[string.rfind('h'):])