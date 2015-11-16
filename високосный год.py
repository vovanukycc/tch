A = int(input())
q = A % 4
print('q = ', q)
w = A % 100
print('w = ', w)
e = A % 400
print('e = ', e)
if (((q == 0) and (w != 0)) or (e == 0)):
    print('Високосный')
else:
    print('Обычный')
