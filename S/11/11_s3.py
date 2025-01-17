#[[1, 1, 1], [1, 1, 0], [1, 2, 1], [2, 8, 5]]
POINTS_1 = {(1,0),(2,0),(3,0),(2,1) }
POINTS_2 = { (1,1),(2,2),(3,1) }

def looking_glass(lst):
    for magnification,p_x,p_y in lst:
        if check_func(magnification,p_x,p_y):
            print("crystal")
        else:
            print("empty")

def check_func(magnification,p_x,p_y):
    
    if magnification == 1:
        return (p_x,p_y) in POINTS_1
    p_x_copy,p_y_copy = p_x//5,p_y//5
    if (p_x_copy,p_y_copy) in POINTS_1:
        return True
    # p_x_copy,p_y_copy = p_x%5,p_y%5
    if (p_x_copy,p_y_copy) in POINTS_2:
        return check_func(magnification - 1,p_x%5,p_y%5)
    
    return False            

def take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    return lst

lst = take_input()
looking_glass(lst)