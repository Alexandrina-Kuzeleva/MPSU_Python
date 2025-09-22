string = str(input())
result = ''
for i in range(len(string)):
    if i % 3 != 0:  
        result += string[i]
print(result)