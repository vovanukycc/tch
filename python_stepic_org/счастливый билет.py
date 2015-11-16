__author__ = 'vovanukycc'
s = input()
sum_l = int(s[0])+int(s[1])+int(s[2])
sum_r = int(s[3])+int(s[4])+int(s[5])
if sum_r == sum_l:
    print("Счастливый")
else:
    print("Обычный")