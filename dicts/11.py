n = int(input())
dictionary = {}

for i in range(n):
    word = input().strip()
    lower_word = word.lower()
    if lower_word not in dictionary:
        dictionary[lower_word] = set()
    dictionary[lower_word].add(word)

text = input().split()
errors = 0

for word in text:
    lower_word = word.lower()
    
    if lower_word not in dictionary:
        stresses = sum(1 for c in word if c.isupper())
        if stresses != 1:
            errors += 1
    else:
        if word not in dictionary[lower_word]:
            errors += 1

print(errors)