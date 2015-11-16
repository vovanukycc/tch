x = float(input())
y = float(input())
s = input(())
if s == '+':
    print("%.2f" % (x+y))
    if s == '-':
        print("%.2f" % (x-y))
    if s == '*':
                print("%.2f" % (x*y))
    if s == '/':
        if y != 0:
            print("%.2f" % (x/y))
	else:
            print("Деление на ноль!")
else:
    print("Неверный знак операции!")
