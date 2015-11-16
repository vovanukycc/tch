a = [int(i) for i in input().split()]
for i in range(len(a)):
    b = a.count(i)
    if b > 1:
        print(i, sep='  ', end=' ')