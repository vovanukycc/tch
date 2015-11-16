n = int(input())
i = 1
up, right = 0, 0
while i <= n:
    sp = [a for a in input().split()]
    if sp[0] == 'север':
        up += int(sp[1])
    elif sp[0] == 'юг':
        up -= int(sp[1])
    elif sp[0] == 'восток':
        right += int(sp[1])
    elif sp[0] == 'запад':
        right -= int(sp[1])
    i += 1
print(right, ' ', up)