with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
words = text.split()
unique_words = set(words)
print(len(unique_words))