text = []
while True:
    try:
        line = input()
        text.append(line)
    except:
        break

words = ' '.join(text).split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

pairs = []
for word, count in freq.items():
    pairs.append((-count, word))

pairs.sort()

for count, word in pairs:
    print(word)