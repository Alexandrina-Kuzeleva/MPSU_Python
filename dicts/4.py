votes = {}

while True:
    try:
        vote = input().split()
        candidate = vote[0]
        count = int(vote[1])
        votes[candidate] = votes.get(candidate, 0) + count
    except EOFError:
        break

for i in sorted(votes.keys()):
    print(i, votes[i])