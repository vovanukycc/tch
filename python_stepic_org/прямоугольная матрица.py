lst = []
jm = 0
im = 0
while True:
    a = input()
    if a == 'end':
        break
    b = [int(i) for i in a.split()]
    jm = len(b)
    im += 1
    lst.append(b)
a = [[0 for j in range(jm)] for i in range(im)]
for i in range(im):
    for j in range(jm):
        xx = i + 1
        xy = j + 1
        if i == im - 1:
            xx = 0
        if j == jm - 1:
            xy = 0
        a[i][j] = lst[i - 1][j] + lst[xx][j] + lst[i][j - 1] + lst[i][xy]
for i in range(im):
    for j in range(jm):
        print(a[i][j], end=' ')
    print()
