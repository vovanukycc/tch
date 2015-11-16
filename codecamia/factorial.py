__author__ = 'vovanukycc'


def factorial(x):
    f = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            print('i=', i)
            f *= i
            print('f=', f)
        return f


#x = 3
#f = 1
#if x == 1:
#    print('1')
#else:
#    for i in range(1, x + 1):
#        print('f=', f, 'i=',i)
#        f *= i
print factorial(2)