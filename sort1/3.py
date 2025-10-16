n = int(input())
nums = list(map(int, input().split()))
num, place = input().split()

nums.insert(int(place) - 1, num)
print(*nums)