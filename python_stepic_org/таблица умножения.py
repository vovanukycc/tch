a = int(input())
b = int(input()) + 1
c = int(input())
d = int(input()) + 1
for k in range(c, d):
    print('\t', k, end='')
print('')
for i in range(a, b):
    print(i, end='')
    for j in range(c, d):
        print('\t', i * j, end='')
    print('')

