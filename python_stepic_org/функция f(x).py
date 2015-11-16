n = int(input())
b ={}
for i in range(n):
    a = int(input())
    if a not in b:
        c = f(a)
        b[a] = c
        print(c)
    else:
        print(b[a])

