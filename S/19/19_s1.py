def flipper(s):
    update_grid = [1,2,3,4]
    for chr in s:
        if chr == "H":
            new_grid = []
            new_grid = update_grid[2:] + update_grid[0:2]
            update_grid = new_grid
        else:
            new_grid = []
            new_grid = update_grid[0:2][::-1] + update_grid[2:][::-1]
            update_grid = new_grid
    print(*update_grid[0:2])
    print(*update_grid[2:])
    
def take_input():
    s = input()
    return s

s = take_input()
flipper(s)