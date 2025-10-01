N, K = map(int, input().split())
strike_days = set()
for i in range(K):
    a, b = map(int, input().split())
    day = a
    while day <= N:
        if day % 7 != 6 and day % 7 != 0:
            strike_days.add(day)
        day += b
print(len(strike_days))