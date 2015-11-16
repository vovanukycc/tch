__author__ = 'vovanukycc'
x = float(input())
y = float(input())
s = input()
if s == '+':
    print(x + y)
else:
    if s == '-':
        print(x - y)
    else:
        if s == '*':
            print(x * y)
        else:
            if s == '/':
                if y != 0:
                    print(x / y)
                else:
                    print("Деление на 0!")
            else:
                if s == 'mod':
                    if y != 0:
                        print(x % y)
                    else:
                        print("Деление на 0!")
                else:
                    if s == 'pow':
                        print(x ** y)
                    else:
                        if s == 'div':
                            if y != 0:
                                print(x // y)
                            else:
                                print("Деление на 0!")
#                        else:
#                            print("Неверный знак операции!")