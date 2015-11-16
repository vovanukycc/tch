def censor(text, word):
    new_text = []
    a = text.split(" ")
    for i in a:
        if word == i:
            i = "*" * len(word)
        new_text.append(i)
    return " ".join(new_text)


text = "this hack1 is wack hack1"
word = "hack1"
new_text = []
a = text.split(" ")
for i in a:
    if (i == word):
        i = "*" * len(word)
    new_text.append(i)
print(" ".join(new_text))