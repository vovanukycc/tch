gen = str(input())
c1 = gen.count('c')
c2 = gen.count('C')
g1 = gen.count('g')
g2 = gen.count('G')
#for i in gen:
#    if gen[i] == 'c' or gen[i] == 'C':
#        c += 1
#    if gen[i] == 'g' or gen[i] == 'G':
#        g += 1
print(((c2 + c1 + g2 + g1)/len(gen)) * 100)