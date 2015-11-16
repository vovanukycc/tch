X=int(input())
H=int(input())
M=int(input())
h=H+(X//60)
m=M+(X%60)
if m > 59:
    h = h+1
    m = m-60
print(h)
print(m)
