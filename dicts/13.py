n = int(input())
states = {}
electors = {}

for i in range(n):
    state, votes = input().split()
    electors[state] = int(votes)
    states[state] = {}

try:
    while True:
        data = input().split()
        if not data:
            break
        state, candidate = data[0], data[1]
        if state in states:
            states[state][candidate] = states[state].get(candidate, 0) + 1
except EOFError:
    pass

results = {}

for state in states:
    max_votes = -1
    winner = None
    
    for candidate, votes in states[state].items():
        if votes > max_votes or (votes == max_votes and candidate < winner):
            max_votes = votes
            winner = candidate
    
    results[winner] = results.get(winner, 0) + electors[state]

sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))

for candidate, votes in sorted_results:
    print(candidate, votes)