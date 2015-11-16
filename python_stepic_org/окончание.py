a = int(input())
s = 'программист'
if ((a % 10) == 1) and ((a % 100) != 11):
    print(str(a) + ' ' + s)
elif (2 <= (a % 10) <= 4) and (not(12 <= (a % 100) <= 14)):
    print(str(a) + ' ' + s + 'а')
else:
    print(str(a) + ' ' + s + 'ов')