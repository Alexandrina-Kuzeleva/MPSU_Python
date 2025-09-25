data = list(map(int, input().split()))
n = [0]
grades = data[1:]
min = min(grades)
max = max(grades)
result = [min if grade == max else grade for grade in grades]
print(' '.join(map(str, result)))