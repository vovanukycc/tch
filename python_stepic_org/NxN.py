n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
d = 1
while d <= n**2:

    a[i][j] = d
    d += 1
