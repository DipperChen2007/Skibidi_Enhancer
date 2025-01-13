#[[1, 1, 1], [1, 1, 0], [1, 2, 1], [2, 8, 5]]

def looking_glass(lst):
    pass

def check_func(magnification,p_x,p_y):
    if magnification == 1:
        if p_x == 1 and p_x == 3:
            if p_y == 1:
                return True
        elif p_x == 2:
            if p_y == 1 or p_y == 2:
                return True
        else:
            return False
    elif magnification > 1:
        
            

def take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    return lst

lst = take_input()
print(lst)