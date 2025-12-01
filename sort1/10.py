n = int(input())
participants = []

for _ in range(n):
    surname, score = input().split()
    participants.append((surname, int(score)))

participants.sort(key=lambda x: x[1], reverse=True)

for surname, _ in participants:
    print(surname)