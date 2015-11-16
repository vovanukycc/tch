a = int(input())
b = int(input())
c = int(input())
if a > b:
    maxi = a
    mini = b
else:
    maxi = b
    mini = a
if maxi < c:
    maxi = c
if mini > c:
    mini = c
midi = (a + b + c) - (maxi + mini)
print(str(maxi))
print(str(mini))
print(str(midi))