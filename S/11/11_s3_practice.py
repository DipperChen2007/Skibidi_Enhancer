grid = [
    [0,0,0,0,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,0]
]

def print_result(points):
    for magnitude, x, y in points:
        print(looking_glass(magnitude, x, y))

def looking_glass(magnitude, x, y):
    # Base case
    if magnitude == 1:
        if grid[x][y] == 1:
            return "crystal"
        else:
            return "empty"

    new_size = 5 ** (magnitude - 1)
    new_x = x % new_size
    new_y = y % new_size

    return looking_glass(magnitude - 1, new_x, new_y)

def take_input():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))
    return points

points = take_input()
print_result(points)