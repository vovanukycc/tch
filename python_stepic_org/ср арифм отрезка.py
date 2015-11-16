a = int(input())
b = int(input())
sym = 0
kl = 0
sp = 0
for i in range(a, b + 1):
    if i%3 == 0:
        sym += i
        kl += 1
sp = sym / kl
print(sp)