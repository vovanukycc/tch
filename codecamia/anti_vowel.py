def anti_vowel(text):
    i = 0
    text_new = ''
    for c in text:
        if c in "aeiouAEIOU":
            i += 1
        else:
            text_new += c
    return text_new

print(anti_vowel("Hey You!"))