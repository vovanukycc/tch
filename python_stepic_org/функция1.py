def modify_list(l):
    i, n = 0, len(l)
    while i < n:
        if l[i] % 2:
            l.pop(i)
            n -= 1
        else:
            l[i] = int(l[i] / 2)
            i += 1

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)