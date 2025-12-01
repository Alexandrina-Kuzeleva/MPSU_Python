size = int(input())
shoes = list(map(int, input().split()))

shoes.sort()

count = 0
last_size = size - 3

for shoe in shoes:
    if shoe >= size and shoe >= last_size + 3:
        count += 1
        last_size = shoe

print(count)