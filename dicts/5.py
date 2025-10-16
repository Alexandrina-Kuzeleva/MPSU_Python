freq = {}
try:
    while True:
        for word in input().split():
            freq[word] = freq.get(word, 0) + 1
except:
    pass

max_word = ''
max_count = 0
for word, count in freq.items():
    if count > max_count or (count == max_count and word < max_word):
        max_word = word
        max_count = count

print(max_word)