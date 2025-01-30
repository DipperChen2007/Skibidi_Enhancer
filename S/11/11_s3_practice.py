grid = [
    [0,0,0,0,0],
    [1,2,0,0,0],
    [1,1,2,0,0],
    [1,2,0,0,0],
    [0,0,0,0,0]
]

def print_result(points):
    for magnitude, x, y in points:
        print(looking_glass(magnitude, x, y))

def looking_glass(magnitude, x, y):
    # Base case: check if coordinates are valid
    if not (0 <= x < 5**magnitude and 0 <= y < 5**magnitude):
        return "empty"
    
    # Calculate position in current level grid
    cell_size = 5 ** (magnitude - 1)
    current_x = x // cell_size
    current_y = y // cell_size
    
    # Check if coordinates are within bounds
    if not (0 <= current_x < 5 and 0 <= current_y < 5):
        return "empty"
    
    # Get the cell type at current position
    cell_type = grid[current_x][current_y]
    
    if cell_type == 1:
        return "crystal"
    elif cell_type == 2:
        # If it's a recursive cell, check the smaller pattern
        new_x = x % cell_size
        new_y = y % cell_size
        return looking_glass(magnitude - 1, new_x, new_y)
    else:
        return "empty"

def take_input():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))
    return points

points = take_input()
print_result(points)