M, N = map(int, input().split())

perfect_numbers = [6, 28, 496, 8128, 33550336, 8589869056]
found = False
for num in perfect_numbers:
    if M <= num <= N:
        print(num)
        found = True

if not found:
    print("Absent")