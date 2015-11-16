with open('file_name', 'r') as inf:

sp = [a for a in input().lower().split()]
d = {}
for i in sp:
    g = sp.count(i)
    if i not in d:
        d[i] = g
for i in d:
    print(i, d[i])
