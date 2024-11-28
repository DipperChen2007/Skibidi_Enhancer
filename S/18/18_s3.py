def RoboThieves(grid):
    start_r = 0
    start_c = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "C":
                camera(grid, r, c)
            # elif find S, record starting point
            elif grid[r][c] == "S":
                start_r = r 
                start_c = c

    # bfs
    visited = set()
    frontier = [(start_r,start_c,0)]
    while frontier:
        current_r,current_c,step = frontier.pop(0)
        if (current_r,current_c) not in visited:
            # exapnd to 4 directions
            visited.add((current_r,current_c))      
            for result in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_r,new_c = current_r + result[0],current_c + result[1]
                # if the next step is either [U, D, L, R], continue expand
                while in_range_not_wall(new_r,new_c,grid) and (new_r, new_c) not in visited and grid[new_r][new_c] in ["U", "D", "L", "R"]:
                    # update position until it's not U D L R
                    if grid[new_r][new_c] == "U":
                        new_r -= 1
                    elif grid[new_r][new_c] == "D":
                        new_r += 1
                    elif grid[new_r][new_c] == "L":
                        new_c -= 1
                    else:
                        new_c += 1
                
                if in_range_not_wall(new_r,new_c,grid) and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    grid[new_r][new_c] = step + 1
                    frontier.append((new_r,new_c,step+1))
                                     
    # print result
    # for line in grid:
    #     print(line)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] not in ["U", "D", "L", "R","S","W","C"]:
                if grid[row][col] == 0 or grid[row][col] == -1:
                    print(-1)
                else:
                    print(grid[row][col])
        
def in_range_not_wall(r,c,grid):
    if r <= 0 or c <= 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 'W' or grid[r][c] == "C" or grid[r][c] == -1:
        return False
    return True
    
def camera(grid, nop_r, nop_c):
    # 4 directions while in range and not reach wall
    # continue search for empty sapce and turn it to -1
    for left_i in range(nop_c, 0, -1):
        if grid[nop_r][left_i] == "W":
            break
        elif grid[nop_r][left_i] == 0:
            grid[nop_r][left_i] = -1
        
    for right_i in range(nop_c,len(grid[0]) - 1):
        if grid[nop_r][right_i] == "W":
            break
        elif grid[nop_r][right_i] == 0:
            grid[nop_r][right_i] = -1         

    for up_i in range(nop_r, 0,-1):
        if grid[up_i][nop_c] == "W":
            break
        elif grid[up_i][nop_c] == 0:
            grid[up_i][nop_c] = -1

    for down_i in range(nop_r,len(grid) - 1):
        if grid[down_i][nop_c] == "W":
            break
        elif grid[down_i][nop_c] == 0:
           grid[down_i][nop_c] = -1
                
def Take_input():
    n, m = list(map(int, input().split()))
    
    grid = []
    for _ in range(n):
        s = input()
        arr = []
        for c in s:
            if c == ".":
                arr.append(0)
            else:
                arr.append(c)
        grid.append(arr)
    return grid

grid = Take_input()
RoboThieves(grid)
