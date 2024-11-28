n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
c = min([a[0][0], a[0][n-1], a[n - 1][0], a[n - 1][n - 1]])
if a[0][0] == c:
    for i in a:
        print(*i)
elif a[0][n - 1] == c:
    for i in range(n - 1, -1, -1):
        for j in range(n):
            print(a[j][i], end=' ') 
        print()
elif a[n - 1][0] == c:
    for i in range(n):
        for j in range(n - 1, -1, -1): 
            print(a[j][i], end=' ')
        print()
else:
    for i in a[::-1]:
        print(*i[::-1])
        
