n = int(input())
if n == 0:
    print(0)
    print(0)
else:
    m = int(input())
    knowen = {input().strip() for i in range(m)}
    one = knowen.copy()
    for i in range(n - 1):
        m = int(input())
        current_languages = {input().strip() for i in range(m)}
        knowen &= current_languages
        one |= current_languages
    print(len(knowen))
    for i in sorted(knowen):
        print(i)
    print(len(one))
    for i in sorted(one):
        print(i)