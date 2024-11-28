def Sunflowers(n,grid):
    answer_grid = [[0]*n for _ in range(n)]
    #1
    if grid[0][0] < grid[0][1] and grid[0][0] < grid[1][0]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer_grid[i][j] = grid[i][j]
    #2
    elif grid[0][0] > grid[0][1] and grid[0][0] < grid[1][0]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer_grid[i][j] = grid[j][n - 1 - i]
    #3
    elif grid[0][0] > grid[0][1] and  grid[0][0] > grid[1][0]:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer_grid[i][j] = grid[n - 1 - i][n - 1 - j]
    #4
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer_grid[i][j] = grid[n - 1 - j][i]
    
    
    for r in range(len(grid)):
        s = ""
        for c in range(len(grid[0])):
            s = s + str(answer_grid[r][c]) + " "
        print(s)
            
def Take_input():
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int,input().split())))
    return n,grid

n,grid = Take_input()
Sunflowers(n,grid)