n = int(input())
participants = []

for i in range(n):
    id_num, score = map(int, input().split())
    participants.append((id_num, score))

participants.sort(key=lambda x: (-x[1], x[0]))

for id_num, score in participants:
    print(id_num, score)