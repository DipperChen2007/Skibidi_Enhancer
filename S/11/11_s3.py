n = int(input())

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0]
]


def get_answer(mag, x, y):
    if mag == 1:
        if grid[4 - y][x]:
            return True
        else:
            return False

    s = (5 ** mag) // 5
    col = ((x + 1) // s) - 1
    remx = (x + 1) % s
    # print(remx)
    if remx > 0:
        col += 1
    # print(col)

    row = ((y + 1) // s) - 1
    remy = (y + 1) % s
    # print(remy)

    if remy > 0:
        row += 1
    # print(row)

    if row == 4 or row == 3 or col == 0 or col == 4:
        return False
    elif 4 > col > 0 == row:
        return True
    elif col == 2 and row == 1:
        return True
    else:
        return get_answer(mag - 1, x - (s * col), y - (s * row))

    # else:


for i in range(n):
    m, x, y = [int(j) for j in input().split()]

    if get_answer(m, x, y):
        print("crystal")
    else:
        print("empty")
# area = (x + 1 - (5 * ((x + 1) // sec)))
# print(area)
# if (x + 1) // sec == 1 or (x + 1) // sec == 5:
#     print("empty")

'''
1
3 25 24

'''