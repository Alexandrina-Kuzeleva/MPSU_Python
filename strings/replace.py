string = str(input())
print(string[string.index(" ")+1:] + " " + string[:string.index(" ")])