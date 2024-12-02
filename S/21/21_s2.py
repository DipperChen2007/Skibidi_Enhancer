# 0 -> black , 1 -> gold
def MA(grid, lst):
    row_flip = [0] * len(grid)  
    col_flip = [0] * len(grid[0])  
    
    for l, n in lst:
        if l == "R":
            row_flip[n - 1] ^= 1  
        elif l == "C":
            col_flip[n - 1] ^= 1  

    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (row_flip[i] ^ col_flip[j]) == 1:
                answer += 1
    return answer

def take_input():
    m = int(input())
    n = int(input())
    grid = [[0] * n for _ in range(m)]
    t = int(input())
    lst = []
    for i in range(t):
        s, a = input().split()
        lst.append((s, int(a)))
    return grid, lst

grid, lst = take_input()
print(MA(grid, lst))
