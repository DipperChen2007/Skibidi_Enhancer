def bocchi_the_rock(n,m,r,c,grid):
    pass

def take_input():
    n,m,r,c = map(int,input().split())
    grid  = []
    for _ in range(n):
        grid.append('a' * m)
    return n,m,r,c,grid

n,m,r,c,grid = take_input()
print(grid)