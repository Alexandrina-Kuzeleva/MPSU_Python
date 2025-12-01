from itertools import permutations
n = input()
digits = list(n)
numbers = set()
for perm in permutations(digits):
    if perm[0] != '0':
        num = int(''.join(perm))
        if 1000 <= num <= 9999:
            numbers.add(num)
print(min(numbers))