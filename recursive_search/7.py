def next_word(s):
    s = list(s)
    n = len(s)
    
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    
    if i == -1:
        return ''.join(sorted(s))
    
    j = n - 1
    while s[j] <= s[i]:
        j -= 1
    
    s[i], s[j] = s[j], s[i]
    
    left = i + 1
    right = n - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

while True:
    try:
        word = input().strip()
        if not word:
            break
        print(next_word(word))
    except EOFError:
        break