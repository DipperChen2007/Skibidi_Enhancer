def main(grid):
    while x_exists(grid):
        Arithmetic_Square(grid)
    for i in grid:
        print(*i)

def Arithmetic_Square(grid):
    changed = False
    for i in range(3):
        #check if there are two ints in a row
        if check_one_x(grid[i]) == 2:
            #dentify the only unknow position in a row 
            pos_row = dentify_one_x(grid[i])
            if pos_row == 0:
                grid[i][0] = grid[i][1] - (grid[i][2] - grid[i][1])
            elif pos_row == 1:
                grid[i][1] = grid[i][0] + (grid[i][2] - grid[i][0])//2
            else:
                grid[i][2] = grid[i][1] + (grid[i][1] - grid[i][0])
            changed = True 
               
        col = [grid[j][i] for j in range(3)]
        #check if there are two ints in a col
        if check_one_x(col) == 2:
            #dentify the only unknow position in a col
            pos_row = dentify_one_x(col)
            if pos_row == 0:
                grid[0][i] = grid[1][i] - (grid[2][i] - grid[1][i])
            elif pos_row == 1:
                grid[1][i] = grid[0][i] + (grid[2][i] - grid[0][i])//2
            else:
                grid[2][i] = grid[1][i] + (grid[1][i] - grid[0][i])
            changed = True 
            
    if not changed:
        guess(grid)


def guess(grid):
    if grid[1][1] == "X":
        grid[1][1] = 0
    elif grid[0][1] == "X":
        grid[0][1] = 0
    elif grid[1][0] == "X":
        grid[1][0] = 0
    elif grid[1][2] == "X":
        grid[1][2] = 0
    elif grid[2][1] == "X":
        grid[2][1] = 0
    
    elif grid[0][0] == "X":
        grid[0][0]  = 0
    elif grid[0][2]  == "X":
        grid[0][2] = 0
    elif grid[2][2] == "X":
        grid[2][2] = 0
    elif grid[2][0] == "X":
        grid[2][0] = 0


def x_exists(grid):
    for r in grid:
        if "X" in r:
            return True
    return False
    
def check_one_x(lst):
    count = 0
    for e in lst:
        if e != "X":
            count += 1
    return count    
    
    
def dentify_one_x(lst):
    pos = 0
    for i in range(3):
        if lst[i] == "X":
            pos = i
    return pos
        
def Take_input():
    grid = []
    for _ in range(3):
        grid.append(list(input().split()))
    for i in range(3):
        for j in range(3):
            if grid[i][j]!="X":
                grid[i][j] = int(grid[i][j])
    return grid

grid = Take_input()
main(grid)