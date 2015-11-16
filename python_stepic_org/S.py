import math
str = input()
if str == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ( a + b + c ) / 2
    s = math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ))
    print(s)
else:
    if str == 'прямоугольник':
        a = int(input())
        b = int(input())
        s = a*b
        print(s)
    else:
        if str == 'круг':
            r = int(input())
            s = 3.14*r*r
            print(s)

