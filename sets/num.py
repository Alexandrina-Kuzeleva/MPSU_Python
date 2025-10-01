n = int(input())
possible = set(range(1, n + 1))  
while True:
    line = input().strip()
    if line == "HELP":
        break
    question = set(map(int, line.split()))
    answer = input().strip()
    
    if answer == "YES":
        possible &= question
    else:
        possible -= question
print(*sorted(possible))