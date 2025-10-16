def f():
    num = int(input())
    if num == 0:
        print(num)
        return
    f()
    print(num)

f()