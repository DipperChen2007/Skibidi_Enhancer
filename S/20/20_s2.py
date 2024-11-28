from collections import defaultdict, deque
from sys import stdin

def Escape_Room(m,n,grid):
    dic  = defaultdict(list)
    for r in range(m):
        for c in range(n):
            dic[grid[r][c]].append((r + 1, c + 1))        
    visited = set()
    frontier = deque([(m,n)])
    while frontier:
        x,y = frontier.popleft()
        num = x*y
        if num == grid[0][0]:
            return "yes"
        if (x,y) not in visited:
            visited.add((x,y))
            for t in dic[num]:
                frontier.append(t)
    return "no"
        
def take_input():
    input = stdin.readline
    m = int(input())
    n = int(input())
    grid = []
    for _ in range(m):
        grid.append(list(map(int,input().split())))
    return m,n,grid

m,n,grid = take_input()
print(Escape_Room(m,n,grid))