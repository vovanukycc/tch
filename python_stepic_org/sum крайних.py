a = [int(i) for i in input().split()]
count = len(a)
if len(a) == 1:
    print(a[0])
else:
    for i in range(count):
        if count == (i + 1):
            print(a[0]+a[-2], sep='  ', end=' ')
        else:
            print(a[i-1]+a[i+1], sep='  ', end=' ')