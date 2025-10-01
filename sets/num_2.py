n = int(input())
possible = set(range(1, n + 1)) 
answers = []  
while True:
    line = input().strip()
    if line == "HELP":
        break
    question = set(map(int, line.split()))
    if len(question & possible) * 2 == len(possible):
        answer = "NO"
        possible -= question
    else:
        yes_set = possible & question    
        no_set = possible - question      
        if len(yes_set) > len(no_set):
            answer = "YES"
            possible = yes_set
        else:
            answer = "NO"
            possible = no_set
    answers.append(answer)
for ans in answers:
    print(ans)
print(*sorted(possible))