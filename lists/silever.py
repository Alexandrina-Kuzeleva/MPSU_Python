n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(set(numbers))
vasilya = sorted_numbers[-2]
print(vasilya)  