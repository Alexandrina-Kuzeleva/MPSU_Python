n = int(input())
words = {}
for i in range(n):
    key, word = input().split()
    words[key] = word
    words[word] = key
word = input()
print(words[word])