def suma():
    num = int(input())
    if num == 0:
        return 0
    return num + suma()

print(suma())