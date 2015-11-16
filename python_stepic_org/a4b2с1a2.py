gen = str(input())
count = 1
prev = ''
for i in gen:
    if i != prev:
        if prev:
            print(prev, count, sep='', end='')
        count = 1
        prev = i
    else:
        count += 1
print(prev, count, sep='', end='')