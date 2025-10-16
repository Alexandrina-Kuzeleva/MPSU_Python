n = int(input())
tree = {}
heights = {}

for _ in range(n - 1):
    child, parent = input().split()
    tree[child] = parent
    heights[child] = 0
    heights[parent] = 0

for person in heights:
    current = person
    height = 0
    while current in tree:
        current = tree[current]
        height += 1
    heights[person] = height

for person in sorted(heights.keys()):
    print(person, heights[person])