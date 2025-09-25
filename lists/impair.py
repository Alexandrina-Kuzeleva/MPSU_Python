n = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
min1 = sorted_numbers[0]  
min2 = sorted_numbers[1] 
print(min1, min2)