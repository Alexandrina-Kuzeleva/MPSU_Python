n, m = map(int, input().split())
anna = {int(input()) for i in range(n)}
borya = {int(input()) for i in range(m)}

common = anna & borya
only_anna = anna - borya
only_borya = borya - anna

print(len(common))
print(*sorted(common))
print(len(only_anna))
print(*sorted(only_anna))
print(len(only_borya))
print(*sorted(only_borya))