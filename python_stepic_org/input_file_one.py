import re
with open("file.txt", 'r') as s:
    a = re.split("(\d*)", s.readline())[:-1]
    print(''.join([i[1]*int(i[0]) for i in zip(a[1::2], a[::2])]))