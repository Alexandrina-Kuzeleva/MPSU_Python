with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
word_count = {}
result = []

for word in words:
    count = word_count.get(word, 0)
    result.append(str(count))
    word_count[word] = count + 1

print(' '.join(result))