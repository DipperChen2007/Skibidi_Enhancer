# This can be sloved by BFS
from collections import deque

global grid


def getInput():
    matrix = []
    height, width = map(int, input().split())
    for _i in range(height):
        matrix.append(input())
    return (width, height, matrix)

width, height, grid = getInput()


def successor(s, width, height):
    frontier = []
    # if this position has been visited or it's a wall
    if visited[s[0]][s[1]] != None:
        return []
    
    visited[s[0]][s[1]] = step

    if grid[s[0]][s[1]] == "U":
        return successor((s[0] - 1, s[1]), width, height)
    elif grid[s[0]][s[1]] == "D":
        return successor((s[0] + 1, s[1]), width, height)
    elif grid[s[0]][s[1]] == "L":
        return successor((s[0], s[1] - 1), width, height)
    elif grid[s[0]][s[1]] == "R":
        return successor((s[0], s[1] + 1), width, height)


        
    if s[1] < width:
        frontier.append((s[0], s[1] + 1))
    if s[1] >= 0:
        frontier.append((s[0], s[1] - 1))
    if s[0] < height:
        frontier.append((s[0] + 1, s[1]))
    if s[0] >= 0:
        frontier.append((s[0] - 1, s[1]))

    return frontier

def camera(cords, direction):
    # base case is if cords on grid is a wall
    height, width = cords
    if grid[height][width] == "W":
        return
    
    if grid[height][width] == "." or grid[height][width] == "S":
        visited[height][width] = -1

    if direction == "up":
        camera((height - 1, width), "up")
    elif direction == "down":
        camera((height + 1, width), "down")
    elif direction == "left":
        camera((height, width - 1), "left")
    else:
        camera((height, width + 1), "right")
    
    return



def roboThieves(width, height):
    global visited
    global step

    visited = []
    step = 0

    S = (0, 0)
    for i in range(height):
        visited.append([None] * width)
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "W":
                visited[i][j] = -1
            elif grid[i][j] == "S":
                S = (i, j)
            elif grid[i][j] == "C":
                visited[i][j] = -1
                camera((i - 1, j), "up")
                camera((i + 1, j), "down")
                camera((i, j - 1), "left")
                camera((i, j + 1), "right")        

    frontier = deque()
    frontier.append(successor(S, width, height))

    
    while frontier:
        step += 1
        been = frontier.popleft()
        nextPoints = []
        for pos in been:
            nextPoints.extend(successor(pos, width, height))
        if nextPoints:
            frontier.append(nextPoints)
    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == ".":
                if visited[i][j]:
                    print(visited[i][j])
                else:
                    print("-1")

roboThieves(width, height)