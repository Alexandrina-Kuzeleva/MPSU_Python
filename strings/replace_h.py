string = str(input())
print(string[:string.find('h') + 1] + string[string.find('h') + 1:string.rfind('h')].replace("h","H") + string[string.rfind('h'):])