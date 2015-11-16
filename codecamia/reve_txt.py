
def reverse(text):
    rev_txt = ''
    for i in range(len(text)-1, -1, -1):
        rev_txt += text[i]
    return rev_txt


print(reverse('bash'))

