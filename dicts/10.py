n = int(input())
latin_to_english = {}

for _ in range(n):
    line = input().strip()
    eng_word, translations = line.split(' - ')
    latin_words = translations.split(', ')
    
    for latin_word in latin_words:
        if latin_word not in latin_to_english:
            latin_to_english[latin_word] = []
        latin_to_english[latin_word].append(eng_word)

print(len(latin_to_english))
for latin_word in sorted(latin_to_english.keys()):
    english_words = ', '.join(sorted(latin_to_english[latin_word]))
    print(f"{latin_word} - {english_words}")